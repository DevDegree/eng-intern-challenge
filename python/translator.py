import sys

def languageType(input): # tested!
	for c in input:
		if c != "0" and c != ".":
			return "English"

		return "Braille" if not len(input) % 6 else "English"

def translateEnglish(input):
	number = False; # check if it is the first number
	result = "" 

	charDict = {
		"a" : "0.....",
		"b" : "0.0...",
		"c" : "00....",
		"d" : "00.0..",
		"e" : "0..0..",
		"f" : "000...",
		"g" : "0000..",
		"h" : "0.00..",
		"i" : ".00...",
		"j" : ".000..",
		"k" : "0...0.",
		"l" : "0.0.0.",
		"m" : "00..0.",
		"n" : "00.00.",
		"o" : "0..00.",
		"p" : "000.0.",
		"q" : "00000.",
		"r" : "0.000.",
		"s" : ".00.0.",
		"t" : ".0000.",
		"u" : "0...00",
		"v" : "0.0.00",
		"w" : ".000.0",
		"x" : "00..00",
		"y" : "00.000",
		"z" : "0..000",
		"1" : "0.....",
		"2" : "0.0...",
		"3" : "00....",
		"4" : "00.0..",
		"5" : "0..0..",
		"6" : "000...",
		"7" : "0000..",
		"8" : "0.00..",
		"9" : ".00...",
		"0" : ".000..",
		" " : "......",
	}

	for i, c in enumerate(input):
		if c.isalpha():
			if c.isupper():
				result+=".....0"
			
			result+=charDict[c.lower()]
		
		else:
			if c.isdigit() and not number:
				number = True
				result += ".0.000"
			
			elif c == " ":
				number = False
			
			result += charDict[c]
	
	return result

def translateBraille(input): 
	number, capital = False, False
	result = "" 
	l, r = 0, 5

	numDict = {
		"0....." : "1",
		"0.0..." : "2",
		"00...." : "3",
		"00.0.." : "4",
		"0..0.." : "5",
		"000..." : "6",
		"0000.." : "7",
		"0.00.." : "8",
		".00..." : "9",
		".000.." : "0"
	}
	
	alphaDict = {
		"......" : " ",
		"0....." : "a",
		"0.0..." : "b",
		"00...." : "c",
		"00.0.." : "d",
		"0..0.." : "e",
		"000..." : "f",
		"0000.." : "g",
		"0.00.." : "h",
		".00..." : "i",
		".000.." : "j",
		"0...0." : "k",
		"0.0.0." : "l",
		"00..0." : "m",
		"00.00." : "n",
		"0..00." : "o",
		"000.0." : "p",
		"00000." : "q",
		"0.000." : "r",
		".00.0." : "s",
		".0000." : "t",
		"0...00" : "u",
		"0.0.00" : "v",
		".000.0" : "w",
		"00..00" : "x",
		"00.000" : "y",
		"0..000" : "z",
	}

	while r < len(input):
		# special characters => space, capital follows, number follows
		if input[l:r+1] == ".....0":
			capital = True
		
		elif input[l:r+1] == ".0.000":
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

if __name__ == "__main__":
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