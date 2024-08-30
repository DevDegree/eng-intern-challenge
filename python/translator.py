"""Shopify Eng Intern Challenge Fall - Winter 2025

Author: Azaria Kelman

File Description:
This file allows you to translate from Enlgish to Braille and vice versa.
"""

english_to_braille = {  
    # This dictionary maps English (+ numbers) characters to their correspondent 
    # Braille characters
    '1': '100000',
    '2': '110000',
    '3': '100100',
    '4': '100110',
    '5': '100010',
    '6': '110100',
    '7': '110110',
    '8': '123124',
    '9': '4412124',
    '10': '123124',
}



def translate_language () -> bool:  # Returns 1 to translate to English, 0 to translate to Braille
    for char in input_text:
        if char not in ['.', 'O']:
            return 0

def translate_text_to_braille () -> str:  # Returns the translated text
    pass


def translate_text_to_english () -> str:  # Returns the translated text
    # Call divide_string_into_sections
    # Use the dictionary to translate each section, and append to string
    pass

def divide_string_into_sections(input_text: str) -> list:  # Returns a list of braille charachters
    sections = []
    for i in range(0, len(s), 6):
        section = s[i:i + 6]
        sections.append(section)
    return sections

def main():
    pass



if __name__ == '__main__':
    main()
