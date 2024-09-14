// translator.js - Shopify Eng Intern Challenge

const args = process.argv.slice(2); // Skipping 'node' & 'translator.js', the first two arguments

const EngToBraille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    'capital_follows': '.....O',
    'decimal_follows': '.O...O',
    'number_follows': '.O.OOO',
    ' ': '......'
};

const NumberToBraille = {
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
};

const BrailleToEng = Object.fromEntries(
    Object.entries(EngToBraille).map(([key, value]) => [value, key])
);

const BrailleToNumber = Object.fromEntries(
    Object.entries(NumberToBraille).map(([key, value]) => [value, key])
);

const translate = (values) => {
    // console.log("Checking whether it's English or Braille", values);
    if (values.length === 1 && /^[.O]+$/.test(values[0])) {
        console.log(translateBrailleToEng(values[0]));
    } else {
        let result = '';
        values.forEach(engElement => {
            result += translateEngToBraille(engElement) + '......';
        });

        // The slice is for removing the trailing Braille space at the end
        console.log(result.slice(0, -6));
    }
};

const translateBrailleToEng = (value) => {
    // console.log("Translating to English...", value);
    let result = '';

    const parts = [];
    for (let i = 0; i < value.length; i += 6) {
        parts.push(value.substring(i, i + 6));
    }

    for (let i = 0; i < parts.length; i++) {
        const translatedBraille = BrailleToEng[parts[i]];
        if (translatedBraille === 'capital_follows') {
            result += BrailleToEng[parts[i+1]].toUpperCase();
            i += 1;
            continue;
        } else if (translatedBraille === 'number_follows') {
            for (let j = i+1; j < parts.length; j++) {
                if (parts[j] === '......') {break;}
                const translatedNumber = BrailleToNumber[parts[j]];
                result += translatedNumber;
                i = j;
            }
        } else {
            result += BrailleToEng[parts[i]];
        }
    }
    return result;
};

const translateEngToBraille = (value) => {
    // console.log("Translating to Braille...", value);

    let result = '';
    const chars = value.split('');
    
    for (let i = 0; i < chars.length; i++) {
        const char = chars[i];
        if (!isNaN(char)) {
            // Add a number follows Braille character once numbers start.
            if (i === 0 || (i > 0 && isNaN(chars[i-1]))) {
                result += EngToBraille['number_follows'];
            }

            result += NumberToBraille[char];

            // Add a space once last number is reached & if there is a letter after it...
            // to maintain Braille readability & to stick to its rules.
            if (i < chars.length-1 && isNaN(chars[i+1])) {
                result += '......';
            }
        } else if (char === char.toLowerCase()) { // Lowercase Characters
            result += EngToBraille[char];
        } else {                                  // Uppercase Characters
            result += EngToBraille['capital_follows'] + EngToBraille[char.toLowerCase()];
        }
    }
    return result;
};

translate(args);
