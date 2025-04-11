using Archipelago.Core.Models;
using Archipelago.Core.Util;
using Newtonsoft.Json;

namespace GuacameleeAP.Models {
    public class GuacameleeLocation {
        public string Name { get; set; }
        public int Id { get; set; }
        [JsonConverter(typeof(HexToUIntConverter))]
        public uint Address { get; set; }
        public LocationCheckType CheckType { get; set; }
        public int AddressBit { get; set; }
        public string Category { get; set; }
    }
}
