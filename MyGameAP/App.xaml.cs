using Archipelago.Core;
using Archipelago.Core.MauiGUI;
using Archipelago.Core.MauiGUI.Models;
using Archipelago.Core.MauiGUI.ViewModels;
using Archipelago.Core.Models;
using Archipelago.Core.Util;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using Archipelago.MultiClient.Net.MessageLog.Messages;
using GuacameleeAP.Models;
using Newtonsoft.Json;
using Serilog;

namespace MyGameAP {
    public partial class App : Application {
        static MainPageViewModel Context;
        public static ArchipelagoClient Client { get; set; }
        private DeathLinkService _deathlinkService;
        private static readonly object _lockObject = new object();
        private static List<GuacameleeItem> guacameleeItems { get; set; }
        private static int healthChunks = 0;
        private static int staminaChunks = 0;
        private static int intensoChunks = 0;

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

            await Client.Login(e.Slot,!string.IsNullOrWhiteSpace(e.Password) ? e.Password : null);

            //if (Client.Options.ContainsKey("EnableDeathlink") && (bool)Client.Options["EnableDeathlink"]) {
            //    var _deathlinkService = Client.EnableDeathLink();
            //    _deathlinkService.OnDeathLinkReceived += _deathlinkService_OnDeathLinkReceived;
            //    //ToDo listen for player death
            //}

            var myLocations = Helpers.GetLocations();
            guacameleeItems = Helpers.GetItems();

            //var goalLocation = myLocations.First(x => x.Name.Contains("GoalLocationName"));
            //Memory.MonitorAddressBitForAction(goalLocation.Address, goalLocation.AddressBit, () => Client.SendGoalCompletion());

            Client.MonitorLocations(myLocations);

            Context.ConnectButtonEnabled = true;

            foreach(Item item in Client.GameState.ReceivedItems) {
                var itemToAdd = guacameleeItems[(int)item.Id - 1];
                if(itemToAdd.Name != "500 Gold Coin" || itemToAdd.Name != "5000 Gold Coins" || itemToAdd.Name != "5 Silver Coins") {
                    AddItem(itemToAdd.Name, itemToAdd.Address, itemToAdd.AddressBit, item.Quantity);
                }
            }

            Memory.WriteBit(0x00911654, 4, true);
        }

        private void _deathlinkService_OnDeathLinkReceived(DeathLink deathLink) {
            //Todo kill player
        }

        private static void Client_ItemReceived(object? sender, ItemReceivedEventArgs e) {
            LogItem(e.Item);
            var itemId = e.Item.Id;
            var itemToReceive = guacameleeItems.FirstOrDefault(x => x.Id == itemId);
            if(itemToReceive != null) {
                Log.Logger.Verbose($"Received {itemToReceive.Name} ({itemToReceive.Id})");
                AddItem(itemToReceive.Name, itemToReceive.Address, itemToReceive.AddressBit);
            }
        }

        private static void AddItem(string name, ulong address, int bit, int quantity = 1) {
            if(name == "Pollo Power") {
                Memory.WriteBit(0x10A9141B, 0, true);
            }
            if(name == "Health Chunk") {
                healthChunks += quantity;
                var curHealth = Memory.ReadFloat(address);
                float addHealth = 20 * (float)Math.Floor((double)healthChunks / 3);
                Memory.Write(address, curHealth + addHealth);
                Log.Logger.Information($"Health Chunk {healthChunks % 3} / 3 (Total {healthChunks})");
                Log.Logger.Verbose($"New Health {curHealth + addHealth}");
                return;
            }
            if(name == "Stamina Chunk") {
                staminaChunks += quantity;
                var curStamina = Memory.ReadFloat(address);
                float addStamina = (float)Math.Floor((double)staminaChunks / 3);
                Memory.Write(address,curStamina + addStamina); 
                Log.Logger.Information($"Stamina Chunk {staminaChunks % 3} / 3 (Total {staminaChunks})");
                Log.Logger.Verbose($"New Stamina {curStamina + addStamina}");
                return;
            }
            if(name == "Intenso Chunk") {
                intensoChunks += quantity;
                var curIntenso = Memory.ReadFloat(address);
                float addIntenso = 10 * (float)Math.Floor((double)intensoChunks / 3);
                Memory.Write(address,curIntenso + addIntenso);
                Log.Logger.Information($"Intenso Chunk {intensoChunks % 3} / 3 (Total {intensoChunks})");
                Log.Logger.Verbose($"New Intenso {curIntenso + addIntenso}");
                return;
            }

            Memory.WriteBit(address, bit, true);
        }

        private void Client_MessageReceived(object? sender, Archipelago.Core.Models.MessageReceivedEventArgs e) {
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
            lock (_lockObject)
            {
                Application.Current.Dispatcher.DispatchAsync(() =>
                {
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
