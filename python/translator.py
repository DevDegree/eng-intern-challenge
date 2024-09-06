def braille_to_english(inpt):
    #inpt is in braille, convert to english
    print("braille input: ", inpt)

def english_to_braille(inpt):
    #inpt is in english, convert to braille
    print("english input: ", inpt)

def main():
    print("Running")
    inpt = input()
    braille = False
    i = 0 #character counter
    while i < 6:
        if inpt[i] == ".":
            braille = True
            break
    if braille == True:
        braille_to_english(inpt)
    else:
        english_to_braille(inpt)