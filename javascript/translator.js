const brailleMap = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..', 'F': 'OOO...', 'G': 'OOOO..',
    'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.', 'P': 'OOO.O.', 'Q': 'OOOOO.',
    'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO', 'Z': 'O..OOO', 'UPPERCASE':
        '.....O', ' ': '......'
};

const brailleNumsMap = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7':
        'OOOO..', '8': 'O.OO..', '9': '.OO...', 'NUM_INDICATOR': '.O.OOO'
};

function englishToBraille(textInput) {
    let brailleResult = '';
    let isNumberMode = false;

    for (let index = 0; index < textInput.length; index++) {
        let currentChar = textInput[index];
        if (currentChar >= 'A' && currentChar <= 'Z') {
            brailleResult += brailleMap['UPPERCASE'] + brailleMap[currentChar];
        } else if (currentChar >= '0' && currentChar <= '9') {
            if (!isNumberMode) {
                brailleResult += brailleNumsMap['NUM_INDICATOR'];
                isNumberMode = true;
            }
            brailleResult += brailleNumsMap[currentChar];
        } else if (brailleMap[currentChar]) {
            isNumberMode = false;
            brailleResult += brailleMap[currentChar];
        } else {
            isNumberMode = false;
            brailleResult += brailleMap[currentChar.toUpperCase()] || '';
        }
    }

    return brailleResult;
}

const reverseBrailleLetters = Object.keys(brailleMap).reduce((acc, key) => {
    acc[brailleMap[key]] = key;
    return acc;
}, {});

const reverseBrailleNumbers = Object.keys(brailleNumsMap).reduce((acc, key) => {
    acc[brailleNumsMap[key]] = key;
    return acc;
}, {});

function brailleToEnglish(brailleInput) {
    let brailleSegments = brailleInput.match(/.{1,6}/g);
    let textResult = '';
    let isUppercase = false;
    let isNumMode = false;

    brailleSegments.forEach(segment => {
        if (segment === brailleMap['UPPERCASE']) {
            isUppercase = true;
        } else if (segment === brailleNumsMap['NUM_INDICATOR']) {
            isNumMode = true;
        } else if (isNumMode && reverseBrailleNumbers[segment]) {
            textResult += reverseBrailleNumbers[segment];
        } else if (isUppercase) {
            textResult += reverseBrailleLetters[segment].toUpperCase();
            isUppercase = false;
        } else {
            textResult += reverseBrailleLetters[segment].toLowerCase();
        }
        if (reverseBrailleLetters[segment] === ' ') {
            isNumMode = false;
        }
    });

    return textResult;
}

function handleInput(input) {
    if (input.includes('O') || input.includes('.')) {
        console.log(brailleToEnglish(input));
    } else {
        console.log(englishToBraille(input));
    }
}

const input = process.argv.slice(2).join(' ');
handleInput(input);
