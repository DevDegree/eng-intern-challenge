import sys

# A dictionary mapping English keys to Braile values
# White circle -> .
# Black circle -> O
engToBraileDict = {
    "a" : "O.....", "b" : "O.O...", "c" : "OO....", "d" : "OO.O..", "e" : "O..O..",
    "f" : "OOO...", "g" : "OOOO..", "h" : "O.OO..", "i" : ".OO...", "j" : ".OOO..", 
    "k" : "O...O.", "l" : "O.O.O.", "m" : "OO..O.", "n" : "OO.OO.", "o" : "O..OO.",
    "p" : "OOO.O.", "q" : "OOOOO.", "r" : "O.OOO.", "s" : ".OO.O.", "t" : ".OOOO.",
    "u" : "O...OO", "v" : "O.O.OO", "w" : ".OOO.O", "x" : "OO..OO", "y" : "OO.OOO",
    "z" : "O..OOO", " " : "......", "capitalFollows" : ".....O", "numberFollows" : ".O.OOO",
}


# A dictionary mapping numbers to letter values
numToLetterDict = {"1" : "a", "2" : "b", "3" : "c", "4" : "d", "5" : "e", 
                    "6" : "f", "7" : "g", "8" : "h", "9" : "i", "0" : "j",}


def main() -> None:
    args = sys.argv
    assert(len(args) > 1)

    # Translate Braile -> English case
    if "." in args[1]:
        translateBraile(args[1])

    # Translate English -> Braile case
    else:
        for i in range(1, len(args)):
            translateEnglish(args[i])
            
            if i != len(args) - 1:
                print(engToBraileDict[" "], end='')


def translateBraile(word : str) -> None:
    # Ensure Braile input is valid
    assert(len(word) % 6 == 0)

    # Function states
    capFollowState = False
    numFollowState = False

    # Invert global dictionarys
    braileToEngDict = {value : key for key, value in engToBraileDict.items()}
    letterToNumDict = {value : key for key, value in numToLetterDict.items()}

    # Split the input into a list of size 6 strings
    words = [word[i:i+6] for i in range(0, len(word), 6)]

    for word in words:
        # Update function states according to word
        if word == engToBraileDict["capitalFollows"]:
            capFollowState = True
            continue
        elif word == engToBraileDict["numberFollows"]:
            numFollowState = True
            continue
        elif word == engToBraileDict[" "]:
            numFollowState = False

        # Handle printing of the word
        if numFollowState:
            print(letterToNumDict[braileToEngDict[word]], end='')
        elif capFollowState:
            print(braileToEngDict[word].upper(), end='')
            capFollowState = False
        else:
            print(braileToEngDict[word], end='')


# Converts number to their associated number ordering
def numToLetter(num : str) -> str:
    return numToLetterDict[num]


def translateEnglish(word : str) -> None:
    # Number follows state
    numState = False
    
    # Translate each character at a time
    for char in word:
        # Print uppercase and number follows Braile if needed
        if char.isupper():
            print(engToBraileDict["capitalFollows"], end='')
            char = char.lower()
        elif (not numState) and char.isnumeric():
            numState = True
            print(engToBraileDict["numberFollows"], end='')

        if char.isnumeric():  
            char = numToLetter(char)

        # Print the character directly translated to Braile
        print(engToBraileDict[char], end='')


if __name__ == "__main__":
    main()
