export const BRAILLE_TO_LETTER_MAP = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 
    'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', 
    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 
    'OO.OOO': 'y', 'O..OOO': 'z',
} as {[key: string]: string};

export const BRAILLE_TO_DIGIT_MAP = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', 
    '.OO...': '9', '.OOO..': '0',
} as {[key: string]: string};

export const BRAILLE_TO_SYMBOL_MAP = {
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/',
    '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')',
} as {[key: string]: string};

function reverseMap(map: {[key: string]: string}): {[key: string]: string} {
    return Object.entries(map).reduce((acc: {[key: string]: string}, [key, value]) => {
        acc[value] = key;
        return acc;
    }, {});
}

export const LETTER_TO_BRAILLE_MAP = {
    ...reverseMap(BRAILLE_TO_LETTER_MAP),
    ...reverseMap(BRAILLE_TO_DIGIT_MAP),
    ...reverseMap(BRAILLE_TO_SYMBOL_MAP),
};
