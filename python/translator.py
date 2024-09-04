from Braille_Dictionary import LETTERS, NUMBERS, cap_follows, decimal_follows, num_follows, space



arg1 = "HeLLo WorlD"

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
                translated_msg.append(cap_follows["braille"])
                translated_msg.append(LETTERS[j]["braille"])
                break
            elif chars[i] == LETTERS[j]["char"]:
                translated_msg.append(LETTERS[j]["braille"])
                break
            elif chars[i] == space["char"]:
                translated_msg.append(space["braille"])
                number_found = False
                break
        # checking if it there is a number
        for k in range(len(NUMBERS)):
            if chars[i] == NUMBERS[k]["char"]:
                if number_found is False:
                    translated_msg.append(num_follows["braille"])
                    number_found = True
                translated_msg.append(NUMBERS[k]["braille"])

    print(translated_msg)
    print("".join(translated_msg))
    # print("".join(translated_msg) == ".O.OOOOO.O..O.O...")
    # print("".join(translated_msg) == ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")

translate_to_braille(arg1)
translate_to_braille(42)

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
    for i in range(len(braille_chars)):
        for j in range(len(LETTERS)):
            if braille_chars[i] == cap_follows["braille"]:
                capital = True
                break
            if capital and braille_chars[i] == LETTERS[j]["braille"]:
                translated_chars.append(LETTERS[j]["char"].upper())
                capital = False
                break
            elif braille_chars[i] == LETTERS[j]["braille"]:
                translated_chars.append(LETTERS[j]["char"])

                break
            elif braille_chars[i] == space["braille"]:
                translated_chars.append(space["char"])
                break
    print(translated_chars)

translate_from_braille(".....OO.OO..O..O.......OO.O.O......OO.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O......OOO.O..")

