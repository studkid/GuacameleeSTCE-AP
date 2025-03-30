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

        // [[game.exe + 50CC04] + B4] + X
        public static uint GetChestFlag(uint address) {
            uint baseAddress = 0x00400000;
            uint initialAddress = baseAddress + 0x50cc04;

            var pointer1 = Memory.ReadUInt(initialAddress);
            var pointer2 = Memory.ReadUInt(pointer1 + 0xb4);
            var result = pointer2 + address;
            return result;
        }

        // [[game.exe + 51F710] + X] + 18
        public static uint GetSaveDataFlag(uint address) {
            uint baseAddress = 0x00400000;
            uint initialAddress = baseAddress + 0x51F710;

            var pointer1 = Memory.ReadUInt(initialAddress);
            var pointer2 = Memory.ReadUInt(pointer1 + address);
            var result = pointer2 + 0x18;
            return result;
        }

        // [[[[[[[[[game.exe + 50B214] + 4] + 150] + 64] + 60] + 60] + 2E0] + 70] + 52C] + X
        public static uint GetPolloFlag(uint address) {
            uint baseAddress = 0x00400000;
            uint initialAddress = baseAddress + 0x50B214;
            var pointer1 = Memory.ReadUInt(initialAddress);
            uint[] offsets = [0x4,0x150,0x64,0x60,0x60,0x2E0,0x70,0x52C];

            foreach(uint offset in offsets) {
                pointer1 = Memory.ReadUInt(pointer1 + offset);
            }
            
            var result = pointer1 + address;
            return result;
        }

        // [[[[[[[[[game.exe + 50B214] + 4] + 194] + 64] + 60] + 60] + 2E0] + 70] + 52C] + X
        public static uint GetPowerFlag(uint address) {
            uint baseAddress = 0x00400000;
            uint initialAddress = baseAddress + 0x50B214;
            var pointer1 = Memory.ReadUInt(initialAddress);
            uint[] offsets = [0x4,0x194,0x64,0x60,0x60,0x2E0,0x70,0x52C];

            foreach (uint offset in offsets) {
                pointer1 = Memory.ReadUInt(pointer1 + offset);
            }

            var result = pointer1 + address;
            return result;
        }

        // [[[[game.exe + 0051F3F0] + 10] + 64] + 6C] + X
        public static uint GetHealthFlag(uint address) {
            uint baseAddress = 0x00400000;
            uint initialAddress = baseAddress + 0x0051F3F0;
            var pointer1 = Memory.ReadUInt(initialAddress);
            uint[] offsets = [0x10,0x64,0x6C];

            foreach (uint offset in offsets) {
                pointer1 = Memory.ReadUInt(pointer1 + offset);
            }

            var result = pointer1 + address;
            return result;
        }

        // [[game.exe + 0051F3E0] + 0] + X
        public static uint GetStaminaFlag(uint address) {
            uint baseAddress = 0x00400000;
            uint initialAddress = baseAddress + 0x0051F3E0;

            var pointer1 = Memory.ReadUInt(initialAddress);
            var pointer2 = Memory.ReadUInt(pointer1 + 0x0);
            var result = pointer2 + address;
            return result;
        }
    }
}
