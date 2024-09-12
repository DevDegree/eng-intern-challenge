import sys
import braille_data


class BrailleTranslator:
    def __init__(self):
        self.braille_alphabet = braille_data.braille_alphabet
        self.braille_numbers = braille_data.braille_numbers
        self.braille_special = braille_data.braille_special

        # Braille to English (reverse lookup)
        self.reverse_braille_alphabet = {v: k for k, v in self.braille_alphabet.items()}
        self.reverse_braille_numbers = {v: k for k, v in self.braille_numbers.items()}

    def english_to_braille(self, text):
        result = []
        number_mode = False

        for char in text:
            if char.isdigit():
                if not number_mode:
                    result.append(self.braille_special["number"])
                    number_mode = True
                result.append(self.braille_numbers[char])
            elif char.isalpha():
                if number_mode:
                    number_mode = (
                        False  # Reset number mode after encountering a non-digit
                    )
                if char.isupper():
                    result.append(self.braille_special["capital"])
                    result.append(self.braille_alphabet[char.lower()])
                else:
                    result.append(self.braille_alphabet[char])
            elif char == " ":
                result.append(self.braille_alphabet[" "])
                number_mode = False  # Reset number mode after encountering a space

        return "".join(result)

    def braille_to_english(self, braille):
        result = []
        number_mode = False
        capital_mode = False
        i = 0

        while i < len(braille):
            # Take 6 character block
            char = braille[i : i + 6]

            if char == self.braille_special["number"]:
                # Interpret as a number
                number_mode = True

            elif char == self.braille_special["capital"]:
                # Capitalize next letter
                capital_mode = True

            elif char == "......":
                result.append(" ")
                number_mode = False

            else:
                if number_mode:
                    if char in self.reverse_braille_numbers:
                        result.append(self.reverse_braille_numbers[char])
                    else:
                        # Non-number character
                        number_mode = False
                        if char in self.reverse_braille_alphabet:
                            result.append(self.reverse_braille_alphabet[char])
                else:
                    if char in self.reverse_braille_alphabet:
                        letter = self.reverse_braille_alphabet[char]

                        if capital_mode:
                            result.append(letter.upper())
                            capital_mode = False
                        else:
                            result.append(letter)

            i += 6

        return "".join(result)

    def translate(self, input_text):
        # Detect if the input is Braille or English
        if set(input_text).issubset({"O", "."}):
            return self.braille_to_english(input_text)
        else:
            return self.english_to_braille(input_text)


# Main function to handle command-line inputs
def main():
    # Initialize the BrailleTranslator object
    translator = BrailleTranslator()

    # Join the input arguments into a single string
    input_text = " ".join(sys.argv[1:])

    # Translate and print the result
    print(translator.translate(input_text))


if __name__ == "__main__":
    main()
