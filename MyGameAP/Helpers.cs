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
                    Address = GetChestFlag(loc.Address),
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

        public static ulong OffsetPointer(ulong ptr,int offset) {
            ushort offsetWithin4GB = (ushort)(ptr & 0xFFFF);
            ushort newOffset = (ushort)(offsetWithin4GB + offset);
            ulong newAddress = (ptr & 0xFFFF0000) | newOffset;
            return newAddress;
        }

        public static ulong GetChestFlag(ulong address) {
            return Archipelago.Core.Util.Helpers.ResolvePointer(0x1721A3B8, [address]);
        }
    }
}
