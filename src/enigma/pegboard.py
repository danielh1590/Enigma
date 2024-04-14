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
