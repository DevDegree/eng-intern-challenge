const CONFIG = {
    VALID_ENGLISH_REGEX: /^[a-zA-Z0-9 ,.?!:;\-/<>()]+$/,
    VALID_BRAILLE_REGEX: /^[O.]+$/,
    NUMBER_CHARS: 'jabcdefghi',
};


function translator() {
    const brailleToEnglish = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z',
        '..O...': ',', '..OO..': '.', '..O.O.': '?', '..OO.O': '!', '..OO.': ':',
        '..O..': ';', '..OO..': '-', '.O..O.': '/', '.O.O..': '<', '.O.O.O': '>',
        '.O.O..': '(', '.O..O.': ')', '.O.OOO': 'number', '.....O': 'capital', '......': ' ',
    };

    const englishToBraille = {};
    for (const [brailleChar, englishChar] of Object.entries(brailleToEnglish)) {
        englishToBraille[englishChar] = brailleChar;
    }

    function detectAndTranslate(input) {
        try {
            if (!input || typeof input !== 'string') {
                throw new TranslationError('Input must not be an empty string.', 'INVALID_INPUT')
            }

            const trimedInput = input.trim();
            if (trimedInput.length === 0) {
                throw new TranslationError('Input can not be empty or whitespace.', 'EMPTY_INPUT')
            }

            if (CONFIG.VALID_BRAILLE_REGEX.test(trimedInput)) {
                if (trimedInput.length % 6 !== 0) {
                    throw new TranslationError('Invalid Braille input. Each Braille character should be 6 dots.', 'INVALID_BRAILLE_LENGTH')
                }
                return translateBrailleToEnglish(trimedInput)
            } else if (CONFIG.VALID_ENGLISH_REGEX.test(trimedInput)) {
                return translateEnglishToBraille(trimedInput)
            } else {
                throw new TranslationError('Invalid input format.')
            }
        } catch (error) {
            if (error instanceof TranslationError) {
                return {
                    success: false,
                    error: {
                        message: error.message,
                        code: error.code,
                    }
                }
            }
            return {
                success: false,
                error: {
                    message: 'Unexpected error.',
                    code: 'UNKNOWN_ERROR',
                }
            }
        }


    }

    function translateBrailleToEnglish(input) {
        const arrOfBraille = [];
        const output = [];
        let isCapitalNext = false;
        let isNumberMode = false;

        // split input into Braille unit
        for (let i = 0; i < input.length; i += 6) {
            const brailleUnit = input.slice(i, i + 6);
            arrOfBraille.push(brailleUnit);
        }

        // translate braille units into english
        for (let j = 0; j < arrOfBraille.length; j++) {
            const englishChar = brailleToEnglish[arrOfBraille[j]];
            if (englishChar === undefined) {
                throw new TranslationError(`Unknown Braille character ${arrOfBraille[j]}`, 'UNKNOWN_BRAILLE_CHAR')
            }
            if (englishChar === 'capital') {
                isCapitalNext = true;
            } else if (englishChar === 'number') {
                isNumberMode = true;
            } else {
                if (isNumberMode) {
                    const number = CONFIG.NUMBER_CHARS.indexOf(englishChar);
                    output.push(number === -1 ? englishChar : number.toString())
                } else {
                    output.push(isCapitalNext ? englishChar.toUpperCase() : englishChar);
                    isCapitalNext = false;
                }
                if (englishChar === ' ') isNumberMode = false;
            }
        }
        return output.join('');
    }

    function translateEnglishToBraille(input) {
        let output = '';
        let isNumberMode = false;

        for (let char of input) {
            if (char >= '0' && char <= '9') {
                if (!isNumberMode) {
                    output += englishToBraille['number']
                    isNumberMode = true;
                }
                output += englishToBraille[CONFIG.NUMBER_CHARS[char]];
            } else {
                if (char === ' ') isNumberMode = false;
                if (char === char.toUpperCase() && char !== ' ' && isNaN(char) && char.match(/[a-z]/i)) {
                    output += englishToBraille['capital'];
                    char = char.toLowerCase();
                }
                output += englishToBraille[char] || ''
            }
        }
        return output;
    }

    const args = process.argv.slice(2);

    if (args.length === 0) {
        console.log('Usage: node translator.js <text to translate>');
        console.log('Example: node translator.js "Hello World"');
        process.exit(1)
    }

    const userInput = args.join(' ');
    const result = detectAndTranslate(userInput);
    if (result.success === false) {
        console.error('Translation Error:')
        console.error(` Message: ${result.error.message}`)
        console.error(` Code: ${result.error.code}`)
    } else {
        console.log(output);
    }
}

translator();


class TranslationError extends Error {
    constructor(message, code) {
        super(message);
        this.name = 'TranslationError';
        this.code = code;
    }
}