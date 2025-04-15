from BaseClasses import Location
from typing import Dict, List, TypeVar, NamedTuple, Optional

class GuacLocation(Location):
    game: str = "Guacamelee Super Turbo Champioship Edition"

class GuacLocationData(NamedTuple):
    id: int
    area: str
    name: str
    type: str

location_table: List[GuacLocation] = {
    # Temple of Rain 1-50
    GuacLocationData(1, "ToR", "Goat Jump Puzzle Chest", "chest"),
    GuacLocationData(2, "ToR", "Near Entrance Omlec Chest", "chest"),
    GuacLocationData(3, "ToR", "Omlec Wing Standalone Chest", "chest"),
    GuacLocationData(4, "ToR", "Near Netrance Jump Puzzle Chest", "chest"),
    GuacLocationData(5, "ToR", "Heart Chest Room 1", "chest"),
    GuacLocationData(6, "ToR", "Heart Chest Room 2", "chest"),
    GuacLocationData(7, "ToR", "Heart Chest Room 3", "chest"),
    GuacLocationData(8, "ToR", "Heart Chest Room 4", "chest"),
    GuacLocationData(9, "ToR", "Heart Chest Room 5", "chest"),
    GuacLocationData(10, "ToR", "Heart Chest Room 6", "chest"),
    GuacLocationData(11, "ToR", "Shortcut Chest", "chest"),
    GuacLocationData(12, "ToR", "Before Alrbrije Chase Chest", "chest"),
    GuacLocationData(13, "ToR", "After Alrbrije Chase Chest", "chest"),
    GuacLocationData(14, "ToR", "Near Luchita Chest", "chest"),

    # Forest del Chivo 50-99
    GuacLocationData(51, "FdC", "Near Pueblucho Chest", "chest"),
    GuacLocationData(52, "FdC", "Lower Pollo Chest", "chest"),
    GuacLocationData(53, "FdC", "Near Chivo Store Chest", "chest"),
    GuacLocationData(54, "FdC", "Alcove Near Luchita Chest", "chest"),
    GuacLocationData(55, "FdC", "Main Shaft Red Challenge Chest", "chest"),
    GuacLocationData(56, "FdC", "Main Shaft Yellow Challenge Chest", "chest"),
    GuacLocationData(57, "FdC", "Main Shaft Blue Challenge Chest", "chest"),
    GuacLocationData(58, "FdC", "Near Tule Tree Chest", "chest"),
    GuacLocationData(59, "FdC", "Chivo Alcove Chest", "chest"),
    GuacLocationData(60, "FdC", "Chivo Pollo Chest", "chest"),
    GuacLocationData(61, "FdC", "Main Shaft Green Challenge Chest", "chest"),
    GuacLocationData(62, "FdC", "Skull Lever Chest", "chest"),
    GuacLocationData(63, "FdC", "High Platform Chest", "chest"),
    GuacLocationData(64, "FdC", "Near Canal Chest", "chest"),

    # Tule Tree 101-150
    GuacLocationData(101,"TT","4F Outside Chest","chest"),
    GuacLocationData(102,"TT","5F Inside Chest","chest"),
    GuacLocationData(103,"TTP","9F Outside Chest","chest"),
    GuacLocationData(104,"TT","12F Fight Chest","chest"),
    GuacLocationData(105,"TT","12F Pollo Chest","chest"),
    GuacLocationData(106,"TT","12F Jump Puzzle Chest","chest"),
    GuacLocationData(107,"TT","6F Outside Chest","chest"),
    GuacLocationData(108,"TT","13F Outside Chest","chest"),

    # Sierra Morena 151-200
    GuacLocationData(151,"SM","Near Upper Pico De Gallo Chest","chest"),
    GuacLocationData(152,"SM","Near Luchita Chest","chest"),
    GuacLocationData(153,"SM","Dimension Swap Climb Chest","chest"),
    GuacLocationData(154,"SM","Near Lower Pico De Gallo Chest","chest"),
    GuacLocationData(155,"SM","Hidden Goat Fly Chest","chest"),
    GuacLocationData(156,"SM","Hidden Goat Fly And Climb Chest","chest"),
    GuacLocationData(157,"SM","Near Great Temple Lower Chest","chest"),
    GuacLocationData(158,"SM","Near Great Temple Upper Chest","chest"),

    # Pueblucho 201-250
    GuacLocationData(201, "Pb", "Outside Church Chest", "chest"),
    GuacLocationData(202, "Pb", "Pollo Chest", "chest"),
    GuacLocationData(203, "Pb", "X'tabay Chest", "chest"),
    GuacLocationData(204, "Pb", "Inside Church Chest", "chest"),

    # Great Temple 251-300
    GuacLocationData(251,"GT","Pollo Maze Chest","chest"),
    GuacLocationData(252,"GT","Near Entrance Jump Puzzle Chest","chest"),
    GuacLocationData(253,"GT","Goat Fly Puzzle Chest","chest"),
    GuacLocationData(254,"GT","Pollo Hole Chest","chest"),
    GuacLocationData(255,"GT","Alux Fight Chest","chest"),
    GuacLocationData(256,"GT","Barrel Room Near Sierra Chest","chest"),
    GuacLocationData(257,"GT","WarpMazeChest","chest"),

    # Temple of War 301-350
    GuacLocationData(301,"ToW","Dead End Chest","chest"),
    GuacLocationData(302,"ToW","Pollo Hole Chest","chest"),
    GuacLocationData(303,"ToW","Cactus Jump Puzzle Chest","chest"),
    GuacLocationData(304,"ToW","After Flame Face Chest","chest"),
    GuacLocationData(305,"ToW","Goat Climb Chute Chest","chest"),
    GuacLocationData(306,"ToW","Wall Slide Puzzle Chest","chest"),
    GuacLocationData(307,"ToW","Blue Block Jump Puzzle Chest","chest"),
    GuacLocationData(308,"ToW","Halfway Blue Block Chest","chest"),
    GuacLocationData(309,"ToW","Cactus Exploder Fight Chest","chest"),
    GuacLocationData(310,"ToW","Upper Side Room Chest","chest"),
    GuacLocationData(311,"ToW","Upper Jump Puzzle Chest","chest"),
    GuacLocationData(312,"ToW","Entrance Pollo Bomba Chest","chest"),

    # Caverna del Pollo 351-400
    GuacLocationData(351, "CdP", "Challegne 1 Chest", "chest"),
    GuacLocationData(352, "CdP", "Challegne 2 Left Chest", "chest"),
    GuacLocationData(353, "CdP", "Challegne 2 Right Chest", "chest"),

    #La Mansion del Presidente 400
    GuacLocationData(400, "LmdP", "Platform Chest", "chest"),

    # Agave Field
    GuacLocationData(401, "AF", "Juan House Chest", "chest"),

    # Santa Luchita 451-500
    GuacLocationData(451, "SL", "Upper Inn Chest", "chest"),
    GuacLocationData(452, "SL", "Lower Inn Chest", "chest"),
    GuacLocationData(453, "SL", "Hernandos Chest", "chest"),
    GuacLocationData(454, "SL", "Hernandos Pollo Chest", "chest"),
    GuacLocationData(455, "SL", "Near Caverna Chest", "chest"),

    #Canal de las Flores 501-550
    GuacLocationData(501, "CdlF", "Near Forest Left Chest", "chest"),
    GuacLocationData(502, "CdlF", "Near Forest Right Chest", "chest"),
    GuacLocationData(503, "CdlF", "Path to Bridge Chest", "chest"),
    GuacLocationData(504, "CdlF", "Pollo Bomba West of Tower Chest", "chest"),
    GuacLocationData(505, "CdlF", "Pollo Dimension Maze Chest", "chest"),
    GuacLocationData(506, "CdlF", "Pollo Hole Chest", "chest"),
    GuacLocationData(507,"CdlF", "Town Chest", "chest"),
    GuacLocationData(508, "CdlF", "Near Choozo Chest", "chest"),
    GuacLocationData(509, "CdlF", "Above Town Chest", "chest"),
    GuacLocationData(510, "CdlF", "East of Town Chest", "chest"),
    GuacLocationData(511, "CdlF", "Right of Ferry Chest", "chest"),
    GuacLocationData(512, "CdlF", "Above Ferry Chest", "chest"),
    GuacLocationData(513, "CdlF", "West of Town Chest", "chest"),
    GuacLocationData(514, "CdlF", "Near Pico de Gallo Chest", "chest"),
    GuacLocationData(515, "CdlF", "Bridge Jump Puzzle Chest", "chest"),
    GuacLocationData(516, "CdlF", "Above Bridge Chest", "chest"),
    GuacLocationData(517,"CdlF","Clubhouse Top Chest","chest"),
    GuacLocationData(518,"CdlF","Clubhouse Bottom Left Chest","chest"),
    GuacLocationData(519,"CdlF","Clubhouse Bottom Right Chest","chest"),

    # Pico de Gallo 551-600
    GuacLocationData(551,"PdG","Lava Goat Fly Passage High Chest","chest"),
    GuacLocationData(552,"PdG","Chute Chest","chest"),
    GuacLocationData(553,"PdG","Outside Above Entrance Chest","chest"),
    GuacLocationData(554,"PdG","Destroyed Town Chest","chest"),
    GuacLocationData(555,"PdG","Dashing Derpderp Passage Chest","chest"),
    GuacLocationData(556,"PdG","Pollo Bomba Jump Puzzle Chest","chest"),
    GuacLocationData(557,"PdG","Pollo Bomba Chest","chest"),
    GuacLocationData(558,"PdG","Lava Goat Fly Passage Low Chest","chest"),
    GuacLocationData(559,"PdG","Inside Near Entrance Pollo Chest","chest"),
    GuacLocationData(560,"PdG","Skeleton Room Chest","chest"),
    GuacLocationData(561,"PdG","Near Choozo Chest","chest"),
    GuacLocationData(562,"PdG","Spinning Block Arena Chest","chest"),
    GuacLocationData(563,"PdG","Void Alux Quest Chest 1","chest"),
    GuacLocationData(564,"PdG","Void Alux Quest Chest 2","chest"),
    GuacLocationData(565,"PdG","Void Alux Quest Chest 3","chest"),
    GuacLocationData(566,"PdG","Lava Filled Passage Chest","chest"),
    GuacLocationData(567,"PdG","Near Sierra Exit Chest","chest"),
    GuacLocationData(568,"PdG","Moving Gear Jump Puzzle Chest","chest"),
    
    # Desierto Caliente 601-650
    GuacLocationData(601, "DC", "Near Tule Tree Chest", "chest"),
    GuacLocationData(602, "DC", "Near Luchita Chest", "chest"),
    GuacLocationData(603, "DC", "Chupacabra Pollo Hole Chest", "chest"),
    GuacLocationData(604, "DC", "Chupacabra Mound Chest", "chest"),
    GuacLocationData(605, "DC", "Dimension Swap Platform Chest", "chest"),
    GuacLocationData(606, "DC", "Under Overhang Chest", "chest"),
    GuacLocationData(607, "DC", "Above Overhang Chest", "chest"),
    GuacLocationData(608, "DC", "Near Temple of War Chest", "chest"),
    GuacLocationData(609, "DC", "Pollo Above Shield Intro Chest", "chest"),
    GuacLocationData(610, "DC", "Central Room Left Chest", "chest"),
    GuacLocationData(611, "DC", "Central Room Right Chest", "chest"),
    GuacLocationData(612, "DC", "Before Pollo Maze Lower Chest", "chest"),
    GuacLocationData(613, "DC", "Before Pollo Maze Upper Chest", "chest"),
    GuacLocationData(614, "DC", "Pollo Below Shield Intro Chest", "chest"),

    # El Infierno 651-700
    GuacLocationData(651,"EI","Silver Room Chest","chest"),
    GuacLocationData(652,"EI","Bronze Room Chest","chest"),
}