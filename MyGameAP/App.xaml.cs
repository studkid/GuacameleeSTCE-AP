using Archipelago.Core;
using Archipelago.Core.MauiGUI;
using Archipelago.Core.MauiGUI.Models;
using Archipelago.Core.MauiGUI.ViewModels;
using Archipelago.Core.Models;
using Archipelago.Core.Traps;
using Archipelago.Core.Util;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using Archipelago.MultiClient.Net.MessageLog.Messages;
using GuacameleeAP.Models;
using Newtonsoft.Json;
using Serilog;
using System.Net;
using System.Xml.Linq;
using Windows.Media.Protection.PlayReady;

namespace MyGameAP {
    public partial class App : Application {
        static MainPageViewModel Context;
        public static ArchipelagoClient Client { get; set; }
        private DeathLinkService _deathlinkService;
        private static readonly object _lockObject = new object();
        private static List<GuacameleeItem> guacameleeItems { get; set; }
        private static List<GuacameleeLocation> guacameleeLocations { get; set; }
        private static uint baseAddress = 0x00400000;
        private static float healthChunks = 0;
        private static float staminaChunks = 0;
        private static float intensoChunks = 0;
        private static int progKick = 0;

        public App() {
            InitializeComponent();

            Context = new MainPageViewModel();
            Context.ConnectClicked += Context_ConnectClicked;
            Context.CommandReceived += (e, a) => {
                Client?.SendMessage(a.Command);
            };
            MainPage = new MainPage(Context);
            Context.ConnectButtonEnabled = true;
        }

        private async void Context_ConnectClicked(object? sender, ConnectClickedEventArgs e) {
            Context.ConnectButtonEnabled = false;
            Log.Logger.Information("Connecting...");
            if (Client != null)  {
                Client.Connected -= OnConnected;
                Client.Disconnected -= OnDisconnected;
                Client.ItemReceived -= Client_ItemReceived;
                Client.MessageReceived -= Client_MessageReceived;
                if (_deathlinkService != null) {
                    _deathlinkService.OnDeathLinkReceived -= _deathlinkService_OnDeathLinkReceived;
                    _deathlinkService = null;
                }
                Client.CancelMonitors();
            }

            GenericGameClient client = new GenericGameClient("Game");
            var connected = client.Connect();
            if (!connected) {
                Log.Logger.Error("Guacamelee not running, open Guacamelee before connecting!");
                Context.ConnectButtonEnabled = true;
                return;
            }

            Client = new ArchipelagoClient(client);

            Client.Connected += OnConnected;
            Client.Disconnected += OnDisconnected;

            await Client.Connect(e.Host,"Guacamelee Super Turbo Champioship Edition");

            Client.ItemReceived += Client_ItemReceived;
            Client.MessageReceived += Client_MessageReceived;
            Client.LocationCompleted += Client_LocationCompleted;

            guacameleeLocations = Helpers.GetGuacameleeLocations();
            var apLocations = Helpers.GetLocations(guacameleeLocations);
            guacameleeItems = Helpers.GetItems();

            await Client.Login(e.Slot,!string.IsNullOrWhiteSpace(e.Password) ? e.Password : null);

            //if (Client.Options.ContainsKey("EnableDeathlink") && (bool)Client.Options["EnableDeathlink"]) {
            //    var _deathlinkService = Client.EnableDeathLink();
            //    _deathlinkService.OnDeathLinkReceived += _deathlinkService_OnDeathLinkReceived;
            //    //ToDo listen for player death
            //}

            //var goalLocation = myLocations.First(x => x.Name.Contains("GoalLocationName"));
            //Memory.MonitorAddressBitForAction(goalLocation.Address, goalLocation.AddressBit, () => Client.SendGoalCompletion());

            Client.MonitorLocations(apLocations);

            Context.ConnectButtonEnabled = true;

            foreach(Item item in Client.GameState.ReceivedItems) {
                var itemToAdd = guacameleeItems[(int)item.Id - 1];
                if(itemToAdd.Category != "Money" && itemToAdd.Category != "Enemy Trap") {
                    AddItem(itemToAdd.Name, itemToAdd.Category, itemToAdd.Address, itemToAdd.SaveAddress, itemToAdd.AddressBit, item.Quantity);
                }
            }

            //Enable stamina bar
            Memory.WriteBit(Helpers.GetSaveDataFlag(0x0020), 0, true);
        }

