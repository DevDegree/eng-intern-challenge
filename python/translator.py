import sys

#define dictionary for Braille characters to ASCII characters
braille_num_dict = {
    # numbers
    'O.....' : '1',
    'O.O...' : '2',
    'OO....' : '3',	
    'OO.O..' : '4',
    'O..O..' : '5',
    'OOO...' : '6',
    'OOOO..' : '7',
    'O.OO..' : '8',
    '.OO...' : '9',
    '.OOO..' : '0',
    '.O...O' : '.',
}

braille_dict = {
    'O.....' : 'a',
    'O.O...' : 'b',
    'OO....' : 'c',	
    'OO.O..' : 'd',
    'O..O..' : 'e',
    'OOO...' : 'f',
    'OOOO..' : 'g',
    'O.OO..' : 'h',
    '.OO...' : 'i',
    '.OOO..' : 'j',
    'O...O.' : 'k',
    'O.O.O.' : 'l',
    'OO..O.' : 'm',
    'OO.OO.' : 'n',
    'O..OO.' : 'o',
    'OOO.O.' : 'p',
    'OOOOO.' : 'q',
    'O.OOO.' : 'r',
    '.OO.O.' : 's',
    '.OOOO.' : 't',
    'O...OO.' : 'u',	
    'O.O.OO' : 'v',
    '.OOO.O' : 'w',
    'OO..OO' : 'x',
    'OO.OOO' : 'y',
    'O..OOO' : 'z',
    #flags
    '.....O' :'Capital',
    '.O...O' : '.',
    '.O.OOO' : 'Number',
    #special characters
    # '..OO.O' : '.',
    # '..O...' : ',',
    # '..O.OO' : '?',
    # '..OOO.' : '!',
    # '..OO..' : ':',
    # '..O.O.' : ';',
    # '....OO' : '-',	
    # '.O..O.' : '/',
    # '.OO..O' : '<',
    # 'O..OO.' : '>',
    # 'O.O..O' : '(',
    # '.O.OO.' : ')',
    '......' : ' ',
}

# define dictionary for ASCII characters to Braille characters
eng_dict = dict((v,k) for k,v in braille_dict.items())
eng_num_dict = dict((v,k) for k,v in braille_num_dict.items())

def main():
    #take in the input from command line arguments
    full_string = sys.argv[1:]
    string = full_string[0]
    output = []
    # check if all characters in the string are either braille or English alphabets or numbers
    if set(string).issubset({'.', 'O'}):
        # cases for braille translation
        cap = False
        Num = False
        # parse braille string, split into 6-character chunks
        braille_string = [ string[i:i+6] for i in range(0, len(string), 6) ]

        for braille_char in braille_string:
            if Num:
                output.append(braille_num_dict[braille_char])
                
            elif braille_dict[braille_char] == 'Capital':
                cap = True
                
            elif braille_dict[braille_char] == 'Number':
                Num = True
                
            elif braille_dict[braille_char] == ' ':
                cap = False
                Num = False
                output.append(braille_dict[braille_char])

            elif cap:
                output.append(braille_dict[braille_char].upper())
                cap = False
                
            else:
                output.append(braille_dict[braille_char])
    else:
        # case for text translation
        s_parse = []
        # Flag for start of number
        start_num = False
        #get a list of individual characters in the string
        for s in full_string:
            s_parse.extend(list(s))
            s_parse.append(' ')
            
        # remove extra space
        s_parse = s_parse[:-1]

        for char in s_parse:
            if char.isupper():
                output.append(eng_dict['Capital'])
                output.append(eng_dict[char.lower()])
                
            elif char.isdigit():
                if not start_num:
                    output.append(eng_dict['Number'])
                output.append(eng_num_dict[char])
                start_num = True
                
            elif char == ' ':
                start_num = False
                output.append(eng_dict[char])
                
            else: 
                output.append(eng_dict[char])
                
    #combine list of outputs into one single string
    res = ''.join(output)
    print(res)


if __name__ == "__main__":
    main()