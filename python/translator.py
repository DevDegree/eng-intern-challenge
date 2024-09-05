import argparse

braille_to_alphabet = { 'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 
    'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', 
    '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 
    'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', 
    '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 
    'OO.OOO': 'y', 'O..OOO': 'z' }
braille_to_number = {'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', 
    '.OOO..': '0'}

alphabet_to_braille = {v:k for k,v in braille_to_alphabet.items()}
numbres_to_braille = {v:k for k,v in braille_to_number.items()}

#special characters
capital_next = '.....O'
decimal_next = '.O...O'
number_next = '.O.OOO'
space = "......"


def braille_to_text(braille : str) -> str :
    braille_characters  = []
    text = ""

    for n in range(0, len(braille), 6):
        braille_characters.append(braille[n:n+6])

    
    n = 0

    while n < len(braille_characters):
        #handles the space character since it a "special" character
        if braille_characters[n] == space:
            text += " "
        #handles capitals
        elif braille_characters[n] == capital_next:
            n += 1
            text += braille_to_alphabet.get(braille_characters[n],"(mistake)").upper()
        #handles numbers
        elif braille_characters[n] == number_next:
            n += 1
            while n < len(braille_characters) and braille_characters[n] != space :
                text += braille_to_number.get(braille_characters[n],"(mistake)")
                n += 1
            continue
        #handles alphabetical characters
        else:
            text += braille_to_alphabet.get(braille_characters[n],"(mistake)")
        n += 1
    
    return  text
    

def text_to_braille(text:str) -> str:
    text_characters = list(text)
    braille = ""

    n = 0
    while n < len(text_characters):
        if text_characters[n] == " ":
            braille += space
        elif text_characters[n].isupper():
            braille += capital_next
            braille += alphabet_to_braille.get(text_characters[n].lower(),"(mistake)")
        elif text_characters[n].isdigit():
            braille += number_next
            while n < len(text_characters) and text_characters[n] != " ":
                braille += numbres_to_braille.get(text_characters[n],"(mistake)")
                n += 1
            continue
        else:
            braille += alphabet_to_braille.get(text_characters[n],"(mistake)")
        n += 1
    
    return braille



def check_first_two_char(text:str) -> bool:
    if len(text) < 2:
        return False
    else:
        first_two_char = text[:2]
        
        for char in first_two_char:
            if char not in ['.','O']:
                return False
    return True



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converts braille to text or text to braille")
    parser.add_argument("text", type=str, nargs="+" ,help="a string that will be converted to braille or to text")

    args=parser.parse_args()

    text = " ".join(args.text)
    #print(f'the arg(s): {text}')

    if(check_first_two_char(text)):
        print(braille_to_text(text))
    else:
        print(text_to_braille(text))


        
