import sys

from braille_dict import braille_to_english, braille_to_nums, english_to_braille


def is_braille(input_str):
    for char in input_str:
        if char not in {"O", "."}:
            return False

    return True


def translate_braille_to_english(braille_str):
    english_output = []
    in_number_mode = False
    i = 0

    while i < len(braille_str):
        braille_char = braille_str[i : i + 6]
        if braille_char == english_to_braille["cap"]:
            next_char = braille_str[i + 6 : i + 12]
            english_output.append(braille_to_english.get(next_char, "?").upper())
            i += 12
        elif braille_char == english_to_braille["num"]:
            in_number_mode = True
            i += 6
        else:
            # Regular character, replace unknown chars with "?"
            if in_number_mode:
                char = braille_to_nums.get(braille_char, "x")
                if braille_char == english_to_braille[" "]:
                    in_number_mode = False
            else:
                char = braille_to_english.get(braille_char, "?")
            english_output.append(char)
            i += 6
    return "".join(english_output)


def translate_english_to_braille(english_str):
    braille_output = []
    in_number_mode = False

    for char in english_str:
        if char.isdigit() and not in_number_mode:
            braille_output.append(english_to_braille["num"])
            in_number_mode = True

        if char.isalpha():
            in_number_mode = False
            if char.isupper():
                braille_output.append(english_to_braille["cap"])
                braille_output.append(english_to_braille[char.lower()])
            else:
                braille_output.append(english_to_braille[char])
        elif char.isdigit():
            braille_output.append(english_to_braille[char])
        elif char == " ":
            braille_output.append(english_to_braille[" "])

    return "".join(braille_output)


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        return

    arguments = sys.argv[1:]
    input_text = " ".join(arguments)

    if is_braille(input_text):
        print(translate_braille_to_english(input_text))
    else:
        print(translate_english_to_braille(input_text))


if __name__ == "__main__":
    main()
