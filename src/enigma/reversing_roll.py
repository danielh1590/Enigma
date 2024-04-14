REVERSING_ROLLS = ["EJMZALYXVBWFCRQUONTSPIKHGD", "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                   "FVPJIAOYEDRZXWGCTKUQSBNMHL"]
OUTPUT_ROLLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class ReversingRoll:
    def __init__(self, chosen_roll):
        self.input_roll = list(REVERSING_ROLLS[chosen_roll])
        self.output_roll = list(OUTPUT_ROLLS)

    def reverse(self, letter_index):
        temp = self.input_roll[letter_index]
        for i, value in enumerate(self.output_roll):
            if temp == value:
                return i
