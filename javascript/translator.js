const brailleToEnglish = {
    '......': ' ', '.O....': 'a', 'O.....': '1', 'OO....': 'b', 'OO.O..': '2',
    '.O.O..': 'c', '.OOO..': '3', '.OO...': 'd', '.OOOO.': '4', '.O.O.O': 'e',
    'O..O..': '5', 'OO.O..': 'f', 'OOO...': '6', 'OO....': 'g', 'OOO.O.': '7',
    'O.OO..': 'h', '.OOO..': '8', '.O.O..': 'i', '.OOOO.': '9', '.OOO..': 'j',
    'O....O': '0', 'O.O...': 'k', 'O.OO..': 'l', 'OO....': 'm', 'OO.O..': 'n',
    'O.O.O.': 'o', 'OOO...': 'p', 'OOOO..': 'q', 'O.OO.O': 'r', '.OO...': 's',
    '.OO.O.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O.O.OO': 'z'
};

const englishToBraille = Object.fromEntries(
    Object.entries(brailleToEnglish).map(([k, v]) => [v, k])
);

function brailleToEnglishTranslate(input) {
    let result = '';
    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i + 6);
        result += brailleToEnglish[brailleChar] || '';
    }
    return result;
}

function englishToBrailleTranslate(input) {
    return input.toLowerCase().split('').map(char => englishToBraille[char] || '').join('');
}

function translate(input) {
    if (input.match(/^[.O]+$/)) {
        return brailleToEnglishTranslate(input);
    } else {
        return englishToBrailleTranslate(input);
    }
}

// Get input from command line arguments
const input = process.argv.slice(2).join(' ');

if (input) {
    console.log(translate(input));
} else {
    console.log("Please provide input text or Braille pattern.");
}