        private void _deathlinkService_OnDeathLinkReceived(DeathLink deathLink) {
            //Todo kill player
        }

        private static void Client_ItemReceived(object? sender, ItemReceivedEventArgs e) {
            var itemId = e.Item.Id;
            var itemToReceive = guacameleeItems.FirstOrDefault(x => x.Id == itemId);
            if(itemToReceive != null) {
                e.Item.Category = itemToReceive.Category;
                LogItem(e.Item);
                Log.Logger.Debug($"Received {itemToReceive.Name} ({itemToReceive.Id})");
                AddItem(itemToReceive.Name, itemToReceive.Category, itemToReceive.Address, itemToReceive.SaveAddress, itemToReceive.AddressBit);
            }
        }

        private static void AddItem(string name, string category, uint address, uint address2, int bit, int quantity = 1) {
            if(category == "Simple") {
                var newAddress = baseAddress + address;
                Memory.WriteBit(newAddress, bit, true);
            }

            else if(category == "Health") {
                healthChunks += quantity;
                float addHealth = 20 * (float)Math.Floor((double)healthChunks / 3);
                Memory.Write(Helpers.GetHealthFlag(address), 80 + addHealth);
                Memory.Write(baseAddress + 0x51F7B0,healthChunks);
                Memory.Write(Helpers.GetSaveDataFlag(address2),healthChunks);
                Log.Logger.Information($"Health Chunk {healthChunks % 3} / 3 (Total {healthChunks})");
                Log.Logger.Debug($"New Health {80 + addHealth}");
            }

            else if(category == "Stamina") {
                staminaChunks += quantity;
                float addStamina = (float)Math.Floor((double)staminaChunks / 3);
                Memory.Write(Helpers.GetStaminaFlag(address),2 + addStamina);
                Memory.Write(baseAddress + 0x51F7D0,staminaChunks);
                Memory.Write(Helpers.GetSaveDataFlag(address2),staminaChunks);
                Log.Logger.Information($"Stamina Chunk {staminaChunks % 3} / 3 (Total {staminaChunks})");
                Log.Logger.Debug($"New Stamina {2 + addStamina}");
            }

            else if(category == "Intenso") {
                intensoChunks += quantity;
                var newAddress = baseAddress + address;
                float addIntenso = 15 * (float)Math.Floor((double)intensoChunks / 3);
                Memory.Write(newAddress, 70 + addIntenso);
                Memory.Write(baseAddress + 0x51F7D8,intensoChunks);
                Memory.Write(Helpers.GetSaveDataFlag(address2),intensoChunks);
                Log.Logger.Information($"Intenso Chunk {intensoChunks % 3} / 3 (Total {intensoChunks})");
                Log.Logger.Debug($"New Intenso {70 + addIntenso}");
            }

            else if(category == "Power") {
                Log.Logger.Debug($"Adding {name}");
                Memory.WriteBit(Helpers.GetPowerFlag(address),bit,true);
                if (address2 != 0 || name == "Goat Jump") {
                    Memory.WriteBit(Helpers.GetSaveDataFlag(address2),bit,true);
                }

                if(name == "Grab Ability") {
                    Memory.WriteBit(baseAddress + 511654,3,true);
                }
            }

            else if (category == "FalsePower") {
                Log.Logger.Debug($"Adding {name}");
                Memory.WriteBit(Helpers.GetPowerFlag(address),bit,false);
                Memory.WriteBit(Helpers.GetSaveDataFlag(address2),bit,false);
            }

            else if(category == "Pollo") {
                Memory.WriteBit(Helpers.GetPolloFlag(address),bit,true);
                if (name == "Pollo Power") {
                    Memory.WriteBit(Helpers.GetPowerFlag(address2),bit,true);
                    Memory.WriteBit(Helpers.GetSaveDataFlag(0xF0),bit,true);
                    Memory.WriteBit(Helpers.GetSaveDataFlag(0x140),bit,true);
                }
                else if(name == "Pollo Fly") {
                    Memory.Write(Helpers.GetSaveDataFlag(address2),0x47C34F80);
                }
                else {
                    Memory.WriteBit(Helpers.GetSaveDataFlag(address2),bit,true);
                }

                Log.Logger.Debug($"Adding {name}");
            }

            else if (category == "Kick") {
                progKick =+ quantity;
                if(progKick == 1) {
                    var itemToReceive = guacameleeItems.FirstOrDefault(x => x.Id == 27);
                    if (itemToReceive != null) {
                        Log.Logger.Debug($"New Kick State: {itemToReceive.Name} ({itemToReceive.Id})");
                        AddItem(itemToReceive.Name,itemToReceive.Category,itemToReceive.Address,itemToReceive.SaveAddress,itemToReceive.AddressBit);
                    }
                }
                else if (progKick == 2) {
                    var itemToReceive = guacameleeItems.FirstOrDefault(x => x.Id == 28);
                    if (itemToReceive != null) {
                        Log.Logger.Debug($"New Kick State: {itemToReceive.Name} ({itemToReceive.Id})");
                        AddItem(itemToReceive.Name,itemToReceive.Category,itemToReceive.Address,itemToReceive.SaveAddress,itemToReceive.AddressBit);
                    }
                }
            }

            else if (category == "Save") {
                Log.Logger.Debug($"Adding {name}");
                Memory.WriteBit(Helpers.GetSaveDataFlag(address),bit,true);
            }

            else if (category == "Money") {
                if (name == "500 Gold Coins") {
                    var curGold = Memory.ReadUInt(baseAddress + address);
                    Memory.Write(baseAddress + address,curGold + 500);
                    Log.Logger.Debug($"Adding gold ({curGold} -> {curGold + 500})");
                }
                else if (name == "5000 Gold Coins") {
                    var curGold = Memory.ReadUInt(baseAddress + address);
                    Memory.Write(baseAddress + address,curGold + 5000);
                    Log.Logger.Debug($"Adding gold ({curGold} -> {curGold + 5000})");
                }
                else if (name == "5 Silver Coins") {
                    var curGold = Memory.ReadUInt(baseAddress + address);
                    Memory.Write(baseAddress + address,curGold + 5);
                    Log.Logger.Debug($"Adding silver ({curGold} -> {curGold + 5})");
                }
            }

            else if (category == "Trap") {
                //LagTrap lag = new LagTrap();
                //lag.Start();

                //Log.Logger.Debug($"Lag Trap Starting");
            }
        }

