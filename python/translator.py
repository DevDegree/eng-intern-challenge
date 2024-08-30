# CHALLENGE OUTLINE:
# The string to translate will be passed into your application as an argument at runtime. 
# Your application must be smart enough to determine if the string given to it is either Braille or English and automatically convert it to the appropriate opposite.
# For the purposes of this challenge Braille must be displayed as O (the letter O) and . (a period) where O represents a raised dot. 
# You must include the entire English alphabet, the ability to capitalize letters, add spaces, and the numbers 0 through 9 as well.
# After conversion, output the translated string--and nothing else--to the terminal.

# NOTES: 
# - Decimals are already dealt with because of the rule "When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol."
# - o and > have the same braille symbol but no special character such as SPECIAL_CHARACTER_FOLLOWS to differentiate between them
# - I forked the repo at a time when the expected output in the test file was incorrect, so my code was failing. The expected output has since been updated in the orginal repo to the correct version. Instead of forking the repo again, I simply changed the expected output to the one that was updated. I hope that's okay.
# - I decided to go with a simple architecture and not create a class for the translator. This was simply a design choice due to the project requirements and the fact that isn't something that needs to scale. It would be easy enough to change the architecture though, -- if circumstances change -- as everything is laid out nicely.

import sys
import utils


def main():
    """
    INPUT: This program takes user input as commands given in the command line when running the file. Example usage would be: 'python3 translator.py these words will be translated' or 'python3 translator.py .OOOO.O.OO..O..O...OO.O.O..O.........OOO.OO..OO.O.OOO.OO.O...OO.O........OOO.O.OO...O.O.O.O.O.O.......O.O...O..O.........OOOO.O.OOO.O.....OO.OO..OO.O.O.O.O.O......OOOO.O..O..OO.O..' as it will translate both ways with automatic detection.

    STATE & OUTPUT: I use the concept of a state to decided what is the correct character/symbol to add to the output at each iteration. Both the state and creating an output string instead of printing each iteration make the code super easy to write as well as to understand, and finally it makes it really easy to add functionality for more symbols in the future if desired.
    
    MIRRORED LOGIC: The logic for translating braille to english is basically a mirror of translating english to braille, but there are enough differences where I thought it would be better to just create a different control flow for each one.
    
    SWITCH-CASE: If python 3.8 had switch statements I likely would have used that instead, since the architecture here more closely follows that of a switch-case construct than of an if-elif-else.
    
    [0] & [1]: For the braille to english translation I'm using the [0] and [1] structure as that is the way I decided to go about handling the fact that the symbols for a through j and 0 through 9 are the same.
    """

    input = " ".join(sys.argv[1:])
    output = ''
    state = ''
    
    
    if utils.is_valid_braille(input):
        braille_symbols = utils.chunk_braille_input(input)

        for symbol in braille_symbols:
            
            # If this is passed it will make sure not to print the symbol as text, and that the next letter that is printed is uppercased.
            if symbol == utils.english_braille_map['CAPITAL_FOLLOWS']:
                state = 'capital'

            # If this condition is passed it will make sure that all characters that follow are numbers.
            elif symbol == utils.english_braille_map['NUMBER_FOLLOWS']:
                state = 'number'

            # Condition to actually print the capital letter, triggered by the state
            elif state == 'capital':
                output += utils.english_braille_map[symbol][0].upper()
                state = 'character'

            # If we are in the state of printing numbers, and a no space has been reached, keep printing numbers
            # If a space is found, the state will go back to one of printing letters
            elif state == 'number' and symbol != utils.english_braille_map[' ']:
                output += utils.english_braille_map[symbol][1]

            # Otherwise, print letters as usual, keeping the state in character mode until circumstances change
            else:
                output += utils.english_braille_map[symbol][0]
                state = 'character'


    elif utils.is_valid_english(input):
        for char in input:

            # If the character is a capital letter, add to the output the 'capital follows' braille symbol as well as the braille symbol of the letter
            if utils.is_capital(char):
                output += utils.english_braille_map['CAPITAL_FOLLOWS'] + utils.english_braille_map[char.lower()]

            # If we are in the state of printing number symbols, and a no space has been reached, keep printing number symbols
            # If a space is found, the state will go back to one of printing letter symbols
            elif state == 'number' and char != ' ':
                output += utils.english_braille_map[char]

            # If we reach a number in the input, add to the output the 'number follows' braille symbol as well as the braille symbol of the number
            # and change the state to one of continuing to print number symbols
            elif utils.is_number(char):
                output += utils.english_braille_map['NUMBER_FOLLOWS'] + utils.english_braille_map[char]
                state = 'number'

            # Otherwise, print regular braille symbols as normal
            else:
                output += utils.english_braille_map[char]
                state = 'character'


    else:
        print("The input you submitted isn't in the correct format.")


    print(output)


if __name__ == "__main__":
    main()
