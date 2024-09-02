#importing sys library for reading input from terminal
import sys   

########create dictionaries for brail to english mode##################
brail_to_eng_dic_dec = {'O.....':'a',
                    'O.O...':'b',
                   'OO....':'c',
                   'OO.O..':'d',
                   'O..O..':'e',
                   'OOO...':'f',
                   'OOOO..':'g',
                   'O.OO..':'h',
                   '.OO...':'i',
                   '.OOO..':'j',
                   'O...O.':'k',
                   'O.O.O.':'l',
                   'OO..O.':'m',
                   'OO.OO.':'n',
                    'O..OO.':'o',
                   'OOO.O.':'p',
                   'OOOOO.':'q',
                   'O.OOO.':'r',
                   '.OO.O.':'s',
                   '.OOOO.':'t',
                   'O...OO':'u',
                   'O.O.OO':'v',
                   '.OOO.O':'w',
                   'OO..OO':'x',
                   'OO.OOO':'y',
                   'O..OOO':'z',
                   '......':' '
                   }

brail_to_eng_dic_num = {
                   'O.....':'1',
                   'O.O...':'2',
                   'OO....':'3',
                   'OO.O..':'4',
                   'O..O..':'5',
                   'OOO...':'6',
                   'OOOO..':'7',
                   'O.OO..':'8',
                   '.OO...':'9',
                   '.OOO..':'O'}
#######################################################################


########create dictionaries for english to brail mode##################
eng_to_brail_dic_dec = {}
eng_to_brail_dic_num = {}

for key in brail_to_eng_dic_dec.keys():
    eng_to_brail_dic_dec[brail_to_eng_dic_dec[key]]=key
    
for key in brail_to_eng_dic_num.keys():
    eng_to_brail_dic_num[brail_to_eng_dic_num[key]]=key
########################################################################


output_text = ""
input_text = str(sys.argv[1])

arguments = sys.argv[1:]
input_text = (" ".join(arguments))


if input_text[0] in ['O','.']:
    index = 0
    while index<=len(input_text)-6:
        char = input_text[index:index+6]
        if char == '.....O':   #capital follows
            index += 6
            output_text += brail_to_eng_dic_dec[input_text[index:index+6]].upper()
        elif char == '.O.OOO':  #number follows until next space
            index += 6
            while input_text[index:index+6] != '......' and index<=len(input_text)-6:    #read numbers until next space
                output_text += brail_to_eng_dic_num[input_text[index:index+6]]
                index += 6
            if input_text[index:index+6] == '......':
                output_text += " "    #space is seen and added to the output
        else:

            output_text += brail_to_eng_dic_dec[input_text[index:index+6]]   #read non upper case and non numerical
            
        index += 6

else:
   input_text = str(input_text)
   index = 0
   while index<=len(input_text)-1:
        if input_text[index].isalpha() or input_text[index]==' ':   #if charachter is alpha or space
            if input_text[index].isupper():   #if upper case
                output_text += '.....O'  
                output_text += eng_to_brail_dic_dec[input_text[index].lower()]
            else:   #if alpha and lower case
                output_text += eng_to_brail_dic_dec[input_text[index]]

        elif input_text[index].isnumeric():   #if char is numeric
            output_text += '.O.OOO'
            while index < len(input_text) and input_text[index] != ' ':   #we should continue reading numeric until we see space
                output_text+= eng_to_brail_dic_num[input_text[index]]
                index += 1
            if index < len(input_text) and input_text[index] == ' ':   #if we have seen space
                output_text += '......'

        index +=1

print(output_text)
