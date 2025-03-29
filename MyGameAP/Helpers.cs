using Archipelago.Core.Util;
using GuacameleeAP.Models;
using Newtonsoft.Json;
using Serilog;
using System.Reflection;

namespace MyGameAP {
    public class Helpers {
        public static List<Archipelago.Core.Models.Location> GetLocations() {
            List<Archipelago.Core.Models.Location> locations = new List<Archipelago.Core.Models.Location>();
            locations.AddRange(GetChestLocations());
            return locations;
        }

        public static List<Archipelago.Core.Models.Location> GetChestLocations() {
            List<Archipelago.Core.Models.Location> locations = new List<Archipelago.Core.Models.Location>();
            var json = OpenEmbeddedResource("GuacameleeAP.Resources.Chests.json");
            var list = JsonConvert.DeserializeObject<List<GuacameleeChest>>(json);

            foreach(var loc in list) {
                locations.Add(new Archipelago.Core.Models.Location {
                    Name = loc.Name,
                    Id = loc.Id,
                    CheckType = loc.CheckType,
                    Address = (ulong)GetChestFlag(loc.Address),
                    AddressBit = loc.AddressBit
                });
            }
            return locations;
        }

        public static List<GuacameleeItem> GetItems() {
            var json = OpenEmbeddedResource("GuacameleeAP.Resources.Items.json");
            var list = JsonConvert.DeserializeObject<List<GuacameleeItem>>(json);
            return list;
        }

        public static string OpenEmbeddedResource(string resourceName) {
            var assembly = Assembly.GetExecutingAssembly();
            using (Stream stream = assembly.GetManifestResourceStream(resourceName))
            using (StreamReader reader = new StreamReader(stream)) {
                string file = reader.ReadToEnd();
                return file;
            }
        }

        public static uint GetChestFlag(uint address) {
            uint baseAddress = 0x00400000;
            uint initialAddress = baseAddress + 0x50cc04;

            var pointer1 = Memory.ReadUInt(initialAddress);
            var pointer2 = Memory.ReadUInt(pointer1 + 0xb4);
            var result = pointer2 + address;
            Log.Logger.Information($"Address: {string.Format("0x{0:X}", address)} | Bit: {Memory.ReadInt(result)}");
            return result;
        }
    }
}
