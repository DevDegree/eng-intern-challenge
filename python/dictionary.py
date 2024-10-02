import itertools
import string

def make_dictionary(elements):
    braille_combinations = list(itertools.product(elements, repeat=6))
    braille_combinations = [''.join(combination) for combination in braille_combinations]
    
    letters = list(string.ascii_lowercase)
    digits = list("0123456789")
    additional_char = ['C','D','N','.',',','?','!',':',';','-','/','<','>','(',')',' ']
    english_combinations = letters + digits + additional_char
    
    indices_dict = {        
        1: [16, None],
        3: [6,33],
        5: [15, None],
        7: [5, 32],
        8: [24, None],
        9: [13, None],
        11: [3, 30],
        12: [23, None],
        13: [12, None],
        15: [2, 29],
        17: [17, None],
        19: [7,34],
        20: [21, None],
        21: [11, None],
        22: [49, None],
        23: [1,28],
        24: [25, None],
        25: [14, None],
        27: [4, 31],
        28: [20, None],
        29: [10, None],
        31: [0,27],
        33: [19, None],
        34: [22, None],
        35: [9,26],
        37: [18, None],
        38: [47, None],
        39: [8,35],
        40: [38, None],
        41: [50, None],
        45: [46, None],
        46: [37, None],
        49: [42, None],
        50: [39, None],
        51: [43, None],
        52: [41, None],
        53: [44, None],
        55: [40, None],
        60: [45, None],
        62: [36, None],
        63: [51, None]
    }

    braille_to_english_dict = {}
    for key, value in indices_dict.items():
        braille_to_english_dict[braille_combinations[key]] = [english_combinations[value[0]]]
        if value[1] is not None:
            braille_to_english_dict[braille_combinations[key]] += [english_combinations[value[1]]]
    
    return braille_to_english_dict