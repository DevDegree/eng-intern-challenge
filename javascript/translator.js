const args = process.argv.slice(2);
let input;

if (args.length > 0) {
    input = args[0];
} else {
    console.log("No input provided.");
    return
}

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
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    // '<': '.OO..O',
    // '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO',
    'space': '......'
}

let brailleToEnglish = {}
for (const key in englishToBraille)
    brailleToEnglish[englishToBraille[key]] = key;

function translateBrailleToEnglish(input) {
    let english = "";
    let isCapital = false;
    let isNumber = false;
    for (let i = 0; i < input.length; i+=6) {
        let char = brailleToEnglish[input.slice(i, i+6)];
        switch (char) {
            case 'capital':
                isCapital = true;
                break;
            case 'decimal':
                english += ".";
                break;
            case 'space':
                english += " ";
                isNumber = false;
                break;
            case 'number':
                isNumber = true;
                break;
            default:
                if (isCapital) {
                    english += char.toUpperCase();
                    isCapital = false;
                } else if (isNumber) {
                    let number = char.charCodeAt(0) - 96
                    english += number == 10 ? 0 : number < 10 ? number : "";
                } else {
                    english += char;
                }
        }
    }
    return english;
}

console.log(translateBrailleToEnglish(input));