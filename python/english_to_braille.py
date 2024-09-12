from maps import english_to_braille_map

def english_to_braille(text):
    result = []
    digit = False
    for letter in text:
        if(letter.isalpha()):
            if(letter.isupper()):
                result.append(english_to_braille_map['capital_follows'])
            result.append(english_to_braille_map[letter.lower()])
        elif(letter.isnumeric()):
            if(not digit):
                result.append(english_to_braille_map['number_follows'])
                digit = True
            result.append(english_to_braille_map[letter])
        elif(letter==" "):
            digit = False
            result.append(english_to_braille_map['space'])
    return "".join(result)
    