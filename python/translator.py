import sys

# Braille map
braille_map = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': "OO.OO.", 't': "OOOO.O",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", ' ': "......", '1': "O.....", '2': "O.O...", '3': "OO....",
    '4': "OO.O..", '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
    '9': ".OO...", '0': ".OOO..", '#': ".O.OOO", '^': ".....O"
}

reverse_braille_map = {
    "O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd', "O..O..": 'e',
    "OOO...": 'f', "OOOO..": 'g', "O.OO..": 'h', ".OO...": 'i', ".OOO..": 'j',
    "O...O.": 'k', "O.O.O.": 'l', "OO..O.": 'm', "OO.OO.": 'n', "O..OO.": 'o',
    "OOO.O.": 'p', "OOOOO.": 'q', "O.OOO.": 'r', "OO.OO.": 's', "OOOO.O": 't',
    "O...OO": 'u', "O.O.OO": 'v', ".OOO.O": 'w', "OO..OO": 'x', "OO.OOO": 'y',
    "O..OOO": 'z', "......": ' ', ".O.OOO": '#', ".....O": '^'
}

def solve(s: str) -> str:
    count_o = s.count('O')
    count_d = s.count('.')

    ans = ""

    if count_o + count_d == len(s):
        f = 0
        f2 = 0
        i = 0

        while i < len(s):
            cur = s[i:i + 6]
            i += 6

            if cur in reverse_braille_map:
                char = reverse_braille_map[cur]

                if char == ' ':
                    f = 0
                    f2 = 0
                    ans += " "
                elif char == '#':
                    f2 = 1
                    continue
                elif char == '^':
                    f = 1
                else:
                    if f2 == 1:
                        pk = str(ord(char) - 96)
                        ans += pk
                    else:
                        if f == 0:
                            ans += char
                        else:
                            ans += chr(ord(char) - 32)
                            f = 0
        return ans

    f1 = 0
    for char in s:
        if 'A' <= char <= 'Z':
            ans += braille_map['^']
            ans += braille_map[char.lower()]
        elif '0' <= char <= '9':
            if f1 == 1:
                ans += braille_map[char]
            else:
                f1 = 1
                ans += braille_map['#']
                ans += braille_map[char]
        elif char == ' ':
            f1 = 0
            ans += braille_map[char]
        else:
            ans += braille_map.get(char, '')

    return ans

def main():
    if len(sys.argv) > 1:
        input_str = " ".join(sys.argv[1:])
        print(solve(input_str))

if __name__ == "__main__":
    main()
