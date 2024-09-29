"""
Author Usaid Malik 
Date: 09/29/2024

This is a program that 
takes arguments from the command
line and outputs the corresponding
Braille or English test
"""
import sys
from typing import List

def 

def main(argc: int, argv: List[int]):
    if argc != 2:
        # returning anything that isnt 2 because more arguments shouldnt be given unnecesarily either
        print("IMPROPER USAGE! Correct Usage: python translator.py [source_text]")
        return
    sourceText = argv[2] # getting the source text at the second index

if __name__ == "__main__":
    argv = sys.argv # this is in a variable so i dont call sys.argv twice
    main(len(argv), argv)
    # passing in the source text from the CLI