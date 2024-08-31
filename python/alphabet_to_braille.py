import maps

def translate(text):
    """ Translates the English text to Braile text, charcter by character. """
    # Initialization of result and number mode tracking
    result = ''
    is_prev_char_number = False

    for character in text:
        # Get the corresponding English character from the appropriate map
        # Numbers
        if character.isnumeric():
            if not is_prev_char_number:
                result += maps.escape_characters_to_braille.get('num')

            result += maps.number_to_braille.get(character)
            is_prev_char_number = True

        # Spaces
        elif character == ' ':
            result += maps.escape_characters_to_braille.get(' ')
            is_prev_char_number = False

        # Alphabet  
        else:
            # Upper cases
            if character.isupper():
                result += maps.escape_characters_to_braille.get('cap')
                character = character.lower()
            
            result += maps.alphabet_to_braille.get(character)
            is_prev_char_number = False
    
    # Output to stdout
    print(result)