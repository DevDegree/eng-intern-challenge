import sys

from reference_key import ENG_TO_BRAILLE, BRAILLE_TO_ENG


def is_braille(text: str) -> bool:
    unique_chars = set(list(text))
    return (
        len(unique_chars) == 2
        and "." in unique_chars
        and "O" in unique_chars
        and len(text) % 6 == 0
    )


if __name__ == "__main__":
    input_seq = sys.argv[1:]
    if len(input_seq) == 1 and is_braille(input_seq[0]):
        # Translate from Braille to English
        text_to_translate = input_seq[0]
        translated_text = ""
        capital = False
        number = False
        for i in range(0, len(text_to_translate), 6):
            current_char = text_to_translate[i : i + 6]
            assert current_char in BRAILLE_TO_ENG
            translated_char = BRAILLE_TO_ENG[current_char]
            if translated_char == "capital":
                capital = True
            elif translated_char == "number":
                number = True
            elif translated_char == " ":
                number = False
                translated_text += " "
            elif capital:
                translated_text += translated_char.upper()
                capital = False
            elif number:
                translated_text += str((ord(translated_char) - ord("a") + 1) % 10)
            else:
                translated_text += translated_char
    else:
        # Translate from English to Braille
        text_to_translate = " ".join(input_seq)
        translated_text = ""
        capital = False
        number = False
        for current_char in text_to_translate:
            if ord(current_char) >= ord("0") and ord(current_char) <= ord("9"):
                if not number:
                    translated_text += ENG_TO_BRAILLE["number"]
                    number = True
                translated_text += (
                    ENG_TO_BRAILLE["j"]
                    if current_char == "0"
                    else ENG_TO_BRAILLE[chr(ord("a") + ord(current_char) - ord("1"))]
                )
            elif current_char == " ":
                number = False
                translated_text += ENG_TO_BRAILLE[current_char]
            elif current_char.isupper():
                translated_text += (
                    ENG_TO_BRAILLE["capital"] + ENG_TO_BRAILLE[current_char.lower()]
                )
            else:
                translated_text += ENG_TO_BRAILLE[current_char]
    print(translated_text)
