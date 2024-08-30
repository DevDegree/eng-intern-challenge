import translator

def test_period():
    # Test the translation of underscore
    input_string = "."
    print(f"Testing period: {input_string}")
    output = translator.translate_to_braille(input_string)
    print(f"Output: {output}")

def test_uppercase_o():
    # Test the translation of uppercase 'O'
    input_string = "O"
    print(f"Testing uppercase 'O': {input_string}")
    output = translator.translate_to_braille(input_string)
    print(f"Output: {output}")

if __name__ == "__main__":
    test_period()  # Run the underscore test
    test_uppercase_o()  # Run the uppercase 'O' test
