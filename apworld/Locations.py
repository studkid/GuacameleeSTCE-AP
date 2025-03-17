from BaseClasses import Location
from typing import Dict, List, TypeVar, NamedTuple, Optional

class GuacLocation(Location):
    game: str = "Guacamelee Super Turbo Champioship Edition"

class GuacLocationData(NamedTuple):
    area: str
    name: str
    type: str

location_table: List[GuacLocation] = {
    # Temple of Rain
    GuacLocationData("ToR", "Goat Jump Puzzle Chest", "chest"),
    GuacLocationData("ToR", "Near Entrance Omlec Chest", "chest"),
    GuacLocationData("ToR", "Omlec Wing Standalone Chest", "chest"),
    GuacLocationData("ToR", "Near Netrance Jump Puzzle Chest", "chest"),
    GuacLocationData("ToR", "Heart Chest Room 1", "chest"),
    GuacLocationData("ToR", "Heart Chest Room 2", "chest"),
    GuacLocationData("ToR", "Heart Chest Room 3", "chest"),
    GuacLocationData("ToR", "Heart Chest Room 4", "chest"),
    GuacLocationData("ToR", "Heart Chest Room 5", "chest"),
    GuacLocationData("ToR", "Heart Chest Room 6", "chest"),
    GuacLocationData("ToR", "Shortcut Chest", "chest"),
    GuacLocationData("ToR", "Before Alrbrije Chase Chest", "chest"),
    GuacLocationData("ToR", "After Alrbrije Chase Chest", "chest"),
    GuacLocationData("ToR", "Near Luchita Chest", "chest"),

    # Forest del Chivo
    GuacLocationData("FdC", "Near Pueblucho Chest", "chest"),
    GuacLocationData("FdC", "Lower Pollo Chest", "chest"),
    GuacLocationData("FdC", "Near Chivo Store Chest", "chest"),
    GuacLocationData("FdC", "Alcove Near Luchita Chest", "chest"),
    GuacLocationData("FdC", "Main Shaft Red Challenge Chest", "chest"),
    GuacLocationData("FdC", "Main Shaft Yellow Challenge Chest", "chest"),
    GuacLocationData("FdC", "Main Shaft Blue Challenge Chest", "chest"),
    GuacLocationData("FdC", "Near Tule Tree Chest", "chest"),
    GuacLocationData("FdC", "Chivo Alcove Chest", "chest"),
    GuacLocationData("FdC", "Chivo Pollo Chest", "chest"),
    GuacLocationData("FdC", "Main Shaft Green Challenge Chest", "chest"),
    GuacLocationData("FdC", "Skull Lever Chest", "chest"),
    GuacLocationData("FdC", "High Platform Chest", "chest"),
    GuacLocationData("FdC", "Near Canal Chest", "chest"),

    # Tule Tree
    GuacLocationData("TT", "Gold Coin Chest X180 Y145", "chest"),
    GuacLocationData("TT", "Health Chest X75 Y140", "chest"),
    GuacLocationData("TT", "Gold Coin Chest X270 Y250", "chest"),
    GuacLocationData("TT", "Silver Coin Chest X-125 Y345", "chest"),
    GuacLocationData("TT", "Gold Coin Chest X-40 Y325", "chest"),
    GuacLocationData("TT", "Health Chest X-90 Y325", "chest"),
    GuacLocationData("TT", "Stamina Chest X5 Y210", "chest"),
    GuacLocationData("TT", "Stamina Chest X175 Y465", "chest"),

    # Sierra Morena
    GuacLocationData("SM", "Intenso Chest X595 Y355", "chest"),
    GuacLocationData("SM", "Stamina Chest X340 Y110", "chest"),
    GuacLocationData("SM", "Gold Coin Chest X525 Y195", "chest"),
    GuacLocationData("SM", "Gold Coin Chest X685 Y260", "chest"),
    GuacLocationData("SM", "Silver Coin Chest X960 Y440", "chest"),
    GuacLocationData("SM", "Intenso Chest X1280 Y505", "chest"),
    GuacLocationData("SM", "Stamina Chest X2195 Y725", "chest"),
    GuacLocationData("SM", "Gold Coin Chest X2170 Y740", "chest"),

    # Pueblucho
    GuacLocationData("Pb", "Outside Church Chest", "chest"),
    GuacLocationData("Pb", "Pollo Chest", "chest"),
    GuacLocationData("Pb", "X'tabay Chest", "chest"),
    GuacLocationData("Pb", "Inside Church Chest", "chest"),

    # Great Temple
    GuacLocationData("GT", "Gold Coin Chest X5 Y275", "chest"),
    GuacLocationData("GT", "Intenso Chest X110 Y105", "chest"),
    GuacLocationData("GT", "Health Chest X40 Y405", "chest"),
    GuacLocationData("GT", "Intenso Chest X10 Y545", "chest"),
    GuacLocationData("GT", "Gold Coin Chest X-185 Y470", "chest"),
    GuacLocationData("GT", "Gold Coin Chest X5 Y50", "chest"),
    GuacLocationData("GT", "Silver Coin Chest X-55 Y815", "chest"),

    # Temple of War
    GuacLocationData("ToW", "Gold Coin Chest X180 Y-70", "chest"),
    GuacLocationData("ToW", "Gold Coin Chest X430 Y65", "chest"),
    GuacLocationData("ToW", "Health Chest X310 Y-120", "chest"),
    GuacLocationData("ToW", "Stamina Chest X-180 Y315", "chest"),
    GuacLocationData("ToW", "Stamina Chest X-200 Y280", "chest"),
    GuacLocationData("ToW", "Health Chest X460 Y65", "chest"),
    GuacLocationData("ToW", "Stamina Chest X485 Y180", "chest"),
    GuacLocationData("ToW", "Gold Coin Chest X370 Y145", "chest"),
    GuacLocationData("ToW", "Gold Coin Chest X235 Y185", "chest"),
    GuacLocationData("ToW", "Health Chest X135 Y165", "chest"),
    GuacLocationData("ToW", "Intenso Chest X135 Y225", "chest"),
    GuacLocationData("ToW", "Silver Coin Chest X-75 Y-120", "chest"),

    # Caverna del Pollo
    GuacLocationData("CdP", "Challegne 1 Chest", "chest"),
    GuacLocationData("CdP", "Challegne 2 Chest", "chest"),
    GuacLocationData("CdP", "Challegne 3 Chest", "chest"),

    #La Mansion del Presidente
    GuacLocationData("LmdP", "Platform Chest", "chest"),

    # Agave Field
    GuacLocationData("AF", "Juan House Chest", "chest"),

    # Santa Luchita
    GuacLocationData("SL", "Upper Inn Chest", "chest"),
    GuacLocationData("SL", "Lower Inn Chest", "chest"),
    GuacLocationData("SL", "Hernandos Chest", "chest"),
    GuacLocationData("SL", "Hernandos Pollo Chest", "chest"),
    GuacLocationData("SL", "Near Caverna Chest", "chest"),

    #Canal de las Flores
    GuacLocationData("CdlF", "Near Forest Left Chest", "chest"),
    GuacLocationData("CdlF", "Near Forest Right Chest", "chest"),
    GuacLocationData("CdlF", "Path to Bridge Chest", "chest"),
    GuacLocationData("CdlF", "Pollo Bomba West of Tower Chest", "chest"),
    GuacLocationData("CdlF", "Pollo Dimension Maze Chest", "chest"),
    GuacLocationData("CdlF", "Pollo Hole Chest", "chest"),
    GuacLocationData("CdlF", "Town Chest", "chest"),
    GuacLocationData("CdlF", "Near Choozo Chest", "chest"),
    GuacLocationData("CdlF", "Above Town Chest", "chest"),
    GuacLocationData("CdlF", "East of Town Chest", "chest"),
    GuacLocationData("CdlF", "Right of Ferry Chest", "chest"),
    GuacLocationData("CdlF", "Above Ferry Chest", "chest"),
    GuacLocationData("CdlF", "West of Town Chest", "chest"),
    GuacLocationData("CdlF", "Near Pico de Gallo Chest", "chest"),
    GuacLocationData("CdlF", "Bridge Jump Puzzle Chest", "chest"),
    GuacLocationData("CdlF", "Above Bridge Chest", "chest"),
    GuacLocationData("CdlF", "Baby Calaca Top Chest", "chest"),
    GuacLocationData("CdlF", "Baby Calaca Bottom Right Chest", "chest"),

    # Pico de Gallo
    GuacLocationData("PdG", "Gold Coin Chest X1655 Y390", "chest"),
    GuacLocationData("PdG", "Gold Coin Chest X1875 Y380", "chest"),
    GuacLocationData("PdG", "Gold Coin Chest X850 Y-30", "chest"),
    GuacLocationData("PdG", "Gold Coin Chest X740 Y-90", "chest"),
    GuacLocationData("PdG", "Gold Coin Chest X1600 Y260", "chest"),
    GuacLocationData("PdG", "Gold Coin Chest X1010 Y225", "chest"),
    GuacLocationData("PdG", "Gold Coin Chest X1025 Y270", "chest"),
    GuacLocationData("PdG", "Gold Coin Chest X1510 Y375", "chest"),
    GuacLocationData("PdG", "Health Chest X1620 Y0", "chest"),
    GuacLocationData("PdG", "Intenso Chest X1395 Y15", "chest"),
    GuacLocationData("PdG", "Stamina Chest X1660 Y315", "chest"),
    GuacLocationData("PdG", "Intenso Chest X1825 Y90", "chest"),
    GuacLocationData("PdG", "Gold Coin Chest X575 Y-120", "chest"),
    GuacLocationData("PdG", "Health Chest X570 Y-130", "chest"),
    GuacLocationData("PdG", "Stamina Chest X550 Y-120", "chest"),
    GuacLocationData("PdG", "Gold Coin Chest X1670 Y30", "chest"),
    GuacLocationData("PdG", "Silver Coin Chest X1340 Y355", "chest"),
    GuacLocationData("PdG", "Health Chest X1730 Y-65", "chest"),
    
    # Desierto Caliente
    GuacLocationData("DC", "Near Tule Tree Chest", "chest"),
    GuacLocationData("DC", "Near Luchita Chest", "chest"),
    GuacLocationData("DC", "Chupacabra Pollo Hole Chest", "chest"),
    GuacLocationData("DC", "Chupacabra Mound Chest", "chest"),
    GuacLocationData("DC", "Dimension Swap Platform Chest", "chest"),
    GuacLocationData("DC", "Under Overhang Chest", "chest"),
    GuacLocationData("DC", "Above Overhang Chest", "chest"),
    GuacLocationData("DC", "Near Temple of War Chest", "chest"),
    GuacLocationData("DC", "Pollo Above Shield Intro Chest", "chest"),
    GuacLocationData("DC", "Central Room Left Chest", "chest"),
    GuacLocationData("DC", "Central Room Right Chest", "chest"),
    GuacLocationData("DC", "Before Pollo Maze Lower Chest", "chest"),
    GuacLocationData("DC", "Before Pollo Maze Upper Chest", "chest"),
    GuacLocationData("DC", "Pollo Below Shield Intro Chest", "chest"),

    # El Infierno
    GuacLocationData("EI", "5000 Gold Coin Chest X-285 Y30", "chest"),
    GuacLocationData("DC", "Gold Coin Chest X-370 Y30", "chest"),
}