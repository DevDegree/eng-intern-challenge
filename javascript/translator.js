const CONFIG = {
    VALID_ENGLISH_REGEX: /^[a-zA-Z0-9 ,.?!:;\-/<>()]+$/,
    VALID_BRAILLE_REGEX: /^[O.]+$/,
    NUMBER_CHARS: 'jabcdefghi',
    BRAILLE_CHAR_LENGTH: 6,
};


function translator() {
    const brailleToEnglishMap = {
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

    const englishToBrailleMap = {};
    for (const [brailleChar, englishChar] of Object.entries(brailleToEnglishMap)) {
        englishToBrailleMap[englishChar] = brailleChar;
    }

    function detectAndTranslate(input) {
        try {
            if (!input || typeof input !== 'string') {
                throw new TranslationError('Input must not be an empty string.', 'INVALID_INPUT')
            }

            const trimmedInput = input.trim();
            if (trimmedInput.length === 0) {
                throw new TranslationError('Input can not be empty or whitespace.', 'EMPTY_INPUT')
            }

            if (CONFIG.VALID_BRAILLE_REGEX.test(trimmedInput)) {
                if (trimmedInput.length % BRAILLE_CHAR_LENGTH !== 0) {
                    throw new TranslationError('Invalid Braille input. Each Braille character should be 6 dots.', 'INVALID_BRAILLE_LENGTH')
                }
                return translateBrailleToEnglish(trimmedInput)
            } else if (CONFIG.VALID_ENGLISH_REGEX.test(trimmedInput)) {
                return translateEnglishToBraille(trimmedInput)
            } else {
                throw new TranslationError('Invalid input format.', 'INVALID_FORMAT')
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

    function translateBrailleToEnglish(brailleText) {
        const brailleChars = [];
        const translatedChars = [];
        let isCapitalNext = false;
        let isNumberMode = false;

        // split input into Braille unit
        for (let i = 0; i < brailleText.length; i += BRAILLE_CHAR_LENGTH) {
            const brailleChar = brailleText.slice(i, i + BRAILLE_CHAR_LENGTH);
            brailleChars.push(brailleChar);
        }

        // translate braille units into english
        for (const brailleChar of brailleChars) {
            const englishChar = brailleToEnglishMap[brailleChar];
            if (englishChar === undefined) {
                throw new TranslationError(`Unknown Braille character ${arrOfBraille[j]}`, 'UNKNOWN_BRAILLE_CHAR')
            }
            if (englishChar === 'capital') {
                isCapitalNext = true;
            } else if (englishChar === 'number') {
                isNumberMode = true;
            } else {
                if (isNumberMode) {
                    const numberIndex = CONFIG.NUMBER_CHARS.indexOf(englishChar);
                    translatedChars.push(numberIndex === -1 ? englishChar : numberIndex.toString())
                } else {
                    translatedChars.push(isCapitalNext ? englishChar.toUpperCase() : englishChar);
                    isCapitalNext = false;
                }
                if (englishChar === ' ') isNumberMode = false;
            }
        }
        return { success: true, result: translatedChars.join('') }
    }

    function translateEnglishToBraille(englishText) {
        let brailleOutput = '';
        let isNumberMode = false;

        for (const char of englishText) {
            if (char >= '0' && char <= '9') {
                if (!isNumberMode) {
                    brailleOutput += englishToBrailleMap['number']
                    isNumberMode = true;
                }
                brailleOutput += englishToBrailleMap[CONFIG.NUMBER_CHARS[char]];
            } else {
                if (char === ' ') isNumberMode = false;
                if (char === char.toUpperCase() && char !== ' ' && isNaN(char) && char.match(/[a-z]/i)) {
                    brailleOutput += englishToBrailleMap['capital'];
                }
                const lowerChar = char.toLowerCase();
                brailleOutput += englishToBrailleMap[lowerChar] || ''
            }
        }
        return { success: true, result: brailleOutput };
    }

    const commandLineArgs = process.argv.slice(2);

    if (commandLineArgs.length === 0) {
        console.log('Usage: node translator.js <text to translate>');
        console.log('Example: node translator.js "Hello World"');
        process.exit(1)
    }

    const userInput = commandLineArgs.join(' ');
    const translationResult = detectAndTranslate(userInput);
    if (translationResult.success === false) {
        console.error('Translation Error:')
        console.error(` Message: ${translationResult.error.message}`)
        console.error(` Code: ${translationResult.error.code}`)
    } else {
        console.log(translationResult.result);
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