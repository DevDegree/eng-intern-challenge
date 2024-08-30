import re

def is_braille(text: str) -> bool:
	# Check if text comprises of only Braille symbols
	if len(text) % 6 == 0 and all(char in "O." for char in text):
		return True
	else:
		return False 

def is_english(text: str) -> bool:
	# Check for given English characters and punctuation
	english_pattern = r'^[a-zA-Z0-9\s.,?!:;/<>()\-\']*$'
	return bool(re.match(english_pattern, text))