        private void Client_LocationCompleted(object? sender, LocationCompletedEventArgs e) { 
            var locId = e.CompletedLocation.Id;
            var locToReceive = guacameleeLocations.FirstOrDefault(x => x.Id == locId);
            Log.Logger.Verbose($"locId {locId} locToReceive {locToReceive}");
            if (locToReceive != null) {
                //e.CompletedLocation.Category = locToReceive.Category;
                Log.Logger.Debug($"Removing {locToReceive.Category} ({locToReceive.Id})");
                RemoveItem(locToReceive.Category);
            }
        }

        private void RemoveItem(string category) {
            var itemToRemove = guacameleeItems.FirstOrDefault(x => x.Name == category);
            if(itemToRemove != null) {
                var address = itemToRemove.Address;
                var address2 = itemToRemove.SaveAddress;

                if (category == "Health Chunk") {
                    float addHealth = 20 * (float)Math.Floor((double)healthChunks / 3);
                    Memory.Write(Helpers.GetHealthFlag(address),80 + addHealth);
                    Memory.Write(baseAddress + 0x51F7B0,healthChunks);
                    Memory.Write(Helpers.GetSaveDataFlag(address2),healthChunks);
                    Log.Logger.Debug($"Health Chunk {healthChunks % 3} / 3 (Total {healthChunks})");
                    Log.Logger.Debug($"New Health {80 + addHealth}");
                }

                else if (category == "Stamina Chunk") {
                    float addStamina = (float)Math.Floor((double)staminaChunks / 3);
                    Memory.Write(Helpers.GetStaminaFlag(address),2 + addStamina);
                    Memory.Write(baseAddress + 0x51F7D0,staminaChunks);
                    Memory.Write(Helpers.GetSaveDataFlag(address2),staminaChunks);
                    Log.Logger.Debug($"Stamina Chunk {staminaChunks % 3} / 3 (Total {staminaChunks})");
                    Log.Logger.Debug($"New Stamina {2 + addStamina}");
                }

                else if(category == "Intenso Chunk") {
                    var newAddress = baseAddress + address;
                    float addIntenso = 15 * (float)Math.Floor((double)intensoChunks / 3);
                    Memory.Write(newAddress,70 + addIntenso);
                    Memory.Write(baseAddress + 0x51F7D8,intensoChunks);
                    Memory.Write(Helpers.GetSaveDataFlag(address2),intensoChunks);
                    Log.Logger.Debug($"Intenso Chunk {intensoChunks % 3} / 3 (Total {intensoChunks})");
                    Log.Logger.Debug($"New Intenso {70 + addIntenso}");
                }

                else if(category == "500 Gold Coins") {
                    var curGold = Memory.ReadUInt(baseAddress + address);
                    Memory.Write(baseAddress + address, Math.Max(curGold - 500, 0));
                    Log.Logger.Debug($"Removing gold ({curGold} -> {Math.Max(curGold - 500, 0)})");
                }

                else if (category == "5000 Gold Coins") {
                    var curGold = Memory.ReadUInt(baseAddress + address);
                    Memory.Write(baseAddress + address, Math.Max(curGold - 5000, 0));
                    Log.Logger.Debug($"Removing gold ({curGold} -> {Math.Max(curGold - 5000, 0)})");
                }

                else if (category == "5 Silver Coins") {
                    var curGold = Memory.ReadUInt(baseAddress + address);
                    Memory.Write(baseAddress + address, Math.Max(curGold - 5, 0));
                    Log.Logger.Debug($"Removing silver ({curGold} -> {Math.Max(curGold - 5, 0)})");
                }
            }
        }

