//Parse arguments from command line to String variable
const inputString = process.argv.slice(2).join(' ');

//Declare maps of english to braille characters
let specCharMap = {};
specCharMap['capital'] = '.....O';
specCharMap['decimal'] = '.O...O';
specCharMap['number'] = '.O.OOO';
specCharMap['space'] = '......';

let charMap = {};
charMap['A'] = 'O.....';
charMap['B'] = 'O.O...';
charMap['C'] = 'OO....';
charMap['D'] = 'OO.O..';
charMap['E'] = 'O..O..';
charMap['F'] = 'OOO...';
charMap['G'] = 'OOOO..';
charMap['H'] = 'O.OO..';
charMap['I'] = '.OO...';
charMap['J'] = '.OOO..';
charMap['K'] = 'O...O.';
charMap['L'] = 'O.O.O.';
charMap['M'] = 'OO..O.';
charMap['N'] = 'OO.OO.';
charMap['O'] = 'O..OO.';
charMap['P'] = 'OOO.O.';
charMap['Q'] = 'OOOOO.';
charMap['R'] = 'O.OOO.';
charMap['S'] = '.OO.O.';
charMap['T'] = '.OOOO.';
charMap['U'] = 'O...OO';
charMap['V'] = 'O.O.OO';
charMap['W'] = '.OOO.O';
charMap['X'] = 'OO..OO';
charMap['Y'] = 'OO.OOO';
charMap['Z'] = 'O..OOO';
charMap['.'] = '..OO.O';
charMap[','] = '..O...';
charMap['?'] = '..O.OO';
charMap['!'] = '..OOO.';
charMap[':'] = '..OO..';
charMap[';'] = '..O.O.';
charMap['-'] = '....OO';
charMap['/'] = '.O..O.';
charMap['<'] = '.OO..O';
charMap['>'] = 'O..OO.';
charMap['('] = 'O.O..O';
charMap[')'] = '.O.OO.';

let numMap = {};
numMap['1'] = 'O.....';
numMap['2'] = 'O.O...';
numMap['3'] = 'OO....';
numMap['4'] = 'OO.O..';
numMap['5'] = 'O..O..';
numMap['6'] = 'OOO...';
numMap['7'] = 'OOOO..';
numMap['8'] = 'O.OO..';
numMap['9'] = '.OO...';
numMap['0'] = '.OOO..';


//Main Function 
let isBraille = determineLanguage(inputString);
var output;

if(isBraille) {
    //braille to english function
    //output = function return
}
else {
    //english to braille function
    output = englishToBraille(inputString);
}

//Output final translation
console.log(output);


//Determine if string is braille or english
function determineLanguage(inputString) {
    const charArray = inputString.split("");
    //const charSet = new Set();
    //const setIter = charSet.values();

    // for(var i=0;i<charArray.length;i++) {
    //     charSet.add(charArray[i]);
    // }

    var currentChar;
    for(var i=0;i<charArray.length;i++) {
        currentChar = charArray[i];
        if(currentChar != "O" && currentChar != ".") {
            return false;
        }
    }

    return true;
}

function englishToBraille(inputString) {
    const englishChars = inputString.split('');
    console.log(englishChars);
    var currentChar;
    var i=0;
    var output = "";

    while(i<englishChars.length) {
        currentChar = englishChars[i];
        if(currentChar === " ") {
            output +=specCharMap['space'];
            i++;
        }

        else if(isNaN(currentChar)) {
            if(currentChar == currentChar.toUpperCase()) {
                output += specCharMap['capital'];
                output += charMap[currentChar];
            }
            else {
                output += charMap[currentChar.toUpperCase()];
            }
            i++;
        }
        else {
            output += specCharMap['number'];
            output += numMap[currentChar];
            
            while(!isNaN(englishChars[++i])) {
                currentChar = englishChars[i];
                output += numMap[currentChar];
            }
        }
    }
    return output;
}