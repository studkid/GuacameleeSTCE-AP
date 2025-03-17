from dataclasses import dataclass
from Options import PerGameCommonOptions, Toggle, DefaultOnToggle

class Nothing(Toggle):
    """Placeholder"""
    display_name = "Placeholder Setting"

@dataclass 
class GuacOptions(PerGameCommonOptions):
    placeholder: Nothing
