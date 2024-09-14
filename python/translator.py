
#Ryan Rahman
import sys

# Braille dictionary: English to Braille
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O','decimal':'.O...O', 'number':'.O.OOO',
    '.':'..OO.O',',':'..O...'#,'?':'..O.OO','!':'..OOO.',':':'..OO..',';':'..O.O.',
    #'-':'....OO','/':'.O..O.','<':'.OO..O','>':'O..OO.','(':'O.O..O',')':'.O.OO.'
}

# English dictionary: Braille to English
english_alphabet = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'capital', '.O.OOO': 'number','.O...O':'decimal', '.O...O': '.',
    '......': ' ','..O...':',' #,'..O.OO':'?','..OOO.':'!','..OO..':':','..O.O.':';',
    #'....OO':'-','.O..O.':'/','.OO..O':'<','O..OO.':'>','O.O..O':'(','.O.OO.':')'

}

# English numbers: Braille to English
english_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
    '......': ' '
}

#Check if input is in braille or english
def is_braille(input_string):
    for char in input_string:
        if char != 'O' or char != '.':
            return False
        else:
            return True

#Function to split braille strings into a list of substrings all of length 6
def split_string(s, length=6):
    return [s[i:i+length] for i in range(0, len(s), length)]

#Translating English to Braille
def translate_to_braille(english_text):
    is_num = 0 #variable to keeo track of whether term is number or not
    braille_text = [] #List to append braille characters
    for char in range(len(english_text)):
        #print(english_text[char])
        if english_text[char].lower() in braille_alphabet.keys(): #Ensure characters are in dictionary
            if english_text[char].isupper() == True: #Account for capital characters
                braille_text.append(braille_alphabet['capital'])  
            if english_text[char].isnumeric() == True and is_num == 0: #If term is a number
                #print(english_text[char])
                braille_text.append(braille_alphabet['number'])
                is_num += 1 #Ensure the number next character is not put before every digit
            if english_text[char] == '.' and english_text[char-1].isnumeric() == True: #Check if . is a decimal
                braille_text.append(braille_alphabet['decimal'])
            if english_text[char] == ' ': #Reset number variable after each space
                is_num -= is_num
            braille_text.append(braille_alphabet.get(english_text[char].lower())) #Append braile to list


    return ''.join(braille_text) #Combine list into string and return

#Translating Braille to English
def translate_to_english(braille_text):
    is_capital = False #Check if next character is a capital
    is_number = False #Check if next term is a number
    braille_chars = split_string(braille_text,6) #Split braille into substrings of 6
    #print(braille_chars)
    english_text = [] #List of english characters
    for braille_char in braille_chars:

        #Attempt 1:
        # if braille_chars[char] in english_alphabet.keys():
        #     if braille_chars[char-1] == '.....O':
        #         english_text.append(english_alphabet.get(braille_chars[char]).upper())
        #         continue
        #     elif braille_chars[char] == '......':
        #         is_num -= is_num
        #         continue
        #     elif braille_chars[char-1] == '.O.OOO':
        #         english_text.append(english_numbers.get(braille_chars[char]).upper())
        #         continue
        #     elif braille_chars[char] == '.....O':
        #         continue
        #     elif braille_chars[char] == '.O.OOO':
        #         is_num += 1
        #         continue
        #     elif braille_chars[char] == '.O...O':
        #         continue 
        #     else:
        #         if is_num == 0:
        #             english_text.append(english_alphabet.get(braille_chars[char]))
        #         else:
        #             english_text.append(english_numbers.get(braille_chars[char]))
        #     print(english_text)
        #print(braille_char)

        #Working code
        if braille_char == '.....O':  # Capitalization indicator
            is_capital = True 
            continue

        if braille_char == '.O.OOO':  # Number mode indicator
            is_number = True
            continue

        if is_number:
            translated_char = english_numbers.get(braille_char,'') #Look at numbers dict if the term is a number
        else:
            translated_char = english_alphabet.get(braille_char,'') #Look at regular alphabet dict if term is a word

        if is_capital:
            translated_char = translated_char.upper()
            is_capital = False  # Reset capitalization after applying it
        
        english_text.append(translated_char)
        #print(english_text)

        # Reset number mode when a space is encountered
        if braille_char == '......':
            is_number = False
        
        print(english_text)
    
    return ''.join(english_text)

#test = translate_to_braille('Abc 123 xYz')
#print(translate_to_english(test))

def main():
    #Get input text from command and join words with spaces
    input_text = ' '.join(sys.argv[1:])

    # If no input is provided
    if not input_text:
        print("Please provide a string to translate.")
        return
    # Detect if the input is Braille and translate accordingly
    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))
if __name__ == "__main__":
    main()
