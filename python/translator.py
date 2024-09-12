import sys

# Init map to do looks from English to Braille
braille = {
    'a': "O.....",
    'b': "O.O...", 
    'c': "OO....", 
    'd': "OO.O..", 
    'e': "O..O..", 
    'f': "OOO...", 
    'g': "OOOO..", 
    'h': "O.OO..", 
    'i': ".OO...", 
    'j': ".OOO..", 
    'k': "O...O.", 
    'l': "O.O.O.", 
    'm': "OO..O.", 
    'n': "OO.OO.", 
    'o': "O..OO.", 
    'p': "OOO.O.", 
    'q': "OOOOO.", 
    'r': "O.OOO.", 
    's': ".OO.O.", 
    't': ".OOOO.", 
    'u': "O...OO", 
    'v': "O.O.OO", 
    'w': ".OOO.O", 
    'x': "OO..OO", 
    'y': "OO.OOO", 
    'z': "O..OOO",
    '1': "O.....", 
    '2': "O.O...", 
    '3': "OO....", 
    '4': "OO.O..", 
    '5': "O..O..", 
    '6': "OOO...", 
    '7': "OOOO..", 
    '8': "O.OO..", 
    '9': ".OO...", 
    '0': ".OOO.."
}

caps_follow = ".....O"
nums_follow = ".O.OOO"
braile_space = "......"

# Checks for type
def braille_check(text: str) -> bool:
    for char in text:
        if char != '.' and char != 'O':
            return False

    return len(text) % 6 == 0

# Handles english chars input
def english_to_braille(text: str) -> str:
    braille_output = []
    number_follows = False

    for char in text:
        if char.isdigit() and not number_follows:
            braille_output.append(nums_follow)
            number_follows = True
        elif not char.isdigit() and number_follows:
            number_follows = False

        if char.isupper():
            braille_output.append(caps_follow)
            char = char.lower()

        if char.isdigit():
            braille_output.append(braille[char])
        elif char == ' ':
            braille_output.append(braile_space)
        elif char.isalpha():
            braille_output.append(braille[char])

    return ''.join(braille_output)

# Handles braille to enlgish chars
def braille_to_english(braille: str) -> str:
    braille_input = []
    for i in range(0, len(braille), 6):
        braille_input.append(braille[i:i+6])

    text_output = []
    number_follows = False
    capitalize_follows = False

    for symbol in braille_input:
        if symbol == caps_follow:
            capitalize_follows = True
            continue
        elif symbol == nums_follow:
            number_follows = True
            continue
        elif symbol == braile_space:
            text_output.append(' ')
            number_follows = False
            continue

        if number_follows:
            for num, braille_num in braille.items():
                if symbol == braille_num:
                    text_output.append(num)
                    break
        else:
            for letter, braille_letter in braille.items():
                if symbol == braille_letter:
                    if capitalize_follows:
                        text_output.append(letter.upper())
                        capitalize_follows = False
                    else:
                        text_output.append(letter)
                    break

    return ''.join(text_output)


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input>")
        sys.exit(1)

    input_string = sys.argv[1] if len(sys.argv) >= 2 else '' 
    for i in range(2, len(sys.argv)):
        input_string = f'{input_string} {sys.argv[i]}'

    if braille_check(input_string):
        print(braille_to_english(input_string).strip())
    else:
        print(english_to_braille(input_string).strip())

if __name__ == "__main__":
    main()