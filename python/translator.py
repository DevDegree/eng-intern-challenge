import sys

class BrailleTranslator:
    def translate(self, s):
        if not s:
            return s
        
        result = ""

        if len(s) % 6 != 0 or any(c not in '.O' for c in s):
            result = self.english(s)
        else:
            result = self.braille(s)
        
        return result

    def english(self, s):
        result = ""
        translation = {
            'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..",
            'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..",
            'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
            'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.",
            'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
            'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
            'y': "OO.OOO", 'z': "O..OOO",
            '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
            '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
            '9': ".OO...", '0': ".OOO..",
            '.': "..OO.O", ',': "..O...", '?': "..O.OO", '!': "..OOO.",
            ':': "..OO..", ';': "..O.O.", '-': ".....OO", '/': ".O..O.",
            '<': ".OO..O", '>': "O..OO.", '(': "O.O..O", ')': ".O.OO.", 
            ' ': "......"  
        }
        upper = ".....O"
        num = ".O.OOO"
        dec = ".O...O"

        i = 0
        while i < len(s):
            if s[i].lower() not in translation:
                return "invalid character"
            
            if s[i].isupper():
                result += upper
            elif s[i].isdigit():
                result += num
                while i < len(s) and (s[i].isdigit() or s[i] == '.'):
                    if s[i] == '.':
                        result += dec
                    result += translation[s[i]]
                    i += 1
                if i < len(s) and s[i]!=' ':
                    result+="......"
                continue
            
            if s[i].isalpha():
                result += translation[s[i].lower()]
            else:
                result += translation[s[i]]
            i += 1

        return result

    def braille(self, s):
        result = ""
        translation = {v: k for k, v in {
            'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..",
            'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..",
            'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
            'm': "OO..O.", 'n': "OO.OO.",  'p': "OOO.O.",
            'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
            'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
            'y': "OO.OOO", 'z': "O..OOO",
            # '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
            # '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
            # '9': ".OO...", '0': ".OOO..",
            '.': "..OO.O", ',': "..O...", '?': "..O.OO", '!': "..OOO.",
            ':': "..OO..", ';': "..O.O.", '-': ".....OO", '/': ".O..O.",
            '<': ".OO..O", '>': "O..OO.", '(': "O.O..O", ')': ".O.OO.", 'o': "O..OO.", 
            ' ': "......" 
        }.items()}
# 'o' and '>' are the same which is problematic in translating from braille to english. prioritize 'o'
        upper = ".....O"
        num = ".O.OOO"
        dec = ".O...O"

        i = 0
        while i < len(s):
            ch = s[i:i+6]
            if ch not in translation and ch not in (upper, num, dec):
                return "invalid braille"
            
            if ch == num:
                i += 6
                while i < len(s) and s[i:i+6] != "......":
                    ch = s[i:i+6]
                    if ch == ".OOO..":
                        result += '0'
                        i += 6
                        continue
                    elif ch == dec:
                        result += '.'
                        i += 12
                        continue
                    result += chr(ord(translation[ch]) - 48)
                    i += 6
                if s[i:i+6] == "......":
                    result += ' '
                i += 6
                continue
            
            if ch == upper:
                ch = s[i+6:i+12]
                result += translation[ch].upper()
                i += 6
            else:
                result += translation[ch]
            i += 6

        return result

def main():

    input_str =' '.join(sys.argv[1:])
    solution = BrailleTranslator()
    print(solution.translate(input_str).strip()) 



if __name__ == "__main__":
    main()

