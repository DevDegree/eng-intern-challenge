//English characters to braille object
const brailleDict = {
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
    'k': 'O....O',
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
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    '-': '....OO',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

//English numbers to braille object
const brailleNums = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

//Braille to English characters object
engDict = Object.fromEntries(Object.entries(brailleDict).map(([key, value]) => ([value,key])));

//Braille to English numbers object
engNums = Object.fromEntries(Object.entries(brailleNums).map(([key, value]) => ([value, key])));

const capitalNextIndicator = '.....O';
const numberNextIndicator = '.O.OOO';
const decimalNextIndicator = '.O...O';

//function to tranlate English to braille
function translateEngToBraille(input) {
    let capitalize = false;
    let inNumberMode = false;

    return input
    .split('')
    .map((char) => {
        if (char === char.toUpperCase() && char !== char.toLowerCase()) {
            capitalize = true;
        }

        if (capitalize) {
            capitalize = false;
            return capitalNextIndicator + brailleDict[char.toLowerCase()] || 'ERROR';
        }

        if (/^\d$/.test(char)) {
            inNumberMode = true;
            return numberNextIndicator + brailleNums[char] || 'ERROR'
        }

        if (char === '.' && inNumberMode) {
            return decimalNextIndicator + brailleDict[char] || 'ERROR';
        }

        if (char === ' ' && inNumberMode) {
            inNumberMode = false;
        }

        return brailleDict[char] || 'ERROR'
    })
    .join('');
}

//function to translate braille to English
function translateBrailleToEng(input) {
    let capitalize = false;
    let inNumberMode = false;
    const regex = /.{6}/g
    const brailleSegments = input.match(regex)

    return brailleSegments
        .map((brailleSegment) => {
            if (brailleSegment === capitalNextIndicator) {
                capitalize = true;   
                return '';         
            }

            if (brailleSegment === decimalNextIndicator) {
                return '.';

            }

            if (brailleSegment === numberNextIndicator) {
                inNumberMode = true;
                return '';
            }

            let charNum = engNums[brailleSegment] || 'ERROR';

            if (inNumberMode) {
                if (brailleSegment === '......') {
                    inNumberMode = false;
                    return ' ';
                }
                return charNum;
            }

            let char = engDict[brailleSegment] || 'ERROR';

            if (char) {
                if(capitalize) {
                    capitalize = false;
                    return char.toUpperCase();
                }
                return char;
            }
        })
        .join('');
}

//function to detect language (English or braille), and translate to opposite

function detectLanguageAndTranslate(input) {
    const braillePattern = /^[O.]+$/
    const brailleSegmentPattern = /^([O.]{6})+$/

    const isBraille = brailleSegmentPattern.test(input) && braillePattern.test(input);

    if (isBraille) {
        return translateBrailleToEng(input)
    } else {
        return translateEngToBraille(input)
    }
}

//execute in command line
if (require.main === module) {
    const args = process.argv.slice(2);

    if (args.length < 1) {
        console.error('Input on command line required');
        process.exit(1);
    }

    const input = args.join(' ');
    const result = detectLanguageAndTranslate(input);

    console.log(result)
}