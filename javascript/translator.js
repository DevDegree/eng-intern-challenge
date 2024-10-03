#!/usr/bin/env node

class BrailleTranslator {
    constructor() {
        this.BRAILLE_TO_ENGLISH = {
            'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
            'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
            '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
            'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
            'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
            'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
            'OO.OOO': 'y', 'O..OOO': 'z',
            '......': ' ',
            '.....O': 'capital_follows',
            '.O.OOO': 'number_follows'
        };

        this.NUMBER_MAP = {
            'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
            'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
        };

        this.ENGLISH_TO_BRAILLE = Object.entries(this.BRAILLE_TO_ENGLISH).reduce(
            (acc, [braille, english]) => ({ ...acc, [english]: braille }),
            {}
        );
    }

    translate(input) {
        if (/^[O.]+$/.test(input)) {
            return this.brailleToEnglish(input);
        } else {
            return this.englishToBraille(input);
        }
    }

    brailleToEnglish(input) {
        let result = "";
        let capitalized = false;
        let numberMode = false;

        const brailleChars = input.match(/.{6}/g) || [];

        for (const char of brailleChars) {
            if (char === this.ENGLISH_TO_BRAILLE['capital_follows']) {
                capitalized = true;
            } else if (char === this.ENGLISH_TO_BRAILLE['number_follows']) {
                numberMode = true;
            } else if (char === this.ENGLISH_TO_BRAILLE[' ']) {
                result += ' ';
                numberMode = false;
            } else {
                let letter = this.BRAILLE_TO_ENGLISH[char];
                if (letter) {
                    if (numberMode && this.NUMBER_MAP[letter]) {
                        result += this.NUMBER_MAP[letter];
                    } else {
                        result += capitalized ? letter.toUpperCase() : letter;
                    }
                    capitalized = false;
                }
            }
        }

        return result;
    }

    englishToBraille(input) {
        let result = "";
        let wasLastCharNumber = false;

        for (const char of input) {
            if (/[A-Z]/.test(char)) {
                result += this.ENGLISH_TO_BRAILLE['capital_follows'];
                result += this.ENGLISH_TO_BRAILLE[char.toLowerCase()];
                wasLastCharNumber = false;
            } else if (/[0-9]/.test(char)) {
                if (!wasLastCharNumber) {
                    result += this.ENGLISH_TO_BRAILLE['number_follows'];
                    wasLastCharNumber = true;
                }
                const letterEquivalent = Object.keys(this.NUMBER_MAP)
                    .find(key => this.NUMBER_MAP[key] === char);
                if (letterEquivalent) {
                    result += this.ENGLISH_TO_BRAILLE[letterEquivalent];
                }
            } else {
                wasLastCharNumber = false;
                if (char === ' ') {
                    result += this.ENGLISH_TO_BRAILLE[' '];
                } else if (this.ENGLISH_TO_BRAILLE[char]) {
                    result += this.ENGLISH_TO_BRAILLE[char];
                }
            }
        }

        return result;
    }
}

// Main execution
const args = process.argv.slice(2);
if (args.length === 0) {
    console.error("Please provide a string to translate");
    process.exit(1);
}

const inputString = args.join(' ');
const translator = new BrailleTranslator();
console.log(translator.translate(inputString));