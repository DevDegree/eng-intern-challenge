import sys

pattern = {'a': 'O.....','b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..','f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...','j': '.OOO..','k': 'O...O.','l': 'O.O.O.','m': 'OO..O.',
    'n': 'OO.OO.','o': 'O..OO.','p': 'OOO.O.','q': 'OOOOO.','r': 'O.OOO.','s': '.OO.O.','t': '.OOOO.', 'u': 'O...OO',
   'v': 'O.O.OO','w': '.OOO.O', 'x': 'OO..OO','y': 'OO.OOO','z': 'O..OOO',  

    '1': 'O.....','2': 'O.O...','3': 'OO....','4': 'OO.O..','5': 'O..O..','6': 'OOO...','7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...','0': '.OOO..',

    'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO',

    '.':'..OO.O', ',':'..O...', '?':'..O.OO', '!':'..OOO.',':':'..OO..', ';':'..O.O.', '-':'....OO', 
    '/':'.O..O.', '<':'.OO..O', '>':'O..OO.', '(':'O.O..O',  ')':'.O.OO.',
  
    ' ': '......',  
  
}
# reverse the dictionary for braille -> english translation
reverse_pattern = {}
    
for key, value in pattern.items():
    if value in reverse_pattern:
            reverse_pattern[value].append(key)
    else:
            reverse_pattern[value] = [key]

#To check if the dictionary follows the correct pattern
# for key, pattern in pattern.items():
#         if len(pattern) != 6:
#             print(f"The pattern for '{key}' does not have a length of 6. It has length {len(pattern)}.")
        
#         else:
#             print(f"The pattern for '{key}' is valid.")


def detect_braille(word):
    for char in word:
        if char not in ['O', '.']:
            return False
    return True

#To split braille input into groups of 6
def seperate(s, size=6):
    chunks = []
    for i in range(0, len(s), size):
        chunks.append(s[i:i + size])
    return chunks 

def english_to_braille(word):
    first_number = True
    output = ''
    for char in word:
        if not first_number and not char.isnumeric(): #turn first_number on so nuber braille will be added for the start of the next number
            first_number= True                         
        if char.isnumeric() and first_number: 
            output += pattern['number'] #start reading numbers
            first_number = False
        if char.isupper():
            output += pattern["capital"]
            output += pattern[char.lower()]
        elif char in pattern:
            output+= pattern[char]
    return output

def braille_to_english(word):
    capital = False
    number = False
    decimal = False
    output = ''
    braille = seperate(word)
    if len(word)%6 != 0: #Infor user if their sentence is not a multiple of 6
        print("There are some extra/missing characters. Your sentence may not be translated properly.")
    for char in braille:
        
        if char in reverse_pattern:
            value = reverse_pattern[char]
            if value[0] == "capital":
                capital = True
            elif value[0] == "number":
                number = True
            elif value[0] == "decimal":
                decimal = False #just to avoid putting this down
            else:
                if value[0] == " ":
                    number = False
                if number:
                    try:
                        output += value[1]
                    except IndexError:
                        output += value[0] #if char is not a number. wont work for chars withe a value e.g e/5
                elif capital:
                    output+= value[0].upper()
                    capital = False
                else:
                    output+= value[0]
        else:
            print(f"{char} can not be translated")
     
    return output

def translate(word):
    if not detect_braille(word):
        print(english_to_braille(word))
    else:
        print(braille_to_english(word))

# print(reverse_pattern)
def main():
    text = " ".join(sys.argv[1:]) #get cmd line arguments.
    translate(text)

if __name__ == "__main__":
    main()

