
import sys 
import argparse
import typing


alphabet = {
	'a':'0.....',
	'b':'0.0...',
	'c':'00....',
	'd':'00.0..',
	'e':'0..0..',
	'f':'000...',
	'g':'0000..',
	'h':'0.00..',
	'i':'.00...',
	'j':'.000..',
	'k':'0...0.',
	'l':'0.0.0.',
	'm':'00..0.',
	'n':'00.00.',
	'o':'0..00.',
	'p':'000.0.',
	'q':'00000.',
	'r':'0.000.',
	's':'.00.0.',
	't':'.0000.',
	'u':'0...00',
	'v':'0.0.00',
	'w':'.000.0',
	'x':'00..00',
	'y':'00.000',
	'z':'0..000',
}
numbers = {
	'1':'0.....',
	'2':'0.0...',
	'3':'00....',
	'4':'00.0..',
	'5':'0..0..',
	'6':'000...',
	'7':'0000..',
	'8':'0.00..',
	'9':'.00...',
	'0':'.000..',
}

capital = '.....0'
space = '......'
num_follows = '.0.000'

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
			number = numbers.get(char)
			translation.append(number)
			continue

		letter = alphabet.get(char)

		if flag:
			letter = letter.upper()
			translation.append(letter)

	return ''.join(translation)

def english_to_braille(input_string: str) -> str:
	translation = []
	for char in input_string:

		if char.isupper():
			translation.append(capital)
			translation.append(alphabet[char])
			continue

		if char.isnumeric():
			translation.append(num_follows)
			translation.append(number[char])
			continue

		if char == ' ':
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
	list_of_words = args
	language = english_or_braille(list_of_words)
	res = []

	if language == 'english':
		for word in list_of_words: 
			translation = english_to_braille(word)
			res.append(translation)
			res.append(space)

	print(''.join(res))
			

if __name__=='__main__':
	args = sys.argv[1:]

	# for arg in args:
	# 	if isinstance(arg,str):
	# 		# inputs.append(arg)
	# 	continue
	# # elif isinstance(arg, list) and all(isinstance(item,str) for item in arg):
	# # 	inputs.extend(arg)
	# else:
	# 	raise Error('wrong type of input')
	translate(args)

## if captial follows, only next element is capital
## if number follows, symbol is read as number until spaces
## if space, exit while loop of numbers if exists otherwise, just add space