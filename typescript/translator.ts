const args = process.argv.slice(2);
const message = args.join(' ');

const braille = {
    a: 'O.....', b: 'O.O...', c: 'OO....', d: 'OO.O..', e: 'O..O..', f: 'OOO...', g: 'OOOO..', h: 'O.OO..',
    i: '.OO...', j: '.OOO..', k: 'O...O.', l: 'O.O.O.', m: 'OO..O.', n: 'OO.OO.', o: 'O..OO.', p: 'OOO.O.',
    q: 'OOOOO.', r: 'O.OOO.', s: '.OO.O.', t: '.OOOO.', u: 'O...OO', v: 'O.O.OO', w: '.OOO.O', x: 'OO..OO',
    y: 'OO.OOO', z: 'O..OOO', '.': '..OO.O', ' ': '......',
};

const functions = {
    capital: '.....O',
    number: '.O.OOO',
};

const alphabet: { [key: string]: string } = {};
Object.keys(braille).forEach((key) => {
    const brailleSymbol = braille[key]; 
    alphabet[brailleSymbol] = key; 
});

const numberMap = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
    '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
};

const reverseNumberMap = {
    a: '1', b: '2', c: '3', d: '4', e: '5', f: '6',
    g: '7', h: '8', i: '9', j: '0'
};


// Function to convert English text to Braille
const englishToBraille = (text: string) => {
    let brailleOutput = [];
    let isNumber = false;

    for (let char of text) {
        if (/[A-Z]/.test(char)) {
            brailleOutput.push(functions.capital);
            brailleOutput.push(braille[char.toLowerCase()]);
        } else if (/\d/.test(char)) {
            if (!isNumber) {
                brailleOutput.push(functions.number);
                isNumber = true;
            }
            brailleOutput.push(braille[numberMap[char]]); 
        } else if (char === ' ') { 
            brailleOutput.push(braille[' ']); 
            isNumber = false; 
        } else {
            brailleOutput.push(braille[char] || braille[' ']);
        }
    }
    return brailleOutput.join('');
};


const brailleToEng = (brailleStr: string) => {
    let engOutput = [];
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < brailleStr.length; i += 6) {
        const brailleChar = brailleStr.slice(i, i + 6);

        if (brailleChar === functions.capital) {
            isCapital = true;
            continue;
        } else if (brailleChar === functions.number) {
            isNumber = true;
            continue;
        }

        let engChar = alphabet[brailleChar] || ' ';

        if (engChar === ' ') {
            isNumber = false;
        }

        if (isCapital && engChar !== ' ') {
            engChar = engChar.toUpperCase();
            isCapital = false;
        }

        if (isNumber && engChar !== ' ') {
            engChar = reverseNumberMap[engChar];
        }

        engOutput.push(engChar);
    }
    return engOutput.join('');
}

const isBraille = (input: string): boolean => {
    return /^[O. ]+$/.test(input); // Allow only 'O', '.', and spaces
};

if (isBraille(message)) {
    console.log(brailleToEng(message)); // Translate Braille to English
} else {
    console.log(englishToBraille(message)); // Translate English to Braille
}