import sys

# Dictionary mapping English alphabet to Braille patterns
English_Dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'capital': '.....O', 'number': '.O.OOO', ' ': '......'
}

# Dictionary mapping digits to Braille patterns
English_Digits = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
}

# Reverse mappings from Braille to English alphabet and digits
Braille_Dict = {value: key for key, value in English_Dict.items()}
Braille_Digits = {value: key for key, value in English_Digits.items()}


# Function to translate English text to Braille
def translateEnglishToBraille(input_str):
    outp = []  # Output list to collect Braille representation
    isDigit = False  # Flag to track if current context is numeric
    for char in input_str:
        # If we encounter a non-digit character, reset the isDigit flag
        if isDigit and not char.isdigit():
            isDigit = False

        # Translate digits if isDigit flag is set
        if isDigit and char.isdigit():
            outp.append(English_Digits[char])
        elif char.isupper():
            # Add capital Braille prefix and then lowercase equivalent
            outp.append(English_Dict['capital'])
            outp.append(English_Dict[char.lower()])
        elif char.islower():
            # Translate lowercase letters directly
            outp.append(English_Dict[char])
        elif char.isdigit():
            # Set isDigit flag and translate the digit
            isDigit = True
            outp.append(English_Dict['number'])
            outp.append(English_Digits[char])
        elif char.isspace():
            # Add space character in Braille
            outp.append(English_Dict[' '])
        else:
            # Handle unexpected characters
            print("found something out of the ordinary!")

    # Join the Braille list into a single string and return
    return ''.join(outp)

# Function to translate Braille to English text
def translateBrailleToEnglish(input_str):
    outp = []  # Output list to collect English representation
    isDigit = False  # Flag to track if current context is numeric
    isCapital = False  # Flag to track if the next letter is capitalized
    for i in range(0, len(input_str), 6):
        char = input_str[i:i+6]  # Each Braille character is 6 characters long

        # Handle Braille space pattern
        if char == '......' and not isDigit:
            outp.append(' ')
            continue

        if char not in Braille_Dict and char not in Braille_Digits:
            print(f"Error: Undefined Braille pattern encountered - '{char}'")
            return "Error: Undefined Braille pattern"
        
        if isCapital:
            # Convert the Braille to uppercase English letter
            outp.append(Braille_Dict[char].upper())
            isCapital = False
        elif isDigit:
            # Check for space to reset digit context, otherwise convert digit
            if char == '......':
                isDigit = False
                outp.append(Braille_Dict[char])
            else:
                outp.append(Braille_Digits[char])
        elif char == ".....O":
            # If Braille capital indicator, set isCapital flag
            isCapital = True
        elif Braille_Dict[char] == 'number':
            # If Braille number indicator, set isDigit flag
            isDigit = True
        else:
            # Convert Braille to corresponding English character
            outp.append(Braille_Dict[char])
    return ''.join(outp)


if __name__ == "__main__":
    
    # Check if there are any command-line arguments
    if (len(sys.argv) <= 1):
        # If no input is given, print instructions and exit
        print("No command-line arguments were given. Enter an input after the program.")
        exit()
    # Determine if the input is English or Braille based on the first argument
    if all(char in 'O.' for char in sys.argv[1]):
        English = False  # If only . and O, assume it's Braille
    else:
        English = True  # Otherwise, assume it's English

    # Gather the input string to be translated
    input_str = ""

    if English:
        # Join all arguments as input string for English translation
        input_str = ' '.join(sys.argv[1:])
        outp = translateEnglishToBraille(input_str)
    else:
        # Assume single argument for Braille input
        input_str = sys.argv[1]
        outp = translateBrailleToEnglish(input_str)

    # Print the translated output
    print(outp)