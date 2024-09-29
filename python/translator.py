# For simplicity, we will consider each braille character to be a 6-dimensional row vector
# We start by building an English - Braille lookup table.

# We note that the letter A to J form the "base set"
table = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
}

# In the range of letters ["k", ..., "t"], the ith letter can be related to the ith letter in the range ["a", ..., "j"]:
rangeTenTwenty = [chr(i) for i in range(ord('k'), ord('t') + 1)] # the ten next letters after j (after the base set)
for letter in rangeTenTwenty:
    base_braille = list(table[chr(ord(letter) - 10)]) # get the braille rep of the corresponding letter in the base set
    base_braille[4] = 'O' # the rule relating the letters in the base set to those in rangeTenTwenty is that the '.' at index 4 is replaced by a 'O'
    table[letter] = "".join(base_braille)

# Same concept for the letters ["u", ..., "v"] 
rangeTwentyTwentySix = [chr(i) for i in range(ord('u'), ord('z') + 1)] # the two next letters after t 
offset = 10

for letter in rangeTwentyTwentySix:
    if letter == 'w':
        table[letter] = ".OOO.O" # w is an exception to the rule we came up with
        offset = 11 # the bases of the letters after w are then offset by 1 more 
        continue

    base_braille = list(table[chr(ord(letter) - offset)]) # get the braille rep of the corresponding letter in the base set
    base_braille[5] = 'O' # '.' at index 5 is replaced by a 'O'
    table[letter] = "".join(base_braille)


# add the digits
numberFlag = ".O.OOO" # when met, everything that follows is a number UNTIL space pattern
decimalFlag = ".O...O" # signifies a fractional part coming up; continues until space is met. 
for digit in range(10):
    if digit == 0:
        table[str(digit)] = table["j"]
        continue

    table[str(digit)] = table[chr(ord('a') + digit - 1)]

# add capital letters
capitalFlag = ".....O" # when met, only next letter is capital
for ascii in range(ord('a'), ord('z') + 1):
    table[chr(ascii).upper()] = capitalFlag + table[chr(ascii)]


