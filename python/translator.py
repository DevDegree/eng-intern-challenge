import re
import sys

#GLOBALS
MAPPING_CHARS_LETTERS_SC = {
    #letters
    'a': 'O.....', 
    'b': 'O.O...', 
    'c': 'OO....', 
    'd': 'OO.O..', 
    'e': 'O..O..',
    'f': 'OOO...', 
    'g': 'OOOO..', 
    'h': 'O.OO..', 
    'i': '.OO...', 
    'j': '.OOO..',
    'k': 'O...O.', 
    'l': 'O.O.O.', 
    'm': 'OO..O.', 
    'n': 'OO.OO.', 
    'o': 'O..OO.',
    'p': 'OOO.O.', 
    'q': 'OOOOO.', 
    'r': 'O.OOO.', 
    's': '.OO.O.', 
    't': '.OOOO.',
    'u': 'O...OO', 
    'v': 'O.O.OO', 
    'w': '.OOO.O', 
    'x': 'OO..OO', 
    'y': 'OO.OOO', 
    'z': 'O..OOO',

    #special characters
    '.': '..OO.O',
    ' ': '......',
    #follows
    'cap_follows': '.....O',
}

MAPPING_DIGITS = {
    #digits
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..',
    '6': 'OOO...', 
    '7': 'OOOO..',
    '8': 'O.OO..', 
    '9': '.OO...', 
    '0': '.OOO..',
    
    #special characters
    'number_follows': '.O.OOO',
    'decimal_follows': '.O...O',
    #follows
    '.': '..OO.O',
}

INVERSE_MAPPING_LETTERS_SC = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    
    #special characters
    '..OO.O': '.',
    '......': ' ',
    
    #follows
    '.....O': 'cap_follows',
    '.O.OOO': 'number_follows'
}

INVERSE_MAPPING_DIGITS = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
    
    #follows
    '.O...O': 'decimal_follows',
    
    #special characters
    '..OO.O': '.',
    '......': ' ',
}

#function to check language eng or braille
def translate(input_string):
    num_values = len(set(input_string))
    if len(input_string) % 6 == 0 and num_values == 2 and "O" in set(input_string) and "." in set(input_string):
        final_translation = convert_braille_to_eng(input_string)
    else:
        final_translation = convert_eng_to_braille(input_string)
    
    return final_translation

#conversion methods from english to braille
def convert_eng_to_braille(input_string: str) -> str:
    """Convert the english input into braille output.
    
    Parameters
    ----------
    input_string : str
        input of the string in english format.
    
    Returns
    -------
    translated_sentenced : str
        translated sentence from english to braille.
    
    """
    #split the input_string into a list of partitions of numbers/non-number strings
    #this regex expression splits inputs based on any occurence of decimal numbers
    parts = re.split(r'(\d+\.?\d*)', input_string)
    #remove any empty strings
    parts = [part for part in parts if part]
    
    translation_list = []
    for partition in parts:
        #translate each partition into braille
        translation = translate_eng_to_braille(partition)
        #join the translated partition into the constructed translation
        translation_list.extend(translation)
        
    #join all the constructed partitions together into a final string
    translated_sentence = ''.join(translation_list)
    return translated_sentence

def translate_eng_to_braille(partition):
    """Translate a given partition.
    
    Parameters
    ----------
        partition : str
            a partition input in format of a sequence of letters
            or a sequence of numbers (float or integer)
    Returns
    -------
        translation : str
            outputted translation of partition in braille
    """
    #check if the first character is a digit or a letter
    if partition[0].isdigit():
        #use digit mapping
        translation = translate_digits(partition)
    else:
        #use letters_sc mapping
        translation = translate_letters(partition)

    return translation
        
def translate_digits(partition):
    """Translate a given partition.
        Assumes that the given partition is a integer/float
        in string format.
        
    Parameters
    ----------
        partition : str
            a sequence of numbers (float or integer) in string format
    Returns
    -------
        translation : str
            outputted translation of partition in braille

    """
    translation = []
    translation.append(MAPPING_DIGITS["number_follows"])
    
    #an edge scenario where it so happens the digit partition
    #ends with a period but is an integer
    #eg '34.'
    last_value_period = False
    if partition[-1] == '.':
        last_value_period = True
        partition = partition.replace(".", '')

    for digit in partition:
        if digit.isdigit():
            translation.append(MAPPING_DIGITS[digit])
        else:
            translation.append(MAPPING_DIGITS["decimal_follows"])
            translation.append(MAPPING_DIGITS["."])
    
    #if edge scenario, add back the period instead of calling a decimal mapping
    if last_value_period:
        translation.append(MAPPING_DIGITS["."])
        
    return translation
            
