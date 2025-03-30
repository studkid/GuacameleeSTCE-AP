using Archipelago.Core.Util;
using Newtonsoft.Json;

namespace GuacameleeAP.Models {
    public class GuacameleeItem {
        public string Name { get; set; }
        public int Id { get; set; }
        [JsonConverter(typeof(HexToUIntConverter))]
        public uint Address { get; set; }
        [JsonConverter(typeof(HexToUIntConverter))]
        public uint SaveAddress { get; set; }
        public int AddressBit { get; set; }
        public string Category { get; set; }
    }
}
