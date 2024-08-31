import sys

# numbers -> the number of colored dots 
# bools -> if there are any occurences of colored dots on the last two dots
# cf -> caps found 
# nf -> number found 
# df -> decmail found 
bradic = {
    0:{True: {}, False: {" ": "...."}}, 
    1:{True: {"cf":".....O"}, False: {",":"..O.", "a": "O...", "1":"O..."}}, 
    2:{True: {"k":"O...O.", "df": ".O...O", ";":"..O.O.", "-":"....OO", "/":".O..O."}, False: {":":"..OO","9":".O.O", "2":"O.O.", "3":"OO..","5":"O..O", "b":"O.O.", "c":"OO..", "e":"O..O", "i":".O.O."}}, 
    3:{True: {".":"..OO.O", "<":".OO..O", ">":"O.O..O", "(":"O.O..O", ")":".O.OO.", "?":"..0.00", "!": "..OOO.", "l":"O.O.O.", "m":"OO..O.", "s":".OO.O.", "u":"O...OO", "o":"O..OO." }, False: {"0":".OOO", "8":"O.OO","6": "OOO.","4":"OO.O", "d":"OO.O", "f":"OOO.", "h":"O.OO", "j":".OOO"}}, 
    4:{True: {"n": "OO.OO.", "p": "OOO.O.", "nf":".O.OOO", "r": "O.OOO.", "t":".OOOO.", "v":"O.O.OO", "w":".OOO.O", "x":"OO..OO","z":"O..OOO"} , False: {"g":"OOOO", "7":"OOOO"}}, 
    5:{True: {"q":"OOOOO.", "y":"OO.OOO"}, False: {}}, 
}

def identify(userSent):   
    """
    This function identifies which conversion is needed
    and checks that the users input is valid, if invalid 
    it re promts the user for another answer 

    Args:
        userSent (string): what the user has typed in to the terminal
    """
    valid = True
    while(valid): 
        if not isinstance(userSent, str):
            userSent = input("Please enter a string, as you have failed to provide one: ")            
        else: 
            valid = False 
        
    if all(char in {'O', '.'} for char in userSent) and len(userSent) % 6 == 0:
        btoe(userSent)
        
    else:
        etob(list(userSent))

def btoe(userSent):
    """
    loops through each braille letter, checks the num of colored O and if there are 
    any O in the bottom. Based on that an index is found in the bradic and items are 
    then checked based on any flagged requirements until the correct letter is found

    Args:
        userSent (list): a list of strings with a length of 6 containing each braille 
    """
    num, dec, cap = False , False, False 
    strs = []
    for i in range(0, len(userSent), 6): 
        x= list(userSent[i:i+6])   
        amount = x.count("O")
        status = False if x[-2:].count("O") == 0 else True
        for key, value in bradic[amount][status].items():
            x = x if status else x[:4]
            if value == ''.join(x) and not num and not key.isnumeric():
                cap, num = (True, cap)[key != "cf"], (True, num)[key != "nf"]
                if key in ["cf", "nf", "df"]: break
                else:   
                    if cap:
                        cap = False
                        key = (chr(ord(key) - 32))
                    else: 
                        cap = False
                strs.append(str(key))
                break 
            elif value == ''.join(x) and num and key.isnumeric(): 
                strs.append(str(key))
            elif value == ''.join(x) and num and key == ' ':
                num = False
                strs.append(str(key))
    print(''.join(strs))
                
def inner(temp, p):
    """
    Finds in the temp dictonary the braille character that was needed 

    Args:
        temp (dictonary): all possible key pairs 
        p (string): character that we need translation for

    Returns:
        bool or string: either indacting nothing was found or the braille that was found 
    """
    if p in temp:
        if len(temp[p]) == 4: 
            final = temp[p]+ '..'
        else: 
            final = temp[p]
        return final
    else:
        return False
    
def etob(userSent):
    """
    loops through the global table dictonary and stores it as temp as all possible entries.
    checks if there are any flags that need to be set up in braille, if not calls on the 
    inner function to find the correct braille letter and stores it as a string to be returned. 

    Args:
        userSent (string): what the user wants to translte to braille 
    """
    returns = ""
    temp = {}
    for level in bradic.values():
        for state, mappings in level.items():
            temp.update(mappings)

    numbo = False
    for p in userSent:
        if p.isupper():
            p = chr(ord(p)+ 32)
            returns += inner(temp, "cf")
        if p.isnumeric() and numbo == False: 
            numbo = True
            returns += inner(temp, "nf") 
        if numbo and p == " ": 
            numbo = False
        if inner(temp, p) == False: 
            pass
        else: 
            returns += inner(temp, p)
    
    print(returns)


def main(): 
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_string>")
        sys.exit(1) 
        
    user_input = ' '.join(sys.argv[1:])    
    identify(user_input)    

if __name__ == "__main__":
    main()
