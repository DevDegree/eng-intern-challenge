import sys

texttobraille_dict = {
    'a':'O.....','b':'O.O...','c':'OO....','d':'OO.O..',
    'e':'O..O..','f':'OOO...','g':'OOOO..','h':'O.OO..',
    'i':'.OO...','j':'.OOO..','k':'O...O.','l':'O.O.O.',
    'm':'OO..O.','n':'OO.OO.','o':'O..OO.','p':'OOO.O.',
    'q':'OOOOO.','r':'O.OOO.','s':'.OO.O.','t':'.OOOO.',
    'u':'O...OO','v':'O.O.OO','w':'.OOO.O','x':'OO..OO',
    'y':'OO.OOO','z':'O..OOO','1':'O.....','2':'O.O...',
    '3':'OO....','4':'OO.O..','5':'O..O..','6':'OOO...',
    '7':'OOOO..','8':'O.OO..','9':'.OO...','0':'.OOO..',
    'number':'.O.OOO','capital':'.....O',' ':'......',
}


brailletotext_dict = {v: k for k, v in texttobraille_dict.items()}

def EngtoBraille(text):
    braille_text = []
    is_number = False

    for char in text:
        if char.isdigit() and not is_number:
            braille_text.append(texttobraille_dict['number'])
            is_number = True
        elif not char.isdigit():
            is_number = False

        if char.isupper():
            braille_text.append(texttobraille_dict['capital'])

        braille_text.append(texttobraille_dict[char.lower()])

    return ''.join(braille_text)

def BrailletoEng(brailleword):
    braille_cells = [brailleword[i:i + 6] for i in range(0, len(brailleword), 6)]
    text, is_number, is_capital = [], False, False

    for cell in braille_cells:
        if cell == texttobraille_dict['number']:
            is_number = True
            continue
        elif cell == texttobraille_dict['capital']:
            is_capital = True
            continue

        if is_number and cell in brailletotext_dict:
            text.append(brailletotext_dict[cell])  # Numbers map to their corresponding text
        elif cell in brailletotext_dict:
            letter = brailletotext_dict[cell].upper() if is_capital else brailletotext_dict[cell]
            text.append(letter)

        if cell == texttobraille_dict[' ']:
            is_number = False

        is_capital = False

    return ''.join(text)

def detect_input_type(input_string):
    return "braille" if all(char in '.O' for char in input_string) and len(input_string) % 6 == 0 else "english"

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string>")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])
    input_type = detect_input_type(input_string)

    if input_type == "braille":
        result = BrailletoEng(input_string)
    elif input_type == "english":
        result = EngtoBraille(input_string)

    print(result)

if __name__ == "__main__":
    main()

