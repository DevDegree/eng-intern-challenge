import sys
braille_translations = [
['a','O.....'],['b','O.O...'],['c','OO....'],['d','OO.O..'],['e','O..O..'],['f','OOO...'],
['g','OOOO..'],['h','O.OO..'],['i','.OO...'],['j','.OOO..'],['k','O...O.'],['l','O.O.O.'],
['m','OO..O.'],['n','OO.OO.'],['o','O..OO.'],['p','OOO.O.'],['q','OOOOO.'],['r','O.OOO.'],
['s','.OO.O.'],['t','.OOOO.'],['u','O...OO'],['v','O.O.OO'],['w','.OOO.O'],['x','OO..OO'],
['y','OO.OOO'],['z','O..OOO'],['1','O.....'],['2','O.O...'],['3','OO....'],['4','OO.O..'],
['5','O..O..'],['6','OOO...'],['7','OOOO..'],['8','O.OO..'],['9','.OO...'],['0','.OOO..'],
['.','..OO.O'],[',','..O...'],['?','..O.OO'],['!','..OOO.'],[':','..OO..'],[';','..O.O.'],
['-','....OO'],['/','.O..O.'],['<','.OO..O'],['>','O..OO.'],['(','O.O..O'],[')','.O.OO.'],
[' ','......'],['capital','.....O'],['decimal','.O...O'],['number','.O.OOO']
]



def is_braille(string):
    return all(c in {'.', 'O'} for c in string ) and len(string) % 6 == 0



def translator(argument):
    if is_braille(argument):
        return braille_english(argument)
    else:
        return english_braille(argument)

#translate braille to english
def braille_english(braille):
    res = ''
    capital = False
    number = False
    decimal = False
    for i in range(0,len(braille),6):
        input_slice = braille[i:i+6]
        current_translation = english_find(input_slice, "")
        if current_translation == "capital":
            capital = True
        elif current_translation == "decimal":
            res += '.'
        elif current_translation == "number":
            number = True
        else:
            if current_translation == " ":
                number = False
                res += " "
            elif capital:
                res += current_translation.upper()
                capital = not capital
            elif not capital and not number:
                res += current_translation.lower()
            elif number:
                res += english_find(input_slice, "number")
    return res

#finds english translation in dictionary
def english_find(braille, searchType):
    for pair in braille_translations:
        if pair[1] == braille and (pair[0].isdigit() if searchType =="number" else (pair[0].isalpha() or pair[0] == " ")):
            return pair[0]

#finds braille translation in dictionary
def braille_find(english, searchType):
    for pair in braille_translations:
        if pair[0] == english and (pair[0].isdigit() if searchType =="number" else  (pair[0].isalpha() or pair[0] == " ")):
            return pair[1]

#translate english to braille
def english_braille(english):
    digit = False
    res = ''
    for char in english:
        if char.isalpha() and char.isupper():
            res += braille_find("capital","") + braille_find(char.lower(),"").upper()
        elif char.isdigit():
            if digit == False:
                digit = True
                res += braille_find("number","")
            res += braille_find(char, 'number')
        else:
            if char  == ' ':
                digit = False
                res += braille_find(" ","")
            elif char == '.' and digit:
                res += braille_find("decimal","")
            else:
                res += braille_find(char, "")
    return res
            
if __name__ == '__main__':
    # print(translator(".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."))

    arguments = sys.argv[1:]  # Exclude the script name

    # Process each argument and translate it
    comp_arg = ''
    for arg in arguments:
        comp_arg += arg + (" " if arg != arguments[-1] else "")
    print(translator(comp_arg), end='')