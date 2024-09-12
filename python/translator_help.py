# this file contains all the dictionaries and variables needed for translating between braille and English

# the format for english_to_braille_char and number_to_braille is as follows: 
# the key contains the character,
# the value contains a list of the numbers for the respective raised dots in each 3x2 grid, using the following legend: 
# 1 2
# 3 4
# 5 6

english_to_braille_char = {
        'a': [1],
        'b': [1,3],
        'c': [1,2], 
        'd': [1,2,4],
        'e': [1,4],
        'f': [1,2,3],
        'g': [1,2,3,4],
        'h': [1,3,4],
        'i': [2,3],
        'j': [2,3,4],
        'k': [1,5],
        'l': [1,3,5],
        'm': [1,2,5],
        'n': [1,2,4,5],
        'o': [1,4,5],
        'p': [1,2,3,5],
        'q': [1,2,3,4,5],
        'r': [1,3,4,5],
        's': [2,3,5],
        't': [2,3,4,5],
        'u': [1,5,6], 
        'v': [1,3,5,6], 
        'w': [2,3,4,6], 
        'x': [1,2,5,6], 
        'y': [1,2,4,5,6], 
        'z': [1,4,5,6]
    }

number_to_braille_char = {
    '1': [1],
    '2': [1,3],
    '3': [1,2], 
    '4': [1,2,4],
    '5': [1,4],
    '6': [1,2,3],
    '7': [1,2,3,4],
    '8': [1,3,4],
    '9': [2,3],
    '0': [2,3,4]
}

# this helper function changes list of numbers above into O and . for hashability in the following dictionaries
def number_to_braille_code(raised_dots: list) -> str: 
    raised = [False] * 6
    for dot in raised_dots: 
        try:
            raised[dot - 1] = True
        except: 
            print("Out of index when trying to convert list of numbers into braille code")
    result_braille = ""
    for i in range(6): 
        if raised[i]: 
            result_braille += 'O'
        else: 
            result_braille += '.'
    assert(len(result_braille) == 6)
    return result_braille

# braille_to_english_char and braille_to_number_char are the reverses of the two dictionaries above, 
# but then the keys would be changed into O and . for hashability

braille_to_english_char = {number_to_braille_code(value): key for key, value in english_to_braille_char.items()}

braille_to_number_char = {number_to_braille_code(value): key for key, value in number_to_braille_char.items()} 

capital_follows_braille = ".....O" # braille code for capital follows 

number_follows_braille = ".O.OOO" # braille code for number follows 