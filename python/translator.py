import sys
from braille_to_eng import translate_braille
from eng_to_braille import translate_english



if __name__ == '__main__':
    # create a string by joining all of the arguments passed through; join by spaces
    text = ' '.join(sys.argv[1:])

    # check if the text contains only 'O' and '.' and the length of the text is a multiple of 6 as this indicates Braille
    if (set(text)) == set(['O', '.']) and len(text) % 6 == 0:
        # translate braille to english
        result = translate_braille(text)
        print(result, file=sys.stdout)
    else:
        # translate english to braille
        result = translate_english(text)
        print(result, file=sys.stdout)