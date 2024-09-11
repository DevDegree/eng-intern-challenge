import sys

# English to Braille mappings
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', '.':'...O.O'
}
braille_numbers={
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', '.':'...O.O'
}

# Reverse the dictionary for Braille to English mapping
braille_to_english_dict = {v: k for k, v in braille_alphabet.items()}
braille_to_english_num_dict = {v: k for k, v in braille_numbers.items()}

# Braille symbols for special markers
braille_capital = '.....O'
braille_number = '.O.OOO'
braille_decimal = '...O.O'

# Function to convert English to Braille
def english_to_braille(text):
    result = []
    is_number = False
    for char in text:
        if char.isdigit():
            if not is_number:
                result.append(braille_number)  # Add number sign before digits
                is_number = True
            result.append(braille_numbers[char])
        elif char == '.':
            result.append(braille_alphabet['.'])  # Braille symbol for decimal
        elif char.isalpha():
            if is_number:
                is_number = False  # Reset number sign after letters
            if char.isupper():
                result.append(braille_capital)  # Add capital sign for uppercase
            result.append(braille_alphabet[char.lower()])
        else:
            result.append(braille_alphabet[char])
    return ''.join(result)

# Function to convert Braille to English
def braille_to_english(text):
    result = []
    char =[]
    i = 0
    is_capital = False
    is_number = False
    while i < len(text):
        symbol = text[i:i+6]

        if symbol == braille_capital:
            is_capital = True
        elif symbol == braille_number:
            is_number = True
        elif symbol == braille_decimal:  # Braille symbol for decimal
            result.append('.')
        elif symbol in braille_to_english_dict:
            if not is_number:
              char = braille_to_english_dict[symbol]
              if is_capital:
                result.append(char.upper())
                is_capital = False
              else:
                result.append(char)
            elif is_number:
                char = braille_to_english_num_dict[symbol]
                result.append(char)

            is_number = False if char.isalpha() else is_number
        i += 6
    return ''.join(result)

# Function to determine if the input is Braille or English
def is_braille(text):
    return all(c in 'O.' for c in text) and len(text) % 6 == 0



# Main function
def main():
    # Ensure there are 1 or more input is provided
    if len(sys.argv) < 2:
        return
    i=1
    while i < len(sys.argv):
      #add spaces between arguments
      if i == 1 : input_text = sys.argv[i]
      else: input_text = " " + sys.argv[i]

      # Detect if input is Braille or English and translate
      if is_braille(input_text):
        print(braille_to_english(input_text),end="" )
      else:
        print(english_to_braille(input_text), end="" )
      i+= 1
    return
if __name__ == "__main__":
    main()
