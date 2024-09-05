import sys

def translate_to_braille(text):
    return text

def translate_to_english(braille):
    return braille


if __name__ == '__main__':
    input_text = sys.argv[1]

    if all(c in 'O.' for c in input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))