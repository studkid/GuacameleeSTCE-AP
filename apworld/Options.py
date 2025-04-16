from dataclasses import dataclass
from Options import PerGameCommonOptions, Toggle, Range, Choice, StartInventoryPool

class TrueEnding(Toggle):
    """
    Require true ending to be achieved for goal.
    """
    display_name = "Require True Ending"

class ShuffleOrbs(Toggle):
    """
    Shuffle ChacMool Orb Locations.  If false, orbs will be placed in the vanilla locations.
    """
    display_name = "Shuffle Orbs"

class AvailableOrbs(Range):
    """
    Number of orbs to be placed into the world.
    Only applicable with 'Shuffle Orbs' set to true
    """
    display_name = "Available Orbs"
    range_start = 1
    range_end = 30
    default = 6

class RequiredOrbs(Range):
    """
    Number of orbs required to trigger the true ending.
    Only applicable with 'Shuffle Orbs' set to true
    """
    display_name = "Required Orbs"
    range_start = 1
    range_end = 30
    default = 6

class ShuffleInfierno(Choice):
    """
    Determines El Infierno medals behavior
    Vanilla: Unchanged
    Start With Medals: Start with all gold medals
    Single Medal: Beating a challenge room is a location.  Shuffles gold medals per challenge into the pool.
    All Medals: All medal requirements are locations.  Shuffles 3 progressive medals into the pool per challenge
    """
    display_name = "Shuffle Infierno Medals"
    option_vanilla = 0
    option_start_with_medals = 1
    option_single_medal = 2
    option_all_medals = 3
    default = 0

class MedalRequired(Choice):
    """
    Determines the medal time required for gold/location check in El Infierno
    """
    display_name = "Required Medal Goal"
    option_bronze = 0
    option_silver = 1
    option_gold = 2
    default = 2

class ShuffleAttacks(Toggle):
    """
    Shuffle grab, punch combo, lucahdor lift and downercut, and air kick combo into the item pool
    """
    display_name = "Shuffle Base Attacks"

class ShuffleDodge(Toggle):
    """
    Shuffle dodge ability
    """
    display_name = "Shuffle Dodge"

@dataclass 
class GuacOptions(PerGameCommonOptions):
    true_ending: TrueEnding
    shuffle_orbs: ShuffleOrbs
    available_orbs: AvailableOrbs
    required_orbs: RequiredOrbs
    shuffle_infierno: ShuffleInfierno
    shuffle_attacks: ShuffleAttacks
    shuffle_dodge: ShuffleDodge
    start_inventory_from_pool: StartInventoryPool