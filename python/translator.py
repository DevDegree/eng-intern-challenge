
import sys 
import argparse
import typing


alphabet = {
	'a':'O.....',
	'b':'O.O...',
	'c':'OO....',
	'd':'OO.O..',
	'e':'O..O..',
	'f':'OOO...',
	'g':'OOOO..',
	'h':'O.OO..',
	'i':'.OO...',
	'j':'.OOO..',
	'k':'O...O.',
	'l':'O.O.O.',
	'm':'OO..O.',
	'n':'OO.OO.',
	'o':'O..OO.',
	'p':'OOO.O.',
	'q':'OOOOO.',
	'r':'O.OOO.',
	's':'.OO.O.',
	't':'.OOOO.',
	'u':'O...OO',
	'v':'O.O.OO',
	'w':'.OOO.O',
	'x':'OO..OO',
	'y':'OO.OOO',
	'z':'O..OOO',
}
numbers = {
	'1':'O.....',
	'2':'O.O...',
	'3':'OO....',
	'4':'OO.O..',
	'5':'O..O..',
	'6':'OOO...',
	'7':'OOOO..',
	'8':'O.OO..',
	'9':'.OO...',
	'0':'.OOO..',
}

capital = '.....O'
space = '......'
num_follows = '.O.OOO'

def get_key_from_value(d, value):
	for k, v in d.items():
		if v == value:
			return k
	return None

def braille_to_english(input_string: str) -> str:
	translation = []
	flag = False
	num = False

	for i in range(0,len(input_string),6):
		char = input_string[i:i+6]
		if char == capital:
			flag = True
			continue

		if char == num_follows:
			num = True
			continue

		if char == space:
			num = False
			translation.append(' ')
			continue

		if num:
			number = get_key_from_value(numbers, char)
			translation.append(number)
			continue

		letter = get_key_from_value(alphabet, char)

		if flag:
			letter = letter.upper()
			flag = False
		translation.append(letter)

	return ''.join(translation)

def english_to_braille(input_string: str) -> str:
	translation = []
	flag = False
	for char in input_string:

		if char.isupper():
			translation.append(capital)
			translation.append(alphabet[char.lower()])
			continue

		if char.isnumeric() and not flag:
			flag = True
			translation.append(num_follows)
			translation.append(numbers[char])
			continue

		if char.isnumeric() and flag:
			translation.append(numbers[char])
			continue

		if char == ' ':
			flag = False
			translation.append(space)
			continue

		letter = translation.append(alphabet[char])

	return ''.join(translation)

def english_or_braille(input_string: str) -> str:
	if input_string[0].isalnum():
		return 'english'
	else:
		return 'braille'

def translate(args):
	words = args
	language = english_or_braille(words)
	res = []

	if language == 'english':
		for word in words:
			translation = english_to_braille(word)
			res.append(translation)

	if language == 'braille':
		for word in words:
			res.append(braille_to_english(word))

	print(space.join(res))
			

if __name__=='__main__':
	args = sys.argv[1:]
	translate(args)

## if captial follows, only next element is capital
## if number follows, symbol is read as number until spaces
## if space, exit while loop of numbers if exists otherwise, just add space