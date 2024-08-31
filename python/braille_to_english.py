import sys
from matrix_dict import matrix_dict


def b2e(input_string):

    md = matrix_dict()

    translated_string = ''

    substrings = [input_string[i:i+6] for i in range(0, len(input_string), 6)]

    translated_substrings = [[key for key, value in md.items() if value == substring] for substring in substrings]

    skip_counter = 0

    for i in range(0,len(translated_substrings)):

        if skip_counter != 0:
            skip_counter -= 1
            continue

        if 'capf' in translated_substrings[i]:
            translated_string += translated_substrings[i+1][0].upper()
            skip_counter += 1
        elif 'decimalf' in translated_substrings[i]:
            continue
        elif 'numberf' in translated_substrings[i]:

            sublist = []
            translated_num_string = ''

            for j in range(i,len(translated_substrings)):
                sublist.append(translated_substrings[j])
                if translated_substrings[j][0] == ' ':
                    break
                skip_counter+=1
        
            for k in sublist:
                for m in k:
                    if m == ' ' or m.isdigit():
                        translated_num_string += m

            translated_string += translated_num_string

        else:
            translated_string += translated_substrings[i][0]

    return translated_string