function translator() {
    // Create mapping between Braille and English characters
    const brailleToEnglish = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z',
        '.O.OOOO.....': '0', '.O.OOOO.....': '1', '.O.OOOO.O...': '2', '.O.OOOO....': '3',
        '.O.OOOO.O..': '4', '.O.OOOO..O..': '5', '.O.OOOOO....': '6', '.O.OOOOOO...': '7',
        '.O.OOOO.OO..': '8', '.O.OOO.OO...': '9',
        '..O...': ',',
        '..OO..': '.',
        '..O.O.': '?',
        '..OO.O': '!',
        '..OO.': ':',
        '..O..': ';',
        '..OO..': '-',
        '.O..O.': '/',
        '.O.O..': '<',
        '.O.O.O': '>',
        '.O.O..': '(',
        '.O..O.': ')',
        '.O.OOO': 'number', '.....O': 'capital', '......': ' ',
    };

    const englishToBraille = {};
    for (const [brailleChar, englishChar] of Object.entries(brailleToEnglish)) {
        englishToBraille[englishChar] = brailleChar;
    }

    // implement a function to detect input format
    // detect the braille input
    function detectAndTranslate(input) {
        const isBraille = /^[O.]+$/.test(input) && input.length % 6 === 0;
        const isEnglish = /^[a-zA-Z0-9 ,.?!:;\-/<>()]+$/.test(input);
        
        if (isBraille) {
            return translateBrailleToEnglish(input)
        } else if (isEnglish) {
            return translateEnglishToBraille(input)
        } else {
            return 'Error: Invalid input format.'
        }

    }

    function translateBrailleToEnglish(input) {
        const arrOfBraille = [];
        const output = [];
        let capitalNext = false;

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
            if(englishChar === 'capital') {
                capitalNext = true;
            } else {
                output.push(capitalNext ? englishChar.toUpperCase() : englishChar);
                capitalNext = false;
            }
        }
        return output.join('');
    }

    function translateEnglishToBraille(input) {
        let output = '';

        for (let char of input) {
            if (char === char.toUpperCase() && char !== ' ' && isNaN(char) && char.match(/[a-z]/i)) {
                output += englishToBraille['capital'];
                char = char.toLowerCase();
            }

            if (englishToBraille[char]) {
                output += englishToBraille[char]
            } else {
                return `Error: unknown character ${char}`
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