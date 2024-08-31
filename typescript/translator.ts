// Indicate that the symbol that follows is a capital letter
const capitalFollows: string = '.....O';

// Indicate that the symbol that follows is a number
const numberFollows: string = '.O.OOO';

// Indicate that the current symbol is a space
const isSpace: string = '......';

// Maps a letter to its Braille representation
const brailleLetterTranslations: { [letter: string]: string } = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO'
};

// Create a reverse mapping for the brailleLetterTranslations object
const reverseBrailleTranslations: { [braille: string]: string } = 
  Object.fromEntries(Object.entries(brailleLetterTranslations).map(([k, v]) => [v, k]));

// Maps a number to its Braille representation
const brailleNumberTranslations: { [number: string]: string } = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..'
};

// Create a reverse mapping for the brailleNumberTranslations object
const reverseBrailleNumberTranslations: { [braille: string]: string } =
    Object.fromEntries(Object.entries(brailleNumberTranslations).map(([k, v]) => [v, k]));

// Translates English to Braille
const translateToBraille = (words: string): string => {
    let braille = ''; 
    let isNumber = false; // flag to indicate we are currently translating a number
    for (let i = 0; i < words.length; i++) {
        if (words[i] === ' ') {
            braille += isSpace;
        }
        else if (words[i].match(/[A-Z]/)) { 
            braille += capitalFollows;
            braille += brailleLetterTranslations[words[i].toLowerCase()];
        }
        else if (words[i].match(/[a-z]/)) { 
            braille += brailleLetterTranslations[words[i]];
            isNumber = false;
        }
        else { 
            if (!isNumber) {
                braille += numberFollows;
            }
            isNumber = true;
            braille += brailleNumberTranslations[words[i]];
        }
    }
    return braille;
}

// Translates Braille to English
const translateFromBraille = (braille: string): string => {
    let words = '';
    let isNumber = false; // flag to indicate we are currently translating a number
    for (let i = 0; i < braille.length; i += 6) {
        let brailleLetter = braille.slice(i, i + 6);
        if (brailleLetter === isSpace) {
            words += ' ';
            isNumber = false;
        }
        else if (brailleLetter === capitalFollows) {
            i += 6;
            brailleLetter = braille.slice(i, i + 6);
            words += reverseBrailleTranslations[brailleLetter].toUpperCase();
        }
        else if (brailleLetter === numberFollows) {
            if (!isNumber) {
                i += 6;
                brailleLetter = braille.slice(i, i + 6);
                isNumber = true;
            }
            words += reverseBrailleNumberTranslations[brailleLetter];
        }
        else {
            if (isNumber) {
                words += reverseBrailleNumberTranslations[brailleLetter];
            }
            else {
                words += reverseBrailleTranslations[brailleLetter];
            }
        }
    }
    return words;
}

// Check if the input is Braille or English
const isBraille = (input: string): boolean => {
    for (let i = 0; i < input.length; i++) {
        if (input[i] !== '.' && input[i] !== 'O') {
            return false;
        }
    }
    return true;
}

const main = (args: string[]): void => {
    if (args.length < 2) {
        console.log('Usage: ts-node translator.ts <text>');
        return;
    }
    const words = args.slice(2).join(' ');
    if (isBraille(words)) {
        console.log(translateFromBraille(words));
    }
    else {
        console.log(translateToBraille(words));
    }
}

main(process.argv);
