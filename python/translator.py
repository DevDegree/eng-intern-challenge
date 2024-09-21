from argparse import ArgumentParser, ArgumentTypeError

from braille_alphabet import (
    braille_to_letters,
    braille_to_numbers,
    braille_to_rules,
    braille_to_special_characters,
)
from english_alphabet import (
    letters_to_braille,
    numbers_to_braille,
    rules_to_braille,
    special_characters_to_braille,
)


def main():
    message, is_english = get_args()
    if is_english:
        print(translate_english_to_braille(message))
    else:
        print(translate_braille_to_english(message))


def get_args():
    message_builder = []
    is_english = False
    parser = ArgumentParser("English <-> Braille translator")
    parser.add_argument(
        "message",
        help="Message to translate",
        nargs="+",
        type=(check_message_part_format),
    )
    parsed_args = parser.parse_args().message
    for parsed_arg in parsed_args:
        message_builder.append(parsed_arg[0])
        is_english = is_english or parsed_arg[1]

    return " ".join(message_builder), is_english


def check_message_part_format(message_part):
    ptr = 0
    is_english = True
    while ptr < len(message_part):
        char = message_part[ptr]
        ptr += 1
        lower_c = char.lower()
        if (
            (lower_c not in letters_to_braille)
            and (lower_c not in numbers_to_braille)
            and (lower_c not in special_characters_to_braille)
            and (char not in {"O", "."})
        ):
            raise ArgumentTypeError(f"Unsupported character: {char}")
        if char in numbers_to_braille:
            while ptr < len(message_part):
                if message_part[ptr] not in numbers_to_braille:
                    raise ArgumentTypeError(f"Numbers must end a word")
                ptr += 1
        if char == ".":
            is_english = False
    if not is_english:
        if not len(message_part) % 6 == 0:
            raise ArgumentTypeError(
                f"Braille message must be a multiple of 6 characters"
            )
        for i in range(0, len(message_part), 6):
            message_part_braille_range = message_part[i : i + 6]
            if (
                (message_part_braille_range not in braille_to_letters)
                and (message_part_braille_range not in braille_to_rules)
                and (message_part_braille_range not in braille_to_special_characters)
            ):
                raise ArgumentTypeError(
                    f"Unsupported braille syntax: {message_part[i:i+6]}"
                )

    return message_part, is_english


def translate_english_to_braille(message):
    braille_message_builder = []
    ptr = 0

    while ptr < len(message):
        char = message[ptr]
        ptr += 1
        if char.isupper():
            braille_message_builder.append(rules_to_braille["capital_follows"])
            braille_message_builder.append(letters_to_braille[char.lower()])
        elif char in numbers_to_braille:
            braille_message_builder.append(rules_to_braille["number_follows"])
            braille_message_builder.append(numbers_to_braille[char])
            while ptr < len(message) and message[ptr] != " ":
                braille_message_builder.append(numbers_to_braille[message[ptr]])
                ptr += 1
        elif char == " ":
            braille_message_builder.append(special_characters_to_braille[char])
        else:
            braille_message_builder.append(letters_to_braille[char])
    return "".join(braille_message_builder)


def translate_braille_to_english(message):
    english_message_builder = []

    is_in_number_section = False
    ptr = 0

    while ptr < len(message):
        char = message[ptr : ptr + 6]
        ptr += 6
        if char == special_characters_to_braille[" "]:
            english_message_builder.append(" ")
            is_in_number_section = False
        elif char == rules_to_braille["capital_follows"]:
            english_message_builder.append(
                braille_to_letters[message[ptr : ptr + 6]].upper()
            )
            ptr += 6
        elif char == rules_to_braille["number_follows"]:
            is_in_number_section = True
        elif is_in_number_section:
            if char == " ":
                is_in_number_section = False
                continue
            english_message_builder.append(braille_to_numbers[char])
        else:
            english_message_builder.append(braille_to_letters[char])
    return "".join(english_message_builder)


if __name__ == "__main__":
    main()
