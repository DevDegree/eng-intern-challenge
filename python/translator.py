import sys

def main():
    #extract the input words
    input = sys.argv[1:]
    try:
        word = input[0]
    except:
        print("No input provided")
    braille_to_eng = False       
    if (len(word) % 6 == 0) and '.' in word:
        #every Braille world conatains '.' but the English alphabet in
        #this challenge does not so if we find '.' it is a Braille word
        braille_to_eng = True 
    #read text from map.txt file
    map_file = open("map.txt","r")
    map_text = []
    for line in map_file:
        map_text.append(line.strip())
    map_file.close()
    #Braille to English conversion
    if(braille_to_eng):
        braille_map = {}
        for line in map_text:
            eng_word, braille_word = line.split(' ')
            braille_map[braille_word] = eng_word
        output = ""
        capital = False
        number = False
        for i in range(0, len(word), 6):
            try:
                english_word = braille_map[word[i:i+6]]
            except:
                print("Unrecognized Braille input")
            if english_word == "space":
                if number == True:
                    number = False
                else:
                    output += " "
            elif english_word == "number":
                number = True
            elif english_word == "capital":
                capital = True
            else:
                char = english_word
                if capital:
                    char = char.upper()
                    capital = False
                if number:
                    char = "0" if (char == 'j') else str(ord(char) - ord('a')+1)
                output += char
            if capital and number: #no defined behaviour 
                raise Exception("Unrecognized Braille input")
        print(output)
    #English to Braille Conversion
    else:
        english_map = {}
        for line in map_text:
            eng_word, braille_word = line.split(' ')
            english_map[eng_word] = braille_word
        output = ""
        number = False
        for i in range(len(input)):
            word = input[i]
            for c in word:
                if not c.isalnum():
                    raise Exception("Unrecognized English symbol (only alphanumerics allowed)")
                if c.isdigit():
                    char = 'j' if (int(c) == 0) else chr(int(c)+ord('a')-1)
                    if not number:
                        output += english_map["number"]
                        number = True
                    output += english_map[char]
                else:
                    if number:
                        output += english_map["space"]
                        number = False
                    if c.upper() == c: #letter is capitalized
                        output += english_map["capital"]
                        output += english_map[c.lower()]
                    else:
                        output += english_map[c]
            if i != len(input)-1:
                output += english_map["space"]
        print(output)

if __name__ == "__main__":
    main()