# import IO

# add maps to convert english to braille
# reverse the map for braille to english?


#main function
'''
receive string from argument
determine if string is braille or english
    braille: if string is all O or .
    english: else

call one of:
    braille to english
    english to braille

print result to terminal
'''

#braille to english


#english to braille


'''
edge cases
    english encountered in braille string?
        translate entire string as english
    incomplete braille letter at end of string
        ignore trailing 1-5 characters (6 would be another braille letter)
    inalid braille letter found in string
        ignore, print nothing for this letter
    unrecognized/invalid english letter found in string
        ignore, print nothing for this letter
    empty string as argument
        print nothing
    forgetting to put space-flag after numbers conclude (invalid braille to english)
        treat as usual braille (if letters A to J, translate into numbers - else, invalid)
'''

'''
other notes: overall
    global vars for flags (capitals/numbers/decimals) and the chunk size, 6
    use a dict to append substrings to the end_translation string and then join it all together at the end

other notes: english to braille
    use bools to track capitals/numbers/decimals
    slice the string in chunks of 6 (i:i+6)

other notes: braille to english
    just read in the next char, check for flags in the char (capitals/numbers/decimals)
    append accordingly
'''