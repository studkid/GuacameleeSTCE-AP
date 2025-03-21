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
    GuacLocationData(101, "TT", "Gold Coin Chest X180 Y145", "chest"),
    GuacLocationData(102, "TT", "Health Chest X75 Y140", "chest"),
    GuacLocationData(103, "TT", "Gold Coin Chest X270 Y250", "chest"),
    GuacLocationData(104, "TT", "Silver Coin Chest X-125 Y345", "chest"),
    GuacLocationData(105, "TT", "Gold Coin Chest X-40 Y325", "chest"),
    GuacLocationData(106, "TT", "Health Chest X-90 Y325", "chest"),
    GuacLocationData(107, "TT", "Stamina Chest X5 Y210", "chest"),
    GuacLocationData(108, "TT", "Stamina Chest X175 Y465", "chest"),

    # Sierra Morena 151-200
    GuacLocationData(151, "SM", "Intenso Chest X595 Y355", "chest"),
    GuacLocationData(152, "SM", "Stamina Chest X340 Y110", "chest"),
    GuacLocationData(153, "SM", "Gold Coin Chest X525 Y195", "chest"),
    GuacLocationData(154, "SM", "Gold Coin Chest X685 Y260", "chest"),
    GuacLocationData(155, "SM", "Silver Coin Chest X960 Y440", "chest"),
    GuacLocationData(156, "SM", "Intenso Chest X1280 Y505", "chest"),
    GuacLocationData(157, "SM", "Stamina Chest X2195 Y725", "chest"),
    GuacLocationData(158, "SM", "Gold Coin Chest X2170 Y740", "chest"),

    # Pueblucho 201-250
    GuacLocationData(201, "Pb", "Outside Church Chest", "chest"),
    GuacLocationData(202, "Pb", "Pollo Chest", "chest"),
    GuacLocationData(203, "Pb", "X'tabay Chest", "chest"),
    GuacLocationData(204, "Pb", "Inside Church Chest", "chest"),

    # Great Temple 251-300
    GuacLocationData(251, "GT", "Gold Coin Chest X5 Y275", "chest"),
    GuacLocationData(252, "GT", "Intenso Chest X110 Y105", "chest"),
    GuacLocationData(253, "GT", "Health Chest X40 Y405", "chest"),
    GuacLocationData(254, "GT", "Intenso Chest X10 Y545", "chest"),
    GuacLocationData(255, "GT", "Gold Coin Chest X-185 Y470", "chest"),
    GuacLocationData(256, "GT", "Gold Coin Chest X5 Y50", "chest"),
    GuacLocationData(257, "GT", "Silver Coin Chest X-55 Y815", "chest"),

    # Temple of War 301-350
    GuacLocationData(301, "ToW", "Gold Coin Chest X180 Y-70", "chest"),
    GuacLocationData(302, "ToW", "Gold Coin Chest X430 Y65", "chest"),
    GuacLocationData(303, "ToW", "Health Chest X310 Y-120", "chest"),
    GuacLocationData(304, "ToW", "Stamina Chest X-180 Y315", "chest"),
    GuacLocationData(305, "ToW", "Stamina Chest X-200 Y280", "chest"),
    GuacLocationData(306, "ToW", "Health Chest X460 Y65", "chest"),
    GuacLocationData(307, "ToW", "Stamina Chest X485 Y180", "chest"),
    GuacLocationData(308, "ToW", "Gold Coin Chest X370 Y145", "chest"),
    GuacLocationData(309, "ToW", "Gold Coin Chest X235 Y185", "chest"),
    GuacLocationData(310, "ToW", "Health Chest X135 Y165", "chest"),
    GuacLocationData(311, "ToW", "Intenso Chest X135 Y225", "chest"),
    GuacLocationData(312, "ToW", "Silver Coin Chest X-75 Y-120", "chest"),

    # Caverna del Pollo 351-400
    GuacLocationData(351, "CdP", "Challegne 1 Chest", "chest"),
    GuacLocationData(352, "CdP", "Challegne 2 Chest", "chest"),
    GuacLocationData(353, "CdP", "Challegne 3 Chest", "chest"),

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
    GuacLocationData(517, "CdlF", "Baby Calaca Top Chest", "chest"),
    GuacLocationData(518, "CdlF", "Baby Calaca Bottom Right Chest", "chest"),

    # Pico de Gallo 551-600
    GuacLocationData(551, "PdG", "Gold Coin Chest X1655 Y390", "chest"),
    GuacLocationData(552, "PdG", "Gold Coin Chest X1875 Y380", "chest"),
    GuacLocationData(553, "PdG", "Gold Coin Chest X850 Y-30", "chest"),
    GuacLocationData(554, "PdG", "Gold Coin Chest X740 Y-90", "chest"),
    GuacLocationData(555, "PdG", "Gold Coin Chest X1600 Y260", "chest"),
    GuacLocationData(556, "PdG", "Gold Coin Chest X1010 Y225", "chest"),
    GuacLocationData(557, "PdG", "Gold Coin Chest X1025 Y270", "chest"),
    GuacLocationData(558, "PdG", "Gold Coin Chest X1510 Y375", "chest"),
    GuacLocationData(559, "PdG", "Health Chest X1620 Y0", "chest"),
    GuacLocationData(560, "PdG", "Intenso Chest X1395 Y15", "chest"),
    GuacLocationData(561, "PdG", "Stamina Chest X1660 Y315", "chest"),
    GuacLocationData(562, "PdG", "Intenso Chest X1825 Y90", "chest"),
    GuacLocationData(563, "PdG", "Gold Coin Chest X575 Y-120", "chest"),
    GuacLocationData(564, "PdG", "Health Chest X570 Y-130", "chest"),
    GuacLocationData(565, "PdG", "Stamina Chest X550 Y-120", "chest"),
    GuacLocationData(566, "PdG", "Gold Coin Chest X1670 Y30", "chest"),
    GuacLocationData(567, "PdG", "Silver Coin Chest X1340 Y355", "chest"),
    GuacLocationData(568, "PdG", "Health Chest X1730 Y-65", "chest"),
    
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
    GuacLocationData(651, "EI", "5000 Gold Coin Chest X-285 Y30", "chest"),
    GuacLocationData(652, "DC", "Gold Coin Chest X-370 Y30", "chest"),
}