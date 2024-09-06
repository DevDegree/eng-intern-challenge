def convert_to_braille(text_input):
    code_mapping = {
        "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D", "O..O..": "E", 
        "OOO...": "F", "OOOO..": "G", "O.OO..": "H", ".OO...": "I", ".OOO..": "J", 
        "O...O.": "K", "O.O.O.": "L", "OO..O.": "M", "OO.OO.": "N", "O..OO.": "O", 
        "OOO.O.": "P", "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T", 
        "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X", "OO.OOO": "Y", 
        "O..OOO": "Z", ".O.OOO": "NUMBER_MARK", ".....O": "CAPITAL_MARK", "......": "SPACE"
    }
    
    reverse_mapping = {value: key for key, value in code_mapping.items() if value not in ["NUMBER_MARK", "CAPITAL_MARK"]}
    output_sequence = []
    
    for char in text_input:
        if char.isdigit():
            output_sequence.append(".O.OOO")
            for num in char:
                output_sequence.append(reverse_mapping[num])
        elif char.isupper():
            output_sequence.append(".....O")
            output_sequence.append(reverse_mapping[char.upper()])
        else:
            output_sequence.append(reverse_mapping[char.lower()])
    
    return ''.join(output_sequence)

def handle_translation(input_sequence):
    if input_sequence[0] in ['O', '.']:
        return convert_to_english(input_sequence)
    else:
        return convert_to_braille(input_sequence)
