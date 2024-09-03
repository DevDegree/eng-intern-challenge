import sys
from braille_to_eng import translate_braille
from eng_to_braille import translate_english



if __name__ == '__main__':
    # assume that only one string argument is passed in
    text = sys.argv[1]

    # check if the text contains only 'O' and '.' as this indicates Braille
    if (set(text)) == set(['O', '.']):
        # translate braille to english
        result = translate_braille(text)
        print(result)
    else:
        # translate english to braille
        result = translate_english(text)
        print(result)