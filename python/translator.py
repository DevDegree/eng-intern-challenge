import sys

# A dictionary that maps from from alphabet to braille
eng_to_braille = {
    "A": "O.....", "B": "O.O...", "C": "OO....", "D": "OO.O..", "E": "O..O..", "F": "OOO...", "G": "OOOO..", "H": "O.OO..", "I": ".OO...", "J": ".OOO..",
    "K": "O...O.", "L": "O.O.O.", "M": "OO..O.", "N": "OO.OO.", "O": "O..OO.", "P": "OOO.O.", "Q": "OOOOO.", "R": "O.OOO.", "S": ".OO.O.", "T": ".OOOO.",
    "U": "O...OO", "V": "O.O.OO", "W": ".OOO.O", "X": "OO..OO", "Y": "OO.OOO", "Z": "O..OOO", 
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", 
    " ": "......", "capital": ".....O", "number": ".O.OOO"
}
# A dictionary that maps from braille to the alphabet - simply reverse the eng_to_braille map
braille_to_eng = {j: i for i, j in eng_to_braille.items() if i not in '0123456789'}
braille_to_number = {j: i for i, j in eng_to_braille.items() if i in '0123456789 '}

# braille_or_english(ipt: str) will take in an input, and determine whether or not it is Braille or English
# PARAMETERS:
#   - ipt (str): the input string that we will be checking
def braille_or_english(ipt: str) -> str:
    if all(c in 'O.' for c in ipt) and len(ipt) % 6 == 0:
        return 'BRAILLE'
    else:
        return 'ENGLISH'

# translator(direction: str, text: str) is a function that will either translate the 'text' from English to Braille or from Braille to English
#   depending on what is specified by 'direction'.
# PARAMETERS:
#   - direction (str): must be either "ENGLISH_TO_BRAILLE" or "BRAILLE_TO_ENGLISH"
#   - text (str): this will be the initial text passed for translation (English or Braille)
def translator(direction: str, text: str) -> str:
    # English to Braille translation
    if direction == "ENGLISH_TO_BRAILLE":
        # List to store the braille
        braille = []
        # Flag determining whether or not the number flag is on
        is_num = False
        # Iterate through each character in the text
        for i in text:
            # Case work if we encounter a digit
            if i.isdigit():
                if not is_num:
                    braille.append(eng_to_braille['number'])
                    is_num=True
                braille.append(eng_to_braille[i])
            # Case work for if we encounter an alphabet letter
            elif i.isalpha():
                if i.isupper():
                    braille.append(eng_to_braille['capital'])
                braille.append(eng_to_braille[i.upper()])
                is_num=False
            # Case work for a space
            elif i == ' ':
                braille.append(eng_to_braille[' '])
                is_num=False

        # Ret the list as one string joined together
        return ''.join(braille)
    # Braille to English translation
    elif direction == "BRAILLE_TO_ENGLISH":
        # List for letters
        english = []
        # Num flag (same as above)
        is_num = False
        # Counter since we will be incrementing by 6 now for each braille char
        counter = 0
        n = len(text)
        # Loop through the braille chars
        while counter < n:
            # Take a len 6 substring for each braille character
            cur_sym = text[counter:counter+6]
            # If it's the capital flag, append the next letter capitalized
            if cur_sym == eng_to_braille['capital']:
                counter += 6
                next_sym = text[counter:counter+6]
                english.append(braille_to_eng[next_sym].upper())
            # If it's the number flag, just turn the boolean switch 'is_num' on
            elif cur_sym == eng_to_braille['number']:
                is_num = True
            else:
                if cur_sym == "......":
                    is_num = False
                # otherwise, append either the number or letter depending on the boolean switch
                if is_num:
                    english.append(braille_to_number[cur_sym])
                else:
                    english.append(braille_to_eng[cur_sym].lower())
            counter += 6

        # Return the list as one string
        return ''.join(english)
    raise ValueError('Must be a valid direction (Either put ENGLISH_TO_BRAILLE or BRAILLE_TO_ENGLISH as the direction parameter)')


def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <input_string>")
        return
    
    ipt_str = sys.argv[1]
    str_type = braille_or_english(ipt_str)

    if str_type == 'ENGLISH':
        translated_txt = translator('ENGLISH_TO_BRAILLE', ipt_str)
    else:
        translated_txt = translator('BRAILLE_TO_ENGLISH', ipt_str)
    
    print(translated_txt)

if __name__ == "__main__":
    main()


