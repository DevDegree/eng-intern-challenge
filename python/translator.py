import sys

#Special characters in braille
CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"

#Dictionary which maps english letters to braille
english_to_braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'}

#Dictionary which maps numbers to braille
number_to_braille_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

#Dictionary which maps braille to english letters
braille_to_english_map = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z'
}

#Dictionary which maps braille to numbers
braille_to_number_map = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

def isBraille(text:str)->bool:
    #Braille if only characters are O and . and the text length is multiple of 6
    return all(char in "O." for char in text) and len(text)%6==0

def english_to_braille(english:str)->str:
    braille = ''

    #When this flag is set to true, all braille characters that follow are assumed to be numbers.
    num_flag = False

    for char in english:
        if char.isalpha(): #if character is english letter
            if char.isupper(): #if capital, append special braille character indiciating so
                braille+=CAPITAL_FOLLOWS
            braille+=english_to_braille_map[char.lower()]
        elif char.isnumeric(): #if character is number
            if not num_flag: #if this is the first number we encounter, set number flag to true
                num_flag = True
                braille+=NUMBER_FOLLOWS
            braille+=number_to_braille_map[char]
        elif char == ' ':
            num_flag = False #reset number flag when we encounter a space
            braille+=SPACE
        
    return braille

def braille_to_english(braille:str)->str:
    english = ''

    #6 braille characters = 1 english character
    braille_grouping = [braille[i:i+6] for i in range (0, len(braille), 6)] 

    #special flags for numbers and capital letters
    num_flag = False
    upper_flag = False

    for char in braille_grouping:
        if char == SPACE:
            num_flag = False #reset number flag when we encounter a space
            english+=' '
        elif char == NUMBER_FOLLOWS:
            num_flag = True #set number flag when we encounter special char
        elif char == CAPITAL_FOLLOWS:
            upper_flag = True #set capital flag when we encounter special char
        elif num_flag == True:
            english+=braille_to_number_map[char] #append a number if number flag set
        elif upper_flag == True:
            english+=braille_to_english_map[char].upper() #append upper case letter if upper flag set
            upper_flag = False
        else:
            english+=braille_to_english_map[char] #append english letter

    return english

def main():
    assert len(sys.argv) >= 2

    s = " ".join(sys.argv[1:])

    if isBraille(s):
        print(braille_to_english(s))
    else:
        print(english_to_braille(s))

if __name__ == "__main__":
    main()