def translate_letters(partition):
    """Translate a given partition.
        Assumes that the given partition is in letters format
        
    Parameters
    ----------
        partition : str
            a sequence of letters/capitalized letters and special characters
    Returns
    -------
        translation : str
            outputted translation of partition in braille

    """
    translation = []
    for i in range(len(partition)):

        if partition[i].isupper():
            #if the current letter is capitalized, add braile 'cap_follows'
            translation.append(MAPPING_CHARS_LETTERS_SC["cap_follows"])
            letter_ = partition[i].lower()
            translation.append(MAPPING_CHARS_LETTERS_SC[letter_])
        else:
            translation.append(MAPPING_CHARS_LETTERS_SC[partition[i]])
    return translation

#conversion methods to translate from braille to english
def partition_braille(input_string):
    """Partition braille into sequence of length 6 characters
    
    Parameters
    ----------
    input_string : str
            Braille sentence
            
    Returns
    -------
    partitions : list
        Returns a partitioned list of braille sequences, each with a one-to-one
        mapping to an english corresponding meaning. 
    """
    partitions = [input_string[i:i+6] for i in range(0, len(input_string), 6)]
    
    return partitions

def convert_braille_to_eng(input_string):
    """Partition braille into sequence of length 6 characters.
    
    Parameters
    ----------
    input_string : str
            Braille sentence
            
    Returns
    -------
    translated_sentence : str
        Returns a translated sentence in the english language
    """
    #boolean to indicate whether to use the letter mapping or the digit mapping
    num_true_letter_false = False
    translation_list = []
    
    #divide the input_string into 6 characters each
    list_of_partitions = partition_braille(input_string)
    
    if len(list_of_partitions) == 1:
        #if the length of the list is one, we know its a letter/sc since
        #digits would require 'number_follows' which
        #means len > 1
        return get_mapping(input_string, num_true_letter_false)
    else:
        translation = get_mapping(list_of_partitions[0], num_true_letter_false)
        if translation == "number_follows":
            num_true_letter_false = True
        else:
            translation_list.append(translation)
            
        i = 1
        while i < len(list_of_partitions):
            if list_of_partitions[i-1] == ".....O":
                #if previous value is cap_follows
                #capitalize the current value
                translation_list.append(get_mapping(list_of_partitions[i], num_true_letter_false).upper())
            
            elif list_of_partitions[i] == ".O.OOO":
                #if the current value is 'number_follows'
                #switch mapping to digits
                num_true_letter_false = True
            
            elif list_of_partitions[i] == ".O...O":
                pass
            
            elif list_of_partitions[i] == "......":
                num_true_letter_false = False
                translation_list.append(get_mapping(list_of_partitions[i], num_true_letter_false))
                
            else:
                translation_list.append(get_mapping(list_of_partitions[i], num_true_letter_false))
            i += 1
    #remove any values of 'cap_follows' from the translated sentence
    translation_list = [translation for translation in translation_list if translation != "cap_follows"]
    
    #construct the english sentence using the translated partitions
    translated_sentence = ''.join(translation_list)
    return translated_sentence

def get_mapping(braille_symbol, mapping):
    """Mapping function to pick correct mapping.
    
    Parameters
    ----------
    braille_symbol : str
        input partition to be translated to english
    
    mapping : bool
        boolean to determine which mapping dictionary to use
        if mapping = True, use the digit mapping
        if mapping = False, use the character mapping
            
    Returns
    -------
    translation : str
        translated mapping from braille to english
    """
    if mapping:
        mapper = INVERSE_MAPPING_DIGITS
    else:
        mapper = INVERSE_MAPPING_LETTERS_SC
    
    translation = mapper[braille_symbol]
    return translation

#main method
def main():
    arguments = sys.argv[1:]
    input_string = ' '.join(arguments)
    result = translate(input_string)
    print(result)

if __name__ == "__main__":
    main()