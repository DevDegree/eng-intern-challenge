import re

def is_decimal(text: str) -> bool:
	# Regular expression to find a dot between digits
	pattern = r'(?<=\d)\.(?=\d)'
	return bool(re.search(pattern, text))

def is_braille(text: str) -> bool:
	# Braille Unicode range for basic Braille patterns (U+2800 to U+28FF)
	if len(text) % 6 == 0 and all(char in "O." for char in text):
		return True
	else:
		return False 

def is_english(text: str) -> bool:
	# Check for typical English characters and punctuation
	english_pattern = r'^[a-zA-Z0-9\s.,?!:;/<>()\-\']*$'
	return bool(re.match(english_pattern, text))