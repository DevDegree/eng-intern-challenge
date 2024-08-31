from sys import argv
from src.parser.base_parser import BaseParser
from src.parser.braille_parser import BrailleParser
from src.parser.english_parser import EnglishParser
from src.util.is_text_braille import is_text_braille

def main():
    text_argument = " ".join(argv[1:])
    
    parser: BaseParser = None
    if(is_text_braille(text_argument)):
        parser = BrailleParser()
    else:
        parser = EnglishParser()

    print(parser.translate_all(text_argument))

if __name__ == '__main__':
    main()
