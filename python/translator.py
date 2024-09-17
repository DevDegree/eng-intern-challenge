brailleToNumber = {
	"O....." : "1",
	"O.O..." : "2",
	"OO...." : "3",
	"OO.O.." : "4",
	"O..O.." : "5",
	"OOO..." : "6",
	"OOOO.." : "7",
	"O.OO.." : "8",
	".OO..." : "9",
	".OOO.." : "0",
}

numberToBraille = {
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
}

brailleToChar = {
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

	".....O" : "capital",
	".O...O" : "decimal",
	".O.OOO" : "number",

	"..OO.O" : ".",
	"..O..." : ",",
	"..O.OO" : "?",
	"..OOO." : "!",
	"..OO.." : ":",
	"..O.O." : ";",
	"....OO" : "-",
	".O..O." : "/",
	".OO..O" : "<",
	"O..OO." : ">",
	"O.O..O" : "(",
	".O.OO." : ")",
	"......" : " "
}

charToBraille = {
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

	"capital" : ".....O",
	"decimal" : ".O...O",
	"number" : ".O.OOO",

	"." : "..OO.O",
	"," : "..O...",
	"?" : "..O.OO",
	"!" : "..OOO.",
	":" : "..OO..",
	";" : "..O.O.",
	"-" : "....OO",
	"/" : ".O..O.",
	"<" : ".OO..O",
	">" : "O..OO.",
	"(" : "O.O..O",
	")" : ".O.OO.",
	" " : "......"
}

def main(input):
	print(input)
	if isBraille(input):
		brailleStrings = splitBraille(input)
		return translateBrailleStringsToEnglish(brailleStrings)
	else:
		englishChars = list(input)
		return(englishChars)
			

def isBraille(input):
	for c in input:
		if (c != '.' and c != 'O'):
			return False
	return True

def splitBraille(input):
	return splitBrailleTail(input, [])


def splitBrailleTail(input, output):
	if len(input) == 0:
		return output
	else:
		output.append(input[0:6])
		return splitBrailleTail(input[6:], output)
	
def translateBrailleStringsToEnglish(brailleStrings):
	translatedSentence = ""
	specialFollowingCharacter = 0 # 0 for nothing, 1 for capital, 2 for decimal, 3 for number
	
	for string in brailleStrings:
		englishGlyph = brailleToChar[string]
		# space will mark the end of a potential number
		if (englishGlyph == " "):
			specialFollowingCharacter = 0

		# translating a capital
		if (specialFollowingCharacter == 1):
			englishGlyph = englishGlyph.capitalize()
		# translating a number
		elif (specialFollowingCharacter == 3):
			numberGlyph = brailleToNumber[string]
			translatedSentence += numberGlyph
			continue
			
		# special characters which stipulate the translation of following character(s)
		if (englishGlyph == "capital"):
			specialFollowingCharacter = 1
			continue
		elif (englishGlyph == "decimal"):
			specialFollowingCharacter = 2
			continue
		elif (englishGlyph == "number"):
			specialFollowingCharacter = 3
			continue
	
		translatedSentence += englishGlyph
		specialFollowingCharacter = 0

	return translatedSentence



print(main(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"))


