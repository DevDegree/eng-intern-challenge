def main():
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "capital", "number", " "]
    braille = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO", ".....O", ".O.OOO", "......"];

    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    braille_n = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO.."]


    #i need seperate dictionaries since numbers have the same braille as some letters
    char_to_braille = {characters[i]: braille[i] for i in range(len(characters))}
    char_to_braille_n = {num[i]: braille_n[i] for i in range(len(num))}
    braille_to_char = {braille[i]: characters[i] for i in range(len(characters))}
    braille_to_char_n = {braille_n[i]: num[i] for i in range(len(num))}

    str_translate = str(input())
    #alph is true when the string is an alphabetical input, false if braille
    alph = True
    translated = "" 

    #checking if the string is alphabetical or braille: only braille should have "."
    j = 0
    while j < 6 and j < len(str_translate):
        if str_translate[j] == ".":
            alph = False
            break
        j += 1



    #for alphabetical input
    if alph:
        num_bool = False
        for i in range(len(str_translate)):

            if str_translate[i] == " ":
                num_bool = False

            #a capital letter is a special case: 
            #adds a capital indicator, makes the char lowercase, moves on
            if str_translate[i] != str_translate[i].lower():
                translated += char_to_braille["capital"]
                str_translate = str_translate[:i] + str_translate[i].lower() + str_translate[i+1:]


            temp_braille = char_to_braille.get(str_translate[i], False)

            #the char is not in the non numerical list, must mean the char is a number 
            if not temp_braille:
                if not num_bool:
                    translated += char_to_braille["number"]
                    num_bool = True
                temp_braille = char_to_braille_n.get(str_translate[i], False)

            translated += temp_braille



    #for braille input
    else:
        #show that the next char should be capital
        capital_bool = False
        #show that every char until the next space should be a number
        num_bool = False


        for i in range(0, len(str_translate), 6):
            temp_braille = str_translate[i:i+6]

            #if there is a space then that means a number has ended 
            if str_translate == char_to_braille[" "]:
                num_bool = False

            #this if is to diferenciate between nums and alphabetical chars.
            if num_bool:
                temp_alph = braille_to_char_n[temp_braille]
                #if not temp_alph:
                    #print("whuoh")
            else:
                temp_alph = braille_to_char[temp_braille]
        
            #capital_bool true when the previous was a capital indicator.
            if capital_bool:
                temp_alph = temp_alph.upper()
                capital_bool = False


            #the 'continue's are here since capital and number shouldn't actually be in the string        
            if temp_alph == "capital":
                capital_bool = True
                continue 
            if temp_alph == "number":
                num_bool = True
                continue

            translated += temp_alph

    print(translated)



if __name__ == "__main__":
    main()
