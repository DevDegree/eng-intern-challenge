from variable import eng_to_braille_dict, braille_to_eng_dict, braille_to_eng_number_dict, eng_to_braille_number_dict


class converter:
    def __init__(self):
        self.RAISE_DOT = 'O'
        self.BLANK_DOT = '.'
        self.output = ""

 # Function to check whether the input string is braille or english
    def checker(self, inp_string):
        if self.RAISE_DOT not in inp_string or self.BLANK_DOT not in inp_string:
            return True
        return False

 # Function to convert a Braille string into English text
    def braille_to_english(self, inp_string):
        # Splitting the input Braille string into a list of 6-character Braille cells
        braille_list = self.split(inp_string)

        # Flags to handle special cases
        capital_flag = False
        decimal_flag = False
        number_flag = False

        # Loop through each Braille cell in the list
        for braille_cell in braille_list:
            # Check for control flags in the dictionary (capital, decimal, number)
            braille_char = braille_to_eng_dict.get(braille_cell, "")

            if braille_char == "capital_next":
                print(braille_cell + " " + braille_char)
                capital_flag = True
                continue

            elif braille_char == "decimal_next":
                decimal_flag = True
                continue

            elif braille_char == "number_next":
                print(braille_cell + " " + braille_char)
                number_flag = True
                continue

            elif braille_char == "space":
                print(braille_cell + " " + braille_char)
                self.output += ' '  # Add space and reset number flag
                number_flag = False
                continue

            # Handle capitalized letters
            if capital_flag:
                self.output += braille_char.upper()
                print(braille_cell + " " + braille_char.upper())
                capital_flag = False
                continue

            # Handle numbers if number flag is set
            if number_flag:
                print(braille_cell + " " +
                      braille_to_eng_number_dict.get(braille_cell, ""))
                self.output += braille_to_eng_number_dict.get(braille_cell, "")
                continue

            # Default case for regular Braille cells
            self.output += braille_char
            print(braille_cell + " " + braille_char)

        return self.output

    # Function to split the Braille string into 6-character cells
    def split(self, inp_string):
        # Use list comprehension for more efficiency
        return [inp_string[i:i+6] for i in range(0, len(inp_string), 6)]

# Function to convert a English string into Braille text
    def english_to_braille(self, inp_string):
        # Flag to track whether the previous character was not a number
        number_flag = True

        # Iterate through each character in the input string
        for char in inp_string:

            # If the character is a space, add a space representation in Braille
            if char == " ":
                self.output += eng_to_braille_dict["space"]
                # Reset number_flag to True after space
                number_flag = True

            # If the character is alphabetic
            elif char.isalpha():
                # Add the capital flag for uppercase letters
                if char.isupper():
                    self.output += eng_to_braille_dict["capital_next"]
                # Convert the letter to lowercase and add the corresponding Braille symbol
                self.output += eng_to_braille_dict[char.lower()]
                # Reset number_flag since the letter isn't a number
                number_flag = True

            # If the character is numeric
            elif char.isdigit():
                # If the previous character was not a number, add the number flag in Braille
                if number_flag:
                    self.output += eng_to_braille_dict["number_next"]
                    number_flag = False
                # Add the corresponding Braille number symbol
                self.output += eng_to_braille_number_dict[char]

        # Return the Braille translation
        return self.output
