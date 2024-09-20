
const brailleAlphabet = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "capital": ".....O",
    "number": ".O.OOO",
    "space": "......"
};

const brailleNum = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

const reversedBrailleAlphabet = Object.fromEntries(
    Object.entries(brailleAlphabet).map(([key, value]) => [value, key])
);

const reversedBrailleNum = Object.fromEntries(
    Object.entries(brailleNum).map(([key, value]) => [value, key])
);


// Detect Braille or English
function detectLanguage(input) {
    const regex = /^[A-Za-z0-9\s]+$/;
    
    return regex.test(input) ? "English" : "Braille"
}

// English to Braille
function engToBraille(input) {
    let result = "";

    // Store input String as char array
    let charArray = input.split('');
    let checkNum = false

    for (let x = 0; x < charArray.length; x++) {
        let char = charArray[x];

        // Check for spaces
        if(char === " "){
            result += brailleAlphabet["space"];

            // Cancel number input
            checkNum = false;
        }else if(/[A-Z]/.test(char)){
            result += brailleAlphabet["capital"];
            result += brailleAlphabet[char.toLowerCase()];
        }else if(/\d/.test(char)){

            // if detect current char is a number and number mode is not turned on, add number symbol, and turn on number mode.
            if(!checkNum){
                result += brailleAlphabet["number"];
                checkNum = true;
            }

            result += brailleNum[char];
        }else{
            result += brailleAlphabet[char];
        }
    }
    
    return result;
}

// Braille to English
function brailleToEng(input){
    let result = "";
    let checkCapital = false;
    let checkNum = false;

    for(let x = 0; x < input.length; x += 6){
        let char = input.substring(x, x+6);
        if(char === brailleAlphabet["capital"]){
            checkCapital = true;
            continue;
        }else if(char === brailleAlphabet["number"]){
            checkNum = true;
            continue;
        }else if(char === brailleAlphabet["space"]){
            result += " ";
            checkNum = false;
            continue;
        }

        let engChar
        if(checkNum){
            engChar = reversedBrailleNum[char];
        }else{
            engChar = reversedBrailleAlphabet[char];
        }

        if (checkCapital) {
            result += engChar.toUpperCase();
            checkCapital = false;
        }else {
            result += engChar;
        }
    }


    
    return result;
}



// THIS DOESNT WORK, FIX IN MORNING.
const args = process.argv.slice(2);
const userInput = args.join(" ");

const result = detectLanguage(userInput) === "English" ? engToBraille(userInput) : brailleToEng(userInput)

console.log(result);

//".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
//".....OO.....O.O...OO.....O.OOOO.....O.O...OO....OO..OO.....OOO.OOOO..OOO"
