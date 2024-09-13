import argparse


# Dictionaries for Braille representations
braille_dict_letters = {
   " ": "......",  # Blank space


   # Letters a to z (lowercase)
   "a": "O.....",
   "b": "O.O...",
   "c": "OO....",
   "d": "OO.O..",
   "e": "O..O..",
   "f": "OOO...",
   "g": "OOOO..",
   "h": "O.OO..",
   "i": ".OO...",
   "j": ".OOO..",
   "k": "O...O.",
   "l": "O.O.O.",
   "m": "OO..O.",
   "n": "OO.OO.",
   "o": "O..OO.",
   "p": "OOO.O.",
   "q": "OOOOO.",
   "r": "O.OOO.",
   "s": ".OO.O.",
   "t": ".OOOO.",
   "u": "O...OO",
   "v": "O.O.OO",
   "w": ".OOO.O",
   "x": "OO..OO",
   "y": "OO.OOO",
   "z": "O..OOO",


   # Capital letter prefix
   "capital": ".....O",
}


braille_dict_numbers = {
   "1": "O.....",
   "2": "O.O...",
   "3": "OO....",
   "4": "OO.O..",
   "5": "O..O..",
   "6": "OOO...",
   "7": "OOOO..",
   "8": "O.OO..",
   "9": ".OO...",
   "0": ".OOO..",
}


def braille_to_English(text) -> str:
   strArr = [text[i:i + 6] for i in range(0, len(text), 6)]
   print (strArr)
   result = []
   capitalize_next = False
   number_mode = False


   for braille_char in strArr:
       if braille_char == braille_dict_letters["capital"]:
           capitalize_next = True
           continue


       if braille_char == ".O.OOO":
           number_mode = True
           continue


       if braille_char == braille_dict_letters[" "]:
           result.append(" ")
           number_mode = False
           continue


       if number_mode:
           found_number = False
           for number, pattern in braille_dict_numbers.items():
               if braille_char == pattern:
                   result.append(number)
                   found_number = True
                   break
           if not found_number:
               result.append("?")
       else:
           if braille_char in braille_dict_letters.values():
               letter = [k for k, v in braille_dict_letters.items() if v == braille_char][0]
               if capitalize_next:
                   letter = letter.upper()
                   capitalize_next = False
               result.append(letter)
           else:
               result.append("?")


   return ''.join(result)




def english_to_braille(*texts) -> str:
   # Combine all input strings with a single space between them
   combined_text = ' '.join(texts)
   result = []
   number_mode = False


   for char in combined_text:
       if char == " ":
           result.append(braille_dict_letters[" "])
           number_mode = False  # Reset number mode when encountering a space
       elif char.isdigit():
           if not number_mode:
               result.append(".O.OOO")  # Start number mode if not already in number mode
               number_mode = True
           result.append(braille_dict_numbers.get(char, "?"))
       elif char.isalpha():
           if number_mode:
               result.append(braille_dict_letters[" "])  # Add space Braille to switch from numbers to letters
               number_mode = False  # Turn off number mode
           if char.isupper():
               result.append(braille_dict_letters["capital"])  # Capital letter prefix
           result.append(braille_dict_letters[char.lower()])  # Append Braille for the letter
       else:
           result.append("?")  # Unknown character represented by "?"


   return ''.join(result)

def detect_input_type(input_str):
   # Check if input contains only Braille characters (O and .)
   if all(c in 'O.' for c in input_str):
       return 'braille'
   else:
       return 'english'

def process_input(input_str):
   input_type = detect_input_type(input_str)


   if input_type == 'braille':
       return braille_to_English(input_str)
   elif input_type == 'english':
       return english_to_braille(input_str)
   else:
       return "Unknown input type"


def main():
   parser = argparse.ArgumentParser(description="Convert between English and Braille.")
   parser.add_argument('texts', nargs='+', type=str, help="Text to convert. Use 'O' and '.' for Braille input.")
   args = parser.parse_args()
   # Combining the input strings into one string with spaces for the test case
   combined_text = ' '.join(args.texts).strip()
   result = english_to_braille(*args.texts)
   print(result)


if __name__ == "__main__":
   main()
