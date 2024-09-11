import sys
from enum import Enum

#start by creating a dictionary of the letters as keys and brailles as value:
letter_conversion = {
    "a" : "O.....",
    "b" : "O.O...",
    "c" : "OO....",
    "d" : "OO.O..",
    "e" : "O..O..",
    "f" : "OOO...",
    "g" : "OOOO..",
    "h" : "O.OO..",
    "i" : ".OO...",
    "j" : ".OOO..",
    "k" : "O...O.",
    "l" : "O.O.O.",
    "m" : "OO..O.",
    "n" : "OO.OO.",
    "o" : "O..OO.",
    "p" : "OOO.O.",
    "q" : "OOOOO.",
    "r" : "O.OOO.",
    "s" : ".OO.O.",
    "t" : ".OOOO.",
    "u" : "O...OO",
    "v" : "O.O.OO",
    "w" : ".OOO.O",
    "x" : "OO..OO",
    "y" : "OO.OOO",
    "z" : "O..OOO",
    "." : "..OO.O",
    "," : "..O...",
    "?" : "..O.OO",
    "!" : "..OOO.",
    ":" : "..OO..",
    ";" : "..O.O.",
    "-" : "....OO",
    "/" : ".O..O.",
    "<" : ".OO..O",
    ">" : "O..OO.",
    "(" : "O.O..O",
    ")" : ".O.OO.",
    " " : "......",
}

number_conversion = {
    "1" : "O.....",
    "2" : "O.O...",
    "3" : "OO....",
    "4" : "OO.O..",
    "5" : "O..O..",
    "6" : "OOO...",
    "7" : "OOOO..",
    "8" : "O.OO..",
    "9" : ".OO...",
    "0" : ".OOO..",
    "." : "..OO.O",
}

conditional_conversion = {"capital_follow" : ".....O", "number_follows" : ".O.OOO", "decimal_follows" : ".O...O"}


class Language(Enum):
    English = 1
    Braille = 2

#function to detect what language the input is in
#if the string is less than 6 then the string is in english since braille comes in 6 sections
#if the string is >= 6 check the whole string if it contains a character different than O & ., if found then translate to braille if not then to english
def DetectLanguage(stream):
    if len(stream) < 6:
        translate_to = Language.Braille
        return translate_to

    for character in stream:

        #if we found a character that is different than the braille character
        if(character != 'O' and character != '.' ):
            translate_to = Language.Braille
            return translate_to
        
    #we didn't find any english character
    translate_to = Language.English
    return translate_to

def IsEnglishNumberDecimal(stream: str, character):
    index = stream.find(character)
    temp_string = stream[index : len(stream)]
    space_index = temp_string.find(' ')

    if space_index > 0:
        return temp_string.find('.',0,space_index)
    
    else:
        return temp_string.find('.')

def EnglishToBraille(stream):
    braille_stream = ""
    is_number = False
    for character in stream:

        #we need to check if the character is uppercase -> done
        #we need to check if the character is a number -> done
        #we need to detect space to nullify the number effect -> done

        #detecting decimal -> not clear in the instructions where to use the decimal
        #it was inserted right after the number follows notation as mentioned by the wikipedia

        if character.isupper():
            braille_stream += conditional_conversion["capital_follow"]

        elif (character.isdigit() and is_number == False):
            braille_stream += conditional_conversion["number_follows"]

            # if is_number = True then stop print the letter conversion and print the number conversion
            is_number = True
            if IsEnglishNumberDecimal(stream,character) > 0:
                braille_stream += conditional_conversion["decimal_follows"]

        elif character == " ":
            is_number = False

        #finalizing string
        if is_number:
            braille_stream += number_conversion[character]

        else:
            braille_stream += letter_conversion[character.lower()]

    return braille_stream

def BrailleToEnglish(stream):
    English_stream = ""
    is_number = False
    is_capital = False

    letter_conversion_inverse = {v: k for k, v in letter_conversion.items()}
    number_conversion_inverse = {v: k for k, v in number_conversion.items()}

    #for the braille we have to read the string 6 characters at a time
    for i in range(0,len(stream),6):
        notation = stream[i:i+6]
        #we need to check if the notation is uppercase -> done
        #we need to check if the notation is a number -> done
        #we need to detect space to nullify the number effect -> done

        if notation == conditional_conversion["capital_follow"]:
            is_capital = True
            continue

        elif (notation == conditional_conversion["number_follows"] and is_number == False):
            is_number = True
            continue

        elif notation == letter_conversion[' ']:
            is_number = False

        #finalizing string
        if is_capital:
            if notation == "O..OO.":
                English_stream += 'O'

            else:
                English_stream += letter_conversion_inverse.get(notation).upper()

        elif is_number:
            if notation == "O..OO.":
                English_stream += '>'
            else:
                English_stream += number_conversion_inverse.get(notation)

        else:
            if notation == "O..OO.":
                English_stream += 'o'

            else:
                English_stream += letter_conversion_inverse.get(notation)
        
        is_capital = False

    return English_stream


def main():
    list_stream = sys.argv
    translated_string = "" 

    for i in range(1,len(list_stream)):
        stream = list_stream[i]

        translate_to = DetectLanguage(stream=stream)
        if translate_to == Language.Braille:
           translated_string += EnglishToBraille(stream=stream)

        else:
            translated_string += BrailleToEnglish(stream=stream)

    print(translated_string)

if __name__ =='__main__':
    main()