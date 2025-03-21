using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace MyGameAP {
    public class Helpers  {
        public static List<Archipelago.Core.Models.Location> GetLocations() {
            var json = OpenEmbeddedResource("MyGameAP.Resources.Locations.json");
            var list = JsonConvert.DeserializeObject<List<Archipelago.Core.Models.Location>>(json);
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
