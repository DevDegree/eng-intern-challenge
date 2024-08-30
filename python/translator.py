input = input("input: \n")

brailAlpha = {
    "a": "0.....",
    "b": "0.0...",
    "c": "00....",
    "d": "00.0..",
    "e": "0..0..",

}


def isbrail(input):
    alpha = False
    for letter in input:
        if letter != "0" and letter != ".":
            alpha = True
    if alpha == True:
        return False
    else:
        return True

if isbrail(input):


