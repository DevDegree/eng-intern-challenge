import dictionaries as dt
#GLOBAL VARIABLE TO INDICATE WHETHER SERIES OF NUMERICAL VALUES OR CAPITALS ARE UP COMING
NUMBER_FOLLOWS = False
CAPITAL_FOLLOWS = False

#Accepts user input and determines whether input is english or braille. Then translates and returns text accordingly
def main(input_string):

    is_braille = True #assume string is braille
    for char in input_string:
        if char != 'O' and char != '.': #if non braille character detected
            is_braille = False #english not braille
            break

    if is_braille: #convert braille to english
        print(braille_to_english(input_string))
    else: #convert english to braille
        print(english_to_braille(input_string))


def braille_to_english(input_string):
    global NUMBER_FOLLOWS
    global CAPITAL_FOLLOWS
    continue_again = False
    continue_length = 0
    current_length = 0

    braille_char_length = 6
    #split input string into even sequences of 6 that make up each letter in Braille alphabet
    split_string = [(input_string[i:i+braille_char_length]) for i in range(0, len(input_string), braille_char_length)]
    
    translated_phrase = []
    operators = ['capital_follows', 'number_follows', 'decimal_follows']
    for i, braille_sequence in enumerate(split_string):
        
        #if values have already been updated in handle_text_information fxn, then we move on
        if continue_again:
            if current_length < continue_length:
                current_length += 1 #keep updating until we are at correc iteration
                continue
            else:
                #reset for next time
                current_length = 0 
                continue_length = 0 
                continue_again = False

        english_character = dt.braille_to_english_dict[split_string[i]]
        if english_character not in operators:
            #gets the key (english character) from the braille sequence from the english_to_braille_dict
            translated_phrase.append(english_character) #appends to list
        else: #requires text transformation
            #handles text conversion (capitals, decimals, numerical values)
            english_character = handle_text_transformation(split_string[i], split_string, i)

            if CAPITAL_FOLLOWS: #CAPITAL LETTER WAS ADDED, SKIP NEXT ITTERATION
                continue_length = 1
                continue_again = True
                CAPITAL_FOLLOWS = False

            elif NUMBER_FOLLOWS: #potential sequence, so append all the of them at once
                for number in english_character[1]:
                    translated_phrase.append(number)
                continue_length = english_character[0] #updates index so that next itteration is 
                continue_again = True
                NUMBER_FOLLOWS = False
                continue #next itteration

            translated_phrase.append(english_character) #appends to list

    joined_phrase = ('').join(translated_phrase) #merges list into coherent string

    return joined_phrase

def english_to_braille(input_string):
    
    translated_phrase = []
    for index, english_character in enumerate(input_string):
        if english_character.isupper(): #add uppercase signal
            translated_phrase.append(dt.english_to_braille_dict['capital_follows'])
            translated_phrase.append(dt.english_to_braille_dict[english_character.lower()])

        elif english_character == '.': #add decimal signal
            translated_phrase.append(dt.english_to_braille_dict['decimal_follows'])
            translated_phrase.append(dt.english_to_braille_dict[english_character])

        elif english_character.isnumeric():
            if index == 0 or not input_string[index - 1].isnumeric(): #first time seeing a consecuetive number
                #update braille code to indicate number(s) are coming up
                translated_phrase.append(dt.english_to_braille_dict['number_follows']) 
            translated_phrase.append(dt.number_to_braille_dict[str(english_character)]) #appends to list
        else:
            #gets braille sequence from dictionary lookup
            translated_phrase.append(dt.english_to_braille_dict[english_character]) #appends to list

    joined_phrase = ('').join(translated_phrase) #merges list into coherent string

    return joined_phrase

def handle_text_transformation(character, string, i):
    global NUMBER_FOLLOWS
    global CAPITAL_FOLLOWS

    operation = dt.braille_to_english_dict[character] #get text form of braille operation code
    
    if operation == 'capital_follows': #if next letter is a capital
        #get next letter
        english_character = dt.braille_to_english_dict[string[i+1]]
        CAPITAL_FOLLOWS = True
        return english_character.capitalize() #return capitalized version
    
    if operation == 'decimal_follows': #if next character is a decimal
        number = dt.braille_to_number_dict[string[i+1]] #lookup conversion from braille to number dictionary instead
        return number
                
    if operation == 'number_follows': #if next character(s) are numbers
        NUMBER_FOLLOWS = True #set to true for check in  braille to english function
        number_sequence = []
        for index, char in enumerate(string[i:]): #while character is not space operator code
            if index + 1 < len(string) and dt.braille_to_english_dict[string[index+1]] != ' ': 
                number_sequence.append(dt.braille_to_number_dict[string[index+1]]) # append number to number sequence to be returned later
            else:
                return [index, number_sequence] #return index (before space), and numbers to be appended
            
if __name__ == "__main__":
    import sys
    input_string = " ".join(sys.argv[1:])
    main(input_string)