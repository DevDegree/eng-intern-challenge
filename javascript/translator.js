import { CONFIG } from './config.js';
import { TranslationError } from './errors.js';
import { punctuationMapping, brailleToEnglishMap, englishToBrailleMap } from './mappings.js';

function translator() {

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

            if (!CONFIG.VALID_ENGLISH_REGEX.test(trimmedInput) && !CONFIG.VALID_BRAILLE_REGEX.test(trimmedInput)) {
                throw new TranslationError('Invalid input format.', 'INVALID_FORMAT');
            }

            if (CONFIG.VALID_BRAILLE_REGEX.test(trimmedInput)) {
                if (trimmedInput.length % CONFIG.BRAILLE_CHAR_LENGTH !== 0) {
                    throw new TranslationError('Invalid Braille input. Each Braille character should be 6 dots.', 'INVALID_BRAILLE_LENGTH')
                }
                return translateBrailleToEnglish(trimmedInput)
            } else if (CONFIG.VALID_ENGLISH_REGEX.test(trimmedInput)) {
                return translateEnglishToBraille(trimmedInput)
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
                    message: 'Unexpected error.' + error.message,
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
        let isNumberMode = false;
        let isCapital = false;

        for (let i = 0; i < brailleText.length; i += CONFIG.BRAILLE_CHAR_LENGTH) {
            const brailleChar = brailleText.slice(i, i + CONFIG.BRAILLE_CHAR_LENGTH);
            brailleChars.push(brailleChar);
        }

        for (const brailleChar of brailleChars) {
            const englishChar = brailleToEnglishMap[brailleChar];
            if (englishChar === 'capital') {
                isCapital = true;
            } else if (englishChar === 'number') {
                isNumberMode = true;
            } else {
                let translatedChar = handleNumberMode(englishChar, isNumberMode);
                if (isCapital) {
                    translatedChar = translatedChar.toUpperCase();
                    isCapital = false;
                }
                translatedChars.push(translatedChar);
                if (englishChar === ' ') {
                    isNumberMode = false;
                }
            }
        }
        return { success: true, result: translatedChars.join('') };
    }


    /**
     * Translates English text to Braille.
     * @param {string} englishText - The English text to be translated.
     * @returns {Object} An object containing the translation result.
     */

    function translateEnglishToBraille(englishText) {
        let brailleOutput = '';
        let isNumberMode = false;

        for (let i = 0; i < englishText.length; i++) {
            const char = englishText[i];
            if (char >= CONFIG.NUMBER_MIN && char <= CONFIG.NUMBER_MAX) {
                if (!isNumberMode) {
                    brailleOutput += englishToBrailleMap['number'];
                    isNumberMode = true;
                }
                brailleOutput += englishToBrailleMap[char];
            } else if (char === ' ') {
                isNumberMode = false;
                brailleOutput += englishToBrailleMap[' '];
            } else if (char === char.toUpperCase() && char.match(/[A-Z]/)) {
                brailleOutput += englishToBrailleMap['capital'];
                brailleOutput += englishToBrailleMap[char.toLowerCase()];
                isNumberMode = false;
            } else {
                brailleOutput += punctuationMapping[char] || englishToBrailleMap[char.toLowerCase()] || '';
                isNumberMode = false;
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

    function handleNumberMode(char, isNumberMode) {
        if (isNumberMode) {
            const numberIndex = CONFIG.NUMBER_CHARS.indexOf(char);
            return numberIndex === -1 ? char : numberIndex.toString();
        }
        return char;
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
        process.exit(1);
    } else {
        console.log(translationResult.result);
    }
}

translator();


