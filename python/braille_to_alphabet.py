import maps

class B2A:
    def __init__(self, text) -> None:
        """ Initializes the Braille to Alphabet converter with the provided text. """
        self.text = text
        self.mode = 'alphabet'  # Reading braille as alphabet characters until numbers specified
        self.map = self.set_map()  # Initializes the character map based on the mode

    def set_map(self):
        """ Sets the appropriate character map based on the current mode. """
        if self.mode == 'number':
            return maps.braille_to_escape_characters | maps.braille_to_number
        else:
            return maps.braille_to_escape_characters | maps.braille_to_alphabet

    def set_mode(self, mode):
        """ Sets the mode and updates the map accordingly. """
        self.mode = mode
        self.map = self.set_map()

    def translate(self):
        """ Translates the Braille text to English text based on the current map and mode. """
        # Initialization and organize text into character groups of 6 (Braille cell size)
        braille_groups = [self.text[i:i+6] for i in range(0, len(self.text), 6)]     
        result = ''

        translate_pointer = 0

        while translate_pointer < len(braille_groups):
            # Get the corresponding English character from the map
            braille_char = braille_groups[translate_pointer]
            character = self.map.get(braille_char, '')

            # Handle special characters and modes
            if character == 'cap':
                translate_pointer += 1
                if translate_pointer < len(braille_groups):
                    next_char = self.map.get(braille_groups[translate_pointer], '')
                    result += next_char.upper()
            
            elif character == 'num':
                self.set_mode('number')

            else:
                if character == ' ':
                    self.set_mode('alphabet')
                result += character

            # Increment
            translate_pointer += 1
        
        # Output to stdout
        print(result)