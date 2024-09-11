import sys
from alphaToBraille import translate_alpha_to_braille
from brailleToAlpha import translate_braille_to_alpha
from convert import braille_unicode_to_dots, dots_to_braille_unicode



def is_braille(input_text):
    # check if input is braille. if it only has 'O' and '.' then yes
    return all(char in 'O.' for char in input_text.replace(' ', ''))


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        sys.exit(1)
    
    # concatenate all command-line arguments into a single string
    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        # convert Braille unicode to dots ('O' and '.') representation and then to English
        dots = dots_to_braille_unicode(input_text)
        translated_text = translate_braille_to_alpha(dots)
    else:
        # convert english to braille unicode via dot representation
        braille = translate_alpha_to_braille(input_text)
        translated_text = braille_unicode_to_dots(braille)
    
    print(translated_text)

if __name__ == "__main__":
    main()