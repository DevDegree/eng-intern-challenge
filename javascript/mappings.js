import { CONFIG } from './config.js';
export const punctuationMapping = {
    ',': '..O...', '.': '..OO..', '?': '..O.O.', '!': '..OO.O',
    ':': '..OO..', ';': '..O..', '-': '..OO..', '(': '.O.O..',
    ')': '.O..O.', ' ': '......', '/': '.O..O.', '<': '.O.O..',
    '>': '.O.O.O',
};

export const brailleToEnglishMap = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
    'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z', '.O.OOO': 'number', '.....O': 'capital',
    '......': ' ',
};

export const englishToBrailleMap = Object.fromEntries(
    Object.entries(brailleToEnglishMap).map(([k, v]) => [v, k])
);

for (let i = 0; i <= 9; i++) {
    englishToBrailleMap[i.toString()] = englishToBrailleMap[CONFIG.NUMBER_CHARS[i]];
}