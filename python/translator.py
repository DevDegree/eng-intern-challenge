import sys


# Returns a string built using the command line arguments
def get_argument_input():
    arg_input = ""

    # Iterate over the arguments and add them to the input string
    for arg in sys.argv[1:]:
        # If not the first argument, insert a space between the words
        if arg_input != "":
            arg_input += " "
        arg_input += arg

    return arg_input


def main():
    # Retrieve the input from the arguments
    original_text = get_argument_input()

    print(original_text)


main()