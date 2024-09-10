const brailleToEnglish =  {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " "
}

const brailleToNumber = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

const englishToBraille =  {
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
}

const englishToNumber = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

//get the command line arguments given by user
const args = process.argv.slice(2)

if (args.length < 1) {
    console.log("Please add a string to translate")
}

//check whether input is in braille. 
let inputIsEnglish = false
let output = ""

//if the input is one string, it is likely braille
if (args.length === 1) {
    const suspectedBrailleString = args[0]
    //go over each letter in the suspected braille string, making sure each letter is a 'O' or a '.'
    for (let i = 0; i < suspectedBraille.length; i++) {
        const currentCharacter = suspectedBrailleString[i]
        //check to make sure character is not anything other than 'O' or '.'
        if (currentCharacter !== "." && currentCharacter !== "O") {
            //if it is something else, it must be english
            inputIsEnglish = true;
            break;
        }
    }
}
//if we have more than one string, input will be english
else {
    inputIsEnglish = true
}

//if english, go through each character and translate to braille
if (inputIsEnglish) {

    //remember if we already added a number indicator
    let numberIndicator = false

    //go though every word in the input array
    for (let arg of args) {

        //add a space before starting the next word, as long as it is not the first word
        if (arg !== args[0]) {
            output += "......"
        }

        //go through every letter in the word
        for (let char of arg) {

            //check if character is a number
            const number = parseInt(char)
            if (!isNaN(number)) {
                //if we get here, this means the character is a number
                //make sure to indicate that we are adding numbers if we haven't already
                if (!numberIndicator) {
                    output += ".O.OOO"
                    numberIndicator = true;
                }
                //add the translated number to the output
                output += englishToNumber[char]
            }

            //check if letter is uppercase
            else if (char === char.toUpperCase()) {
                //indicate uppercase
                output += ".....O"
                const brailleChar = englishToBraille[char.toLowerCase()]
                output += brailleChar

                //reset number indicator
                numberIndicator = false
            }
            else {
                //just a normal lowercase letter
                const brailleChar = englishToBraille[char]
                //add the value to the final
                output += brailleChar

                //reset number indicator
                numberIndicator = false
            }
        }
    }
}

//otherwise, go through 6 chars at a time and convert
if (!inputIsEnglish) {

    const braille = args[0].split("")
    let uppercaseIndicator = false
    let numberIndicator = false

    //keep translating while there are are characters left
    while (braille.length > 0) {
        //grab the first six characters in the braille string. This will be converted to one english character
        const brailleChar = braille.splice(0, 6).join("")

        //check for uppercase indicator
        if (brailleChar === ".....O") {
            uppercaseIndicator = true
            continue;
        }

        //check for number indicator
        if (brailleChar === ".O.OOO") {
            numberIndicator = true
            continue
        }

        //check for space to reset number indicator
        if (brailleChar === "......") {
            numberIndicator = false
        }


        //lookup the character and add the english character to the output
        const englishChar = brailleToEnglish[brailleChar]
        //add uppercase if uppercase indicator
        if (uppercaseIndicator) {
            output += englishChar.toUpperCase()
            //remove uppercase
            uppercase = false
        }
        //if weve seen a number indicator, we will add a number
        else if (numberIndicator) {
            const number = brailleToNumber[brailleChar]
            output += number
        }
        else {
            output += englishChar
        }
    }
}

console.log(output)
return