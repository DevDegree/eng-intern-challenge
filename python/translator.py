
# Input: Hello world
# Output: .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..

# Input: 42
# Output: .O.OOOOO.O..O.O...


# Input: .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
# Output: Abc 123


# Step 1: find out whether English or Braille

# Step 2: set language to translate to (give directionality)

# Get English language mapping to Braille
# e.g.
# a = O.....
# A = .....Oa
# 1 = .O.OOOa

# Something to catch we have both a period and a decimal:
# ensure that for the decimal there is a number before it

# If Braille is detected, group into 6
# would it be easier to look for combos of 6 or 12 OR to specify if capital or number or decimal are there to then change the answer?


# Do a .replace( position 3 . to O)
# https://www.perkins.org/how-the-braille-alphabet-works/
# positions:
# 1 4
# 2 5
# 3 6


# Import Libraries
import re

# Step 1: Create dictionary of mapping from english to/from braille
# make a function that you just have to position of 'O' for the string that will already be all .?
eng_to_braille = {
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
    ' ' : '......',
    'capital' : '.....O',
    'number' : '.O.OOO',
    'A' : '.....OO.....',
    'B' : '.....OO.O...',
    '1' : '.O.OOOO.....'
}


braille_to_english = {b:e for e, b in eng_to_braille.items()}


# Step 2: Language Detection Function
def detect_language(message):
    if message != '':
        lang = ''
        # You must include the entire English alphabet, 
        # the ability to capitalize letters, 
        # add spaces, and the numbers 0 through 9 as well.
        english_pattern = r"^[a-zA-Z0-9 ]*$"
        english_match = re.fullmatch(english_pattern, message)
        
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




#### # remove print statements and just put return  ######s
# Step 3: Make function to translate from one language to the next:
def translator_braille_english(message):
	language = detect_language(message)

	if language == 'english':
	    translated_message = ''
	    
	    for i in range(len(message)):
	        translated_message += eng_to_braille[message[i]]
	    print(translated_message)
	    
	elif language == 'braille':
	    translated_message = ''

	    i = 0
	    j = 6
	    # Since braille is in 6 chunks, it should be checked mod 6
	    while i < int(len(message)):
	        message_chunk = braille_to_english[message[i:j]]

	        if message_chunk == 'capital':
	            translated_message += braille_to_english[message[i:j+6]]
	            i += 12
	            j += 12
	        # add statement if it is a number 
	        # if there is a number symbol then it must continue until space
	        # see number word, drop first 6 and then iterate for the following 6 
	        # adding a number symbol to the front
	        # but ensuring I check for a space
	        elif message_chunk == 'number':
	            check_for_space = ''
	            
	            
	            while i < int(len(message)):
	                i += 6 ## Define constant for code readability
	                j += 6
	                check_for_space = braille_to_english[message[i:j]]

	                if check_for_space != ' ' :
	                    translated_message += braille_to_english['.O.OOO' + message[i:j]]
	                if check_for_space == ' ' :
	                    break

	        else:
	            translated_message += message_chunk
	            i += 6
	            j += 6
	    print(translated_message)

	elif language == 'neither':
	    print("Error. Input neither English nor Braille.\n  English: English letters, numbers, and spaces only (no symbols) OR\n  Braille: O or . (no spaces)")
	    


# Step 4: Call main function to be able to run from terminal
if __name__ == "__main___":
	translator_braille_english() # MUST PASS MESSAGE from terminal
	# docop










