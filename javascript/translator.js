

//Steps:
// Get the command line arguments and validate
// Check if the language is braille or english
    // Since braille consists of 0s and 1s, we can check whether the language is braille or not with these criteria
// If it is braille convert to english and print out the output
// Else convert to braille and print out the output

const brailleMap = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '.....O': 'CAPITAL',
    '.O.OOO': 'NUMBER',
    '......': ' '
}

const englishMap = {
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
    'CAPITAL': '.....O',
    'NUMBER': '.O.OOO',
    ' ': '......'
};


const numberMapBraille = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
}

const numberMapEnglish = {
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


const convertToEnglish = (braille) => {
    let output = '';
    let isCapital = false;
    let isNumber = false;
    
    // for loop, and we take 6 characters at a time, then process it to an english alphabet
    for (let i = 0; i < braille.length; i += 6) {
        let chunk = braille.slice(i, i + 6); // first 6 characters
        let letter = brailleMap[chunk];
        
        if (letter === 'CAPITAL') {
            isCapital = true;
        } else if (letter === 'NUMBER') {
            isNumber = true;
        } else {
            if (isNumber){
                letter = numberMapBraille[chunk];
            }
            else if (isCapital) {
                letter = letter.toUpperCase();
                isCapital = false;
            }
            output += letter;
        }
    }

    return output;
}

const convertToBraille = (english) => {
    let output = '';
    let isNumber = false;
    
    for (let letter of english) {
        // Check if the character is a number
        if (/\d/.test(letter)) {
            if (!isNumber) {
                output += englishMap['NUMBER']; // Add number indicator
                isNumber = true;
            }
            output += numberMapEnglish[letter];
        } 
        // Check if the character is a letter
        // Handle space
        else if (letter === ' ') {
            output += englishMap[' '];
        }
        else{
            if (isNumber) {
                isNumber = false; // End of numbers
            }
            if (letter === letter.toUpperCase()) {
                output += englishMap['CAPITAL']; // Add capital indicator
                letter = letter.toLowerCase(); // Convert to lowercase to map correctly
            }
            output += englishMap[letter];
        } 
    }

    return output;
}

const isBraille = (input) => {
    for(let letter of input){
        if(letter !== '.' && letter !== 'O'){
            return false;
        }
    }

    return true;
}


function main(){
    const input = process.argv.slice(2).join(' ');
    if(isBraille(input)){
        console.log(convertToEnglish(input));
    }else{
        console.log(convertToBraille(input))
    }
}


main()