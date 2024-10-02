import sys

braille_to_english_letters = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " "
}

braille_to_english_nums = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

english_to_braille = {
    # Letters
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    # Numbers 
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    " ": "......"
}

def is_braille(s):
    return all(c in "O." for c in s)

def translate_braille_to_english(braille_string):
    """Translate Braille input to English string."""
    braille_list = [braille_string[i:i + 6] for i in range(0, len(braille_string), 6)]
    result = []
    i = 0
    number_mode = False

    while i < len(braille_list):
        if (braille_list[i] == ".....O"):
            i += 1
            result.append(braille_to_english_letters.get(braille_list[i]).upper())
        elif (braille_list[i] == ".O.OOO"):
            i += 1
            result.append(braille_to_english_nums.get(braille_list[i]))
            number_mode = True
        elif (braille_list[i] == ".O...O"):
            result.append(".")
            i+=1
            result.append(braille_to_english_nums.get(braille_list[i]))
            number_mode = True
        else:
            if (number_mode):
                result.append(braille_to_english_nums.get(braille_list[i]))
            else:
                result.append(braille_to_english_letters.get(braille_list[i]))
        i+=1
    return "".join(result)

def translate_english_to_braille(english_string):
    """Translate English input to Braille string."""
    result = []
    is_number_mode = False
    
    for char in english_string:
        if char.isdigit():
            if not is_number_mode:
                result.append(".O.OOO")
                is_number_mode = True
            result.append(english_to_braille[char])
        else:
            if char.isupper():
                result.append(".....O")  
                result.append(english_to_braille[char.lower()])
            elif char == " ": 
                result.append("......")
            else: 
                result.append(english_to_braille.get(char, ""))
            
            is_number_mode = False 
    
    return "".join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string_to_translate> [<string_to_translate> ...]")
        sys.exit(1)
    
    translated_texts = []

    for i, input_string in enumerate(sys.argv[1:], start=1):
        if is_braille(input_string):
            translated_text = translate_braille_to_english(input_string)
            translated_texts.append(translated_text)
            if i < len(sys.argv) - 1:
                translated_texts.append(" ")
        else:
            translated_text = translate_english_to_braille(input_string)
            translated_texts.append(translated_text)

            if i < len(sys.argv) - 1:
                translated_texts.append("......")

    result_string = "".join(translated_texts)
    print(result_string)

if __name__ == "__main__":
    main()