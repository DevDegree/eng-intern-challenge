# Michael Han
# 2024 09 20
# Shopify Engineering Intern Challenge - Winter 2024
# This file contains the functions to translate english to braille and braille to english
# The technical requirements can be found here: https://github.com/michael-han-dev/Shopify-eng-intern-challenge/tree/main
# Test case file called "MH_test_translator.py" can be found in the same directory as this file

import sys

#dictionary for key of english letter and value of braille letter / and or symbol
english_to_braille = {
'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO',
'!': '..OOO.', ":": '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.'
}

#dictionary for reverse key value pairs of braille to english using for loop to reverse
braille_to_english = {}
for key, val in english_to_braille.items():
    braille_to_english[val] = key

#dictionary for key of number and value of braille number
number_to_braille = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',  '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'}

#dictionary for reverse key value pairs of braille to number using for loop to reverse
braille_to_number = {}
for key, val in number_to_braille.items():
    braille_to_number[val] = key

#Braille for if capital follows[0], if decimal follows[1], if number follows[2]
follow_conditionals = ['.....O', '.O...O', '.O.OOO']

#detect if the input is english or braille, return: string
def detect_english_or_braille(input):
    
    #check if all the characters in the input are in the braille alphabet
    if all(characters in '.O' for characters in input):
        
        #check if the input is divisible by 6
        if len(input) % 6 != 0:
            return False
        
        #check if braille input is valid                    
        return 'braille'
           
    return 'english'

#translate the input from english to braille, return: string
def english_to_braille_translation(string):
    
    #initialize empty string to store the braille translation, set flag for digit detection
    braille_translation = ''
    digit = False
    
    #iterate through the input and add the braille translation to the braille_translation string
    for char in string:
        
        if digit:
            braille_translation += number_to_braille[char]
        
        #if the character is a capital letter, add the capital letter symbol
        elif char.isupper():
            braille_translation += follow_conditionals[0]
            braille_translation += english_to_braille[char.lower()]
            
        #if the character is a number, add the number symbol
        elif char.isdigit():
            braille_translation += follow_conditionals[2]
            braille_translation += number_to_braille[char]
            digit = True
        
        #if the character is a decimal, add the decimal symbol
        elif char == '.':
            braille_translation += follow_conditionals[1]
            braille_translation += english_to_braille[char]
        
        #if the character is not in the english alphabet or symbols, add the question mark symbol 3 times. Wasn't sure what to do with this edge case
        elif char not in english_to_braille and char not in number_to_braille:
            braille_translation += english_to_braille['?']*3
        
        elif char == ' ':
            braille_translation += '......'
            digit = False
                         
        #add the braille translation of the character to the braille_translation string
        else:
            braille_translation += english_to_braille[char]
    
    return braille_translation

#translate the input from braille to english, return: string
def braille_to_english_translation(string):
    #initialize empty string to store the english translation
    english_translation = ''
    
    #digit flag to indicate number follows braille symbol was flagged and every charcter after is a number
    digit = False
    
    #counter value to iterate through the input string
    i = 0
    #iterate through the input and add the english translation to the english_translation string
    while i < len(string):
        
        #get the braille character from the string
        braille_char = string[i:i+6]
        
        #if digit true, number follows braille symbol was flagged and every character after is a number
        if digit:
            english_translation += braille_to_number[braille_char]
            i += 6
            
        #if the braille character is a capital letter symbol, add the capital letter to the english translation
        elif braille_char == follow_conditionals[0]:
            i += 6
            braille_char = string[i:i+ 6]
            english_translation += braille_to_english[braille_char].upper()
            i += 6
            
        #if the braille character is a number symbol, add the number to the english translation
        elif braille_char == follow_conditionals[2]:
            i += 6
            braille_char = string[i:i+ 6]
            english_translation += braille_to_number[braille_char]
            digit = True
            i += 6
        
        elif braille_char == follow_conditionals[1]:
            i += 6
            braille_char = string[i:i+ 6]
            english_translation += braille_to_english[braille_char]
                   
        #if space, add space character and set digit flag to false indicating new word
        elif braille_char == '......':
            english_translation += ' '
            digit = False
            i += 6
            
        #add the english translation of the braille character to the english_translation string
        else:
            english_translation += braille_to_english[braille_char]
            i += 6
    
    return english_translation

#main function to run the translator
def main():
    #checks if command line is empty
    args = sys.argv[1:] if len(sys.argv) > 1 else []

    if not args:
        print("No input detected, input a string to translate.")
        return

    translated_output = []
    
    # Process each argument and add translations
    for arg in args:
        input_type = detect_english_or_braille(arg)
        
        if input_type == 'english':
            # Append English to Braille translation (with Braille spaces)
            translated_output.append(english_to_braille_translation(arg))
            
        elif input_type == 'braille':
            # Append Braille to English translation
            translated_output.append(braille_to_english_translation(arg))
        
        else:
            print("Not a valid input.")
            return

    #prints translated output as a string
    print(' '.join(translated_output) if input_type == 'braille' else '......'.join(translated_output), end = '')
    
if __name__ == '__main__':
    main()
