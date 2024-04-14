INPUT_ROLLS = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE",
               "BDFHJLCPRTXVZNYEIWGAKMUSQO", "ESOVPZJAYQUIRHXLNFTGKDCMWB",
               "VZBRGITYUPSDNHLXAWMJQOFECK"]
OUTPUT_ROLLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
REVERSING_ROLLS = ["EJMZALYXVBWFCRQUONTSPIKHGD", "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                   "FVPJIAOYEDRZXWGCTKUQSBNMHL"]
NOTCHES = ["R", "F", "W", "K", "A"]

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


def set_position(roll_list, turn):
    return roll_list[turn:] + roll_list[:turn]


def char_to_int(letter):
    return ord(letter.upper()) - ord('A')


def int_to_char(number):
    return chr(number + ord('A'))


class Enigma:
    def __init__(self, roll_right, roll_right_pos, roll_middle, roll_middle_pos, roll_left, roll_left_pos,
                 reverse_roll, pegboard):
        self.rolls = [Roll(roll_right, roll_right_pos), Roll(roll_middle, roll_middle_pos),
                      Roll(roll_left, roll_left_pos)]
        self.reverse_roll = Reversing_roll(reverse_roll)
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


class Roll:
    def __init__(self, chosen_roll, start_position):
        self.input_roll = list(set_position(INPUT_ROLLS[chosen_roll], start_position))
        self.output_roll = list(set_position(OUTPUT_ROLLS, start_position))
        self.notch = NOTCHES[chosen_roll]
        self.start_position = start_position

    def rotate(self):
        self.input_roll = set_position(self.input_roll, 1)
        self.output_roll = set_position(self.output_roll, 1)

    def check_notch(self):
        if self.notch == self.output_roll[0]:
            return True

    def encrypt_left(self, letter_index):
        temp = self.input_roll[letter_index]
        for i, value in enumerate(self.output_roll):
            if temp == value:
                return i

    def encrypt_right(self, letter_index):
        temp = self.output_roll[letter_index]
        for i, value in enumerate(self.input_roll):
            if temp == value:
                return i


class Reversing_roll:
    def __init__(self, chosen_roll):
        self.input_roll = list(REVERSING_ROLLS[chosen_roll])
        self.output_roll = list(OUTPUT_ROLLS)

    def reverse(self, letter_index):
        temp = self.input_roll[letter_index]
        for i, value in enumerate(self.output_roll):
            if temp == value:
                return i


class Pegboard:
    def __init__(self, pegboard):
        self.pegboard = pegboard

    def select_letter(self, letter):
        for letter1, letter2 in self.pegboard:
            if letter.upper() == letter1:
                return letter2
            elif letter.upper() == letter2:
                return letter1
        return letter.upper()


if __name__ == "__main__":
    enigma = Enigma(ROLL_RIGHT, ROLL_RIGHT_POS, ROLL_MIDDLE, ROLL_MIDDLE_POS,
                    ROLL_LEFT, ROLL_LEFT_POS, ROLL_REVERSE, Pegboard(PEGBOARD))
    while True:
        enigma.start()
