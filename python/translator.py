#Varak Mesropian
#varakmesrop@gmail.com

import sys
braille_letters = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 
    'O..OOO': 'z'
}
braille_numbers = { 
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

#I'm just flipping the dictionaries
english_letters = {v: k for k, v in braille_letters.items()}
english_numbers = {v: k for k, v in braille_numbers.items()}

def to_braille(text):
    braille_str = ''
    number_mode = False

    for char in text:
                
        if char == ' ':
            # Adding space in Braille and reseting the number mode
            braille_str += '......'
            number_mode = False
        
        elif char.lower() in english_letters:
            if char.isupper():
                # Adding the uppercase braille
                braille_str += '.....O'
                braille_str += english_letters[char.lower()] #turning to lower then picking from dictionary
            else:
                braille_str += english_letters[char] 
        elif char in english_numbers:
            if not number_mode:
                number_mode = True
                braille_str += '.O.OOO' #adding the number braille
                braille_str += english_numbers[char]
            else:
                braille_str += english_numbers[char] #adding number no need for the number braille

    return braille_str


def to_english(braille_str):
    english_str = ''
    number_mode = False
    cap_mode = False
    braille_chars = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]
    
    for braille_char in braille_chars:
        if braille_char == '......': #checking for space
            english_str += ' '
            number_mode = False
            cap_mode = False
        elif braille_char == '.....O': #checking for capital letter
            cap_mode = True
            number_mode = False
        elif braille_char == '.O.OOO': #cheking if it's a number
            number_mode = True
            cap_mode = False
        else:
            if number_mode:
                english_str += braille_numbers[braille_char] #using the brail dictionary
            else:
                if cap_mode:
                    english_str += (braille_letters[braille_char]).upper() #making it uppercase
                    cap_mode = False
                else:
                    english_str += braille_letters[braille_char] #just adding the letter
       
    return english_str

def main():
    if len(sys.argv) < 2:
        print("Error, need an input")
        sys.exit(1)
    
    input_str = ' '.join(sys.argv[1:])
    
    if all(c in 'O.' for c in input_str):
        #the input is braille
        result = to_english(input_str)
    else:
        #the input is English
        result = to_braille(input_str)
    
    print(result)

if __name__ == '__main__':
    main()

