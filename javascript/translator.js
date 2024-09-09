//Parse arguments from command line to String variable
const inputString = process.argv.slice(2).join(' ');

//Declare maps of english to braille characters
let specCharMap = new Map();
specCharMap.set('capital', '.....O');
specCharMap.set('decimal', '.O...O');
specCharMap.set('number', '.O.OOO');
specCharMap.set('space', '......');

let charMap = new Map();
charMap.set('A', 'O.....');
charMap.set('B', 'O.O...');
charMap.set('C', 'OO....');
charMap.set('D', 'OO.O..');
charMap.set('E', 'O..O..');
charMap.set('F', 'OOO...');
charMap.set('G', 'OOOO..');
charMap.set('H', 'O.OO..');
charMap.set('I', '.OO...');
charMap.set('J', '.OOO..');
charMap.set('K', 'O...O.');
charMap.set('L', 'O.O.O.');
charMap.set('M', 'OO..O.');
charMap.set('N', 'OO.OO.');
charMap.set('O', 'O..OO.');
charMap.set('P', 'OOO.O.');
charMap.set('Q', 'OOOOO.');
charMap.set('R', 'O.OOO.');
charMap.set('S', '.OO.O.');
charMap.set('T', '.OOOO.');
charMap.set('U', 'O...OO');
charMap.set('V', 'O.O.OO');
charMap.set('W', '.OOO.O');
charMap.set('X', 'OO..OO');
charMap.set('Y', 'OO.OOO');
charMap.set('Z', 'O..OOO');
charMap.set('.', '..OO.O');
charMap.set(',', '..O...');
charMap.set('?', '..O.OO');
charMap.set('!', '..OOO.');
charMap.set(':', '..OO..');
charMap.set(';', '..O.O.');
charMap.set('-', '....OO');
charMap.set('/', '.O..O.');
charMap.set('<', '.OO..O');
charMap.set('>', 'O..OO.');
charMap.set('(', 'O.O..O');
charMap.set(')', '.O.OO.');

let numMap = new Map();
numMap.set('1', 'O.....');
numMap.set('2', 'O.O...');
numMap.set('3', 'OO....');
numMap.set('4', 'OO.O..');
numMap.set('5', 'O..O..');
numMap.set('6', 'OOO...');
numMap.set('7', 'OOOO..');
numMap.set('8', 'O.OO..');
numMap.set('9', '.OO...');
numMap.set('0', '.OOO..');

//Main Function 
let isBraille = determineLanguage(inputString);
var output;

if(isBraille) {
    //braille to english function
    output = brailleToEnglish(inputString);
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
    var currentChar;
    var i=0;
    var output = "";

    while(i<englishChars.length) {
        currentChar = englishChars[i];

        //Check Space
        if(currentChar === " ") {
            output += specCharMap.get('space');
            i++;
        }

        //Check Character
        else if(isNaN(currentChar)) {
            //Check Upper Case
            if(currentChar == currentChar.toUpperCase()) {
                output += specCharMap.get('capital');
                output += charMap.get(currentChar);
            }
            else {
                output += charMap.get(currentChar.toUpperCase());
            }
            i++;
        }

        //Check Number
        else if(!isNaN(currentChar)) {
            output += specCharMap.get('number');

            while(i+1 < englishChars.length && !isNaN(englishChars[i+1])) {
                currentChar = englishChars[i++];
                output += numMap.get(currentChar);
            }
            output +=specCharMap.get('space');
            i++;
        }
    }
    return output;
}

function brailleToEnglish(inputString) {
    
    const brailleChars = [];
    var substring = "";
    
    //Break up braille characters
    for(var i=0;i<inputString.length;i+=6) {
        substring = inputString.substring(i,i+6).trim();
        brailleChars.push(substring);
    }

    var output = "";
    var currentChar;

    for(let i=0;i<brailleChars.length;i++) {
        
        currentChar = brailleChars[i];

        //Check Upper Case
        if(currentChar === specCharMap.get('capital')) {
            i++;
            currentChar = brailleChars[i];
            output += getKey(charMap,currentChar);
        }

        //Check Number
        else if(currentChar === specCharMap.get('number')) {
            i++;
            while(brailleChars[i] != specCharMap.get('space')) {
                currentChar = brailleChars[i];
                output += getKey(numMap,currentChar);
                i++;
            }
            output += " ";
        }

        //Check Space
        else if (currentChar === specCharMap.get('space')) {
            output += " ";
        }

        //Check Character
        else {
            output += getKey(charMap,currentChar).toLowerCase();
        }
    }

    return output;
}
    
function getKey(map,searchValue) {
    let invertedMap = new Map([...map.entries()].map(
        ([key, value]) => ([value, key]))
    );

    return invertedMap.get(searchValue);
}