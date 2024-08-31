import sys
import braille_to_alphabet, alphabet_to_braille

def is_braille(text):
    return all(character in "O." for character in text) and len(text) % 6 == 0

def main():
    input_text = (' '.join(sys.argv[1:]))

    if len(input_text) == 0:
        pass

    elif is_braille(text=input_text):
        translate_object = braille_to_alphabet.B2A(text=input_text)
        translate_object.translate()

    else:
        alphabet_to_braille.translate(text=input_text)

    return

if __name__ == '__main__':
    main()
