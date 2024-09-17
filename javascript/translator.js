const args = process.argv.slice(2);

const EngToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', 'capital_follows': '.....O', 'decimal_follows': '.O...O', 
    'number_follows': '.O.OOO', ' ': '......'
};

const NumberToBraille = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
};

const BrailleToEng = Object.fromEntries(Object.entries(EngToBraille).map(([k, v]) => [v, k]));
const BrailleToNumber = Object.fromEntries(Object.entries(NumberToBraille).map(([k, v]) => [v, k]));

// Function to determine translation type and initiate translation
const translate = (values) => {
    if (values.length === 1 && /^[.O]+$/.test(values[0])) {
        console.log(translateBrailleToEng(values[0]));
    } else {
        console.log(values.map(translateEngToBraille).join('......'));
    }
};

// Translate Braille to English
const translateBrailleToEng = (value) => {
    const parts = value.match(/.{1,6}/g) || [];
    const result = [];
    let i = 0;

    while (i < parts.length) {
        const translatedBraille = BrailleToEng[parts[i]];

        if (translatedBraille === 'capital_follows') {
            result.push(BrailleToEng[parts[++i]].toUpperCase());
        } else if (translatedBraille === 'number_follows') {
            while (++i < parts.length && parts[i] !== '......') {
                result.push(BrailleToNumber[parts[i]]);
            }
        } else {
            result.push(translatedBraille);
        }
        i++;
    }

    return result.join('');
};

// Translate English to Braille
const translateEngToBraille = (value) => {
    let isInNumber = false;

    return value.split('').reduce((result, char, i, chars) => {
        const isNumber = !isNaN(char);

        if (isNumber) {
            if (!isInNumber) {
                result.push(EngToBraille['number_follows']);
                isInNumber = true;
            }
            result.push(NumberToBraille[char]);

            if (i < chars.length - 1 && isNaN(chars[i + 1])) {
                result.push('......');
                isInNumber = false;
            }
        } else {
            isInNumber = false;
            if (char === char.toLowerCase()) {
                result.push(EngToBraille[char]);
            } else {
                result.push(EngToBraille['capital_follows'], EngToBraille[char.toLowerCase()]);
            }
        }

        return result;
    }, []).join('');
};

translate(args);
