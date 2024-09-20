import re
import sys
import json

# notes:
# O is where the dot is
# . is where there is no dot
# read left-to-right from top left
# capital follows = .....O
# number follows = .O.OOO

# load dictionary.json
with open("dictionary.json", "r") as file:
    dictionary = json.loads(file.read())

def translator(input) -> str:
    is_braille = "^(?:[O.]{6})+$"
    is_english_or_num = "[a-z]*[0-9]*[.|,|?|!|:|;|-|/|<|>|(|)|]*"

    if re.search(is_braille, input):
        # translate from values to keys in dictionary
        return braille_to_english(input)
    elif re.search(is_english_or_num, input):
        # translate from keys to values in dictionary
        return english_to_braille(input)

def braille_to_english(input) -> str:
    capital_follows = ".....O"
    number_follows = ".O.OOO"
    is_capital = False
    is_number = False
    # break input into string lengths of 6 in chars array
    chars = []
    curr_braille = ""
    for i in range(1, len(input)+1):
        if i % 6 == 0:
            curr_braille += input[i-1]
            chars.append(curr_braille)
            curr_braille = ""
        else:
            curr_braille += input[i-1]

    # iterate through each c in chars and match it to keys in dictionary
    eng_trans = dictionary["english_to_braille"]
    caps = dictionary["capitalized"]
    nums = dictionary["number_to_braille"]
    result = ""
    for c in chars:
        # check if capital follows
        if c == "......":
            is_number = False
        elif c == capital_follows:
            is_capital = True
            continue
        if is_capital:
            # find in eng_trans first
            cap_char = ""
            for k, v in eng_trans.items():
                if c == v:
                    cap_char = k
            result += caps[cap_char]
            is_capital = False
            continue
        # check if number follows
        if c == number_follows:
            is_number = True
            continue
        if is_number:
            for k, v in nums.items():
                if c == v:
                    result += k
                    break
            continue
        # else translate from eng_trans
        for k, v in eng_trans.items():
            if c == v:
                result += k
                break
        if result == "":
            result = english_to_braille(input)
    return result

def english_to_braille(input) -> str:
    capital_follows = ".....O"
    number_follows = ".O.OOO"
    is_capital = False
    is_number = False
    result = ""
    eng_trans = dictionary["english_to_braille"]
    caps = dictionary["capitalized"]
    nums = dictionary["number_to_braille"]
    for c in input:
        # check if capital
        if c in caps.values():
            for k, v in caps.items():
                if c == v:
                    c = k
                    break
            result += capital_follows
        # check if number
        if c == " ":
           is_number = False
        if is_number:
            result += nums[c]
            continue
        if c in nums.keys():
            is_number = True
            result += number_follows
            result += nums[c]
            continue
        # else translate from eng_trans
        result += eng_trans[c]
    return result


if __name__ == "__main__":
    input = " ".join(sys.argv[1:])
    print(translator(input))