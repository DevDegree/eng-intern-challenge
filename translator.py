import sys
from script_conversion import *

def main():
    """
    Read input text from command-line arguments, determine language,
    and print the translated result.
    """

    # Check that input is provided through command-line arguments.
    if len(sys.argv) < 2:
        print("No input text provided")
        sys.exit(1)

    # Join command-line arguments (excluding script name) into a single string.
    given_string = ' '.join(sys.argv[1:])

    # Translate the input string and print result to stdout.
    print(translate(given_string))
    exit(0)

if __name__ == "__main__":
    main()







