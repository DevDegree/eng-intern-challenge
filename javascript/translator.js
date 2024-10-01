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
        if (!input || typeof input !== 'string') {
            return 'Input should be a non-empty string.'
        }

        const trimedInput = input.trim();
        if (trimedInput.length === 0) {
            return 'Error: Input can not be empty or whitespace.'
        }

        const VALID_ENGLISH_REGEX = /^[a-zA-Z0-9 ,.?!:;\-/<>()]+$/;
        const VALID_BRAILLE_REGEX = /^[O.]+$/;

        if (VALID_BRAILLE_REGEX.test(trimedInput)) {
            if (trimedInput.length % 6 !== 0) {
                return 'Error: Invalid Braille input. Each Braille character should be 6 dots.'
            }
            return translateBrailleToEnglish(trimedInput)
        } else if (VALID_ENGLISH_REGEX.test(trimedInput)) {
            return translateEnglishToBraille(trimedInput)
        } else {
            return 'Error: Invalid input format.'
        }

    }

    function translateBrailleToEnglish(input) {
        const arrOfBraille = [];
        const output = [];
        let capitalNext = false;
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
                return `Error: Unknown Braille character ${arrOfBraille[j]}`
            }
            if (englishChar === 'capital') {
                capitalNext = true;
            } else if (englishChar === 'number') {
                isNumberMode = true;
            } else {
                if (isNumberMode) {
                    const number = 'jabcdefghi'.indexOf(englishChar);
                    output.push(number === -1 ? englishChar : number.toString())
                } else {
                    output.push(capitalNext ? englishChar.toUpperCase() : englishChar);
                    capitalNext = false;
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
                output += englishToBraille['jabcdefghi'[char]];
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
        console.log('Please provide a string to translate');
        process.exit(1)
    }

    const userInput = args.join(' ');
    const output = detectAndTranslate(userInput);
    console.log(output);
}

translator();