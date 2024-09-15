import sys

class BrailleTranslator:

    #dictionary storing the braille cells for each english letter and x follows 
    ENGLISH_TO_BRAILLE = {
        'a': 'O.....', 
        'b': 'O.O...', 
        'c': 'OO....',
        'd': 'OO.O..', 
        'e': 'O..O..', 
        'f': 'OOO...',
        'g': 'OOOO..', 
        'h': 'O.OO..', 
        'i': '.OO...',
        'j': '.OOO..', 
        'k': 'O...O.', 
        'l': 'O.O.O.',
        'm': 'OO..O.', 
        'n': 'OO.OO.', 
        'o': 'O..OO.',
        'p': 'OOO.O.', 
        'q': 'OOOOO.', 
        'r': 'O.OOO.',
        's': '.OO.O.', 
        't': '.OOOO.', 
        'u': 'O...OO',
        'v': 'O.O.OO', 
        'w': '.OOO.O', 
        'x': 'OO..OO',
        'y': 'OO.OOO', 
        'z': 'O..OOO',  
        ' ': '......',
        'capital': '.....O', 
        'decimal': '.O...O', 
        'number': '.O.OOO',
    }

    #dictionary storing the braille cells for each number from 0-9
    #a seperate dictionary is used because a-j and 0-9 have the same braille cell
    NUMBERS_TO_BRAILLE = {
        '1': 'O.....', 
        '2': 'O.O...', 
        '3': 'OO....',
        '4': 'OO.O..', 
        '5': 'O..O..', 
        '6': 'OOO...',
        '7': 'OOOO..', 
        '8': 'O.OO..', 
        '9': '.OO...',
        '0': '.OOO..',
    }

    #inverted dictionaries of the english to braille and numbers to braille to allow conversion in the opposite direction
    BRAILLE_TO_ENGLISH = {braille_char: english_char for english_char, braille_char in ENGLISH_TO_BRAILLE.items()}
    BRAILLE_TO_NUMBERS = {braille_char: number for number, braille_char in NUMBERS_TO_BRAILLE.items()}

    def __init__(self, arguments):
        self.string = arguments
        self.is_braille = False

    #function to identify the language of the arguments and split them into an easier to use state
    def language_identifier(self):

        #if all the characters in the arguments are Os or . then the arguments are braille
        if all(char in 'O.' for char in self.string):
            self.is_braille = True

            #splits the arguments every 6 characters(length of a braille cell) and stores them in a list
            return [self.string[i: i + 6] for i in range(0, len(self.string), 6)]
        
        else:

            #splits the arguments every character(length of a single character) and stores them in a list
            return list(self.string)
    
    #main translator function
    def translate(self):

        #assigns the split string to a variable so it can be translated
        identified_string = self.language_identifier()

        #if the string was identified as braille the braille to english function is called
        if self.is_braille:
            return self.braille_to_english(identified_string)
        
        #if the string was identified as english the english to braille function is called
        else:
            return self.english_to_braille(identified_string)

    #function to convert the split english string to braille
    def english_to_braille(self, english_text):
        
        #list to store the braille characters after translation
        braille_list = []
        
        #flag to indicate if number mode is active (inactive by default)
        is_number = False

        #loops through each character in the english string
        for char in english_text:
            
            #if the character is in the alphabet
            if char.isalpha():

                #appends the capital follows cell before the capital letter
                if char.isupper():
                    braille_list.append(self.ENGLISH_TO_BRAILLE['capital'])
                
                #appends the braille cell to the translated list
                braille_list.append(self.ENGLISH_TO_BRAILLE[char.lower()])
            
            #if the character is a number
            elif char.isdigit():

                #if number mode is not active
                if not is_number:

                    #appends the number follows cell before the number(s)
                    braille_list.append(self.ENGLISH_TO_BRAILLE['number'])
                    
                    #activates number mode
                    is_number = True

                #appends the braille cell to the translated list
                braille_list.append(self.NUMBERS_TO_BRAILLE[char])

            #appends the braille space and deactivates number mode
            elif char == ' ':
                braille_list.append(self.ENGLISH_TO_BRAILLE[' '])
                is_number = False

        #returns the translated braille list as a string
        return ''.join(braille_list)

    #function to convert the split braille string to english
    def braille_to_english(self, braille_text):
        
        #list to store the english characters after translation
        english_list = []

        #flag to indicate if the next letter is capital
        is_capital = False

        #flag to indicate if number mode is active
        is_number = False

        #loops through each braille cell in the braille string
        for braille_cell in braille_text:

            #if the braille cell is the 'capital follows' cell
            if braille_cell == self.ENGLISH_TO_BRAILLE['capital']:
                
                #flags that the next letter is capital
                is_capital = True
                continue
            
            #if the braille cell is the 'number follows' cell
            if braille_cell == self.ENGLISH_TO_BRAILLE['number']:
                
                #activates number mode 
                is_number = True
                continue

            #if the letter is a capital
            if is_capital:

                #appends the capitalized version of that letter
                english_list.append(self.BRAILLE_TO_ENGLISH[braille_cell].upper())
                
                #resets the flag indicating a capital letter
                is_capital = False
                continue

            #if the braille cell is a space number mode is deactivated
            if braille_cell == self.ENGLISH_TO_BRAILLE[' ']:
                is_number = False

            #if number mode is active use the numbers dictionary instead of the letters dictionary
            if is_number:
                english_list.append(self.BRAILLE_TO_NUMBERS[braille_cell])

            else:
                #appends the translated character to the english list
                english_list.append(self.BRAILLE_TO_ENGLISH[braille_cell])
            
        #returns the translated english list as a string
        return ''.join(english_list)
            
def main():

    #takes the runtime arguments and joins them as a string
    arguments = ' '.join(sys.argv[1:])

    #creates an instance of the translator and passes the runtime arguments
    translator = BrailleTranslator(arguments)

    #assigns the output of the translator function to a variable
    result = translator.translate()

    #prints the translated string
    print(result)

if __name__ == '__main__':
    main()


