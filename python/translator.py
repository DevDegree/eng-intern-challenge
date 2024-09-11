###### Python venv 3.8 #####

################ Import Libraries
import re # regular expression matching
from string import ascii_lowercase # lowercase english alphabet
from string import ascii_uppercase # uppercase english alphabet
import sys # to get command line inputs

################ Step 1: Create dictionary of mapping from english to/from braille
## Make function that replaces a . with a O to make it easier to iteratively update the dictionary based on Braille's patterns
def replace_char_in_string(init_string, position, new_char, position_2 = None):
	'''
    Replaces characters at specified positions in a string with a new character.

    Parameters:
    ----------
    init_string : str
        The original string to be modified.
    position : int
        Index of the first character to be replaced (0-based).
    new_char : str
        The character to replace the old character(s).
    position_2 : int, optional
        Index of the second character to be replaced, if provided (default is None).

    Returns:
    -------
    str
        A new string with the specified character replacements.
    '''

	# Convert string to a list to make it easier to specify position of changes
	string_as_list = list(init_string)

	# Replacing the character at the first position with the new character
	string_as_list[position] = new_char

	# Check if there is a second position to change: 
	if position_2 is not None:
		# replace in string if there is
	    string_as_list[position_2] = new_char

	# Converting the list back to string to have your final updated new string
	new_string = ''.join(string_as_list)
	return new_string


# Create dictionary for all letters (english to braille)
## Start with the building block a-j, w, capital, number, and space
### braille follows a pattern after the first 10 letters; 
### only w does not follow this pattern so we must include it in the base as well
e_to_b_base_letters = {
    'a' : 'O.....', # 1
    'b' : 'O.O...', # 1, 3
    'c' : 'OO....', # 1, 2
    'd' : 'OO.O..', # 1, 2, 4
    'e' : 'O..O..', # 1, 4
    'f' : 'OOO...', # 1, 2, 3
    'g' : 'OOOO..', # 1, 2, 3, 4
    'h' : 'O.OO..', # 1, 3, 4
    'i' : '.OO...', # 2, 3
    'j' : '.OOO..', # 2, 3, 4
    'capital' : '.....O',
    'number' : '.O.OOO',
    ' ' : '......',
    'w' : '.OOO.O'
}

## Now we can iteratively add the rest of the letters to a new dictionary:
e_to_b_rest_of_letters = {}

# Since it is grouped by 10 letter patterns we want to iterate through each 10:
## letters k-t
for i, letter in enumerate(ascii_lowercase[10:20]):
	# letters always corresponding to the first 10 letters
    corresponding_base_letter = e_to_b_base_letters[ascii_lowercase[i]]
    # difference lie in the 5th position where instead of a "." it is "O"
    e_to_b_rest_of_letters[letter] = replace_char_in_string(corresponding_base_letter, 4, 'O')

# Since w is in the set u-z, we need to split it into two for loop
# letters u-v
for i, letter in enumerate(ascii_lowercase[20:22]):
    corresponding_base_letter = e_to_b_base_letters[ascii_lowercase[i]]
    # add "O" to the 5th and 6th position
    e_to_b_rest_of_letters[letter] = replace_char_in_string(corresponding_base_letter, 4, 'O', 5)

# letters x-z
for i, letter in enumerate(ascii_lowercase[23:26]):
	# add 2 to index to pick up where the previous for-loop left off at
    corresponding_base_letter = e_to_b_base_letters[ascii_lowercase[i+2]]
    e_to_b_rest_of_letters[letter] = replace_char_in_string(corresponding_base_letter, 4, 'O', 5)

  
# Combine all letters and numbers from the two different dictionaries:
eng_to_braille = {**e_to_b_base_letters, **e_to_b_rest_of_letters}

# We need to now add capital letters to the final dictionary
e_to_b_capitalize = {}

# Go through all letters to make them capital 
for i, letter in enumerate(ascii_uppercase[0:25]):
    # Find the matching lowercase letter in the full dictionary:
    corresponding_base_letter = eng_to_braille[ascii_lowercase[i]]
    # append to the capitalized dictionary the 'capital' indicator along with the corresponding letter in braille
    e_to_b_capitalize[letter] = eng_to_braille['capital']+corresponding_base_letter

# Combine all dictionaries into one to have eng_to_braille conversion:
eng_to_braille = {**eng_to_braille, **e_to_b_capitalize}

# numbers must be done separately due to them only needing the identifier "number" once and then follow the convention of a-j
eng_to_braille_numbers = {}
# numbers 0-9
for i in range(1,11):
    # Since the braille pattern starts at 1 and ends at 0, we need to start our range at 1 but index at 0
    corresponding_base_letter = e_to_b_base_letters[ascii_lowercase[i-1]]
    # We need to take mod 10 to allow us to get 1-9 then 0 in that order:
    eng_to_braille_numbers[str(i%10)] = corresponding_base_letter


# Now simply reverse english and braille key/value in the dictionary to get braille to english
braille_to_eng = {b:e for e, b in eng_to_braille.items()}
# And also for numbers:
braille_to_eng_numbers = {b:e for e, b in eng_to_braille_numbers.items()}



