from typing import Dict, List, NamedTuple
from BaseClasses import Item, ItemClassification

base_id = 1

class GuacItem(Item):
    game: str = "Guacamelee Super Turbo Champioship Edition"

class GuacItemData(NamedTuple):
    name: str
    count: int
    item_type: ItemClassification

item_table: List[GuacItemData] = [
    # Attacks
    GuacItemData("Olmec Headbutt", 1, ItemClassification.progression),
    GuacItemData("Dashing Derp Derp", 1, ItemClassification.progression),
    GuacItemData("Rooster Uppercut", 1, ItemClassification.progression),
    GuacItemData("Frog Slam", 1, ItemClassification.progression),
    GuacItemData("Intenso", 1, ItemClassification.progression),
    GuacItemData("Pollo Bomba", 1, ItemClassification.progression),

    # Abilities
    GuacItemData("Pollo Power", 1, ItemClassification.progression),
    GuacItemData("Dimension Swap", 1, ItemClassification.progression),
    GuacItemData("Double Jump", 1, ItemClassification.progression),
    GuacItemData("Goat Jump", 1, ItemClassification.progression),
    GuacItemData("Goat Climb", 1, ItemClassification.progression),
    GuacItemData("Goat Fly", 1, ItemClassification.progression),
    GuacItemData("Pollo Fly", 1, ItemClassification.progression),

    # Misc
    GuacItemData("Health Chunk", 33, ItemClassification.useful),
    GuacItemData("Stamina Chunk", 20, ItemClassification.useful),
    GuacItemData("Intenso Chunk", 9, ItemClassification.useful),
    GuacItemData("Orb Chunk", 6, ItemClassification.progression),
    GuacItemData("500 Gold Coins", 1, ItemClassification.filler),
    GuacItemData("5000 Gold Coins", 2, ItemClassification.filler),
    GuacItemData("5 Silver Coins", 13, ItemClassification.progression),
    GuacItemData("Enemy Trap", 5, ItemClassification.trap)
]