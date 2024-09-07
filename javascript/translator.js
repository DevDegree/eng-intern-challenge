// Command line arguments
args = process.argv;

// Get string
let argumentString = args.slice(2).join(" ") // Join if differents words (sentence)

//console.log("argumentString:", argumentString) //debug

// Detect if not Braille (contains other than 0 or .)
const isEnglish = /[^.O]/.test(argumentString);

//console.log("isEnglish:", isEnglish); //debug

let englishToBraille = new Map([
    ["a", "O....."],
    ["b", "O.O..."],
    ["c", "OO...."],
    ["d", "OO.O.."],
    ["e", "O..O.."],
    ["f", "OOO..."],
    ["g", "OOOO.."],
    ["h", "O.OO.."],
    ["i", ".OO..."],
    ["j", ".OOO.."],
    ["k", "O...O."],
    ["l", "O.O.O."],
    ["m", "OO..O."],
    ["n", "OO.OO."],
    ["o", "O..OO."],
    ["p", "OOO.O."],
    ["q", "OOOOO."],
    ["r", "O.OOO."],
    ["s", ".OO.O."],
    ["t", ".OOOO."],
    ["u", "O...OO"],
    ["v", "O.O.OO"],
    ["w", ".OOO.O"],
    ["x", "OO..OO"],
    ["y", "OO.OOO"],
    ["z", "O..OOO"],
    ["1", "O....."],
    ["2", "O.O..."],
    ["3", "OO...."],
    ["4", "OO.O.."],
    ["5", "O..O.."],
    ["6", "OOO..."],
    ["7", "OOOO.."],
    ["8", "O.OO.."],
    ["9", ".OO..."],
    ["0", ".OOO.."],
    ["capital follows", ".....O"],
    ["number follows", ".O.OOO"],
    [" ", "......"]
]);


let result = "";

if (isEnglish) {
    brailleResult = "";
    currentlyNumber = false;
    for (let i = 0; i < argumentString.length; i++) {
        let stringCharacter = argumentString.substring(i, i+1);
        
        // If character is first number
        if (/[0-9]/.test(stringCharacter) && !currentlyNumber) {
            brailleResult += englishToBraille.get("number follows");
            currentlyNumber = true;
        // Deactivate number mode
        } else if (/[^0-9]/.test(stringCharacter) && currentlyNumber) {
            currentlyNumber = false;
        }

        // If character is capital letter
        if (/[A-Z]/.test(stringCharacter)) {
            brailleResult += englishToBraille.get("capital follows");
            stringCharacter = stringCharacter.toLowerCase();
        }

        brailleResult += englishToBraille.get(stringCharacter);
    }
    result = brailleResult;
}


let notNumberBrailleToEnglish = new Map();
let numberBrailleToEnglish = new Map();
// Inverse englishToBraille
englishToBraille.forEach(function(value, key) {
    if (/[^0-9]/.test(key)) {
        notNumberBrailleToEnglish.set(value, key);
    } else if(/[0-9]/.test(key)) {
        numberBrailleToEnglish.set(value, key);
    }
}) 

if (!isEnglish) {
    englishResult = "";
    let argumentArray = splitBy6Char(argumentString);

    let capitalFollows = false;
    let numberFollows = false;

    for (let j = 0; j < argumentArray.length; j++) {
        element = argumentArray[j];

        if (capitalFollows) {
            englishResult += notNumberBrailleToEnglish.get(element).toUpperCase();
            capitalFollows = false;
        } else if (numberFollows) {
            if (element === "......") { // if is space
                englishResult += notNumberBrailleToEnglish.get(element);
                numberFollows = false;
            } else {
                englishResult += numberBrailleToEnglish.get(element);
            }
        } else {
            if (notNumberBrailleToEnglish.get(element) === "capital follows") {
                capitalFollows = true;
            } else if (notNumberBrailleToEnglish.get(element) === "number follows") {
                numberFollows = true;
            } else {
                englishResult += notNumberBrailleToEnglish.get(element);
            }
        }
    }

    result = englishResult;

}

console.log(result);
//console.log(result === "Abc 123") //debug
    


function splitBy6Char(string) {
    // separate by chunks of 6 characters
    const array = [];
    for (let i = 0; i < string.length; i+=6) {
        array.push(string.slice(i, i + 6));
    }
    return array;
}