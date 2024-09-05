#Aleksandar Velinovic
#aleksnpetrovic@gmail.com

#Braille/English translator: as the name suggests, braille can be converted to english
#and english into braille, following and exceeding the technical requirements.
#This implementation is also capable of including grammatical symbols (i.e., "?", "!", etc.)
braille_alphabet_library = ["......", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO", "..OO.O", "..O...", "..O.OO", "..OOO.", "..OO..", "..O.O.", "....OO", ".O..O.", ".OO..O", "O..OO.", "O.O..O", ".O.OO."]
braille_numbers = ["......", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO.."]
english_alphabet_library = [" ","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", ",", "?", "!", ":", ";", "-", "/", "<", ">", "(", ")"]
english_numbers = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
capital_next = ".....O"
decimal_next = ".O...O"
number_next = ".O.OOO"

i = 0

def remove_n_chars_from_start(string, n):
    return ''.join([string[i] for i in range(n, len(string))])

def is_braille(string):
    c = 0
    braille_chars = 0
    while c < len(string):
        if string[c] == "." or string[c] == "O":
            braille_chars+=1
        c+=1
    if braille_chars == len(string):
        return 1
    else:
        return 0
def is_next(string):
    if string == ".....O":
        return 1
    elif string == ".O...O":
        return 2
    elif string == ".O.OOO":
        return 3


while i == 0:
    phrase = (input("What would you like to translate?\n"))
    spot = 0
    capital = 0
    character_or_number = 0
    total_index = len(phrase)
    total_words = total_index/6
    phrase_converted = list(phrase)
    d = 0
    translation = ""
    current_char = 0
    cap = 0
    num = 0
    eng_or_braille = is_braille(phrase)
    if eng_or_braille == 1:
        character = [(phrase[i:i+6]) for i in range(0, len(phrase), 6)]

        while total_words > 0:
            phrase = remove_n_chars_from_start(phrase, 6)
            moved = current_char
            while d < len(braille_alphabet_library):
                #test = str(braille_alphabet_library[d])
                if num == 0:
                    if cap == 1:
                        if braille_alphabet_library[d] == character[current_char]:
                            translation = translation + english_alphabet_library[d].upper()

                        #translation = "{in1} {in2}".format(in1=translation, in2=english_alphabet_library[d])
                            current_char = current_char + 1
                            d = len(braille_alphabet_library)
                            cap = 0
                    elif cap == 0:
                        if braille_alphabet_library[d] == character[current_char]:
                            translation = translation + english_alphabet_library[d]

                        #translation = "{in1} {in2}".format(in1=translation, in2=english_alphabet_library[d])
                            current_char = current_char + 1
                            d = len(braille_alphabet_library)
                        
                if num == 1:
                    if braille_alphabet_library[d] == character[current_char]:
                        translation = translation + english_numbers[d]

                        #translation = "{in1} {in2}".format(in1=translation, in2=english_alphabet_library[d])
                        current_char = current_char + 1
                        if character[current_char-1] == braille_numbers[0]:
                            num = 0
                        d = len(braille_alphabet_library)
                    
                if moved == current_char:
                    check = is_next(character[current_char])
                    if check == 1:
                        cap = 1
                        current_char +=1
                        total_words-=1
                    elif check == 2:
                        #if num ==0:
                        num = 1
                        #phrase = remove_n_chars_from_start(phrase, 6)
                        d-=1
                        translation = translation + "."
                        current_char +=1
                        total_words-=1
                    elif check == 3:
                        #if num == 0:
                        num = 1
                        current_char +=1
                        total_words-=1
                            #phrase = remove_n_chars_from_start(phrase, 6)
                        d-=1
                    
                    
                d+=1
            total_words -= 1
            d = 0
    elif eng_or_braille == 0:
        phrase1 = list(phrase)
        firstnum = 1
        while total_index > 0:
            if phrase1[d].isupper() == False:
                e = 0
                while e < len(braille_alphabet_library):
                    if phrase1[d] == " ":
                        translation += braille_numbers[0]
                        total_index -= 1
                        firstnum = 1
                        d+=1
                        e = 0
                    elif phrase1[d] == english_alphabet_library[e]:
                        translation += braille_alphabet_library[e]
                        total_index -= 1
                        d+=1
                        e = 0
                    elif e < len(english_numbers):
                        if phrase1[d] == english_numbers[e]:
                            if firstnum == 1:
                                translation += number_next
                                firstnum = 0
                            translation += braille_numbers[e]
                            total_index -= 1
                            d +=1
                            e = 0
                    e += 1
                    if total_index <= 0:
                        break
            elif phrase1[d].isupper() == True:
                translation += capital_next
                h = phrase[d].lower()
                phrase1[d] = h
    print(translation)

