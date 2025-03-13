using GuacameleeAP.Models;
using Newtonsoft.Json;
using System.Reflection;

namespace MyGameAP {
    public class Helpers {
        public static List<Archipelago.Core.Models.Location> GetLocations() {
            var json = OpenEmbeddedResource("GuacameleeAP.Resources.Locations.json");
            var list = JsonConvert.DeserializeObject<List<Archipelago.Core.Models.Location>>(json);
            return list;
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
    }
}
