from typing import Dict, List, NamedTuple
from BaseClasses import Item, ItemClassification

base_id = 1

class GuacItem(Item):
    game: str = "Guacamelee Super Turbo Champioship Edition"

class GuacItemData(NamedTuple):
    id: int
    name: str
    count: int
    item_type: ItemClassification
    category: str

item_table: List[GuacItemData] = [
    # Attacks
    GuacItemData(1, "Olmec Headbutt", 1, ItemClassification.progression, "Power"),
    GuacItemData(2, "Dashing Derp Derp", 1, ItemClassification.progression, "Power"),
    GuacItemData(3, "Rooster Uppercut", 1, ItemClassification.progression, "Power"),
    GuacItemData(4, "Frog Slam", 1, ItemClassification.progression, "Power"),
    GuacItemData(5, "Intenso", 1, ItemClassification.progression, "Power"),
    GuacItemData(6, "Pollo Bomba", 1, ItemClassification.progression, "Power"),

    # Abilities
    GuacItemData(7, "Pollo Power", 1, ItemClassification.progression, "Ability"),
    GuacItemData(8, "Dimension Swap", 1, ItemClassification.progression, "Ability"),
    GuacItemData(9, "Double Jump", 1, ItemClassification.progression, "Ability"),
    GuacItemData(10, "Goat Jump", 1, ItemClassification.progression, "Ability"),
    GuacItemData(11, "Goat Climb", 1, ItemClassification.progression, "Ability"),
    GuacItemData(12, "Goat Fly", 1, ItemClassification.progression, "Ability"),
    GuacItemData(13, "Pollo Fly", 1, ItemClassification.progression, "Ability"),

    # Misc
    GuacItemData(14, "Health Chunk", 33, ItemClassification.useful, "Stat"),
    GuacItemData(15, "Stamina Chunk", 20, ItemClassification.useful, "Stat"),
    GuacItemData(16, "Intenso Chunk", 9, ItemClassification.useful, "Stat"),
    GuacItemData(17, "Orb", 6, ItemClassification.progression, "Orb"), 
    GuacItemData(18, "500 Gold Coins", 0, ItemClassification.filler, "Filler"),
    GuacItemData(19, "5000 Gold Coins", 2, ItemClassification.filler, "Filler"),
    GuacItemData(20, "5 Silver Coins", 0, ItemClassification.progression, "Filler"),
    # GuacItemData(50, "Enemy Trap", 5, ItemClassification.trap)

    # Base Abilities
    GuacItemData(21, "Grab Ability", 1, ItemClassification.progression, "Attack"),
    GuacItemData(22, "Dodge", 1, ItemClassification.progression, "Dodge"),
    GuacItemData(23, "Punch Combo", 1, ItemClassification.progression, "Attack"),
    GuacItemData(24, "Luchador Lift", 1, ItemClassification.progression, "Attack"),
    GuacItemData(25, "Downercut", 1, ItemClassification.progression, "Attack"),
    GuacItemData(26, "Air Kick Combo", 1, ItemClassification.progression, "Attack"),
]