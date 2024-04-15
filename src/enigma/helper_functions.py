def char_to_int(letter):
    return ord(letter.upper()) - ord('A')


def int_to_char(number):
    return chr(number + ord('A'))


def get_rotor(rotor_str):
    match rotor_str:
        case "Rotor I":
            return 0
        case "Rotor II":
            return 1
        case "Rotor III":
            return 2
        case "Rotor IV":
            return 3
        case "Rotor V":
            return 4


def get_rev_rotor(rotor_str):
    match rotor_str:
        case "Reversing Rotor A":
            return 0
        case "Reversing Rotor B":
            return 1
        case "Reversing Rotor C":
            return 2
