import sys

def translate_to_braille(english_string):
    return "Inside translate to braille"


def translate_to_english(braille_string):
    return "Inside translate to english"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text_to_translate>")
        return

    input_text = " ".join(sys.argv[1:])

    if all(c in "O. " for c in input_text): 
        translated_text = translate_to_english(input_text)
    else:
        translated_text = translate_to_braille(input_text)

    print(translated_text)

if __name__ == "__main__":
    main()

