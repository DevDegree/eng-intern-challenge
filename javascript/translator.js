const args = process.argv.slice(2);
let input;

// check if an argument is passed 
if (args.length > 0) {
    input = args.join(' ');
} else {
    return;
}

// map of English characters to its Braille equivalent 
const englishToBraille = {
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
    // '.': '..OO.O',
    // ',': '..O...',
    // '?': '..O.OO',
    // '!': '..OOO.',
    // ':': '..OO..',
    // ';': '..O.O.',
    // '-': '....OO',
    // '/': '.O..O.',
    // '<': '.OO..O',
    // '>': 'O..OO.',
    // '(': 'O.O..O',
    // ')': '.O.OO.',
    'capital': '.....O',
    // 'decimal': '.O...O',
    'number': '.O.OOO',
    'space': '......'
};

// This method accepts a string of expected English content and returns the Braille translation.
function translateEnglishToBraille(input) {
    let braille = "";
    // flag to check if currently translating a number
    let isNumber = false;
    for (let i = 0; i < input.length; i++) {
        let char = input[i];
        switch (char) {
            case ' ':
                braille += englishToBraille['space'];
                // a space will terminate translation of a number
                isNumber = false;
                break;
            // case '.':
            //     // if currently translating a number and another number follows after this char, '.' is considered a decimal instead of a period 
            //     if (isNumber && i != input.length-1 && /^[0-9]$/.test(input[i+1]))
            //         braille += englishToBraille['decimal'];
            //     else
            //         braille += englishToBraille['.'];
            //     break;
            default:
                // check if numeric
                if (/^[0-9]$/.test(char)) {
                    if (!isNumber) {
                        braille += englishToBraille['number'];
                        isNumber = true;
                    }

                    let charFromDigit = parseInt(char) == 0 ? 'j' : String.fromCharCode(parseInt(char)+96);
                    braille += englishToBraille[charFromDigit];
                } else {
                    // check if capital
                    if (char == char.toUpperCase() && char != char.toLowerCase()) {
                        braille += englishToBraille['capital'];
                        char = char.toLowerCase();
                    }
    
                    braille += englishToBraille[char];
                }
        }
    }

    return braille;
}

// This method accepts a string of expected Braille content and returns the English translation.
function translateBrailleToEnglish(input) {
    // create a reverse map of the englishToBraille dict
    let brailleToEnglish = {};
    for (const key in englishToBraille)
        brailleToEnglish[englishToBraille[key]] = key;

    let english = "";
    // flags used to check if currently translating a number or capital letter
    let isCapital = false;
    let isNumber = false;
    // loop through input with a step size of 6 since Braille symbols are 6 characters long
    // 'i' will always be the index of the first char in a Braille symbol 
    for (let i = 0; i < input.length; i+=6) {
        let char = brailleToEnglish[input.slice(i, i+6)];
        switch (char) {
            case 'capital':
                // set flag so program knows the next char is capitalized
                isCapital = true;
                break;
            // case 'decimal':
            //     english += ".";
            //     break;
            case 'space':
                english += " ";
                // a space will terminate translation of a number
                isNumber = false;
                break;
            case 'number':
                // set flag so program knows it is translating a number
                isNumber = true;
                break;
            default:
                if (isCapital) {
                    english += char.toUpperCase();
                    // captial flag is only valid for one char 
                    isCapital = false;
                } else if (isNumber) {
                    // the first 10 letters of the alphabet have the same Braille symbols as the digits 1,2,...,9,0 , respectively
                    // therefore, since we know we are currently translating a number we can get the digit in respect to the ASCII value of the letter (a -> 1, b -> 2, ...)
                    let number = char.charCodeAt(0) - 96;
                    // since the first letter (a) is maps to 1, the 10th letter (j) maps to 0 instead of 10
                    // assuming a valid input, we should never get a number > 10 (as there are only 10 digits), but the program will translate the symbol to nothing in that case 
                    english += number == 10 ? 0 : number < 10 ? number : "";
                } else {
                    english += char;
                }
        }
    }
    return english;
}

// braille strings only consist of "." (raised dot) and "O" (dot) chars 
const uniqueCharSet = new Set(input);

if (uniqueCharSet.has('.')) {
    console.log(translateBrailleToEnglish(input))
}
else {
    console.log(translateEnglishToBraille(input));
}