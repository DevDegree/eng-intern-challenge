
import sys

'''
first solution that comes to mind:
initialize result string

check if input braille or english (if characters in argument not in ['0', '.']
input = braille:
    create dict for braille to english
    create list with each braille letter seperated
    
    loop through list
        treat special cases (capital follows, decimal follows, number follows)
        append english letter to result

input = english:
    create dict for english to braille
    create list with each character seperated

    loop through list
        treat special cases (capital follows, decimal follows, number follows)
        append braille letter to result

return result
'''

def translate_input(args):
    print(args)

    result = ""
    return result

if __name__ == "__main__":
    args = sys.argv[1:]
    output = translate_input(args)
    print(output)