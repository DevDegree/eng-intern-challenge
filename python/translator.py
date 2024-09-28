from functions import is_braille, translate_braille_to_english, translate_english_to_braille
import sys

def main():
    input_str = " ".join(sys.argv[1::])
    output = None
    
    if not is_braille(input_str):
        output = translate_english_to_braille(input_str)
    else:
        output = translate_braille_to_english(input_str)
    print(output)


if __name__ == "__main__":
    main()