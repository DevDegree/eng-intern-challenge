const brailleLetters = {
    a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..", e: "O..O..",
    f: "OOO...", g: "OOOO..", h: "O.OO..", i: ".OO...", j: ".OOO..",
    k: "O...O.", l: "O.O.O.", m: "OO..O.", n: "OO.OO.", o: "O..OO.",
    p: "OOO.O.", q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.",
    u: "O...OO", v: "O.O.OO", w: ".OOO.O", x: "OO..OO", y: "OO.OOO", z: "O..OOO"
};

const brailleNumbers = {
    1: "O.....", 2: "O.O...", 3: "OO....", 4: "OO.O..", 5: "O..O..",
    6: "OOO...", 7: "OOOO..", 8: "O.OO..", 9: ".OO...", 0: ".OOO.."
};

const brailleSpecial = {
    " ": "......",    
    ".": "O.O.OO",    
    ",": "O.....",    
    "?": ".OOO.O",    
    "!": ".OO.OO",   
    ":": "OO....",    
    ";": "O.O...",    
    "-": "O....O",    
    "/": "O...OO",    
    "<": "OO..OO",    
    ">": ".O.OOO",   
    "(": "O.OO..",    
    ")": "O.OO..",    
    "capital": ".....O", 
    "number": ".O.OOO"   
};


//reverse mapping dictionaries of braille to english
const englishFromBrailleLetters = {};
const englishFromBrailleNumbers = {};
const englishFromBrailleSpecial = {};

for (const key in brailleLetters) {
    englishFromBrailleLetters[brailleLetters[key]] = key;
}
for (const key in brailleNumbers) {
    englishFromBrailleNumbers[brailleNumbers[key]] = key;
}
for (const key in brailleSpecial) {
    englishFromBrailleSpecial[brailleSpecial[key]] = key;
}

//determines if input string is in Braille using regexp matching
function isBraille(input) {
    return /^[O.]+$/.test(input);//regular expression matches only braille characters
}

//converts braille string to english
function toEnglish(brailleText) {
    let result = ''; //final output string
    let isCapital = false; //track if next character will be capitalized
    let isNumber = false; //track if next character will be a number

    //split braille input to array of 6 character segments
    const segments = brailleText.match(/.{1,6}/g) || [];
    
    //loop over braille segments, converting them to their english characters
    for (const segment of segments) {
        if (segment === brailleSpecial.capital) {
            isCapital = true;
            continue;
        } else if (segment === brailleSpecial.number) {
            isNumber = true;
            continue;
        } else if (segment === brailleSpecial.space) {
            result += ' ';
            isNumber = false; //space resets number flag
            continue;
        }

        //choose the correct mapping based on the `isNumber` context and retrieve the appropriate english character for the current braille segment. If not found, then it checks in special characters.
        let char = (isNumber ? englishFromBrailleNumbers : englishFromBrailleLetters)[segment] || englishFromBrailleSpecial[segment];
        
        if (char) { //appends new character to result output if a record found in dictionary
            if (isCapital) {
                char = char.toUpperCase();
                isCapital = false;
            }
            result += char;
        }
    }
    return result;
}

function toBraille(englishText) {
    let result = "";
    let isNumberContext = false; 

    for (let char of englishText) {
        // handle space and reset number flag
        if (char === ' ') {
            result += brailleSpecial[' '];
            isNumberContext = false; // Reset number context on space
            continue;
        }

        //check if the character is a digit and handle number flag
        if (/[0-9]/.test(char)) {
            if (!isNumberContext) { 
                result += brailleSpecial.number; //add number character at the start of a number sequence
                isNumberContext = true; //set number context
            }
            result += brailleNumbers[char]; //append the Braille code for the number
        } else {
            isNumberContext = false; //exit number context when encountering a non-digit

            //check for capital letters and append capital indicator
            if (char.toUpperCase() === char && isNaN(char)) {
                result += brailleSpecial.capital; //add capital indicator for uppercase letters
            }

            //append the Braille code for the letter or special characters
            result += brailleLetters[char.toLowerCase()] || brailleSpecial[char] || ""; //use brailleSpecial mapping for special characters
        }
    }

    return result;
}




//main function to determine the type of input and then returns appropriate translated output
function translate(input) {
    if (isBraille(input)) { 
        return toEnglish(input);
    }else{
        return toBraille(input);
    }
}



const input = process.argv[2]; //grab input from command line
console.log(translate(input)); //translated output is printed to the terminal