# Requirements: 
'''
-

'''

# Imports
import sys

# Constants 

# Helpers

# Returns true if the list of strings should be parsed as a Braille string
def isBraille(args: list[str]) -> bool: 
    rawString = "".join(args)
    numOfO = 0
    numOfDot = 0
    for char in rawString: 
        if char == 'O': 
            numOfO += 1
        elif char == '.': 
            numOfDot +=1
    return numOfO + numOfDot == len(rawString) and len(rawString)%6==0
    
        

# main
def main(): 
    args = sys.argv[1:]
    print(isBraille(args)) 

# Entry
if __name__ == '__main__':
    main()

