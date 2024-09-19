import sys


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing Argument. Need Braille text or English text")

    # Parse the command line arguments and store full text
    system_arguments = sys.argv[1:]
    string_to_translate = " ".join(system_arguments)

    # Check if string is braille or english
    raised_count = string_to_translate.count("O")
    lowered_count = string_to_translate.count(".")

    is_braille_text = raised_count + lowered_count == len(string_to_translate)
    length_divides_six = len(string_to_translate) % 6 == 0

    if is_braille_text and length_divides_six:
        braille_to_english = True
    else:
        braille_to_english = False

