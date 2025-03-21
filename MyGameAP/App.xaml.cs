using Archipelago.Core;
using Archipelago.Core.MauiGUI;
using Archipelago.Core.MauiGUI.Models;
using Archipelago.Core.MauiGUI.ViewModels;
using Archipelago.Core.Models;
using Archipelago.Core.Util;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using Archipelago.MultiClient.Net.MessageLog.Messages;
using Newtonsoft.Json;
using Serilog;

namespace MyGameAP {
    public partial class App : Application {
        static MainPageViewModel Context;
        public static ArchipelagoClient Client { get; set; }
        private DeathLinkService _deathlinkService;
        private static readonly object _lockObject = new object();
        public App() {
            InitializeComponent();

            Context = new MainPageViewModel();
            Context.ConnectClicked += Context_ConnectClicked;
            Context.CommandReceived += (e,a) => {
                Client?.SendMessage(a.Command);
            };
            MainPage = new MainPage(Context);
            Context.ConnectButtonEnabled = true;
        }
        private async void Context_ConnectClicked(object? sender,ConnectClickedEventArgs e) {
            Context.ConnectButtonEnabled = false;
            Log.Logger.Information("Connecting...");
            if (Client != null) {
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

            await Client.Connect(e.Host,"My Game");

            Client.ItemReceived += Client_ItemReceived;
            Client.MessageReceived += Client_MessageReceived;

            await Client.Login(e.Slot,!string.IsNullOrWhiteSpace(e.Password) ? e.Password : null);

            //if (Client.Options.ContainsKey("EnableDeathlink") && (bool)Client.Options["EnableDeathlink"]) {
            //    var _deathlinkService = Client.EnableDeathLink();
            //    _deathlinkService.OnDeathLinkReceived += _deathlinkService_OnDeathLinkReceived;
            //    //ToDo listen for player death
            //}

            var myLocations = Helpers.GetLocations();

            //var goalLocation = myLocations.First(x => x.Name.Contains("GoalLocationName"));
            //Memory.MonitorAddressBitForAction(goalLocation.Address,goalLocation.AddressBit,() => Client.SendGoalCompletion());

            //Client.MonitorLocations(myLocations);

            Context.ConnectButtonEnabled = true;
        }

        private void _deathlinkService_OnDeathLinkReceived(DeathLink deathLink) {
            //Todo kill player
        }
        private static void Client_ItemReceived(object? sender,ItemReceivedEventArgs e) {
            LogItem(e.Item);
            var itemId = e.Item.Id;
            // Todo Give the player the item
        }
        private void Client_MessageReceived(object? sender,Archipelago.Core.Models.MessageReceivedEventArgs e) {
            if (e.Message.Parts.Any(x => x.Text == "[Hint]: ")) {
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

            if (Context.HintList.Any(x => x.TextSpans.Select(y => y.Text) == newMessage)) {
                return; //Hint already in list
            }
            List<TextSpan> spans = new List<TextSpan>();
            foreach (var part in message.Parts) {
                spans.Add(new TextSpan() { Text = part.Text,TextColor = Color.FromRgb(part.Color.R,part.Color.G,part.Color.B) });
            }
            lock (_lockObject) {
                Application.Current.Dispatcher.DispatchAsync(() => {
                    Context.HintList.Add(new LogListItem(spans));
                });
            }
        }
        private static void OnConnected(object sender,EventArgs args) {
            Log.Logger.Information("Connected to Archipelago");
            Log.Logger.Information($"Playing {Client.CurrentSession.ConnectionInfo.Game} as {Client.CurrentSession.Players.GetPlayerName(Client.CurrentSession.ConnectionInfo.Slot)}");
        }

        private static void OnDisconnected(object sender,EventArgs args) {
            Log.Logger.Information("Disconnected from Archipelago");
        }
        protected override Window CreateWindow(IActivationState activationState) {
            var window = base.CreateWindow(activationState);
            if (DeviceInfo.Current.Platform == DevicePlatform.WinUI) {
                window.Title = "Guacamelee STCE Archipelago Randomizer";

            }
            window.Width = 600;

            return window;
        }
    }
}