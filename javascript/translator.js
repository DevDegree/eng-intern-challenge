const CONFIG = {
    VALID_ENGLISH_REGEX: /^[a-zA-Z0-9 ,.?!:;\-/<>()]+$/,
    VALID_BRAILLE_REGEX: /^[O.]+$/,
    NUMBER_CHARS: 'jabcdefghi',
    BRAILLE_CHAR_LENGTH: 6,
    NUMBER_MIN: '0',
    NUMBER_MAX: '9',
};

class TranslationError extends Error {
    constructor(message, code) {
        super(message);
        this.name = 'TranslationError';
        this.code = code;
    }
}


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

    /**
     * Detects the input type and translates accordingly.
     * @param {string} input - The text to be translated.
     * @returns {Object} An object containing the translation result or error information.
     */

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
                if (trimmedInput.length % CONFIG.BRAILLE_CHAR_LENGTH !== 0) {
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

    /**
     * Translates Braille text to English.
     * @param {string} brailleText - The Braille text to be translated.
     * @returns {Object} An object containing the translation result.
     */
    function translateBrailleToEnglish(brailleText) {
        const brailleChars = [];
        const translatedChars = [];
        let isCapitalNext = false;
        let isNumberMode = false;

        // Split input into Braille unit
        for (let i = 0; i < brailleText.length; i += CONFIG.BRAILLE_CHAR_LENGTH) {
            const brailleChar = brailleText.slice(i, i + CONFIG.BRAILLE_CHAR_LENGTH);
            brailleChars.push(brailleChar);
        }

        // Translate braille units into english
        for (const brailleChar of brailleChars) {
            const englishChar = brailleToEnglishMap[brailleChar];
            if (englishChar === undefined) {
                throw new TranslationError(`Unknown Braille character ${brailleChar}`, 'UNKNOWN_BRAILLE_CHAR')
            }
            if (englishChar === 'capital') {
                isCapitalNext = true;
            } else if (englishChar === 'number') {
                isNumberMode = true;
            } else {
                const translatedChar = handleNumberMode(englishChar, isNumberMode, isCapitalNext)
                translatedChars.push(translatedChar);
                isCapitalNext = false;
                if (englishChar === ' ') isNumberMode = false;
            }
        }
        return { success: true, result: translatedChars.join('') }
    }

    /**
     * Translates English text to Braille.
     * @param {string} englishText - The English text to be translated.
     * @returns {Object} An object containing the translation result.
     */

    function translateEnglishToBraille(englishText) {
        let brailleOutput = '';
        let isNumberMode = false;

        for (const char of englishText) {
            if (char >= CONFIG.NUMBER_MIN && char <= CONFIG.NUMBER_MAX) {
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

    /**
     * Handles number mode translation for both Braille to English and English to Braille.
     * @param {string} char - The character to be translated.
     * @param {boolean} isNumberMode - Whether number mode is active.
     * @param {boolean} isCapital - Whether the character should be capitalized.
     * @returns {string} The translated character.
     */

    function handleNumberMode(char, isNumberMode, isCapital = false) {
        if (isNumberMode) {
            const numberIndex = CONFIG.NUMBER_CHARS.indexOf(char);
            return numberIndex === -1 ? char : numberIndex.toString()
        } else {
            return isCapital ? char.toUpperCase() : char;
        }
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


