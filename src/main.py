from src.enigma.pegboard import Pegboard
from src.enigma.reversing_roll import ReversingRoll
from src.enigma.roll import Roll

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


def char_to_int(letter):
    return ord(letter.upper()) - ord('A')


def int_to_char(number):
    return chr(number + ord('A'))


class Enigma:
    def __init__(self, roll_right, roll_right_pos, roll_middle, roll_middle_pos, roll_left, roll_left_pos,
                 reverse_roll, pegboard):
        self.rolls = [Roll(roll_right, roll_right_pos), Roll(roll_middle, roll_middle_pos),
                      Roll(roll_left, roll_left_pos)]
        self.reverse_roll = ReversingRoll(reverse_roll)
        self.pegboard = pegboard

    def start(self):
        input_letter_index = char_to_int(self.pegboard.select_letter(input("Enter a letter: ")))

        self.rolls[0].rotate()
        if self.rolls[0].check_notch():
            self.rolls[1].rotate()
        if self.rolls[1].check_notch():
            self.rolls[2].rotate()

        step0 = self.rolls[0].encrypt_left(input_letter_index)
        step1 = self.rolls[1].encrypt_left(step0)
        step2 = self.rolls[2].encrypt_left(step1)

        reversed_step = self.reverse_roll.reverse(step2)

        step3 = self.rolls[2].encrypt_right(reversed_step)
        step4 = self.rolls[1].encrypt_right(step3)
        step5 = self.rolls[0].encrypt_right(step4)

        res = self.pegboard.select_letter(int_to_char(step5))
        print(res)


if __name__ == "__main__":
    enigma = Enigma(ROLL_RIGHT, ROLL_RIGHT_POS, ROLL_MIDDLE, ROLL_MIDDLE_POS,
                    ROLL_LEFT, ROLL_LEFT_POS, ROLL_REVERSE, Pegboard(PEGBOARD))
    while True:
        enigma.start()