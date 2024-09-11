# Reverse the mapping for converting Unicode Braille to O/. patterns
BRAILLE_UNICODE_TO_DOTS = {
    chr(10241): "O.....",  # ⠁
    chr(10243): "O.O...",  # ⠃
    chr(10249): "OO....",  # ⠉
    chr(10265): "OO.O..",  # ⠙
    chr(10257): "O..O..",  # ⠑
    chr(10251): "OOO...",  # ⠋
    chr(10267): "OOOO..",  # ⠛
    chr(10259): "O.OO..",  # ⠓
    chr(10250): ".OO...",  # ⠊
    chr(10266): ".OOO..",  # ⠚
    chr(10245): "O...O.",  # ⠅
    chr(10247): "O.O.O.",  # ⠇
    chr(10253): "OO..O.",  # ⠍
    chr(10269): "OO.OO.",  # ⠝
    chr(10261): "O..OO.",  # ⠕
    chr(10255): "OOO.O.",  # ⠏
    chr(10271): "OOOOO.",  # ⠟
    chr(10263): "O.OOO.",  # ⠗
    chr(10254): ".OO.O.",  # ⠎
    chr(10270): ".OOOO.",  # ⠞
    chr(10277): "O...OO",  # ⠥
    chr(10279): "O.O.OO",  # ⠧
    chr(10298): ".OOO.O",  # ⠺
    chr(10285): "OO..OO",  # ⠭
    chr(10301): "OO.OOO",  # ⠽
    chr(10293): "O..OOO",  # ⠵
    chr(10272): ".....O",  # ⠼ (Capital Follows)
    chr(10300): ".O.OOO",  # ⠼ (Number Follows)
    chr(10288): "......",
    " ": "......"   # ⠀ (Space)
}

def braille_unicode_to_dots(braille_string):
    """Convert a Braille Unicode string to a dots representation with 'O' and '.'."""
    result = ""
    for char in braille_string:
        if char in BRAILLE_UNICODE_TO_DOTS:
            result += BRAILLE_UNICODE_TO_DOTS[char]
        else:
            print(f"Unrecognized Braille character: {char}")
            #should not happen (never) given this program word constraint
            result += "UNRECOGNIZED"
    return result

# Example usage
# braille_input = '⠼⠙⠃'  # This is the Braille representation for "42"
# converted = braille_unicode_to_dots(braille_input)
# print(converted)  # Output should be '.....O.OO.O..O.O...'

# we reverse mapping from dot patterns ('O' and '.') to braille unicode characters
DOTS_TO_BRAILLE_UNICODE = {v: k for k, v in BRAILLE_UNICODE_TO_DOTS.items()}

def dots_to_braille_unicode(dots_string):
    # let's ensure the input is processed in groups of 6 characters to match Braille dots
    braille_unicode = ""
    for i in range(0, len(dots_string), 6):
        dot_pattern = dots_string[i:i+6]
        if dot_pattern in DOTS_TO_BRAILLE_UNICODE:
            braille_unicode += DOTS_TO_BRAILLE_UNICODE[dot_pattern]
        else:
            print(f"Unrecognized dot pattern: {dot_pattern}")
            braille_unicode += "�"  # unicode replacement character for unrecognized patterns - should never be reached
    return braille_unicode