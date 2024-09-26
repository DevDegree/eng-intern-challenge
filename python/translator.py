import sys

# Hashmap for Braille -> English
braille_to_eng = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
		"OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
		"O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
		"OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
		"O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
		"O..OOO": "z", ".....O": "capital", ".O.OOO": "number", "......": "space"
}

# Hashmap for English -> Braille
eng_to_braille = {
	val: key for key,val in braille_to_eng.items()
}

# Hashmap for Letters -> Numbers in Braille
letter_to_number = {
	"a" : "1", "b" : "2", "c" : "3", "d" : "4", "e" : "5", "f" : "6",
	"g" : "7", "h" : "8", "i" : "9", "j" : "0"
}

# Hashmap for Numbers -> Letters in Braille
number_to_letter = {
	val: key for key,val in letter_to_number.items()
}


def translate_english(str_input: str) -> None:
	braille = []
	numbers_mode = False
	for character in str_input:
		if (character.isdigit()):
			if (not numbers_mode):
				numbers_mode = True
				braille.append(eng_to_braille["number"])

			braille.append(eng_to_braille[number_to_letter[character]])

		elif (character.isupper()):
			braille.append(eng_to_braille["capital"])
			braille.append(eng_to_braille[character.lower()])
		elif (character == " "):
			braille.append(eng_to_braille["space"])
			numbers_mode = False
		else:
			braille.append(eng_to_braille[character])
	
	print("".join(braille))

def translate_braille(str_input: str) -> None:
	english = []
	make_upper = False
	numbers_mode = False

	for i in range(0,len(str_input),6):
		single_input = str_input[i:i+6]

		english_word = braille_to_eng[single_input]

		if (english_word == "capital"):
			make_upper = True
			continue
		
		if (english_word == "number"):
			numbers_mode = True
			continue

		if (english_word == "space"):
			english.append(" ")
			numbers_mode = False
			continue

		if (make_upper):
			english.append(english_word.upper())
			make_upper = False
		elif (numbers_mode):
			english.append(letter_to_number[english_word])
		else:
			english.append(english_word)

	print("".join(english))

def is_braille(str_input: str) -> bool:
	return ((len(str_input) % 6 == 0) and all(c in {"O", "."} for c in str_input[0:6]))


# Main function for reading input and executing appropriate function.
if __name__=="__main__":
	str_input = " ".join(sys.argv[1:]) # Concatenates all the input by the user into a single string to be translated.

	if (is_braille(str_input)):
		translate_braille(str_input)
	else:
		translate_english(str_input)