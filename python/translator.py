from translation import to_english, to_braille
import sys

# Note, [0] is inclusive of translator.py. We do not want this in our input
console_input = " ".join(sys.argv[1:])

# Can be Braille or English
# Detected by the below loop to detect non-braille characters. Default Braille unless proven otherwise
input_type = "Braille"

if len(console_input) % 6 != 0:
    input_type = "English"
else:
    for char in console_input:
        if char != '.' and char != 'O':
            input_type = "English"
            break

output = ""
if input_type == "English":
    # Temporary variable to track numbers
    num_follows = False

    for char in console_input:
        # Stop condition for activating num characters
        if num_follows and char == " ":
            num_follows = False
        # Start condition for activating num characters
        elif char.isnumeric() and not num_follows:
            num_follows = True
            output += to_braille("num_follows")
        elif char.isupper():
            output += to_braille("cap_follows")

        output += to_braille(char)
else:
    # Splits the input into 6 len strings, aka their cells
    cells = [console_input[i:i + 6] for i in range(0, len(console_input), 6)]

    # Temporary variables to track follows
    cap_follows = False
    num_follows = False

    for cell in cells:
        if num_follows and cell == to_braille(" "):
            num_follows = False
        elif num_follows:
            cell = "_" + cell  # Indicates that it is a numeric char by adding _ before braille in dict

        converted = to_english(cell)

        if cap_follows:
            output += converted.upper()
            cap_follows = False
        elif converted == "cap_follows":
            cap_follows = True
        elif converted == "num_follows":
            num_follows = True
        else:
            output += converted

print(output)
