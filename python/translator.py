import sys
from braille_mapper import BrailleMapper

# Braille constants used for parsing logic
CAPITAL_FOLLOWS_INDICATOR = ".....O"
NUMBER_FOLLOWS_INDICATOR = ".O.OOO"
SPACE_BRAILLE_VALUE = "......"

# Initialize our mapping class
mapper = BrailleMapper()

''' Translates a given braille representation into English characters.'''
def translate_to_english(braille):
    translation = []
    i = 0

    # Iterate over all braille values in chunks of 6 input characters at a time
    while i < len(braille):
        chunk = braille[i:i+6]

        # Append the uppercase value of the following value to our translation
        if chunk == CAPITAL_FOLLOWS_INDICATOR:
            i += 6
            next_chunk = braille[i:i+6]
            translation.append(mapper.get_english(next_chunk, False).upper())
        
        # Append all the following numbers that occur until the next "Space" value
        elif chunk == NUMBER_FOLLOWS_INDICATOR:
            i += 6
            while i < len(braille) and braille[i:i+6] != SPACE_BRAILLE_VALUE:
                translation.append(mapper.get_english(braille[i:i+6], True))
                i += 6
            continue
        
        # Append the English value of the braille representation
        else:
            translation.append(mapper.get_english(chunk, False))
        i += 6
    return ''.join(translation)

def translate_to_braille(text):
    translation = []
    is_number = False

    # Iterate overa ll characters in the provided English string
    for char in text:

        # Handle appending a number follows braille value and setting a flag to indicate we are inserting number values
        if char.isdigit():
            if not is_number:
                translation.append(NUMBER_FOLLOWS_INDICATOR)
                is_number = True
            translation.append(mapper.get_braille(char, is_number))

        # Handle alphabetic values by adding a "Space" value if we are no longer appending numbers, and appending a capital follows value if needed
        elif char.isalpha():
            if is_number:
                translation.append(SPACE_BRAILLE_VALUE)
                is_number = False
            if char.isupper():
                translation.append(CAPITAL_FOLLOWS_INDICATOR)
            translation.append(mapper.get_braille(char.lower(), is_number))
        
        # Handle any other non alpha-numeric value
        else:
            if is_number:
                is_number = False
            translation.append(mapper.get_braille(char, is_number))
    return ''.join(translation)

def main():
    # Take command line arguments and form the input string for translation, parsing the input to determine if it's English or braille
    input = ' '.join(sys.argv[1:])
    if all(char in 'O.' for char in input):
        print(translate_to_english(input))
    else:
        print(translate_to_braille(input))

if __name__ == "__main__":
    main()