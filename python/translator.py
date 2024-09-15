import sys
from utils import identify_English_or_braille, convert_input_string_to_brailled_string, convert_braille_to_English
def main():
    input_string = input()
    if not input_string:
        sys.stdout.write("")
        return
        # print nothing to terminal, exit

    if identify_English_or_braille(input_string): #braille input
        ans = convert_braille_to_English(input_string)
        print(ans)
    else: #English input
        ans = convert_input_string_to_brailled_string(input_string)
        print(ans)

if __name__ == '__main__':
    main()