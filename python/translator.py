import sys

# define dictionaries to store the mappings

english_to_braille = {}

braille_to_english = {}

# function to determine input


def is_english(input):
    return True


def is_braille(input):
    return True


def translate(text):
    return


def main():
    if len(sys.args) != 2:
        print("Usage: python translator.py <input>")
        return

    if is_english(sys.args[1]):
        print(translate(sys.args[1]))

    if is_braille(sys.args[1]):
        print(translate(sys.args[1]))


if __name__ == "__main__":
    main()
