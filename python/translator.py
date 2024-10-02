import sys

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

reverse_alphabet = {v: k for k, v in alphabet.items()}
reverse_numbers = {v: k for k, v in numbers.items()}

def braille_to_english(input_string: str) -> str:
	translation = []
	capital_flag = False
	num_flag = False

	for i in range(0,len(input_string),6):
		char = input_string[i:i+6]
		if char == capital:
			capital_flag = True
			continue

		if char == num_follows:
			num = True
			continue

		if char == space:
			num_flag = False
			translation.append(' ')
			continue

		if num_flag:
			number = reverse_numbers.get(char,'')
			translation.append(number)
			continue

		letter = reverse_alphabet.get(char,'')

		if capital_flag:
			letter = letter.upper()
			capital_flag = False
		translation.append(letter)

	return ''.join(translation)

def english_to_braille(input_string: str) -> str:
	translation = []
	num_flag = False
	for char in input_string:

		if char.isupper():
			translation.append(capital)
			translation.append(alphabet.get(char.lower(),''))
			continue

		if char.isnumeric():
			if not num_flag:
				num_flag = True
				translation.append(num_follows)
			translation.append(numbers.get(char,''))
			continue

		if char == ' ':
			num_flag = False
			translation.append(space)
			continue

		letter = translation.append(alphabet.get(char,''))

	return ''.join(translation)

def english_or_braille(input_string: str) -> str:
	braille_chars = {'.', 'O'}
	if all(char in braille_chars for char in input_string):
		return 'braille'
	else:
		return 'english'

def translate(args):
	language = english_or_braille(''.join(args))
	if language == 'english':
		translations = [english_to_braille(word) for word in args]
	else:
		translations = [braille_to_english(word) for word in args]

	print(space.join(translations))
			
if __name__=='__main__':
	args = sys.argv[1:]
	translate(args)
