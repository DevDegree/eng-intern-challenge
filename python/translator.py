#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Aiden Fox Ivey, 2024

import sys
from typing import Dict

# The rest of the alphabet (except w) is formed by modifying these.
BRAILLE_BASE = {
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
}

BRAILLE_NUMS = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

# As best as I can tell, there's not much rhyme or reason to punctuation aside
# from the opening and closing braces being visually (and physically) mirrored.
BRAILLE_PUNCTUATION = {
    ",": "..OO.O",
    ".": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".O.OO.",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
}

control_sequences = [".....O", ".O...O", ".O.OOO"]


# This is definitely overkill. In a serious codebase, I would probably write
# something to generate the Python code itself so that you could inspect it
# and keep it in version control.
def generate_braille() -> Dict[str, str]:
    result = BRAILLE_BASE.copy()

    # In braille, w is a special case.
    result["w"] = ".OOO.O"

    result.update(BRAILLE_PUNCTUATION)

    flip_bit = lambda c: "O" if c == "." else "."
    flip_penultimate = lambda p: p[:4] + flip_bit(p[4]) + p[5]
    flip_bottom_two = lambda p: p[:4] + flip_bit(p[4]) + flip_bit(p[5])

    result.update(
        {
            ch2: flip_penultimate(result[ch1])
            for ch1, ch2 in zip("abcdefghij", "klmnopqrst")
        }
    )

    result.update(
        {ch2: flip_bottom_two(result[ch1]) for ch1, ch2 in zip("abcde", "uvxyz")}
    )

    return result


def panic(message: str) -> None:
    print(message, file=sys.stderr)
    sys.exit(1)


def invert_map(d: Dict) -> Dict:
    return {v: k for k, v in d.items()}


def text_to_braille(
    text: str, braille_map: Dict[str, str], braille_nums: Dict[str, str]
) -> str:
    translation = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch.isupper():
            translation.extend([".....O", braille_map[ch.lower()]])
        elif ch.isnumeric():
            translation.append(".O.OOO")

            while i < len(text) and text[i].isnumeric():
                translation.append(braille_nums[text[i]])
                i += 1
            i -= 1  # since we just broke the loop, we need to re-process this idx
        elif ch == ".":
            translation.extend([".O...O", braille_map[ch]])
        elif ch in braille_map:
            translation.append(braille_map[ch])
        else:
            panic(f"Unsupported character: {ch}")
        i += 1

    return "".join(translation)


def braille_to_text(
    braille: str, inv_map: Dict[str, str], inv_nums: Dict[str, str]
) -> str:
    if len(braille) % 6 != 0:
        panic("Invalid braille provided.")

    chunks = [braille[i : i + 6] for i in range(0, len(braille), 6)]
    translation = []
    i = 0

    while i < len(chunks):
        chunk = chunks[i]
        if chunk in control_sequences:
            if i + 1 >= len(chunks):
                panic("No character following control character.")
                next_chunk = chunks[i + 1]
                if chunk == ".....O":
                    translation.append(inv_map[next_chunk].upper())
                elif chunk == ".O...O":
                    translation.append(inv_map[next_chunk])
                elif chunk == ".O.OOO":
                    i += 1
                    while i < len(chunks) and chunks[i] != "......":
                        translation.append(inv_nums[chunks[i]])
                        i += 1
                    if i < len(chunks):  # if still left, then add mapped char
                        translation.append(inv_map[chunks[i]])
                i += 2  # skip past control character
        elif chunk in inv_map:
            translation.append(inv_map[chunk])
            i += 1
        else:
            panic(f"Unknown Braille sequence: {chunk}")

    return "".join(translation)


def main():
    if len(sys.argv) < 2:
        panic("Usage: python3 translator.py <input>")

    input_text = " ".join(sys.argv[1:])
    braille_map = generate_braille()
    inv_braille = invert_map(braille_map)
    inv_nums = invert_map(BRAILLE_NUMS)

    if set(input_text) <= {".", "O"}:
        result = braille_to_text(input_text, inv_braille, inv_nums)
    else:
        result = text_to_braille(input_text, braille_map, BRAILLE_NUMS)

    print(result)


if __name__ == "__main__":
    main()
