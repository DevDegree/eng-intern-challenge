engTobraille = {"a":"O.....", "b":"O.O...", "c":"OO....", "d":"OO.O..", "e":"O..O..", "f":"OOO...", 
                "g":"OOOO..", "h":"O.OO..", "i":".OO...", "j":".OOO..", "k":"O...O.", "l":"O.O.O.", "m":"OO..O.",
                "n":"OO.OO.", "o":"O..OO.", "p":"OOO.O.", "q":"OOOOO.", "r":"O.OOO.", "s":".OO.O.", "t":".OOOO.", 
                "u":"O...OO", "v":"O.O.OO", "w":".OOO.O", "x":"OO..OO", "y":"OO.OOO", "z":"O..OOO",
                "1":"O.....", "2":"O.O...", "3":"OO....", "4":"OO.O..", "5":"O..O..", "6":"OOO...",
                "7":"OOOO..", "8":"O.OO..", "9":".OO...", "0":".OOO..", ".":"..OO.O", ",":"..O...", 
                "?":"..O.OO", "!":"..OOO.", ":":"..OO..", ";":"..O.O.", "-":"....OO", "/":".O..O.", "<":".OO..O",
                ">":"O..OO.", "(":"O.O..O", ")":".O.OO.", " ": "......" }

cap_next = ".....O"
dec_next = ".O...O"
num_next = ".O.OOO"

brailleToengNotNum = {}
brailleToengNum = {}

for key, value in engTobraille.items():
    if key.isnumeric() or key == ">":
        brailleToengNum[value] = key
    else:
        brailleToengNotNum[value] = key


def translateTo(word):
    # Braille to English or English to Braille
    if word == "":
        print("There is nothing translate")
        return

    if all(c in ['O', '.'] for c in word):
        return translateToenglish(word)
    else:
        return translateTobraille(word)




def translateTobraille(english):
    # Translate to Braille

    braille = ""

    if english[0].isnumeric():
        braille += num_next


    for i, c in enumerate(english):
 
        if c.isnumeric():
            braille += engTobraille[c]
        else:
            
            if not c.isalpha():

                braille += engTobraille[c]
            elif c.isalpha() and c.isupper():
                s = c.lower()
                braille += cap_next
                braille += engTobraille[s]
            else:
                braille += engTobraille[c]

            if not i == (len(english)-1) and english[i+1].isnumeric():
                braille += num_next
        
    return braille


def translateToenglish(braille):
    # Translate to English

    english = ""
    listbrl = []
    temp = braille

    for i in range(len(braille)//6):
        listbrl.append(temp[:6])
        temp = temp[6:]

    isnumber = False

    for i, c in enumerate(listbrl):

        if c == ">":
            english += brailleToengNum[c]
            continue

        if c == num_next:
            isnumber = True
            continue
        elif c == '......':
            isnumber = False
        
        if c not in brailleToengNotNum and c not in brailleToengNum:
            continue

        if isnumber == True:
            english += brailleToengNum[c]
        else:
            if i != 0 and (listbrl[i-1] == cap_next):
                english += brailleToengNotNum[c].upper()
            else:
                english += brailleToengNotNum[c]

    return english

# Execute Here
word = 'Abc 123 xYz'
print(translateTo(word))
