################ Author : zahra Sarayloo
################ Email : zsaraylo@uwaterloo.ca
import sys


## create dictionary for Braille to letter and vice versa

Braille_to_word = {'O.....':'a',
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
                   '.....O':'capital',
                   '.O...O':'decimal',
                   '.O.OOO':'number',
                   '......':'space'
                   }
Braille_to_sign = {'..OO.O':'.',
                   '..O...':',',
                   '..O.OO':'?',
                   '..OOO.':'!',
                   '..OO..':':',
                   '..O.O.':';',
                   '....OO':'-',
                   '.O..O.':'/',
                   '.OO..O':'<',
                   'O..OO.':'>',
                   'O.O..O':'(',
                   '.O.OO.':')'
                   }
                   
Braille_to_num = {'O.....':'1',
                   'O.O...':'2',
                   'OO....':'3',
                   'OO.O..':'4',
                   'O..O..':'5',
                   'OOO...':'6',
                   'OOOO..':'7',
                   'O.OO..':'8',
                   '.OO...':'9',
                   '.OOO..':'0'
                   }

letter_to_Braille = {v:k for k,v in Braille_to_word.items()} 

num_to_Braille = {v:k for k,v in Braille_to_num.items()}

sign_to_Braille = {v:k for k,v in Braille_to_sign.items()}


######### Define function

def isBraille(B):

    if len(B) % 6 != 0:
        return False
    
    
    valid_braille = set(Braille_to_word.keys()).union(
        Braille_to_num.keys(), Braille_to_sign.keys())
    
    for i in range(0, len(B), 6):
        chunk = input_str[i:i+6]

        if chunk not in valid_braille:
            return False

    return True


def translate(A):

    # detect the type of input 

    output = ''
    flag = 0 # recognized first number

    if not(isBraille(A)):

        
        # The input is in english words type
        for letter in A:

            if letter.isdigit():
                if flag == 0:
                    output += letter_to_Braille['number']
                    flag = 1

                output += num_to_Braille[letter]

            elif letter == ' ':
                flag = 0
                output += letter_to_Braille['space']


            elif letter.isalpha():
                flag = 0
                if letter.isupper():

                    output += letter_to_Braille['capital']
                    output += letter_to_Braille[letter.lower()]
                    
                
                else:
                    output += letter_to_Braille[letter]
            else:

                flag = 0
                output += sign_to_Braill[letter]
    else:
        
    
        # The input is in Braille format
        n = len(A)//6

        flag_capital = 0
        flag_num = 0


        for i in range(n):

            char = A[i*6:(i+1)*6]

            if flag_num == 1:
                letter = Braille_to_num.get(char)

                if letter is None:
                    letter =  Braille_to_word.get(char)
                    flag_num = 0
                    if letter in None : 
                        letter = Braille_to_sign.get(char)
            else:

                letter = Braille_to_word.get(char)
            
                if letter is None:

                    letter = Braille_to_sign.get(char)

                    if letter is None:

                        letter = Braille_to_num.get(char)


            if letter == 'capital':
                flag_capital = 1

            elif letter == 'number':
                flag_num = 1

            


            if (flag_capital == 1) & (letter != 'capital') :
                output += letter.upper()
                flag_capital = 0

            elif (flag_num  == 1) & (letter != 'number') :
                output += letter

            elif letter == 'space':
                
                output += ' ' 
            elif (letter != 'capital') & (letter != 'number'):

                output += letter

    
    return output



    


if __name__ == "__main__":
    
    inputs = sys.argv[1:]
    translated_outputs = []
    for input_str in inputs:

        translated = translate(input_str)

        if translated_outputs:
            translated_outputs.append(letter_to_Braille['space'])
        translated_outputs.append(translated)


    final_output = ''.join(translated_outputs)
    print(final_output)
    
    





















