class BrailleTranslator:
    # Number positions are:
    #  1 4 
    #  2 5
    #  3 6

    # Using information from https://www.pharmabraille.com/pharmaceutical-braille/the-braille-alphabet/
    # More scalable using numbers than strings for positioning
    braille_to_letters = {
        1: 'a',
        12: 'b',
        14: 'c',
        145: 'd',
        15: 'e',
        124: 'f',
        1245: 'g',
        125: 'h',
        24: 'i',
        245: 'j',
        13: 'k',
        123: 'l',
        134: 'm',
        1345: 'n',
        135: 'o',
        1234: 'p',
        12345: 'q',
        1235: 'r',
        234: 's',
        2345: 't',
        136: 'u',
        1236: 'v',
        2456: 'w',
        1346: 'x',
        13456: 'y',
        1356: 'z',
        256: '.',
        2: ',',
        236: '?',
        235: '!',
        25: ':',
        23: ';',
        36: '-',
        34: '/',
        246: '<',
        135: '>',
        126: '(',
        345: ')',
        6: 'capital',
        46: 'decimal',
        3456: 'number'
    }

    def __init__(self):
        self.letters_to_braille = {v: k for k, v in self.braille_to_letters.items()}

    def char_to_braille(self, c):
        braille = ''
        if c.isupper():
            braille += self.position_to_braille(self.letters_to_braille['capital'])
        braille += self.position_to_braille(self.letters_to_braille[c.lower()])
        return braille
    
    def braille_to_char(self, s):
        if s == '......':
            return ' '
        num = ''
        pos = [1, 4, 2, 5, 3, 6]
        for i in range(len(pos)):
            if s[pos[i] - 1] == 'O':
                num += str(i + 1)
        return self.braille_to_letters[int(num)]

    def position_to_braille(self, pos):
        res = str(pos)
        braille = ['.','.','.','.','.','.']
        pos_map = [1, 4, 2, 5, 3, 6]
        for i in range(len(pos_map)):
            if str(pos_map[i]) in res:
                braille[i] = "O"
        return ''.join(braille)
