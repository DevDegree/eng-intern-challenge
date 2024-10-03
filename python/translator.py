import sys
import re

# Braille Unicode characters for each letter
ENGLISH_IN_BRAILLE= {
	# Lowercase letters and their corresponding braille
	'a' : 'O.....', 'b' : 'O.O...', 'c' : 'OO....', 'd' : 'OO.O..',
	'e' : 'O..O..', 'f' : 'OOO...', 'g' : 'OOOO..', 'h' : 'O.OO..',
	'i' : '.OO...', 'j' : '.OOO..', 'k' : 'O...O.', 'l' : 'O.O.O.',
	'm' : 'OO..O.', 'n' : 'OO.OO.', 'o' : 'O..OO.', 'p' : 'OOO.O.',
	'q' : 'OOOOO.', 'r' : 'O.OOO.', 's' : '.OO.O.', 't' : '.OOOO.',
	'u' : 'O...OO', 'v' : 'O.O.OO', 'w' : '.OOO.O', 'x' : 'OO..OO',
	'y' : 'OO.OOO', 'z' : 'O..OOO', 
	# # Punctuation marks and their corresponding braille
	# '.' : '..OO.O', ',' : '..O...', '?' : '..O.OO', '!' : '..OOO.',
	# ':' : '..OO..', ';' : '..O.O.', '-' : '....OO', '/' : '.O..O.',
	# '<' : '.OO..O', '>' : 'O..OO.', '(' : 'O.O..O', ')' : '.O.OO.',
	' ' : '......',
	# Rules for capital and number signs
	'CAPITAL' : '.....O', 'NUMBER' : '.O.OOO', 
	# # Rules for decimal point
	# 'DECIMAL' : '.O...O'
}

# English characters for each braille letter 
# (reverse of ENGLISH_IN_BRAILLE)
BRAILLE_IN_ENGLISH = {b: e for e, b in ENGLISH_IN_BRAILLE.items()}

def is_braille(input_str):
	"""
	Checks if the input string is in braille.
	Parameters:
		input_str (str): The input string to check.
	Returns:
		bool: True if the input string is in braille, False otherwise.
	"""
	return set(input_str).issubset({'O', '.'})

def english_to_braille(input_str):
	"""
	Converts an English string to braille.
	Parameters:
		input_str (str): The English string to convert.
	Returns:
		str: The corresponding braille string.
	"""
	output_str = ''
	is_number = False

	for char in input_str:
		# Check if the character is a number
		if char.isdigit():
			if not is_number:
				output_str += ENGLISH_IN_BRAILLE['NUMBER']
				is_number = True
      # Convert digit to corresponding letter (1-0 to a-j)
			letter = chr(ord('a') + int(char) - 1) if int(char) > 0 else 'j'
			output_str += ENGLISH_IN_BRAILLE[letter]
		else:
			is_number = False
			# Check if the character is a capital letter
			if char.isupper():
				output_str += ENGLISH_IN_BRAILLE['CAPITAL']
				char = char.lower()
			output_str += ENGLISH_IN_BRAILLE[char]
    
	return output_str

def braille_to_english(input_str):
	"""
	Converts a braille string to English.
	Parameters:
		input_str (str): The braille string to convert.
	Returns:
		str: The corresponding English string.
  Raise:
    ValueError: If the input string can not be split
                into groups of 6 characters.
	"""
	if len(input_str) % 6 != 0:
		raise ValueError("Input string can not be \
          split into groups of 6 characters")

	output_str = ''
	is_number = False
	is_capital = False

  # Split the input string into groups of 6 characters
	braille_chars = [input_str[i:i+6] 
                  for i in range(0, len(input_str), 6)]

	for braille_char in braille_chars:
		if braille_char == ENGLISH_IN_BRAILLE['NUMBER']:
			is_number = True
		elif braille_char == ENGLISH_IN_BRAILLE['CAPITAL']:
			is_capital = True
		else:
			char = BRAILLE_IN_ENGLISH[braille_char]
			if is_number:
				if char in 'abcdefghij':
					# Convert the letter to the corresponding digit
					digit = str('abcdefghi'.index(char) + 1) if char != 'j' else '0'
					output_str += digit
				else:
					is_number = False
					output_str += char
			else:
				if is_capital:
					char = char.upper()
					is_capital = False
				output_str += char

	return output_str

def main():
	# Check if the input string is provided
	if len(sys.argv) < 2:
		print("Please provide an input string following the rule: \n\
					'python3 translator.py <input_string>'")
		sys.exit(1)
	
	# Join the input arguments to form the input string
	input_str = ' '.join(sys.argv[1:])

	# Check if the input string is in braille
	if is_braille(input_str):
		output_str = braille_to_english(input_str)
	else:
		output_str = english_to_braille(input_str)

	print(output_str)

if __name__ == '__main__':
	main()