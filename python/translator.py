#iImport Libraries
import sys  #import for cmd-line interface

#use a hash map to map letters/char to 

#toBraille
engToBraille = {
    "A":"O.....",
    "B" : "O.O...", 
    "C" : "OO....",
    "D" : "OO.O..", 
    "E" : "O..O..",
    "F" : "OOO...",
    "G" : "OOOO..",
    "H" : "O.OO..",
    "I" : ".OO...", 
    "J" : ".OOO..",
    "K" : "O...O.",
    "L" : "O.O.O.",
    "M" : "OO..O.",
    "N" : "OO.OO.",
    "O" : "O..OO.",
    "P" : "OOO.O.",
    "Q" : "OOOOO.",
    "R" : "O.OOO.",
    "S" : ".OO.O.",
    "T" : ".OOOO.",
    "U" : "O...OO",
    "V" : "O.O.OO",
    "W" : ".OOO.O",
    "X" : "OO..OO",
    "Y" : "OO.OOO",
    "Z" : "O..OOO",
    "1" : "O.....",
    "2" : "O.O...",
    "3" : "OO....",
    "4" : "OO.O..",
    "5" : "O..O..",
    "6" : "OOO...",
    "7" : "OOOO..",
    "8" : "O.OO..",
    "9" : ".OO...",
    "0" : ".OOO..  ",
    "cap" : ".....O",
    "num" : ".O.OOO",
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
    " " : "......"
}

#toEng
brailleToEng = {
    "O....." : ["a", "A", "1"],
    "O.O..." : ["b", "B", "2"], 
    "OO...." : ["c", "C", "3"],
    "OO.O.." : ["d", "D", "4"], 
    "O..O.." : ["e", "E", "5"],
    "OOO..." : ["f", "F", "6"],
    "OOOO.." : ["g", "G", "7"],
    "O.OO.." : ["h", "H", "8"],
    ".OO..." : ["i", "I", "9"], 
    ".OOO.." : ["j", "J", "O"],
    "O...O." : ["k", "K"],
    "O.O.O." : ["l", "L"],
    "OO..O." : ["m", "M"],
    "OO.OO." : ["n", "N"],
    "O..OO." : ["o", "O", ">"],
    "OOO.O." : ["p", "P"],
    "OOOOO." : ["q", "Q"],
    "O.OOO." : ["r", "R"],
    ".OO.O." : ["s", "S"],
    ".OOOO." : ["t", "T"],
    "O...OO" : ["u", "U"],
    "O.O.OO" : ["v", "V"],
    ".OOO.O" : ["w", "W"],
    "OO..OO" : ["x", "X"],
    "OO.OOO" : ["y", "Y"],
    "O..OOO" : ["z", "Z"],
    ".....O" : ["cap"],
    ".O...O" : ["dec"],
    ".O.OOO" : ["num"],
    "..OO.O" : ["."],
    "..O..." : [","],
    "..O.OO" : ["?"],
    "..OOO." : ["!"],
    "..OO.." : [":"],
    "..O.O." : [";"],
    "....OO" : ["-"],
    ".O..O." : ["/"],
    ".OO..O" : ["<"],
    "O.O..O" : ["("], 
    ".O.OO." : [")"],
    "......" :  [" "]
}
#translate to lists because multiple characters use same braille char

class transl:
    
    word = None

    def __init__(self, x):
        self.word = x

    def toEng(self):

        engWord = ""
        check = "" #checks braille letters in increments of 6

        cap = False
        # dec = False
        nums = False

        for i in range(0, len(self.word)):
            check += self.word[i]           
            if(len(check) == 6):

                if check in brailleToEng:
                    # check first for cap/dec/num
                    
                    test = brailleToEng[check][0]
                    if(test == "cap"):
                        cap = True
                        check = ""
                        continue
                    # elif(test == "dec"):
                    #     dec = True
                    #     continue
                    elif(test == "num"):
                        nums = True
                        check = ""
                        continue
                    elif(test == " "):
                        nums = False
                        engWord += brailleToEng[check][0]
                        check = ""
                        continue

                    #add diff ones
                    if(cap):
                        engWord += brailleToEng[check][1]
                        cap = False
                    elif(nums):
                        engWord += brailleToEng[check][2]
                    else:
                        engWord += brailleToEng[check][0]

                    
                check = ""
                    
        return engWord


    def toBr(self):

        brWord = ""
        num = False
        #32 diff btw cap and low in ASCII

        for i in range(0,len(self.word)):
            #cap
            test = self.word[i]
            check = ord(test)

            #upper case
            if(check >= 65 and check <= 90):
                brWord += engToBraille["cap"]
                brWord += engToBraille[test]
            
            #numbers
            elif(check >= 48 and check <= 57):
                if (not num):
                    brWord += engToBraille["num"]
                    num = True
                brWord += engToBraille[test]

            #lower-case
            elif(check >= 97 and check <= 122):
                brWord += engToBraille[test.upper()]

            #space
            elif(test == " "):
                num = False
                brWord += engToBraille[" "]


            #everything else
            else:
                brWord += engToBraille[test]

        return brWord




 
def main():
    
    word = " ".join(sys.argv[1:])
    t = transl(word)
    x = ""
    #check if braille or eng
    if(word[0:6] in brailleToEng):
        x = (t.toEng())
    else:
        x = (t.toBr())
    
    print(x)
    return x

    

if __name__ == "__main__":
    main()
