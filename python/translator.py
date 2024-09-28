
braille_dict = {
    'A': 'O.....',  # ⠁
    'B': 'O.O...',  # ⠃
    'C': 'OO....',  # ⠉
    'D': 'OO.O..',  # ⠙
    'E': 'O..O..',  # ⠑
    'F': 'OOO...',  # ⠋
    'G': 'OOOO..',  # ⠛
    'H': 'O.OO..',  # ⠓
    'I': '.OO...',  # ⠊
    'J': '.OOO..',  # ⠚
    'K': 'O...O.',  # ⠅
    'L': 'O.O.O.',  # ⠇
    'M': 'OO..O.',  # ⠍
    'N': 'OO.OO.',  # ⠝
    'O': 'O..OO.',  # ⠕
    'P': 'OOO.O.',  # ⠏
    'Q': 'OOOOO.',  # ⠟
    'R': 'O.OOO.',  # ⠗
    'S': '.OO.O.',  # ⠎
    'T': '.OOOO.',  # ⠞
    'U': 'O...OO',  # ⠥
    'V': 'O.O.OO',  # ⠧
    'W': '.OOO.O',  # ⠺
    'X': 'OO..OO',  # ⠭
    'Y': 'OO.OOO',  # ⠽
    'Z': 'O..OOO',  # ⠵
    '1': 'O.....',  # ⠁
    '2': 'O.O...',  # ⠃
    '3': 'OO....',  # ⠉
    '4': 'OO.O..',  # ⠙
    '5': 'O..O..',  # ⠑
    '6': 'OOO...',  # ⠋
    '7': 'OOOO..',  # ⠛
    '8': 'O.OO..',  # ⠓
    '9': '.OO...',  # ⠊
    '0': '.OOO..',  # ⠚
    # Capital, decimal, and number fOllOws
    'capital follows': '.....O',  # ⠠
    'decimal follows': '.O...O',  # ⠨
    'number follows': '.O.OOO',   # ⠼
    # COrrected punctuatiOn marks:
    '.': '..OO.O',  # ⠲
    ',': '..O...',  # ⠂
    '?': '..O.OO',  # ⠦
    '!': '..OOO.',  # ⠖
    ':': '..OO..',  # ⠒
    ';': '..O.O.',  # ⠆
    '-': '....OO',  # ⠤
    '/': '.O..O.',  # ⠌
    '<': '.OO..O',  # (symbOl apprOximatiOn)
    '>': 'O..OO.',  # (symbOl apprOximatiOn)
    '(': 'O.O..O',  # ⠷
    ')': '.O.OO.',  # ⠾
    'space': '......'  # ⠀ (space)
    

}



def text2brail(text):
    brail_out = []
    number_mode = False  # To track if we're in number mode
    for s in text:
        if s.isupper():
            brail_out.append(braille_dict['capital follows'])  # Add capital follows flag
            brail_out.append(braille_dict[s])  # Add the corresponding letter
            number_mode = False  # Reset number mode if any
        elif s.isdigit():
            if not number_mode:
                brail_out.append(braille_dict['number follows'])  # Add number follows flag
                number_mode = True
            brail_out.append(braille_dict[s])  # Add the corresponding digit
        elif s.isspace():
            number_mode = False  # Reset number mode on space
            brail_out.append(braille_dict['space'])  # Add the space in Braille
        else:
            number_mode = False  # Reset number mode for any other character
            brail_out.append(braille_dict[s.upper()])  # Convert to Braille for lowercase

    return "".join(brail_out)


def finding_matching_key(value_to_find):
    return next((key for key, value in braille_dict.items() if value == value_to_find), None)

def brail2text(brail):
    text_out = []
    previous_flag = None
    number_mode = False
    chunk_size = 6
    
    for i in range(0, len(brail), chunk_size):
        chunk_brail = brail[i:i+chunk_size].lower()  # Convert to lowercase to match dictionary
        letter = finding_matching_key(chunk_brail)

        if letter == 'space':
            text_out.append(' ')
            previous_flag = None
            number_mode = False
        elif letter == 'capital follows':
            previous_flag = 'capital'
        elif letter == 'number follows':
            number_mode = True
            previous_flag = None
        else:
            if letter is None:
                # Handle unknown chunks
                text_out.append('')
            else:
                if number_mode and letter.isdigit():
                    text_out.append(letter)
                elif previous_flag == 'capital':
                    text_out.append(letter.upper())
                    previous_flag = None
                else:
                    text_out.append(letter.lower() if letter else '')
                number_mode = False  # Reset after number handling

    return "".join(text_out)
# brail = ".....oo............o.oooo.....o.o...oo...............ooo.ooo"
# brail = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
# out = brail2text(brail)
# print(out)

import sys
# Assuming you have your text2brail and brail2text functions already defined

def main():
    input_text = " ".join(sys.argv[1:])  # Join all arguments into a single string
    translated_text = text2brail(input_text)  # Translate to Braille
    print(translated_text)  # Print the output

if __name__ == '__main__':
    main()


# if ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO" == ".....oo............o.oooo.....o.o...oo...............ooo.ooo":
#     print("Yes")