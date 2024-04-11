INPUT_ROLLS = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE",
               "BDFHJLCPRTXVZNYEIWGAKMUSQO", "ESOVPZJAYQUIRHXLNFTGKDCMWB",
               "VZBRGITYUPSDNHLXAWMJQOFECK"]
OUTPUT_ROLLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
UKW = ["EJMZALYXVBWFCRQUONTSPIKHGD", "YRUHQSLDPXNGOKMIEBFZCWVJAT",
       "FVPJIAOYEDRZXWGCTKUQSBNMHL"]
NOTCHES = ["R", "F", "W", "K", "A"]


def set_position(roll_list, turn):
    return roll_list[turn:] + roll_list[:turn]


class Enigma:
    def __init__(self, roll_right, roll_right_pos, roll_middle, roll_middle_pos, roll_left, roll_left_pos):
        self.rolls = [Roll(roll_right, roll_right_pos), Roll(roll_middle, roll_middle_pos),
                      Roll(roll_left, roll_left_pos)]


class Roll:
    def __init__(self, chosen_roll, start_position):
        self.input_roll = list(set_position(INPUT_ROLLS[chosen_roll], start_position))
        self.output_roll = list(set_position(OUTPUT_ROLLS, start_position))
        self.notch = NOTCHES[chosen_roll]
        self.start_position = start_position

    def rotate(self):
        self.input_roll = set_position(self.input_roll, 1)
        self.output_roll = set_position(self.output_roll, 1)


class Ukw_roll:
    def __init__(self, chosen_roll):
        self.input_roll = list(UKW[chosen_roll])
        self.output_roll = list(OUTPUT_ROLLS)


if __name__ == "__main__":
    pass
