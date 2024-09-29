const brailleToAlphabetMap = new Map([
    ["O.....", "a"],
    ["O.O...", "b"],
    ["OO....", "c"],
    ["OO.O..", "d"],
    ["O..O..", "e"],
    ["OOO...", "f"],
    ["OOOO..", "g"],
    ["O.OO..", "h"],
    [".OO...", "i"],
    [".OOO..", "j"],
    ["O...O.", "k"],
    ["O.O.O.", "l"],
    ["OO..O.", "m"],
    ["OO.OO.", "n"],
    ["O..OO.", "o"],
    ["OOO.O.", "p"],
    ["OOOOO.", "q"],
    ["O.OOO.", "r"],
    [".OO.O.", "s"],
    [".OOOO.", "t"],
    ["O...OO", "u"],
    ["O.O.OO", "v"],
    [".OOO.O", "w"],
    ["OO..OO", "x"],
    ["OO.OOO", "y"],
    ["O..OOO", "z"],
    [".....O", "capital follows"],
    [".O.OOO", "number follows"],
    ["......", " "]
]);

const alphabetToBrailleMap = new Map(Array.from(brailleToAlphabetMap, ([key, value]) => [value, key]));

const brailleToNumberMap = new Map([
    ["O.....", "1"],
    ["O.O...", "2"],
    ["OO....", "3"],
    ["OO.O..", "4"],
    ["O..O..", "5"],
    ["OOO...", "6"],
    ["OOOO..", "7"],
    ["O.OO..", "8"],
    [".OO...", "9"],
    [".OOO..", "0"]
]);

const numberToBrailleMap = new Map(Array.from(brailleToNumberMap, ([key, value]) => [value, key]));

const englishCapitalFollows = "capital follows";
const englishNumberFollows = "number follows";
const englishSpace = " ";
const brailleCapitalFollows = ".....O";
const brailleNumberFollows = ".O.OOO";
const brailleSpace = "......";
const brailleSize = 6;

function englishToBraille(englishInput) {
    var output = "";
    var numberFollows = false;

    for (let i = 0; i < englishInput.length; i++) {

        /*
        If it is a number:
        - Add the numberFollows braille if its the first number or if its the first number since a space
        - Use number to braille map to retrieve braille
        */

        //checking if it is between 0-9
        if (englishInput[i] >= "0" && englishInput[i] <= "9") {
            if (numberFollows) {
                output += numberToBrailleMap.get(englishInput[i]);
            }
            else {
                output += (alphabetToBrailleMap.get(englishNumberFollows) + numberToBrailleMap.get(englishInput[i]));
                numberFollows = true;
            }
        }

        /*If it is a letter or special character:
        - Set numberFollows to false if a space is detected
        - Add the capitalFollows braille if its a capital letter
        - Use alphabet to braille map to retrieve braille
        */

        else {
            //checking if its a space, " "
            if (englishInput[i] === englishSpace) {
                numberFollows = false;
            }
            //Checking if the character is capital or not, 65 == A and 90== Z
            if (englishInput.charCodeAt(i) >= 65 && englishInput.charCodeAt(i) <= 90) {
                output += alphabetToBrailleMap.get(englishCapitalFollows);
            }
            output += alphabetToBrailleMap.get(englishInput[i].toLowerCase())
        }
    }
    return output;
}

function brailleToEnglish(brailleInput) {
    let output = "";
    let numberFollows = false;
    let capitalFollows = false;

    for (let i = 0; i < brailleInput.length; i += brailleSize) {
        //Split the array into slices of 6 characters for the size of 1 braille
        let brailleSlice = brailleInput.slice(i, i + brailleSize);

        /*
        Checking conditions:
        - If capital follows or number follows is detected in braille, set the tag to true and continue to the next braille slice
        - If a space is detected, set numberFollows to false
        */
        if (brailleSlice === brailleNumberFollows) {
            numberFollows = true;
            continue;
        }
        else if (brailleSlice === brailleCapitalFollows) {
            capitalFollows = true;
            continue;
        }
        else if (brailleSlice === brailleSpace) {
            numberFollows = false;
        }

        /*
        Based on the value of numberFollows:
        - use the braille to number map if its true
        - use the braille to alphabet map if its false
        - if the next character is a capital, set the value from the map to the capital version of the letter
        */
        if (numberFollows) {
            output += brailleToNumberMap.get(brailleSlice);
        }
        else if (capitalFollows) {
            output += brailleToAlphabetMap.get(brailleSlice).toUpperCase();
            capitalFollows = false;
        }
        else {
            output += brailleToAlphabetMap.get(brailleSlice);
        }
    }
    return output;
}

//check if each letter is braille, if it is not, it is not braille (return false)
function isBraille(stringInput) {
    for (let i = 0; i < stringInput.length; i++) {
        if (stringInput[i] !== "O" && stringInput[i] !== ".") {
            return false;
        }
    }
    return true;
}

function main() {
    //check if there are proper arguments to translate
    if (process.argv <= 2) {
        //console.log("no input to translate")
    }
    else {
        //Combining all inputs into one string to translate
        let input = process.argv.slice(2).join(" ");

        if (isBraille(input)) {
            console.log(brailleToEnglish(input));
        }
        else {
            console.log(englishToBraille(input));
        }
    }
}

main();

