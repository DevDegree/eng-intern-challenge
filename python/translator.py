import argparse

char_map_english= {
    "a": "O.....", "b":"O.O...", "c":"OO....", "d":"OO.O..", "e": "O..O..", "f":"OOO...", "g":"OOOO..",
    "h":"O.OO..", "i" : ".OO...", "j":".OOO..", "k":"O...O.","l":"O.O.O.", "m":"OO..O.", "n":"OO.OO.",
    "o":"O..OO.", "p":"OOO.O.","q":"OOOOO.", "r":"O.OOO.", "s":".OO.O.", "t":".OOOO.", "u":"O...OO",
     "v":"O.O.OO", "w":".OOO.O", "x":"OO..OO", "y":"OO.OOO", "z":"O..OOO", "capitalize": ".....O",
     "decimal":".O...O", "number":".O.OOO", ".":"..OO.O", ",":"..O...","?":"..O.OO","!":"..OOO.",":":"..OO..",
     ";":"..O.O.", "-": "....OO", "/":".O..O.", "<": ".OO..O", ">": "O..OO.", "(":"O.O..O",")":".O.OO.",
     " ":"......"
}

numbers_map_english = {
    "1":"O.....", "2":"O.O...", "3":"OO....", "4":"OO.O..", "5":"O..O..", "6":"OOO...", "7":"OOOO..",
     "8":"O.OO..", "9":".OO...", "0": ".OOO.."
}

char_map_braille = {i:j for j,i in char_map_english.items()}
numbers_map_braille = {i:j for j,i in numbers_map_english.items()}

def translate_english(text):
    # translates words from english to braille
    translated_text = ""  # Initialize translated_text as an empty string
    is_number = False
    for char in text:
        if char == " ":  # Handle spaces
            translated_text += char_map_english[" "]
        elif char.isdigit():
            if not is_number:
                translated_text += char_map_english["number"] 
                is_number = True 
            translated_text += numbers_map_english[char]
        elif char.isalpha(): #if char is a letter
            if char.isupper(): #if captilized
                translated_text += char_map_english["capitalize"]  
                char = char.lower()  #if char is lower
            translated_text += char_map_english[char]
            is_number = False  # Reset after a letter
        else:
            if char in char_map_english:
                translated_text += char_map_english[char]
            is_number = False  # Reset after a non-letter/number
    return translated_text
def translate_braille(text):
     # translates words from braille to english
    translated_text = ""
    i = 0
    is_number = False

    while i < len(text):
        symbol = text[i:i + 6]
        if symbol == char_map_english["number"]:
            is_number = True
        elif symbol == char_map_english["capitalize"]:
            i += 6 #increment i to get the following letter that needs to be capitalized
            symbol = text[i:i + 6]  
            translated_text += char_map_braille.get(symbol, " ").upper() 
        elif symbol == char_map_english[" "]: 
            translated_text += " "
            is_number = False  # Reset number mode after a space
        elif is_number:
            translated_text += numbers_map_braille.get(symbol, " ")
        else:
            translated_text += char_map_braille.get(symbol, " ")
        i += 6
    return translated_text

def detectlang(text):
    #Detects whether translating from braille or from english
    is_braille = True
    for c in text:
        if c not in {"O", ".", " "}: #braille can't have spaces, would use (......)
            is_braille = False
            break

    
    if is_braille and len(text) % 6 == 0:
        return "braille"
    else:
        return "english"

def main():
   
    #Parses argument inputs
    parser = argparse.ArgumentParser(description='Translator Between Braille and English')

    parser.add_argument('text', nargs='+', help='Text to translate')  # Accept multiple arguments
    
    textinput = ' '.join(parser.parse_args().text)  # Join all arguments into a single string
    

    if detectlang(textinput) == 'english':
        translated_text = translate_english(textinput)
    else:
        translated_text = translate_braille(textinput)

    print(translated_text)


    













if __name__ == "__main__":
    main()

