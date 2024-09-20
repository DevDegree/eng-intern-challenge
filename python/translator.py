import sys

text = " ".join(sys.argv[1:])

is_braille = True

output = []

#hashmap for alphabets to braille
alphabets = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": "......"
}

#hashmap for numbers to braille
numbers = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}
#hashmap for braille to alphabets
reverse_alphabets = {}
#hashmap for braille to numbers
reverse_numbers = {}

#creating the hashmaps by reversing the original
for key, val in alphabets.items():
    reverse_alphabets[val] = key

for key, val in numbers.items():
    reverse_numbers[val] = key

#set flags
isCapital = False
isNumber = False

#special char
capital_follows = ".....O"
number_follows = ".O.OOO"


#determine direction of translation
if (len(text) % 6) != 0:
    is_braille = False
else:
    for char in text:
        if char != "O" and char != ".":
            is_braille = False
            break

#braille to english
if is_braille:
    for i in range(0,len(text),6):
        curr = text[i:i+6]
        if curr == alphabets[" "]:
            isNumber = False
        if curr == capital_follows:
            isCapital = True
        elif curr == number_follows:
            isNumber = True
        else:
            if isCapital:
                output.append(reverse_alphabets[curr].upper())
                isCapital=False
            elif isNumber:
                output.append(reverse_numbers[curr])
            else:
                output.append(reverse_alphabets[curr])


#english to braille
isNumber = False
if not is_braille:
    for char in text:
        if char == " ":
            isNumber = False
        if char.isnumeric():
            if isNumber:
                output.append(numbers[char])
            else:
                output.append(number_follows+numbers[char])
                isNumber = True
        elif char.isupper():
            output.append(capital_follows+alphabets[char.lower()])
        else:
            output.append(alphabets[char])


#turn output list into string (required format) and print
print("".join(output))