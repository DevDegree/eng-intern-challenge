

#List of uppercase alphabets
alphabet = []
for i in range (97, 123):
    alphabet.append(chr(i))
#print(alphabet)

alphabet_braille = ["O.....","O.O...","OO....","OO.O..",
                    "O..O..","OOO...","OOOO..","O.OO..",
                    ".OO..",".OO..","O...O.","O.O.O.",
                    "OO..O.","OO.OO.","O..OO.","OOO.O.",
                    "OOOOO.","O.OOO.",".OO.O.",".OOOO.",
                    "O...OO","O.O.OO",".OOO.O","OO..OO",
                    "OO.OOO","O..OOO"]

duplicate_alphabet = alphabet_braille[:]

alpha_dict = {}
for key in alphabet:
    for value in duplicate_alphabet:
        alpha_dict[key] = value
        duplicate_alphabet.remove(value)
        break







#List of numbers
numbers = []
for j in range (1, 10):
    numbers.append(str(j))
    if j == 9:
        numbers.append(str(0))
#print(numbers)


number_braille = alphabet_braille[0:10]
duplicate_number = number_braille[:]
#print(number_braille)
#print(len(numbers))
#print(len(duplicate_number))




number_dict = {}

for key in numbers:
    for value in duplicate_number:
        number_dict[key] = value
        duplicate_number.remove(value)
        break

#print(number_dict)




#List fo special charactes
special_characters = [".",",","?","!",":",";","-","/","<",">","(",")"," "]
#print(special_characters)
#print(len(special_characters))

special_braille = ["..OO.O","..O...","..O.OO","..OOO.",
                   "..OO..","..O.O.","....OO",".O..O.",
                   ".OO..O","O..OO.","O.O..O",".O.OO.",
                   "......"]
#print(len(special_characters))

duplicate_special = special_braille[:]

special_dict = {}

for key in special_characters:
    for value in duplicate_special:
        special_dict[key] = value
        duplicate_special.remove(value)
        break

#print(special_dict)






change = [".....O",".O...O",".O.OOO"]
change_values = ["capital", "decimal", "number"]
#print(change)

merge_dict = {**alpha_dict, **number_dict, **special_dict}
#print(merge_dict)



def alphabets(user_input, merge_dict, change):

    #alphabets to braille
    uppercase_alphabet = [letters.upper() for letters in alphabet]
    final_list = alphabet + uppercase_alphabet + numbers + special_characters
    
    if user_input[0] in final_list and (user_input[0]!= "." and user_input[0]!= "O"):
        user_list = []
        for i in user_input:
            user_list.append(i)
        #print(user_list)

        output = []
        count = 0
        for alpha in user_input:
            if alpha.isupper():
                alpha = alpha.lower()
                output.append(change[0])
            if alpha.isdigit():
                if count == 0:
                    output.append(change[2])
                    count = count + 1
                    if alpha.isalpha():
                        count = 0
            output.append(merge_dict[alpha])

        final_output = ''.join(output)
        #print(output)
        return final_output
    else:

        #Exract the values of braille letters in a list
        userbraille_list = []
        for i in range(0, len(user_input),6):
            chunks = user_input[i : i + 6]
            userbraille_list.append(chunks)
        #print(userbraille_list)

        braille_list = list(merge_dict.values()) + change
        alphabet_list = list(merge_dict.keys()) + change_values
        
        braille_output = []
        capitalize_next = False
        number_mode = False


        for braille in userbraille_list:
            if braille == change[0]:
                capitalize_next = True
                continue
            if braille == ".O.OOO":
                number_mode = True
                count = 0
                continue

            index = braille_list.index(braille)
            found_item = alphabet_list[index]
            if found_item:
                if capitalize_next:
                    found_item = found_item.upper()
                    capitalize_next = False  # Reset flag after capitalizing
                
                if number_mode:
                    number_dict = {"a":"1", "b": "2", "c":"3", "d":"4",
                                   "e":"5", "f":"6","g":"7","h":"8",
                                   "i":"9","j":"0"}
                    found_item = number_dict[found_item]
                    #print(found_item)
      
            braille_output.append(found_item)

        return ''.join(braille_output)

# Example usage
import sys

# Example usage
if len(sys.argv) > 1:
    user_input = ' '.join(sys.argv[1:])  # Combine all arguments into a single string
    print(alphabets(user_input.strip(), merge_dict, change))

        



    



