import sys

# for personal testing
# def resultsMatch(answer, response):
#     if len(answer) != len(response):
#         return False
#     for i, jin zip(answer, response):
#         if i != j:
#             return False
    
#     return True

def EnglishTranslation(input_text, alpha_translator, numeric_translator, capital_follow, number_follow, space):
    result = []
    isNum = False
    isCapital = False
    braille_size = 6
    itr = 0
    # iterate over chunks or 6 characters
    while itr < len(input_text):
        chunk = input_text[itr:itr+braille_size]
        #check for capital
        if chunk == capital_follow:
            isCapital = True
            itr += braille_size
            continue
        #check for num
        elif chunk == number_follow:
            isNum = True
            itr += braille_size
            continue
        #check for space
        elif chunk == space:
            result.append(' ')
            # reset the numbering flag
            isNum = False
            itr += braille_size
            continue
        if isNum:
            result.append(numeric_translator[chunk])
        else:
            translated_char = alpha_translator[chunk]
            if isCapital:
                translated_char = translated_char.upper()
                # reset the cap flag
                isCapital = False
            result.append(translated_char)
        
        itr += braille_size
    
    return ''.join(result)

def BrailleTranslation(word, alpha_translator, numeric_translator, capital_follow, number_follow, space):
    result = []
    isNum = False
    for char in word:
        if char.isupper():
            result.append(capital_follow)
            char = char.lower()
        if char == ' ':
            result.append(space)
            #rest numbering flag
            isNum = False  
        elif char.isdigit():
            if not isNum:
                result.append(number_follow)
                isNum = True
            result.append(numeric_translator[char])
        else:
            if isNum:
                isNum = False
            result.append(alpha_translator[char])
    return ''.join(result)

def translator(input_text):
    #dictionary for english
    alpha_translator = {
        "a": "O.....",
        "b": "O.O...",
        "c": "OO....",
        "d": "OO.O..",
        "e": "O..O..",
        "f": "OOO...",
        "g": "OOOO..",
        "h": "O.OO..",
        "i": ".OO...",
        "j": ".OOO..",
        "k": "O...O.",
        "l": "O.O.O.",
        "m": "OO..O.",
        "n": "OO.OO.",
        "o": "O..OO.",
        "p": "OOO.O.",
        "q": "OOOOO.",
        "r": "O.OOO.",
        "s": ".OO.O.",
        "t": ".OOOO.",
        "u": "O...OO",
        "v": "O.O.OO",
        "w": ".OOO.O",
        "x": "OO..OO",
        "y": "OO.OOO",
        "z": "O..OOO",
    }
    braille_translator = {
        "O.....": "a",
        "O.O...": "b",
        "OO....": "c",
        "OO.O..": "d",
        "O..O..": "e",
        "OOO...": "f",
        "OOOO..": "g",
        "O.OO..": "h",
        ".OO...": "i",
        ".OOO..": "j",
        "O...O.": "k",
        "O.O.O.": "l",
        "OO..O.": "m",
        "OO.OO.": "n",
        "O..OO.": "o",
        "OOO.O.": "p",
        "OOOOO.": "q",
        "O.OOO.": "r",
        ".OO.O.": "s",
        ".OOOO.": "t",
        "O...OO": "u",
        "O.O.OO": "v",
        ".OOO.O": "w",
        "OO..OO": "x",
        "OO.OOO": "y",
        "O..OOO": "z"
    }
    #unique circumstances
    capital_follow = ".....O"
    number_follow = ".O.OOO"
    space = "......"

    #num for eng to braille
    numeric_translator_eng = {
        "0": ".OOO..",
        "1": "O.....",
        "2": "O.O...",
        "3": "OO....",
        "4": "OO.O..",
        "5": "O..O..",
        "6": "OOO...",
        "7": "OOOO..",
        "8": "O.OO..",
        "9": ".OO..."
    }
    
    # braille to eng
    numeric_translator_braille = {
        ".OOO..": "0",
        "O.....": "1",
        "O.O...": "2",
        "OO....": "3",
        "OO.O..": "4",
        "O..O..": "5",
        "OOO...": "6",
        "OOOO..": "7",
        "O.OO..": "8",
        ".OO...": "9"
    }

    # check if word is eng or braille
    isEnglish = False
    for v in input_text:
        if v != '.' and v != 'O':
            isEnglish = True
            break

    result = ""
    # Braille -> English
    if not isEnglish:
        result = EnglishTranslation(input_text, braille_translator, numeric_translator_braille, capital_follow, number_follow, space)
    # English -> Braille
    else:
        result = BrailleTranslation(input_text, alpha_translator, numeric_translator_eng, capital_follow, number_follow, space)
    
    return result

if __name__ == "__main__":
    #personal testing *ignore*

    # input_text = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
    # checker = ".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O.."
    # checker1 = ".O.OOOOO.O..O.O..."
    
    # result = translator(input_text)
    # print(result)
    
    # # if resultsMatch(checker1, checker):
    # #     print("good")
    # # else:
    # #     print("uh oh")
    
    # to handle the test from the test file
    if len(sys.argv) > 1:
        #put arg into input
        input = " ".join(sys.argv[1:])
        print(translator(input))
    else:
        print("Put inputs please :)")
