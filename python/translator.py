import sys

#--------------------------------------
# Dictionaries & Arrays

braille = [
 'O.....',  # a
 'O.O...',  # b
 'OO....',  # c
 'OO.O..',  # d
 'O..O..',  # e
 'OOO...',  # f
 'OOOO..',  # g
 'O.OO..',  # h
 '.OO...',  # i
 '.OOO..',  # j
 'O...O.',  # k
 'O.O.O.',  # l
 'OO..O.',  # m
 'OO.OO.',  # n
 'O..OO.',  # o
 'OOO.O.',  # p
 'OOOOO.',  # q
 'O.OOO.',  # r
 '.OO.O.',  # s
 '.OOOO.',  # t
 'O...OO',  # u
 'O.O.OO',  # v
 '.OOO.O',  # w
 'OO..OO',  # x
 'OO.OOO',  # y
 'O..OOO',  # z
 '..OO.O',  # .
 '..O...',  # ,
 '..O.OO',  # ?
 '..OOO.',  # !
 '..OO..',  # :
 '..O.O.',  # ;
 '....OO',  # -
 '.O..O.',  # /
 '.O.O.O',  # <
 'O.O.O.',  # >
 'O.O..O',  # (
 '.O.OO.',  # )
 '......'   # space
]
special_braille = [
    '.....O',  # capital follows
    '.O...O',  # decimal follows
    '.O.OOO',  # number follows
]

braille_to_index = {
    braille[i] : i for i in range(len(braille))
}

alphabet = list("abcdefghijklmnopqrstuvwxyz,.?!:;-/<>() ")
alphabet_to_index = {
    alphabet[i] : i for i in range(len(alphabet))
}

#------------------------------------------------------
# FUNCTIONS
def translate_to_braille(user_input):
    translated_phrase = ""
    number_mode = False
    for i in range(0, len(user_input)):
        letter = user_input[i]

        if letter.isnumeric():
            if not number_mode:
                translated_phrase += special_braille[2]

            translated_phrase += braille[int(letter) - 1]
            number_mode = True
            continue

        elif letter == '.' and number_mode:
            translated_phrase += special_braille[1]
            continue

        elif letter == ' ':
            number_mode = False

        elif letter.isupper():
            translated_phrase += special_braille[0]

        # add the translated character to the answer
        index = alphabet_to_index[letter.lower()]
        translated_phrase += braille[index]

    return translated_phrase

def translate_to_english(user_input):

    translated_phrase = ""
    capital_mode = False
    number_mode = False
    for i in range(0, len(user_input), 6):
        part = user_input[i: i + 6]

        if part == "......":
            number_mode = False

        elif part == special_braille[0]:
            capital_mode = True
            continue

        elif part == special_braille[1]:
            translated_phrase += "."
            continue

        elif part == special_braille[2]:
            number_mode = True
            continue

        # add the translated character to the answer
        index = braille_to_index[part]
        if number_mode:
            translated_phrase += str((index + 1) % 10)
        else:
            translated_phrase += alphabet[index].upper() if capital_mode else alphabet[index]
            capital_mode = False

    return translated_phrase

#--------------------------------------------------------------------

# driver code

user_input = ' '.join(sys.argv[1:])
# Figure out if we are translating to Braille / English
translating_to_braille = False
for i in range(len(user_input)):
    if user_input[i] != 'O' and user_input[i] != '.':
        translating_to_braille = True
        break

translated_phrase = ""
if translating_to_braille:
    translated_phrase = translate_to_braille(user_input)
else:
    translated_phrase = translate_to_english(user_input)
print(translated_phrase,end="")