################ Step 2: Language Detection Function
def detect_language(message):
	'''
    Detects language of inputted message (either English or Braille).

    Parameters:
    ----------
    message : str
        The message to be checked for language.
   
    Returns:
    -------
    str
        The language found: english, braille, or neither.

    Exception:
    --------
		Returns error if message inputted is blank
    '''
	if message != '':
	    lang = ''
	    # You must include the entire English alphabet, the ability to capitalize letters, add spaces, and the numbers 0 through 9 as well.
	    english_pattern = r"^[a-zA-Z0-9 ]*$"
	    english_match = re.fullmatch(english_pattern, message)
	    
	    # Braille can only consist of O or .
	    braille_pattern = r"^[O.]*$"
	    braille_match = re.fullmatch(braille_pattern, message)

	    if english_match is not None:
	        lang = 'english'
	    elif braille_match is not None:
	        lang = 'braille'
	    else:
	        lang = 'neither'
	    return lang
	else:
	    print("Error. Your message was empty. Please provide a message to translate.")
	    sys.exit()




################ Step 3: Make function to translate from one language to the next:
def translator_braille_english(message):
    '''
    Translates from Braille to English and vice versa.

    Parameters:
    ----------
    message : str
        The message to be translated.

    Returns:
    -------
    str
        The translated message to the opposite language.

    Exception:
    --------
        Returns error if message does not correspond with either English or Braille language guidelines.
    '''

    # detect language of message
    language = detect_language(message)

    # English to Braille:
    if language == 'english':
        # create blank message
        translated_message = ''
        i = 0
        
        # Iterate through each character in message
        while i < len(message):
            character = message[i]
            
            ## Numbers: "When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol."
            if character.isdigit():
                # If it is a number: add the leading "number" braille sign
                translated_message += eng_to_braille['number']

                # Only time it stops being a number is with a space following or end of message
                while i < len(message) and message[i] != ' ':
                    # access the numbers dictionary to map the number to braille
                    translated_message += eng_to_braille_numbers[message[i]] 
                    i += 1
                    
            else:
                # if not number, use regular dictionary to map from english to braille:
                translated_message += eng_to_braille[character]
                i += 1

        # Once all characters have been converted return message
        return translated_message



    # Braille to English:
    elif language == 'braille':
        translated_message = ''
        # Since Braille is done in sequence of 6 characters, we want to define a variable for code readability
        BRAILLE_LETTER_LENGTH = 6
        i = 0
        j = BRAILLE_LETTER_LENGTH

        # Since braille is in 6 chunks, it should be checked mod 6
        if len(message)%6 != 0:
        	print("Error: Braille needs to have groups of 6 characters. Please try again.")
        	sys.exit()

        # Now we iterate through each "letter chunk" until end of whole message
        while i < len(message):
            # create braille "chunks" which would represent one letter in English
            letter_chunk = braille_to_eng[message[i:j]]

            ## Capitals: "When a Braille capital follows symbol is read, assume only the next symbol should be capitalized."
            # If there is a capital signifier in the "6-char chunk" we are looking at we must do 2 things
            if letter_chunk == 'capital':
                # 1: we need to extend the "chunk" to be 12 characters long before mapping it to English to include 'capital' along with letter
                translated_message += braille_to_eng[message[i:j+BRAILLE_LETTER_LENGTH]]
                # 2: we need to skip past 2 chunks to get to the next letter (since it would be 12 in length versus the normal 6)
                i += BRAILLE_LETTER_LENGTH*2
                j += BRAILLE_LETTER_LENGTH*2


            ## Numbers: "When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol."
            elif letter_chunk == 'number':
                # skip number 6-char chunk:
                i += BRAILLE_LETTER_LENGTH 
                j += BRAILLE_LETTER_LENGTH

                # Check if 'letter' is a space or end of message to know if number mapping ends
                while i < len(message) and braille_to_eng[message[i:j]] != ' ':
                    translated_message += braille_to_eng_numbers[message[i:j]]
                    i += BRAILLE_LETTER_LENGTH 
                    j += BRAILLE_LETTER_LENGTH
            
            # If not number or capital, just append letter to message:
            else:
                translated_message += letter_chunk
                i += BRAILLE_LETTER_LENGTH
                j += BRAILLE_LETTER_LENGTH

        return translated_message

    # return error message if not Braille of English
    elif language == 'neither':
        print("Error: Input neither English nor Braille.\n  English: English letters, numbers, and spaces only (no symbols) OR\n  Braille: O or . (no spaces)")
        sys.exit()



# Step 4: Call main function to be able to run from terminal
if __name__ == "__main__":
	# Make sure the command line is not empty:
    if len(sys.argv) > 1:
    	# sys.argv[0] is the "python3" command
    	# sys.argv[1] is the "translator.py" command
        # sys.argv[1:] gives the list of message, which we want to combine into one message with spaces
        message = " ".join(sys.argv[1:])
        
        # Translate the message
        new_message = translator_braille_english(message)

        # Output the translated message
        print(new_message)
    else:
        print("Error. Your message was empty. Please provide a message to translate.")



#### Exemplars ####
# Input: Hello world
# Output: .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..

# Input: 42
# Output: .O.OOOOO.O..O.O...


# Input: .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
# Output: Abc 123






