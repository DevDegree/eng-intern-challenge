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
}

# In the range of letters ["k", ..., "t"], the ith letter can be related to the ith letter in the range ["a", ..., "j"]:
rangeTenTwenty = [chr(i) for i in range(97 + 10, 97+20)] # the ten next letters after j (after the base set)
for letter in rangeTenTwenty:
    base_braille = list(table[chr(ord(letter) - 10)]) # get the braille rep of the corresponding letter in the base set
    base_braille[4] = 'O' # the rule relating the letters in the base set to those in rangeTenTwenty is that the '.' at index 4 is replaced by a 'O'
    table[letter] = "".join(base_braille)

# Same concept for the letters ["u", ..., "z"] 
rangeTwentyTwentySix = [chr(i) for i in range(97 + 20, 97+26)] # the six next letters after t 
for letter in rangeTwentyTwentySix:
    base_braille = list(table[chr(ord(letter) - 10)]) # get the braille rep of the corresponding letter in the base set
    base_braille[5] = 'O' # '.' at index 5 is replaced by a 'O'
    table[letter] = "".join(base_braille)

table['w'] = ".OOO.O" # an exception to the rule we came up with

print(table)