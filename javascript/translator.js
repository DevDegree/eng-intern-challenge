const brailleMap = {
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
    'capital_follows': '.....O',  // Representation for capitalization symbol
    'number_follows': '.O.OOO',   // Representation for number follows symbol
    ' ': '......',            // Space is represented by no raised dots
};

const numberMap = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
};


function Translator(text) {
    const BrailleLang = ["O", "."];
    // Converting from Text to Braille  
    if (!(text.includes(BrailleLang[0]) && text.includes(BrailleLang[1]))) {
        let result = []
        let isNumber = false;
        for (let i = 0; i < text.length; i++) {
            let char = text[i];

            if (char === char.toUpperCase() && /[a-zA-Z]/.test(char)) {
                result.push(brailleMap['capital_follows']);
                char = char.toLowerCase();  // Convert to lowercase for mapping
            }

            // Handle numbers
            if (/[0-9]/.test(char)) {
                if (!isNumber) {
                    result.push(brailleMap['number_follows']);  // Add number follows symbol
                    isNumber = true;  // Enter number mode
                }
                result.push(numberMap[char]);
            } else {
                // If we hit a non-number character, exit number mode
                if (isNumber) {
                    isNumber = false;
                }

                // Handle space
                if (char === ' ') {
                    result.push(brailleMap[' ']);
                } else {
                    // Map the regular letter
                    result.push(brailleMap[char]);
                }
            }
        }
        return result.join('');
    }

    // Converting from Braille to  Text 
    else {
        let result = [];
        let isCapital = false;
        let isNumber = false;
        let characterList = text.split("");
        let totalCharacter = Math.floor(characterList.length / 6);

        for (let j = 0; j < totalCharacter; j++) {
            let brailleSymbol = '';
            for (let k = 0; k < 6; k++) {
                let index = k + j * 6;
                brailleSymbol += characterList[index];
            }

            // Check for special symbols (capitalization or number)
            if (brailleSymbol === '.....O') {  // Capital follows
                isCapital = true;
                continue;
            } else if (brailleSymbol === '.O.OOO') {  // Number follows
                isNumber = true;
                continue;
            } else if (brailleSymbol === '......') {
                isNumber = false;
            }

            // Handle normal letters or numbers
            if (isNumber) {
                result.push(Object.keys(numberMap).find(key => numberMap[key] === brailleSymbol));


            } else {
                let letter = Object.keys(brailleMap).find(key => brailleMap[key] === brailleSymbol);
                if (isCapital && letter !== ' ') {
                    result.push(letter.toUpperCase());
                    isCapital = false;  // Reset after capitalizing the next letter
                } else {
                    result.push(letter);
                }
            }
        }
        return result.join('');
    }

}


const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Enter your input :', input => {
    let finalResult = Translator(input);
    console.log(finalResult);
    readline.close();
});