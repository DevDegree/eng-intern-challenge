import sys

texttobraille_dict = {
'a':'O.....','b':'O.O...','c':'OO....','d':'OO.O..',
'e':'O..O..','f':'OOO...','g':'OOOO..','h':'O.OO..',
'i':'.OO...','j':'.OOO..','k':'O...O.','l':'O.O.O.',
'm':'OO..O.','n':'OO.OO.','o':'O..OO.','p':'OOO.O.',
'q':'OOOOO.','r':'O.OOO.','s':'.OO.O.','t':'.OOOO.',
'u':'O...OO','v':'O.O.OO','w':'.OOO.O','x':'OO..OO',
'y':'OO.OOO','z':'O..OOO','1':'O.....','2':'O.O...',
'3':'OO....','4':'OO.O..','5':'O..O..','6':'OOO...',
'7':'OOOO..','8':'O.OO..','9':'.OO...','0':'.OOO..',
'number':'.O.OOO','capital':'.....O',' ':'......',
}

brailletoalpha_dict = {
'O.....':'a','O.O...':'b','OO....':'c','OO.O..':'d',
'O..O..':'e','OOO...':'f','OOOO..':'g','O.OO..':'h',
'.OO...':'i','.OOO..':'j','O...O.':'k','O.O.O.':'l',
'OO..O.':'m','OO.OO.':'n','O..OO.':'o','OOO.O.':'p',
'OOOOO.':'q','O.OOO.':'r','.OO.O.':'s','.OOOO.':'t',
'O...OO':'u','O.O.OO':'v','.OOO.O':'w','OO..OO':'x',
'OO.OOO':'y','O..OOO':'z', '......':' '
}

brailletonum = {
'O.....':'1','O.O...':'2','OO....':'3','OO.O..':'4',
'O..O..':'5','OOO...':'6','OOOO..':'7','O.OO..':'8',
'.OO...':'9','.OOO..':'0'
}

#function to convert english to braille
def EngtoBraille(text):
    braille_text = []
    is_number = False

    for char in text:
        #checks to see if its a number and flag it if its the first instance 
        if char.isdigit() and not is_number:
            braille_text.append(texttobraille_dict['number'])
            is_number = True
        elif not char.isdigit():
            is_number = False

        #checks to see if the character is a Uppercase
        if char.isupper():
            braille_text.append(texttobraille_dict['capital'])

        braille_text.append(texttobraille_dict[char.lower()])

    return ''.join(braille_text)

#function to convert braille to english
def BrailletoEng(brailleword):
    chunks = []
    text = []
    is_number = False
    is_capital = False

    #splits the braille into 6 characters for each possible instance and puts it in array
    #if it cant be perfectly split into 6 that means the braille is not possible  
    for i in range(0, len(brailleword), 6):
        chunk = brailleword[i:i + 6]
        chunks.append(chunk)
    
    #iterates thru the array 
    for cha in chunks:
        #checks for number sign and flags the number
        if cha == '.O.OOO':  
            is_number = True
            continue
        #checks for capital sign 
        elif cha == '.....O':  
            is_capital = True
            continue
        
        #looks at braille to number dictionary if its a number
        if is_number and cha in brailletonum:
            text.append(brailletonum[cha])
        #looks at the braille to alphabet and space dictionary 
        elif cha in brailletoalpha_dict:
            #makes the letter uppercase if the capital flag is true 
            letter = brailletoalpha_dict[cha].upper() if is_capital else brailletoalpha_dict[cha]
            text.append(letter)
        
        #if theres a space make the number flag zero
        if cha == '......':
            is_number = False
        #makes the capital flag negative 
        is_capital = False

    return ''.join(text)

#function to detect if its braille or text 
def detect_input_type(input_string):
    # Check if the input is likely Braille
    if all(char in '.O' for char in input_string) and len(input_string) % 6 == 0:
        return "braille"
    else:
        return "english"
    
def main():
    #makes sure the arguments being placed on the command line
    if len(sys.argv) < 2:
        print("Usage: python script.py <string>")
        sys.exit(1)

    # Join all command-line arguments into a single string due to possible spaces for the texts 
    input_string = ' '.join(sys.argv[1:])
    input_type = detect_input_type(input_string)

    if input_type == "braille":
        result = BrailletoEng(input_string)
    elif input_type == "english":
        result = EngtoBraille(input_string)

    print(result)

if __name__ == "__main__":
    main()
