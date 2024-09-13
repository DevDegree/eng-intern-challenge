
def isBraille(inp_text: str):
    braille_char_set = {"O", "."}

    is_valid_braille = True

    # validate length
    if len(inp_text) % 6 != 0:
        is_valid_braille = False

    if is_valid_braille:
        # validate characters
        for char in inp_text:
            if char not in braille_char_set:
                is_valid_braille = False
    return is_valid_braille



# main guard
if __name__ == "__main__":
    print(isBraille(""))
