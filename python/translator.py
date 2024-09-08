    # Starter Python script for reading and writing to/from terminal
import sys

def main():
    #English to Braille Lookup Dictionary
    english_to_braille = {
        "a": "O.....",
        "b": "O.O...",
        "c": "OO....",
        "d": "OO.O..",
        "e":"O..O..",
        "f":"OOO...",
        "g":"OOOO..",
        "h":"O.OO..",
        "i":".OO...",
        "j":".OOO..",
        "k":"O...O.",
        "l":"O.O.O.",
        "m":"OO..O.",
        "n":"OO.OO.",
        "o":"O..OO.",
        "p":"OOO.O.",
        "q":"OOOOO.",
        "r":"O.OOO.",
        "s":".OO.O.",
        "t":".OOOO.",
        "u":"O...OO",
        "v":"O.O.OO",
        "w":".OOO.O",
        "x":"OO..OO",
        "y":"OO.OOO",
        "z":"O..OOO",
        " ":"......"
    }

    #Braille to English lookup dictionary
    braille_to_english = {value: key for key, value in english_to_braille.items()}

    #Number dictionary
    numbers_convert={
        '1': 'a',
        '2':'b',
        '3':'c',
        '4':'d',
        '5': 'e',
        '6':'f',
        '7':'g',
        '8': 'h',
        '9':'i',
        '0':'j'
    }

    numbers_convert_braille = {value: key for key, value in numbers_convert.items()}

# Reading input from the terminal
    user_string = " ".join(sys.argv[1:])
    is_english = False
    braille_string = ""
    english_string = ""
    for char in user_string:
        if char != 'O' and char != '.':
            is_english = True
            break
    if is_english is True:
        is_number = False
        for char in user_string:
            if char.isupper():
                braille_string += ".....O" + english_to_braille[char.lower()]
            elif char == " ":
                is_number = False
                braille_string += english_to_braille[char]
            elif char not in english_to_braille:
                search_string = numbers_convert[char]
                if is_number is True:
                    braille_string += english_to_braille[search_string]
                else:
                    braille_string += ".O.OOO" + english_to_braille[search_string]
                    is_number = True
            else:
                braille_string += english_to_braille[char]
    else:
        is_number = False
        is_capital = False
        for i in range(len(user_string)//6):
            letter = user_string[i*6:i*6+6]
            if is_capital is True:
                english_string += braille_to_english[letter].upper()
                is_capital = False
            elif letter == ".....O":
                is_capital = True
            elif letter == "......":
                is_number = False
                english_string += braille_to_english[letter]
            elif is_number is True:
                search_string = braille_to_english[letter]
                english_string += numbers_convert_braille[search_string]
            elif letter == ".O.OOO":
                is_number = True
            else:
                english_string +=braille_to_english[letter]
    if is_english:
        print(braille_string)
    else:
        print(english_string)


if __name__ == "__main__":
    main()

