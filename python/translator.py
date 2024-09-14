import sys


class Solution:
    """
    This class contains the following menthods:
    1. is_braille method to determine if the given string is english or braille.
    2. translate method that takes a string as input and returns the translated string.
    """
    def is_braille(self, s: str) -> bool:
        # Check if the string contains only 'O' or '.' and its length is a multiple of 6
        if all(char in ['O', '.'] for char in s) and len(s) % 6 == 0:
            return True
        else:
            return False

    def translate(self, s: str) -> str:
        # Dictionary for translating english to braille
        etb = {
            'a': 'O.....',
            'b': 'O.O...',
            'c': 'OO....',
            'd': 'OO.O..',
            'e': 'O..O..',
            'f': 'OOO...',
            'g': 'OOOO..',
            'h': 'O.OO..',
            'i': '.OO...',
            'j': '.OOO..',
            'k': 'O...O.',
            'l': 'O.O.O.',
            'm': 'OO..O.',
            'n': 'OO.OO.',
            'o': 'O..OO.',
            'p': 'OOO.O.',
            'q': 'OOOOO.',
            'r': 'O.OOO.',
            's': '.OO.O.',
            't': '.OOOO.',
            'u': 'O...OO',
            'v': 'O.O.OO',
            'w': '.OOO.O',
            'x': 'OO..OO',
            'y': 'OO.OOO',
            'z': 'O..OOO',
            'captial': '.....O',
            'number': '.O.OOO',
            'space': '......',
            '1': 'O.....',
            '2': 'O.O...',
            '3': 'OO....',
            '4': 'OO.O..',
            '5': 'O..O..',
            '6': 'OOO...',
            '7': 'OOOO..',
            '8': 'O.OO..',
            '9': '.OO...',
            '0': '.OOO..',
        }

        # Dictionary for translating braille to english
        bte = {
            'O.....': 'a',
            'O.O...': 'b',
            'OO....': 'c',
            'OO.O..': 'd',
            'O..O..': 'e',
            'OOO...': 'f',
            'OOOO..': 'g',
            'O.OO..': 'h',
            '.OO...': 'i',
            '.OOO..': 'j',
            'O...O.': 'k',
            'O.O.O.': 'l',
            'OO..O.': 'm',
            'OO.OO.': 'n',
            'O..OO.': 'o',
            'OOO.O.': 'p',
            'OOOOO.': 'q',
            'O.OOO.': 'r',
            '.OO.O.': 's',
            '.OOOO.': 't',
            'O...OO': 'u',
            'O.O.OO': 'v',
            '.OOO.O': 'w',
            'OO..OO': 'x',
            'OO.OOO': 'y',
            'O..OOO': 'z',
            '.....O': 'captial',
            '.O.OOO': 'number',
            '......': 'space',
        }

        # Dictionary for translating braille to numbers
        btn = {
            'O.....': '1',
            'O.O...': '2',
            'OO....': '3',
            'OO.O..': '4',
            'O..O..': '5',
            'OOO...': '6',
            'OOOO..': '7',
            'O.OO..': '8',
            '.OO...': '9',
            '.OOO..': '0',
        }

        # Logic for translating english to braille
        if not self.is_braille(s):
            result = ""
            for i in range(0, len(s)):
                if s[i].isupper():
                    result += etb['captial']
                if s[i] == " ":
                    result += etb['space']
                    continue
                if ((i == 0 and s[i].isdigit()) or (i > 0 and s[i].isdigit() and not s[i-1].isdigit())):
                    result += etb['number']
                result += etb[s[i].lower()]
                if (i < len(s) - 1 and s[i].isdigit() and not s[i+1].isdigit() and not s[i+1].isspace()):
                    result += etb['space']
        # Logic for translating braille to english
        else:
            result = ""
            capitial_flag = False
            number_flag = False

            for i in range(0, len(s), 6):
                braille_char = s[i:i+6]
                if braille_char == etb['space']:
                    result += " "
                    number_flag = False
                    continue
                if braille_char == etb['captial']:
                    capitial_flag = True
                    continue
                if braille_char == etb['number']:
                    number_flag = True
                    continue
                if number_flag:
                    result += btn[braille_char]
                else:
                    char = bte[braille_char]
                    if capitial_flag:
                        result += char.upper()
                        capitial_flag = False
                    else:
                        result += char
        return result


def main():
    # Check if the number of arguments is correct
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string to be translated>")
        sys.exit(1)

    # Retrieve arguments from command line, excluding the script name
    args = sys.argv[1:]

    # Translate all the given strings
    solution = Solution()
    # result = ""
    # for arg in args:
    #     result += solution.translate(arg)
    input_string = ' '.join(args)
    result = solution.translate(input_string)
    print(result)


if __name__ == "__main__":
    main()
