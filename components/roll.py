INPUT_ROLLS = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE",
               "BDFHJLCPRTXVZNYEIWGAKMUSQO", "ESOVPZJAYQUIRHXLNFTGKDCMWB",
               "VZBRGITYUPSDNHLXAWMJQOFECK"]
OUTPUT_ROLLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NOTCHES = ["R", "F", "W", "K", "A"]


def set_position(roll_list, turn):
    return roll_list[turn:] + roll_list[:turn]


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
