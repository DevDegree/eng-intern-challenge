from maps import braille_to_english_map

def braille_to_english(text):
    char_count = len(text)//6
    result = []
    braille_char_list = [text[6*i: 6*i+6] for i in range(char_count)]
    capital_follows = '.....O'  # Capital follows indicator
    number_follows = '.O.OOO'
    space = '......'
    capital = False
    number = False 
    for braille_string in braille_char_list:
        if braille_string == capital_follows:
            capital = True 
            continue
        if braille_string == number_follows:
            number = True 
            continue
        if braille_string == space:
            number = False
            capital = False
            result.append(" ")
            continue

        if(capital):
            result.append(braille_to_english_map[braille_string][0].upper())
            capital = False
        elif(number):
            result.append(braille_to_english_map[braille_string][1])
        else:
            result.append(braille_to_english_map[braille_string][0])
    return "".join(result)
