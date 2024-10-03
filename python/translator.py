# program.py
import sys

'''
Quick Rundown:

- User inputs an arguement as specified in instructions
- If it is a sentence, it will join all arguements as one big string first, seperated by space ' '
- Converts this string (or list if only one argument) into a list of chars
- enumarate through list and add braille version of char to braille_list
- convert braille_list to string and returns it

NOTE: I didn't want to make the whole dict, but I couldn't find a pattern between each braille character

'''

def main():
    #if there are multiple arguements, join them with spaces, and then convert it to char list
    user_input = sys.argv[1:]
    if len(sys.argv) > 1:
        char_list = list(' '.join(user_input)  )
    else:
        char_list = list(user_input)
    
    #list where all braille chars will be held
    braille_list = [] 

    braille_dict =	{ #I was going to do something fancy with making a-j correlate to 0-9, but this was just faster
        'a' : "O.....", 'b' : "O.O...", 'c' : "OO....", 'd' : "OO.O..",
        'e' : "O..O..", 'f' : "OOO...", 'g' : "OOOO..", 'h' : "O.OO..", 
        'i' : ".OO...", 'j' : ".OOO..", 'k' : "O...O.", 'l' : "O.O.O.",
        'm' : "OO..O.", 'n' : "OO.OO.", 'o' : "O..OO.", 'p' : "OOO.O.",
        'q' : "OOOOO.", 'r' : "O.OOO.", 's' : ".OO.O.", 't' : ".OOOO.",
        'u' : "O...OO", 'v' : "O.O.OO", 'w' : ".OOO.O", 'x' : "OO..OO",
        'y' : "OO.OOO", 'z' : "O..OOO", 

        '1' : "O.....", '2' : "O.O...", '3' : "OO....", '4' : "OO.O..",
        '5' : "O..O..", '6' : "OOO...", '7' : "OOOO..", '8' : "O.OO..", 
        '9' : ".OO...", '0' : ".OOO..",
        
        '.' : "..OO.O", ',' : "..O...", '?' : "..O.OO", '!' : "..OOO.",
        ':' : "..OO..", ';' : "..O.O.", '-' : "....OO", '/' : ".O..O.",
        '<' : ".OO..O", '>' : "O..OO.", '(' : "O.O..O", ')' : ".O.OO.",
        ' ' : "......"
    }

    is_num = False

    #enumerate char_list and append braille version of each char to braille_list
    #checks if element is number, uppercase or decimal (and not period)
    for index, element in enumerate(char_list):

        #makes it so that if the current and following elements are numbers, we do not keep adding the "is numbers" in braille
        if not element.isdigit():
            is_num = False
        if element.isdigit() and not is_num:
            is_num = True
            braille_list.append(".O.OOO")

        elif element.isupper():
            braille_list.append(".....O")
        
        elif (element == '.') and (index < (len(char_list) - 1)) and char_list[index+1].isdigit():
            braille_list.append(".O...O")

        braille_list.append( braille_dict[element.lower()] )



    final_string = ''.join(braille_list)

    print(final_string)
    return final_string



if __name__ == "__main__":
    main()