        private void Client_MessageReceived(object? sender, MessageReceivedEventArgs e) {
            if (e.Message.Parts.Any(x => x.Text == "[Hint]: "))
            {
                LogHint(e.Message);
            }
            Log.Logger.Information(JsonConvert.SerializeObject(e.Message));
        }

        private static void LogItem(Item item) {
            var messageToLog = new LogListItem(new List<TextSpan>()
            {
                new TextSpan(){Text = $"[{item.Id.ToString()}] -", TextColor = Color.FromRgb(255, 255, 255)},
                new TextSpan(){Text = $"{item.Name}", TextColor = Color.FromRgb(200, 255, 200)},
                new TextSpan(){Text = $"x{item.Quantity.ToString()}", TextColor = Color.FromRgb(200, 255, 200)}
            });
            lock (_lockObject) {
                Application.Current.Dispatcher.DispatchAsync(() => {
                    Context.ItemList.Add(messageToLog);
                });
            }
        }

        private static void LogHint(LogMessage message) {
            var newMessage = message.Parts.Select(x => x.Text);

            if (Context.HintList.Any(x => x.TextSpans.Select(y => y.Text) == newMessage))
            {
                return; //Hint already in list
            }
            List<TextSpan> spans = new List<TextSpan>();
            foreach (var part in message.Parts)
            {
                spans.Add(new TextSpan() { Text = part.Text, TextColor = Color.FromRgb(part.Color.R, part.Color.G, part.Color.B) });
            }
            lock (_lockObject)
            {
                Application.Current.Dispatcher.DispatchAsync(() =>
                {
                    Context.HintList.Add(new LogListItem(spans));
                });
            }
        }

        private static void OnConnected(object sender, EventArgs args) {
            Log.Logger.Information("Connected to Archipelago");
            Log.Logger.Information($"Playing {Client.CurrentSession.ConnectionInfo.Game} as {Client.CurrentSession.Players.GetPlayerName(Client.CurrentSession.ConnectionInfo.Slot)}");
        }


        private static void OnDisconnected(object sender, EventArgs args) {
            Log.Logger.Information("Disconnected from Archipelago");
            healthChunks = 0;
            staminaChunks = 0;
            intensoChunks = 0;
        }

        protected override Window CreateWindow(IActivationState activationState) {
            var window = base.CreateWindow(activationState);
            if (DeviceInfo.Current.Platform == DevicePlatform.WinUI)
            {
                window.Title = "Guacamelee STCE Archipelago Randomizer";

            }
            window.Width = 600;

            return window;
        }
    }
}
