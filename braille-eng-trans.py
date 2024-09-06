import sys

######## ENG <-> BRAILLE Translation Lookups ########

letter_dict = [
    ('a', "0....."),
    ('b', "0.0..."),
    ('c', "00...."),
    ('d', "00.0.."),
    ('e', "0..0.."),
    ('f', "000..."),
    ('g', "0000.."),
    ('h', "0.00.."),
    ('i', ".00..."),
    ('j', ".000.."),
    ('k', "0...0."),
    ('l', "0.0.0."),
    ('m', "00..0."),
    ('n', "00.00."),
    ('o', "0..00."),
    ('p', "000.0."),
    ('q', "00000."),
    ('r', "0.000."),
    ('s', ".00.0."),
    ('t', ".0000."),
    ('u', "0...00"),
    ('v', "0.0.00"),
    ('w', ".000.0"),
    ('x', "00..00"),
    ('y', "00.000"),
    ('z', "0..000"),
    (' ', "......")
]

digit_dict = [
    ('1', "0....."),
    ('2', "0.0..."),
    ('3', "00...."),
    ('4', "00.0.."),
    ('5', "0..0.."),
    ('6', "000..."),
    ('7', "0000.."),
    ('8', "0.00.."),
    ('9', ".00..."),
    ('0', ".000..")
]

cap_follows = ".....0"
num_follows = ".0.000"

######## ENG <-> BRAILLE Translation Lookups ########

# Reading input as one big string (including spaces)
input_str = ""
for i in range(1, len(sys.argv)):
    if (i > 1):
        input_str = input_str + " "
    input_str = input_str + str(sys.argv[i])

str(sys.argv[1])

# Deciding translation direction
trans_to_eng = False
if '.' in input_str:
    trans_to_eng = True

# Splitting into chunks
if trans_to_eng:
    chunk_size = 6
else:
    chunk_size = 1
chunks = []
for i in range(0, len(input_str), chunk_size):
    chunks.append(input_str[i:i+chunk_size])


# Translates c to eng if trans_to_eng=True, translates to braille otherwise
def trans_char(c, is_num=False):
    dict_to_check = letter_dict
    if is_num:
        dict_to_check = digit_dict

    for (eng, braille) in dict_to_check:
        if trans_to_eng and c == braille:
            return eng
        if not trans_to_eng and c == eng:
            return braille


# Moving through chunks  -- creating output string
output_str = ""
capitalize = False
numberize = False
for chunk in chunks:
    if chunk_size == 6:  # converting braille -> eng
        if capitalize:
            output_char = trans_char(chunk).capitalize()
            capitalize = False
        elif numberize:
            output_char = trans_char(chunk, is_num=True)
            numberize = False
        elif chunk == cap_follows:
            capitalize = True
            continue
        elif chunk == num_follows:
            numberize = True
            continue
        else:
            output_char = trans_char(chunk)
    else:  # converting eng -> braille
        if chunk.isupper():
            output_char = cap_follows + trans_char(chunk.lower())
        elif chunk in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            output_char = num_follows + trans_char(chunk, is_num=True)
        else:
            output_char = trans_char(chunk)

    output_str = output_str + output_char

# outputting results
print(output_str)