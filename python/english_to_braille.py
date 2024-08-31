import sys
from matrix_dict import matrix_dict

def capitalize(letter):
       
    md = matrix_dict()

    return md['capf'] + md[letter.lower()]

def numberize(char):
       
    md = matrix_dict()

    translated_string = md['numberf']

    for n in char:
        translated_string += md[n]

    return translated_string + md[' ']

def e2b(input_string):

    md = matrix_dict()

    translated_string = ''

    skip_counter = 0

    for i in range(0,len(input_string)):

        if skip_counter != 0:
            skip_counter -= 1
            continue

        if input_string[i].isupper():
            translated_string += capitalize(input_string[i])
        elif input_string[i].isdigit():
            n = ''
            
            for j in range(i,len(input_string)):
                if input_string[j].isdigit():
                    n += input_string[j]
                    skip_counter += 1
                else:
                    break

            translated_string += numberize(n)
        # handle decimal case
        else:
           
           if input_string[i] == '.':
            if input_string[i-1].isdigit() == True and input_string[i+1].isdigit() == True:
                translated_string = translated_string[:-6] + md['decimalf']
                continue

           translated_string += md[input_string[i]]

    # handle case for number in the end
    if input_string[-1].isdigit():
        translated_string = translated_string[:-6]

    return translated_string