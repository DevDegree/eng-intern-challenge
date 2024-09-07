
import sys
import re

# language_dict: This dictionary contains the Braille equivalent of each English character.
language_dict = {
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
  "caps": ".....O",
  "decimal": ".O...O",
  "number": ".O.OOO",
  ".": "O...O.",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..OO.",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
}

""" 
  This function converts an English text to Braille.
  parameters: text (string): The English text to be converted to Braille.
  returns: final_text (string): The Braille equivalent of the input English text.
"""
def english_to_braille(text):
  # Initial array and flags variables
  new_arr = []
  is_number = False

  # Iterate through each character in the input text.
  for char in text:
    # if the character is uppercase, append the Braille equivalent of the "caps" character and convert the character to lowercase.
    if char.isupper():
      new_arr.append(language_dict["caps"])
      char = char.lower()
    # Check if the character is a number and append the Braille equivalent of the "number" character if it is the first number in the sequence.
    elif char.isdigit():
      # if the character is a number and the previous character was not a number, append the Braille equivalent of the "number" character.
      if is_number == False:
        new_arr.append(language_dict["number"])
        is_number = True
    # Append the Braille equivalent of the character to the new array.
    elif char == ".":
      new_arr.append(language_dict["decimal"])
    else:
      # if the character is not a number, set the is_number variable to False.
      if is_number and not char.isdigit():
        is_number = False
    
    # Append the Braille equivalent of the character to the new array.
    new_arr.append(language_dict[char])
  
  # Join the Braille characters in the new array to form the final Braille text.
  final_text = "".join(new_arr)
  
  # Return the final Braille text.
  return final_text

""" 
  This function converts a Braille text to English.
  parameters: text (string): The Braille text to be converted to English.
  returns: final_text (string): The English equivalent of the input Braille text.
""" 
def braille_to_english(text):
  # Initial array and flags variables
  new_arr = []
  caps = False
  is_number = False
  is_decimal = False

  # Iterate through the Braille text in groups of 6 characters.
  for i in range(0, len(text), 6):
    # Get the Braille character from the text.
    char = text[i:i+6]
    # Iterate through the language_dict to find the corresponding English character.
    for key, value in language_dict.items():
      # check if the Braille character matches the value in the language_dict.
      if value == char:
        if key == "number":
          is_number = True
        elif key == "decimal":
          is_decimal = True
        elif key == "caps":
          caps = True
        else:
          # if the caps flag is True, append the uppercase version of the character to the new array.
          if caps:
            new_arr.append(key.upper())
            caps = False
          # If the character is a number or decimal, append the character to the new array.
          elif is_number or is_decimal:
            if key.isnumeric():
              new_arr.append(key)
            elif key == ".":
              is_decimal = False
              new_arr.append(key)
            elif key == " ":
              is_number = False
              is_decimal = False
            # continue to the next character until a space is found.
            else:
              continue
          else:
            # if the character is not a number or decimal, append the character to the new array.
            if key.isalpha():
              new_arr.append(key)
            elif key == " ":
              new_arr.append(key)
            else:
              # continue to the next character until a space is found.
              continue
  # Join the English characters in the new array to form the final English text.
  final_text = "".join(new_arr)

  # Return the final English text.
  return final_text

""" 
  This function checks if the inputted text is a braille or english text.
  parameters: text (string): The input string to be checked.
  returns: 1 if the string starts with a period, 0 otherwise.
"""
def get_type(text):
  # regex to match the Braille text.
  braille_regex = re.compile(r"^[O.]{6,}$")

  # Check if the text matches the Braille regex and return 1 if it does, 0 otherwise.
  if braille_regex.match(text):
    return 1
  else:
    return 0

""" 
  This function translates the input text to the corresponding language and raises an exception if the input is invalid.
  parameters: input (string): The input string to be translated.
  returns: The translated text.
"""
def translator(input):
  if get_type(input) == 1:
    return braille_to_english(input)
  elif get_type(input) == 0:
    return english_to_braille(input)
  else:
    raise Exception("Invalid input")

""" 
  This is the main function, it gets the user input from the command line arguments 
  and prints the translated text.
"""
def main():
  # Get the user input from the command line arguments.
  user_input = " ".join(sys.argv[1:])

  # Check if the user input is not empty, else raise an exception.
  if user_input:
    # Try to translate the user input and print the result
    try:
      print(translator(user_input))
    except Exception as e:
      print(e)
  else:
    raise Exception("No input provided")
  
if __name__ == "__main__":
  main()