####


####
import sys

class Translator:
    def __init__(self) -> None:
        # Table to convert from alphabet to braille including special characters
        self.table = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
        'cap':'.....O',
        'dec':'.O...O',
        'num':'.O.OOO',
        ' ': '......'
        }
        # Table to convert from braille to alphabet 
        self.table_flipped={'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z', '.....O': 'cap', '.O...O': 'dec', '.O.OOO': 'num','......': ' '}
        # Table to convert from number to braille 
        self.num={'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', ' ': '......'}
        # Table to convert from braille to number
        self.num_flipped={'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0', '......': ' '}


    def parse(self,inp):
        """
        parse parse the strings into either English or Braille
        :param inp: the input string from the console
        :return: the conversion output
        """ 
        inp_set=set(inp)
        if len(inp_set) == 2 and 'O' in inp_set and '.' in inp_set: 
            return self.parse_braille(inp)
        return self.parse_english(inp)
    def parse_braille(self,inp):
        """
        parse convert Braille characters into English
        :param inp: the input string to be converted
        :return: the conversion output
        """ 
        # Convert input into group of 6 characters
        inp = [inp[i:i+6] for i in range(0,len(inp),6)]
        outp = ''
        i=0
        while i < len(inp):
            # Special case for capitalized character
            if self.table_flipped[inp[i]] =='cap':
                outp+=self.table_flipped[inp[i+1]].upper()
                i+=2
            # Special case for numeric character
            elif self.table_flipped[inp[i]] == 'num':
                i+=1
                while i < len(inp) and self.table_flipped[inp[i]]!=' ':
                    # dec added to detect decimal within the number
                    outp += '.' if self.table_flipped[inp[i]]=='dec' else self.num_flipped[inp[i]]
                    i+=1
            else:
                outp += self.table_flipped[inp[i]]
                i+=1
        return outp



    def parse_english(self,inp):
        """
        parse convert English characters into Braille 
        :param inp: the input string to be converted
        :return: the conversion output
        """ 
        i=0
        outp=''
        while i<len(inp):
            if inp[i] not in self.table:
                # case of capitalized letter
                if inp[i].lower() in self.table:
                    outp+=(self.table['cap'] + self.table[inp[i].lower()])
                    i+=1
                # case of number
                elif inp[i] in self.num:
                    outp+= self.table['num']
                    
                    while i < len(inp) and inp[i] != ' ':
                        outp += self.num[inp[i]]
                        i+=1
                    
                else:
                    raise("Error parsing braille:{}".format(inp[i]))
                
            else:
                outp += self.table[inp[i]]
                i+=1
        return outp







if __name__=='__main__':
    t = Translator()
    print(t.parse(' '.join(sys.argv[1:])))














