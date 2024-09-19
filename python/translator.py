
# High-level idea:
# 
# Braille follows this set of rules:
# - Each "character" has length 6
# - Each "character" is composed solely from "O" or "."
# - There is a defined alphabet, BUT:
#       - Some special instructions, such as "capitalize" / "number" / "decimal" exist
# 
# 
# 
# Observations:
# Problem is broken up into two steps; classifying and translating.
# 
# To classify:
# - Can probably use regex to check if strings match the "O" or "." requirements
# - Can also assert that inputString.length() % 6 == 0 to match braille length
# 
# ===================================================================================
# 
# To translate (FROM BRAILLE):
# - Can tokenize each braille character
# - Can check the edge cases (capitalize, number, decimal)
#       - Handle it
# - Can reference a dictionary to replace the characters
# 
# POTENTIAL EDGE CASE: The string "OOOOOO" passes the regex and length requirement,
#                      but would still be an English string, because that character isn't in the Braille alphabet.
#                      => if token not in Braille dict, translate the input string from English -> Braille
# 
# 
# * To translate (FROM ENGLISH):
# - For each char, check:
#       - is number or decimal
#       - is capital
# - Apply transformation rules
# - Replace with braille alphabet entry
# 
# ===================================================================================
#