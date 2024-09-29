import sys

# could definitely merge into one map, but feel like this is easier to read/maintain
# especially when reversing key:values for reverse translations -- there could be duplicates if it was all one map

letters = {
	'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
	'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
	'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
	'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
	'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
	'z': 'O..OOO'
}

numbers = {
	'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
	'6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

symbols = {
	'.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
	';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
	'(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

flags = {
	'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO'
}

# if braille -- 
	# (string length mod 6) == 0
	# string will only contain "." or "O" 
	# could also check to see if it converts to valid english, but i think that's overkill
def is_braille(txt):
	if ((len(txt) % 6) != 0):
		return False
	for char in txt:
		if ((char != '.') and (char != 'O')):
			return False
	return True

def main():
	input_arr = sys.argv[1:]
	if not input_arr:
		sys.exit('Invalid input')
	input_str = ' '.join(input_arr)

if __name__ == "__main__":
	main()
    