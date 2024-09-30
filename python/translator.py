
import sys 
import argparse
import typing
# inputs = []

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

capital = ('CAPITAL','.....0')
space = (' ', '......')

def braille_to_english(input_string: str) -> str:
	continue

def english_to_braille():
	continue
def translate(args):
	continue

if __name__=='__main__':
	args = parse_args()

	for arg in args:
		if isinstance(arg,str):
			# inputs.append(arg)
		continue
	# elif isinstance(arg, list) and all(isinstance(item,str) for item in arg):
	# 	inputs.extend(arg)
	else:
		raise Error('wrong type of input')
	translate(args)

## if captial follows, only next element is capital
## if number follows, symbol is read as number until spaces
## if space, exit while loop of numbers if exists otherwise, just add space