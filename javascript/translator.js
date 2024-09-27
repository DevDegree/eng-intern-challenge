const brailleLetters = {
    'a':'O.....', 'b':'O.O...', 'c':'OO....', 'd':'OO.O..',
    'e':'O..O..', 'f':'OOO...', 'g':'OOOO..', 'h':'O.OO..',
    'i':'.OO...', 'j':'.OOO..', 'k':'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO',
};

const brailleNumbers = {
    '1':'O.....', '2':'O.O...', '3':'OO....', '4':'OO.O..', 
    '5':'O..O..', '6':'OOO...', '7':'OOOO..', '8':'O.OO..',
    '9':'.OO...', '0':'.OOO..',
}

const brailleSpecial = {
    'capital':'.....O', 'number':'.O.OOO', 'space': '......',
};

const reversedBrailleLetters = Object.fromEntries(Object.entries(brailleLetters).map(([key, value]) => [value, key]));
const reversedBrailleNumbers = Object.fromEntries(Object.entries(brailleNumbers).map(([key, value]) => [value, key]));
const reversedBrailleSpecial = Object.fromEntries(Object.entries(brailleSpecial).map(([key, value]) => [value, key]));

function checkIfBraille(text) {
    if (text.includes('O') || text.includes('.')){
        return true;
    }
    return false;
};

function brailleToEnglish(text) {
    let translation = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < text.length; i += 6) {
        let brailleCharacter = text.slice(i, i + 6);

        if (brailleCharacter === brailleSpecial['capital']) {
            isCapital = true;
            continue;
        }
        if (brailleCharacter === brailleSpecial['number']) {
            isNumber = true;
            continue;
        }
        if (brailleCharacter === brailleSpecial['space']) {
            translation += " ";
            isNumber = false;
            continue;
        }

        if (isNumber) {
            translation += reversedBrailleNumbers[brailleCharacter];
        }
        else if (isCapital) {
            translation += reversedBrailleLetters[brailleCharacter].toUpperCase();
            isCapital = false;
        }
        else {
            translation += reversedBrailleLetters[brailleCharacter];
        }
    }
    
    return translation;
};

function englishToBraille(text) {
    let translation = '';
    let isNumber = false;
    
    for (let i = 0; i < text.length; i++) {
        let englishCharacter = text[i];
        
        if (englishCharacter === ' ') {
            translation += brailleSpecial['space'];
        }
        else if (englishCharacter >= 'A' && englishCharacter <= 'Z') {
            englishCharacter = englishCharacter.toLowerCase();
            translation += brailleSpecial['capital'];
            translation += brailleLetters[englishCharacter];
        }
        else if (englishCharacter >= 'a' && englishCharacter <= 'z') {
            translation += brailleLetters[englishCharacter];
        }
        else {
            if (!isNumber) {
                isNumber = true;
                translation += brailleSpecial['number'];
            }

            translation += brailleNumbers[englishCharacter];
        }
    }
    return translation;
};

const inputText = process.argv.slice(2).join(' ');
if (inputText == '') {
    console.log('Error. No input provided');
}
else if (checkIfBraille(inputText)) {
    const translation = brailleToEnglish(inputText);
    console.log(translation);
}
else  {
    const translation = englishToBraille(inputText);
    console.log(translation);
}

