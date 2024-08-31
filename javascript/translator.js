const translationArray = [
    ['a', 'O.....'],
    ['b', 'O.O...'],
    ['c', 'OO....'],
    ['d', 'OO.O..'],
    ['e', 'O..O..'],
    ['f', 'OOO...'],
    ['g', 'OOOO..'],
    ['h', 'O.OO..'],
    ['i', '.OO...'],
    ['j', '.OOO..'],
    ['k', 'O...O.'],
    ['l', 'O.O.O.'],
    ['m', 'OO..O.'],
    ['n', 'OO.OO.'],
    ['o', 'O..OO.'],
    ['p', 'OOO.O.'],
    ['q', 'OOOOO.'],
    ['r', 'O.OOO.'],
    ['s', '.OO.O.'],
    ['t', '.OOOO.'],
    ['u', 'O...OO'],
    ['v', 'O.O.OO'],
    ['w', '.OOO.O'],
    ['x', 'OO..OO'],
    ['y', 'OO.OOO'],
    ['z', 'O..OOO'],
    ['.', '..OO.O'],
    [',', '..O...'],
    ['?', '..O.OO'],
    ['!', '..OOO.'],
    [':', '..OO..'],
    [';', '..O.O.'],
    ['-', '....OO'],
    ['/', '.O..O.'],
    ['<', '.OO..O'],
    ['(', 'O.O..O'],
    [')', '.O.OO.'],
];

const translationArrayNumbers = [
    [1, 'O.....'],
    [2, 'O.O...'],
    [3, 'OO....'],
    [4, 'OO.O..'],
    [5, 'O..O..'],
    [6, 'OOO...'],
    [7, 'OOOO..'],
    [8, 'O.OO..'],
    [9, '.OO...'],
    [0, '.OOO..'],
    [',', '..O...'],
    ['?', '..O.OO'],
    ['!', '..OOO.'],
    [':', '..OO..'],
    [';', '..O.O.'],
    ['-', '....OO'],
    ['/', '.O..O.'],
    ['<', '.OO..O'],
    ['>', 'O..OO.'],
    ['(', 'O.O..O'],
    [')', '.O.OO.']
];

const translateToEnglish = (brailleString) => {
    let newEnglishString = '';
    let currSlice = '';
    let prevIterSkip = false;
    let isNumber = false;

    for (let i = 0; i < brailleString.length; i = i + 6){ 
        if (prevIterSkip) { 
            prevIterSkip = false;

        } else {
            // get the 6 characters per iteration to be translated
            currSlice = brailleString.slice(i, i+6);

            // case : capitalize next string
            if (currSlice == '.....O') { 
                // grab the next substring and tell the program to skip the next iteration to avoid duplicating with prevIterSkip variable
                currSlice = brailleString.slice(i+6, i+12); 
                prevIterSkip = true;

                // using the some function since it breaks when one element is found
                // this reduces the overall runtime
                translationArray.some(function (bval) { 
                    if(bval[1] == currSlice) {
                        newEnglishString += bval[0].toUpperCase();
                    }
                });
            
            // case: next string is a number
            } else if (currSlice == '.O.OOO') {
                currSlice = brailleString.slice(i+6, i+12); 
                prevIterSkip = true;
                // setting isNumber to true ensures strings are only chosen from the numbers array for the rest of the string
                isNumber = true;

                translationArrayNumbers.some(function (bval) { 
                    if(bval[1] == currSlice) {
                        newEnglishString += bval[0];
                    }
                });

            // case: next string is a space
            } else if (currSlice == '......') {
                // a space resets looking for numbers
                isNumber = false;

                // since this case is just for a space, we can save computation time and add it straight away
                newEnglishString += ' ';

            } else if (isNumber) {
                translationArrayNumbers.some(function (bval) { 
                    if(bval[1] == currSlice) {
                        newEnglishString += bval[0];
                    }
                });
            
            // no special condition so just lookup the string slice
            } else { 
                translationArray.some(function (bval) { 
                    if(bval[1] == currSlice) {
                        newEnglishString += bval[0];
                    }
                });
            }
        }
    }
    return newEnglishString;
}

const translateToBraille = (englishString) => {
    let newBrailleString = '';
    let uppercaseRegex = /[A-Z]/;
    let numberRegex = /[0-9]/;
    let isFirstDigit = true;

    for (let i = 0; i < englishString.length; i++){ 
        
        // case: uppercase letter
        if (uppercaseRegex.test(englishString[i])) {
            // add uppercase identifier then add lowercase letter
            newBrailleString += '.....O';

            // then lookup lowercase letter in translation array
            translationArray.some(function (engval) { 
                if(engval[0] == englishString[i].toLowerCase()) {
                    newBrailleString += engval[1];
                }
            });
         
        // case : is a number
        } else if (numberRegex.test(englishString[i])) {
            // add number identifier before first digit then lookup in number array
            if (isFirstDigit) {
                isFirstDigit = false;
                newBrailleString += '.O.OOO';
            }

            translationArrayNumbers.some(function (engval) { 
                if(engval[0] == englishString[i]) {
                    newBrailleString += engval[1];
                }
            });

        // case: decimal
        } else if (englishString[i] == '.') {
            // add identifier if it is a decimal (occurs after a number)
            if (numberRegex.test(englishString[i-1])){
                newBrailleString += '.O...O';
            }
            
            // just add the braille if it occurs after a letter
            newBrailleString += '..OO.O';

        // no special condition
        } else {
            translationArray.some(function (engval) { 
                if(engval[0] == englishString[i]) {
                    newBrailleString += engval[1];
                }
            });
        }
    }
    return newBrailleString;
}

const translate = () => {
    const brailleRegex = /^[O.]+$/;
    let outputString = '';

    process.argv.forEach(function (val, index, _) {
        if (index > 2) { 
            // This means there are multiple variables in the command, indicating spaces which implies English. 
            // We will add a braille space between each translated english word
            outputString += '......';
        }
        if (index > 1){
            // considers each command line argument after 'node' and the file name
            if(brailleRegex.test(val)) { 
                // true here means only '.' and 'O' found in the whole string so translate to English
                outputString += translateToEnglish(val);
                
            } else {
                outputString += translateToBraille(val);
            }
        }
    });
    return outputString;
}

console.log(translate());
