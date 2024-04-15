from src.enigma.enigma import Enigma
from src.enigma.helper_functions import get_rotor, get_rev_rotor
from src.enigma.pegboard import Pegboard
from gui.settings_window import SettingsWindow

ROLL_RIGHT = 0
ROLL_RIGHT_POS = 0
ROLL_MIDDLE = 0
ROLL_MIDDLE_POS = 0
ROLL_LEFT = 0
ROLL_LEFT_POS = 0
ROLL_REVERSE = 1

"""
PEGBOARD = [("C", "R"), ("P", "V"), ("A", "I"), ("D", "K"), ("O", "T"),
            ("M", "Q"), ("E", "U"), ("B", "X"), ("L", "N"), ("G", "J")]
"""
PEGBOARD = []

if __name__ == "__main__":

    settings_window = SettingsWindow()
    settings_window.show()
    values = settings_window.get_values()

    ROLL_RIGHT = get_rotor(values[0][0])
    ROLL_MIDDLE = get_rotor(values[0][1])
    ROLL_LEFT = get_rotor(values[0][2])
    ROLL_RIGHT_POS = int(values[1][0]) - 1
    ROLL_MIDDLE_POS = int(values[1][1]) - 1
    ROLL_LEFT_POS = int(values[1][2]) - 1
    REVERSE = get_rev_rotor(values[2])
    PEGBOARD = values[3]

    enigma = Enigma(ROLL_RIGHT, ROLL_RIGHT_POS, ROLL_MIDDLE, ROLL_MIDDLE_POS,
                    ROLL_LEFT, ROLL_LEFT_POS, ROLL_REVERSE, Pegboard(PEGBOARD))

    while True:
        enigma.start()
