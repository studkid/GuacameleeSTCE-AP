using Archipelago.Core.Util;
using Newtonsoft.Json;

namespace GuacameleeAP.Models {
    public class GuacameleeItem {
        public string Name { get; set; }
        public int Id { get; set; }
        [JsonConverter(typeof(HexToULongConverter))]
        public ulong Address { get; set; }
        public int AddressBit { get; set; }
    }
}
