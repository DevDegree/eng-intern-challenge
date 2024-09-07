import sys
"""
This module contains the functions to translate the input string to the either english or braille.
"""


def input_type(input_str : str) -> str:
    """
    Function to check the type of input string and returns the type of input string.

    :param input_str: Tinput string that is to be checked.
    :type param1: str
    :return: The type of input string. 
    :rtype: str
    """
    # check if the string is divivisble by 6, and only contains '.' and 'O'
    if len(input_str) % 6 == 0 and all(char in ['.', 'O'] for char in input_str):
        return "braille"
    
    # otherwise it's an english string
    return "english"



def main():
   
