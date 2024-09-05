from Braille_Dictionary import LETTERS, NUMBERS, CAP_FOLLOWS, DECIMAL_FOLLOWS, NUM_FOLLOWS, SPACE, SYMBOLS, PERIOD, FOLLOW_MARKERS
import sys



# arg1 = "HeLLo WorlD"

def translate_to_braille(msg):
    chars = list(str(msg))
    """
    loop through each char in the message, check if it is a specific letter and have a separate string translate that letter
    to braile along with checking whether or not it is a captial letter or not, and apply the correct braille marker
    
    also check if it is a number and apply the correct braille marker before translating it to a number
    """

    #letters only translating with captials and spaces and numbers as well
    translated_msg = []

    number_found = False #checks if first time it found a number and assume all symbols after are numbers till a space is found
    for i in range(len(chars)):
        for j in range(len(LETTERS)):
            if chars[i] == LETTERS[j]["char"].upper():
                translated_msg.append(CAP_FOLLOWS["braille"])
                translated_msg.append(LETTERS[j]["braille"])
                break
            elif chars[i] == LETTERS[j]["char"]:
                translated_msg.append(LETTERS[j]["braille"])
                break
            # elif chars[i] == SPACE["char"]:
            #     translated_msg.append(SPACE["braille"])
            #     number_found = False
            #     break


        # checking if there is a number
        for k in range(len(NUMBERS)):
            if chars[i] == NUMBERS[k]["char"]:
                if number_found is False:
                    translated_msg.append(NUM_FOLLOWS["braille"])
                    number_found = True
                translated_msg.append(NUMBERS[k]["braille"])
                break
            elif number_found and chars[i] == PERIOD["char"]:
                translated_msg.append(DECIMAL_FOLLOWS["braille"])
                break
            # ----checking if it is a symbol: space, comma, colon, etc.
        for s in range(len(SYMBOLS)):
            if chars[i] == SYMBOLS[s]["char"]:
                translated_msg.append(SYMBOLS[s]["braille"])
                if SYMBOLS[s] == SPACE:
                    number_found = False
                break

    # print(translated_msg)
    print("".join(translated_msg))
    # print(msg)
    # print("".join(translated_msg) == ".O.OOOOO.O..O.O...")
    # print("".join(translated_msg) == ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")

# translate_to_braille(arg1)
# translate_to_braille(40)
# translate_to_braille("hello 45.6")

# only translates from braille to letters with spacing and capitals no numbers yet
def translate_from_braille(msg):
    braille_counter = 0
    single_char = []
    braille_chars = []
    translated_chars = []
    for i in range(len(msg)):
        braille_counter += 1
        single_char.append(msg[i])
        if braille_counter == 6:
            braille_chars.append("".join(single_char))
            single_char = []
            braille_counter = 0

    capital = False
    number_found = False
    for i in range(len(braille_chars)):
        letter_found = False
        if number_found is False:
            for j in range(len(LETTERS)):
                if braille_chars[i] == CAP_FOLLOWS["braille"]:
                    capital = True
                    letter_found = True
                    break
                if capital and braille_chars[i] == LETTERS[j]["braille"]:
                    translated_chars.append(LETTERS[j]["char"].upper())
                    capital = False
                    letter_found = True
                    break
                elif braille_chars[i] == LETTERS[j]["braille"]:
                    translated_chars.append(LETTERS[j]["char"])
                    letter_found = True
                    break
        if letter_found is False:
            for s in range(len(SYMBOLS)):
                if braille_chars[i] == SYMBOLS[s]["braille"]:

                    translated_chars.append(SYMBOLS[s]["char"])
                    if SYMBOLS[s] == SPACE:
                        number_found = False
                    break
        if number_found:
            for n in range(len(NUMBERS)):
                if braille_chars[i] == NUMBERS[n]["braille"]:
                    translated_chars.append(NUMBERS[n]["char"])
                    break

        if braille_chars[i] == NUM_FOLLOWS["braille"]:
            number_found = True


    # print(translated_chars)
    print("".join(translated_chars))

# translate_from_braille(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")
# translate_from_braille(".O.OOOOO.O...OOO..")
# translate_from_braille("O.OO..O..O..O.O.O.O.O.O.O..OO........O.OOOOO.O..O..O...O...O..OO.OOOO...")

def check_if_braille_or_not(msg):
    # grab the first 6 characters and determine if they are braille characters or not
    chars = str(msg)
    BRAILLE_DICTIONARY = [NUMBERS, SYMBOLS, LETTERS, FOLLOW_MARKERS]
    is_braille = False

    if len(chars) > 6:
        for i in range(len(BRAILLE_DICTIONARY)):
            for j in range(len(BRAILLE_DICTIONARY[i])):
                if chars[:6] == BRAILLE_DICTIONARY[i][j]["braille"]:
                    is_braille = True
                    break
            if is_braille:
                break
    if is_braille:
        translate_from_braille(msg)
    else:
        translate_to_braille(msg)

msgs = sys.argv[1:]
temp = ""
for i in range(len(msgs)):
    temp += str(msgs[i])
    if i < len(msgs) - 2:
        temp += " "
msgs = temp
check_if_braille_or_not(msgs)


