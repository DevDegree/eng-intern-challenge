//============Object to hold key-value pair for the E-B translation===============


/*
For the purposes of this challenge Braille must be displayed as 
O and . where O represents a raised dot. You must include the entire 
English alphabet, the ability to capitalize letters, add spaces, 
and the numbers 0 through 9 as well.
*/

// ----English to Braille----
const brailleToEng = { // only a-zA-Z0-9\s 
    "O.....": ['a', '1'],
    "O.O...": ['b', '2'],
    "OO....": ['c', '3'],
    "OO.O..": ['d', '4'],
    "O..O..": ['e', '5'],
    "OOO...": ['f', '6'],
    "OOOO..": ['g', '7'],
    "O.OO..": ['h', '8'],
    ".OO...": ['i', '9'],
    ".OOO..": ['j', '0'],
    "O...O.": 'k',
    "O.O.O.": 'l',
    "OO..O.": 'm',
    "OO.OO.": 'n',
    "O..OO.": 'o',
    "OOO.O.": 'p',
    "OOOOO.": 'q',
    "O.OOO.": 'r',
    ".OO.O.": 's',
    ".OOOO.": 't',
    "O...OO": 'u',
    "O.O.OO": 'v',
    ".OOO.O": 'w',
    "OO..OO": 'x',
    "OO.OOO": 'y',
    "O..OOO": 'z',
    ".....O": "capFollow",
    ".O.OOO": "numberFollow",
    "......": ' '
};

// ---Braille to English----
const engToBraille = { // only a-zA-Z0-9\s 
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO..",
    "cap_follow": ".....O",
    "number_follow": ".O.OOO",
    "space": "......"
};

//============Function===============
// The input is a string, use regex to detect if a number literal is a number
function isInt(char) {
    return /^\d$/.test(char)
}



const translateEngToBraille = function(string) {
    // Variable
    let result = '' // The return result
    let isNumberTag = false; // The opening tag for number literal string

    for (let i = 0; i < string.length; i++) {
        
        //Check if the current character is number
        if (isInt(string[i])) {
            if(!isNumberTag) { // Faster process, dont need to add Number_follow everytime
                result += engToBraille["number_follow"]
                isNumberTag = true
            }
            result += engToBraille[string[i]]
        }
        
        else { // If the current is not a number literal
            isNumberTag = false //reset the opening tag
            
            // If the next character not lower => then it can only be space and lower
            if (string[i] !== string[i].toLowerCase())  result += engToBraille["cap_follow"] + engToBraille[string[i].toLowerCase()] // Char tag follow with the lower case char
                
            // It can only be space and lower
            else if (string[i] === ' ')  {
                result += engToBraille["space"] // Handle spaces
            }
                
            else  result += engToBraille[string[i]]; // Add the Braille for the lowercase character
        } 
    }
    return result
}

const translateBrailleToEng = function(string) {
    // Variable
    let result = '' // The return result
    let isNumberTag = false // The opening tag for number literal string
    let isCapTag = false // the opening tag for cappital literal

    for (let i = 0; i < string.length; i += 6) {
        // Get sub string from the string input to analyzie it 6 chars by 6 chars
        let segment = string.substring(i, i + 6);

        if (segment === ".....O") isCapTag = true; // Is capital tag

        else if (segment === '.O.OOO') isNumberTag = true; // Is number tag

        else if (segment === '......') { ; // Is space character then we can insert and reset tags
            result += ' '; // Append a space character
            isNumberTag = false; // Reset number tag
            isCapTag = false; // Reset capital tag
            continue; 
        }
        else // Then Append acorrdingly to the tag Bool value 
            
            // If it is a number
            if (isNumberTag) {
                result += brailleToEng[segment][1]// If it is number tag then insert char at index [1] in the k-v object cause it is a number
                continue;
            }  
            
            // If it is a character
            else if (isCapTag) { // If it is capitallize then insert char at index [0] in the k-v object and capital it
                result += brailleToEng[segment][0].toUpperCase(); //Append
                isCapTag = false; // Reset cap tag

            } else result += brailleToEng[segment][0]
    }



    return result
}

//============CommandLineArgument===============
// Get the input string from user
let input = process.argv.slice(2).join(' ')
// if input doesn't contain any . it is not Braille
if (!input.includes('.')) console.log(translateEngToBraille(input)) 
else console.log(translateBrailleToEng(input))
