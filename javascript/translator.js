const englishToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOOOO.', 'q': 'OOOOOO', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', 
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 'capital': '.....O', 
    'number': '.O.OOO', ' ': '......',
};

const brailleToEnglish = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOOOO.': 'p', 'OOOOOO': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '.O.OOO': 'number', '.....O': 'capital'
};

function translate(input) {
    if (input.includes('O') || input.includes('.')) {
        return brailleToEnglishTranslation(input);
    } else {
        return englishToBrailleTranslation(input);
    }
}

function englishToBrailleTranslation(input) {
    let result = '';
    let numberMode = false;
    
    for (let char of input) {
        if (char.match(/[A-Z]/)) {
            result += englishToBraille['capital'];
            char = char.toLowerCase();
        }
        
        if (char.match(/\d/)) {
            if (!numberMode) {
                result += englishToBraille['number'];
                numberMode = true;
            }
        } else {
            numberMode = false;
        }
        
        result += englishToBraille[char];
    }
    
    return result;
}

function brailleToEnglishTranslation(input) {
    let result = '';
    let numberMode = false;
    let capitalizeNext = false;

    const numberMap = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
        'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
    };

    

    for (let i = 0; i < input.length; i += 6) {
        let brailleChar = input.substr(i, 6);

        if (brailleChar === '.....O') {
            capitalizeNext = true;
            numberMode = false; 
        } else if (brailleChar === '.O.OOO') {
            numberMode = true;
        } else {
            let translatedChar = brailleToEnglish[brailleChar];

            if (capitalizeNext) {
                translatedChar = translatedChar.toUpperCase();
                capitalizeNext = false;
            }

            if (numberMode) {
                translatedChar = numberMap[translatedChar] || translatedChar;
            }

            result += translatedChar;
        }
    }

    return result;
}

const input = process.argv.slice(2).join(' ');
console.log(translate(input));
