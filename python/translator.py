import sys

# Special Braile indicators
NEXT_CHAR_IS_CAP = ".....O"
ALL_NEXT_IS_NUMS = ".O.OOO"
DECIMAL_FOLLOWS =  ".O...O"

#copy & pasted from braile.jpg
nums_to_braile_table = {
	"1": "O.....",
	"2": "O.O...",
	"3": "OO....",
	"4": "OO.O..",
	"5": "O..O..",
	"6": "OOO...",
	"7": "OOOO..",
	"8": "O.OO..",
	"9": ".OO...",
	"0": ".OOO.."
}

#copy & pasted from braile.jpg
char_to_braile_table = {
	"a": "O.....",
	"b": "O.O...",
	"c": "OO....",
	"d": "OO.O..",
	"e": "O..O..",
	"f": "OOO...",
	"g": "OOOO..",
	"h": "O.OO..",
	"i": ".OO...",
	"j": ".OOO..",
	"k": "O...O.",
	"l": "O.O.O.",
	"m": "OO..O.",
	"n": "O..OO.",
	"o": "O..OO.",
	"p": "OOO.O.",
	"q": "OOOOO.",
	"r": "O.OOO.",
	"s": ".OO.O.",
	"t": ".OOOO.",
	"u": "O...OO",
	"v": "O.O.OO",
	"w": ".OOO.O",
	"x": "OO..OO",
	"y": "OO.OOO",
	"z": "O..OOO",
}

special_to_braile_table = {
	".": "..OO.O",
	",": "..O...",
	"?": "..O.OO",
	"!": "..OOO.",
	":": "..OO..",
	";": "..O.O.",
	"-": "....OO",
	"/": ".O..O.",
	"<": ".OO..O",
	">": "O..OO.",
	"(": "O.O..O",
	")": ".O.OO."
}

#invert mappings
braile_to_char_table = {val: key for key, val in char_to_braile_table.items()}
braile_to_nums_table = {val: key for key, val in nums_to_braile_table.items()}
braile_to_special_table = {val: key for key, val in special_to_braile_table.items()}


"""
returns a string that is the braile equivalent of its english input
"""
def eng_to_braile(eng):
	result = ""
	num_mode = False
	for idx, ch in enumerate(eng):
		#determine which lookup table to use
		if ch.isdigit():
			if num_mode == False:
				num_mode = True
				result += ALL_NEXT_IS_NUMS
			result += nums_to_braile_table[ch]
		else:
			num_mode = False
			if ch.isalnum():
				if ch.isupper():
					result += NEXT_CHAR_IS_CAP
					result += char_to_braile_table[ch.lower()]
				else:
					result += char_to_braile_table[ch]
			else:
				if ch == " ":
					result += "......"
				else:
					result += DECIMAL_FOLLOWS
					result += special_to_braile_table[ch]
	return result

"""
returns a string that is the english equivalent of its braile input
"""
def braile_to_eng(braile):
	result = ""
	caps_flag = False
	nums_flag = False
	decimal_flag = False
	for i in range(0,len(braile), 6):
		# take braile in six length segments
		segment = braile[i:i+6]

		#check for special braile combinations
		#since the special braile combinations aren't actual chars/symbols, we skip to the next iteration
		if segment == NEXT_CHAR_IS_CAP:
			caps_flag = True
			continue
		elif segment == ALL_NEXT_IS_NUMS:
			nums_flag = True
			continue
		elif segment == DECIMAL_FOLLOWS:
			decimal_flag = True
			continue

		#space char check, seems to work easier than checking its string type
		if segment == "......":
			nums_flag = False
			result += " "
			continue

		#use flag status to determine what to append to result
		if caps_flag:
			caps_flag = False
			result += braile_to_char_table[segment].upper()
		elif nums_flag:
			result += braile_to_nums_table[segment]
		elif decimal_flag:
			decimal_flag = False
			result += braile_to_special_table[segment]
		else:
			if segment in braile_to_char_table:
				result += braile_to_char_table[segment]
			else:
				result += braile_to_special_table[segment]

	return result

"""
determine's if the string given is braile or english
Assumptions: characters the string are given are limited to the charset that braile.jpg contains
result: returns true if the string is in braile, otherwise false
"""
def is_braile(txt):
	#since braile only contains 'O' or '.', the number of unique chars in a braile string is two
	#use set to remove duplicate chars
	char_set = set()
	for idx, ch in enumerate(txt):
		char_set.add(ch)

	#addtional check, each braile char has a length six, thus, its total length should be divisble by six
	if len(char_set) == 2 and len(txt) % 6 == 0:
		return True
	else:
		return False

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("python 3 translator.py <string1> string2> ... <stringN>")
		exit(1)

	text = " ".join(sys.argv[1:])
	if is_braile(text):
		print(braile_to_eng(text))
	else:
		print(eng_to_braile(text))
