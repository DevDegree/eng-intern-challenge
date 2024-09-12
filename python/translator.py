import sys
from constants import *


# Converts alphabet to Braille
def translate_to_braille(text: str):
	output = []

	is_number = False
	for letter in text:
		# If digit, add the "NUMBER_FOLLOWS" prefix if it's not already added
		# is_number is switched to False when we encounter a non-digit character
		if letter.isdigit():
			if not is_number:
				output.append(NUMBER_FOLLOWS)
				is_number = True
			output.append(ALPHABET_TO_BRAILLE[NUMBER_TO_CHAR[letter]])

		else:
			is_number = False
			output.append(ALPHABET_TO_BRAILLE[letter])

	return ''.join(output)


# Converts Braille to alphabet
def translate_to_alphabet(text: str):
	output = []
	is_number = False
	is_capital = False

	for i in range(0, len(text), 6):
		letter = text[i : i + 6]

		if letter == NUMBER_FOLLOWS:
			is_number = True
		elif letter == CAPITAL_FOLLOWS:
			is_capital = True
		else:
			if letter == BRAILLE_SPACE:
				is_number = False

			if is_capital:
				letter = CAPITAL_FOLLOWS + letter
				is_capital = False

			if is_number:
				output.append(CHAR_TO_NUMBER[BRAILLE_TO_ALPHABET[letter]])
			else:
				output.append(BRAILLE_TO_ALPHABET[letter])

	return ''.join(output)


if __name__ == '__main__':
	input_text = ' '.join(sys.argv[1 :])
	if '.' in input_text:
		print(translate_to_alphabet(input_text))
	else:
		print(translate_to_braille(input_text))
