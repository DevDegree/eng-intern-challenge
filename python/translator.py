import sys
from english import English
from braille import Braille
from dictionary import Dictionary

def get_class(input, input_list):
    for i in input:
        if i not in ['O','.']:
            return English  
        
    if len(input) % 6 != 0:
        return English 
    
    braille_values = Dictionary.BRAILLE.values()

    for i in input_list:
        if i not in braille_values:
            print('This braille letter seems having an error!')
            return English  
    return Braille
   

def splitBySix(input):
    splited = list()
    for i in range(len(input)//6):
        splited.append(input[:6])
        input = input[6:]
    return splited


def main(argv):
    word =''
    if argv == '':
        word = input("input : ")
    else:
        word = argv

    input_list = splitBySix(word)
    
    klass = get_class(word, input_list)
    translated = klass(word, input_list).execute()
            
    print(translated)


if __name__ == '__main__':
    arguments = sys.argv
    del arguments[0]
    single_arg = ' '.join(arguments)
    main(single_arg)