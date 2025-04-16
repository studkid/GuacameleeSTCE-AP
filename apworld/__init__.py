from .Options import GuacOptions
from .Items import item_table, base_id, GuacItem
from .Locations import location_table, GuacLocation

from BaseClasses import Region, Location, MultiWorld, Item, LocationProgressType, Tutorial
from worlds.AutoWorld import World, WebWorld
from typing import List, Dict, Any

class GuacWeb(WebWorld):
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Guacamelee STCE integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["studkid"]
    )

class GuacWorld(World):
    """
    Placeholder
    """
    game = "Guacamelee Super Turbo Champioship Edition"
    options_dataclass = GuacOptions
    options: GuacOptions
    topology_present = False

    item_name_to_id = {item.name: (item.id) for index, item in enumerate(item_table)}
    location_name_to_id = {loc.area + ": " + loc.name: (loc.id) for index, loc in enumerate(location_table)}

    required_client_version = (0, 6, 0)

    def create_items(self):
        itempool: List[str] = []
        orb_count = 6

        if self.options.shuffle_orbs:
            orb_count = self.options.available_orbs

        for item in item_table:
            count = item.count

            if item.name == "Orb":
                count = orb_count

            if item.category == "Attack" and not self.options.shuffle_attacks:
                continue

            if item.category == "Dodge" and not self.options.shuffle_dodge:
                continue

            if count <= 0:
                continue
            for _ in range(count):
                itempool.append(self.create_item(item.name))

        # fill remaining locations with gold coin filler
        while len(itempool) < len(location_table):
            itempool.append(self.create_item("500 Gold Coins"))

        self.multiworld.itempool += itempool

    def get_filler_item_name(self):
        return "500 Gold Coins"

    def create_item(self, name):
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id

        return GuacItem(name, item_table[id].item_type, item_id, player=self.player)
    
    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        menu.add_locations(self.location_name_to_id, GuacLocation)