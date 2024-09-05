import sys

alphabets = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO"
}

numbers = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

special_cases = {
    "capital_follows": ".....O",
    "decimal_follows": ".O...O",
    "number_follows": ".O.OOO"
}

special_characters = {
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
}


def braille_to_word(word):
    capital_letter = False
    answer_string = ""
    decimal_follows = False
    number_follows = False

    for i in range(0, len(word), 6):
        braille = word[i:i + 6]

        if braille in special_cases.values():
            if braille == special_cases["capital_follows"]:
                capital_letter = True
            elif braille == special_cases["decimal_follows"]:
                decimal_follows = True
            elif braille == special_cases["number_follows"]:
                number_follows = True

        elif number_follows:
            value = [encoding for encoding, decoding in numbers.items() if decoding == braille]
            if value:
                answer_string += value[0]
            else:
                answer_string += "?"
            number_follows = True if braille in numbers.values() else False

        elif decimal_follows:
            value = [encoding for encoding, decoding in special_characters.items() if decoding == braille]
            if value:
                answer_string += value[0]
            decimal_follows = False

        elif braille in alphabets.values():
            value = [encoding for encoding, decoding in alphabets.items() if decoding == braille]
            if value:
                answer_string += value[0].capitalize() if capital_letter else value[0]
                capital_letter = False

        else:
            value = [encoding for encoding, decoding in special_characters.items() if decoding == braille]
            answer_string += value[0] if value else "?"

    return "".join(answer_string)


def word_to_braille(word):
    answer_string = ""
    number_follows = False

    for i in word:
        if i.isdigit():
            if not number_follows:
                answer_string += special_cases["number_follows"]
                number_follows = True
            answer_string += numbers[i]
        elif i.isalpha():
            if i.isupper():
                answer_string += special_cases["capital_follows"]
                answer_string += alphabets[i.lower()]
            else:
                answer_string += alphabets[i]
            number_follows = False
        else:
            answer_string += special_characters.get(i, "......")
            number_follows = False

    return "".join(answer_string)


def braille_translator(word):
    condition = all(char in ".O" for char in word)

    if condition:
        return braille_to_word(word)
    else:
        return word_to_braille(word)


def main():
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
        translation = braille_translator(input_text)
        sys.stdout.write(translation + "\n")
    else:
        print("Please provide input to translate.")

if __name__ == "__main__":
    main()