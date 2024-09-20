import sys

#translation dictionaries
BrailleToEnglish = { 
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",
    ".....O": "capitalNext",
    ".O.OOO": "numberNext"
}
BrailleToNumber = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}
#creating new dictionaries for reversed translations by flipping key and value
EnglishToBraille = {BrailleToEnglish[a]:a for a in BrailleToEnglish}

NumberToBraille = {BrailleToNumber[a]:a for a in BrailleToNumber}

#function for translating braille to english
def brailleTranslator(string):
    result = ""
    isCapital = False
    isNumber = False
	
	#iterate through braille string
    for i in range(0, len(string) // 6):
		
		#retreive segment of 6 characters and convert with dictionary
        segment = string[6*i:6*i+6]
        char = BrailleToEnglish[segment]  

        #check if segment is a flag to modify next char, if so, move on to next segment
        if char == "capitalNext":
            isNumber = False
            isCapital = True
        elif char == "numberNext":
            isCapital = False
            isNumber = True
			
        else:
			#check for flags and modify capital and number chars as needed
            if isCapital and char.isalpha():
                result += char.capitalize()
            elif isNumber:
                if segment in BrailleToNumber: 
                    result += BrailleToNumber[segment]
					
				#check if space
                elif segment == "......":
                    isNumber = False   
                    result += char
			
			#regular letter, add to string
            else:
                result += char
	
            isCapital = False
    return result

#function to translate english to braille
def englishTranslator(string):
    result = ""
    isNumber = False
	
    for char in string: 
		
		#if character is a number, add number follows in braille followed by number, repeating as long as number flag is raised
        if char.isnumeric():  
            if not isNumber:
                result += EnglishToBraille["numberNext"]
                isNumber = True
            result += NumberToBraille[char]
			
		#if char is alphabetical
        else:
			
			#if number flag is raised, lower flag and check for space to end number sequence
            if isNumber:
                isNumber = False
                if char is not ' ':
                    res += "......"
					
			#add capital flag if letter is capital
            if char.isupper():
                result += EnglishToBraille["capitalNext"]
				
			#add regular lowercase letter translation
            result += EnglishToBraille[char.lower()]
    return result

def translate(string):
	#run enlgish translation if string is not in 6 character segments
	if len(string) % 6 != 0:
		return englishTranslator(string)
	
	#run enlgish translation if string contains character that isnt braille symbol
	for char in string:
		if not (char == 'O' or char == '.'):
			return englishTranslator(string)
	
	#run braille translation otherwise
	return brailleTranslator(string)

if __name__ == "__main__":
    inputString = ' '.join(sys.argv[1:])
    print(translate(inputString))
