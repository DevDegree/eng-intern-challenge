import sys

def languageType(input):
	for c in input:
		if c != "O" and c != ".":
			return "English"

	return "Braille" if not len(input) % 6 else "English"

def translateEnglish(input):
	number = False; 
	result = "" 

	charDict = {
		"a" : "O.....",
		"b" : "O.O...",
		"c" : "OO....",
		"d" : "OO.O..",
		"e" : "O..O..",
		"f" : "OOO...",
		"g" : "OOOO..",
		"h" : "O.OO..",
		"i" : ".OO...",
		"j" : ".OOO..",
		"k" : "O...O.",
		"l" : "O.O.O.",
		"m" : "OO..O.",
		"n" : "OO.OO.",
		"o" : "O..OO.",
		"p" : "OOO.O.",
		"q" : "OOOOO.",
		"r" : "O.OOO.",
		"s" : ".OO.O.",
		"t" : ".OOOO.",
		"u" : "O...OO",
		"v" : "O.O.OO",
		"w" : ".OOO.O",
		"x" : "OO..OO",
		"y" : "OO.OOO",
		"z" : "O..OOO",
		"1" : "O.....",
		"2" : "O.O...",
		"3" : "OO....",
		"4" : "OO.O..",
		"5" : "O..O..",
		"6" : "OOO...",
		"7" : "OOOO..",
		"8" : "O.OO..",
		"9" : ".OO...",
		"0" : ".OOO..",
		" " : "......",
	}

	for i, c in enumerate(input):
		if c.isalpha():
			if c.isupper():
				result+=".....O"
			
			result+=charDict[c.lower()]
		
		else:
			if c.isdigit() and not number:
				number = True
				result += ".O.OOO"
			
			elif c == " ":
				number = False
			
			result += charDict[c]
	
	return result

def translateBraille(input): 
	number, capital = False, False
	result = "" 
	l, r = 0, 5

	numDict = {
		"O....." : "1",
		"O.O..." : "2",
		"OO...." : "3",
		"OO.O.." : "4",
		"O..O.." : "5",
		"OOO..." : "6",
		"OOOO.." : "7",
		"O.OO.." : "8",
		".OO..." : "9",
		".OOO.." : "0"
	}
	
	alphaDict = {
		"......" : " ",
		"O....." : "a",
		"O.O..." : "b",
		"OO...." : "c",
		"OO.O.." : "d",
		"O..O.." : "e",
		"OOO..." : "f",
		"OOOO.." : "g",
		"O.OO.." : "h",
		".OO..." : "i",
		".OOO.." : "j",
		"O...O." : "k",
		"O.O.O." : "l",
		"OO..O." : "m",
		"OO.OO." : "n",
		"O..OO." : "o",
		"OOO.O." : "p",
		"OOOOO." : "q",
		"O.OOO." : "r",
		".OO.O." : "s",
		".OOOO." : "t",
		"O...OO" : "u",
		"O.O.OO" : "v",
		".OOO.O" : "w",
		"OO..OO" : "x",
		"OO.OOO" : "y",
		"O..OOO" : "z",
	}

	while r < len(input):
		if input[l:r+1] == ".....O":
			capital = True
		
		elif input[l:r+1] == ".O.OOO":
			number = True

		else:
			if input[l:r+1] == "......":
				number = False
			
			if number:
				result += numDict[input[l:r+1]]
			
			elif capital:
				result += alphaDict[input[l:r+1]].upper()
				capital = False
			
			else:
				result += alphaDict[input[l:r+1]]

		l, r = l + 6, r + 6
	
	return result

def main():
	if len(sys.argv) > 1:
		user_input=" ".join(sys.argv[1:])
		language = languageType(user_input)

		if language == "English":
			res = translateEnglish(user_input)
		
		else:
			res = translateBraille(user_input)

		print(res);

	else:
		print("Invalid phrase. Try again.")

if __name__ == "__main__":
	main();