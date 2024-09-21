#Shopify Winter Internship Challenge 2025
#Jeremy Thummel
#Braille Translator

entered_text = input()
braille_text_counter = 0
braille_entered = False
decoded_string = ""

for current_char in entered_text:
    if current_char == 'O' or current_char == '.':
        braille_text_counter += 1

if braille_text_counter == len(entered_text):
    braille_entered = True

if braille_entered:
    current_braille_string = ""
    counter = 1
    for current_char in entered_text:
        current_braille_string += current_char