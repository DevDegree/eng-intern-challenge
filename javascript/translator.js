// letters (english to braille)
const englishToBrailleLetters = {
    a: "O.....",
    b: "O.O...",
    c: "OO....",
    d: "OO.O..",
    e: "O..O..",
    f: "OOO...",
    g: "OOOO..",
    h: "O.OO..",
    i: ".OO...",
    j: ".OOO..",
    k: "O...O.",
    l: "O.O.O.",
    m: "OO..O.",
    n: "OO.OO.",
    o: "O..OO.",
    p: "OOO.O.",
    q: "OOOOO.",
    r: "O.OOO.",
    s: ".OO.O.",
    t: ".OOOO.",
    u: "O...OO",
    v: "O.O.OO",
    w: ".OOO.O",
    x: "OO..OO",
    y: "OO.OOO",
    z: "O..OOO",
};

// numbers (english to braille)
const englishToBrailleNumbers = {
    1: "O.....",
    2: "O.O...",
    3: "OO....",
    4: "OO.O..",
    5: "O..O..",
    6: "OOO...",
    7: "OOOO..",
    8: "O.OO..",
    9: ".OO...",
    0: ".OOO..",
}

// special characters (english to braille)
const englishToBrailleSpecialChars = {
    capital: ".....O",
    number: ".O.OOO",
    " ": "......",
}

// letters (braille to english)
const brailleToEnglishLetters = {}
for (const [engChar, brailleChar] of Object.entries(englishToBrailleLetters)) {
    brailleToEnglishLetters[brailleChar] = engChar;
}

// numbers (braille to english)
const brailleToEnglishNumbers = {}
for (const [engChar, brailleChar] of Object.entries(englishToBrailleNumbers)) {
    brailleToEnglishNumbers[brailleChar] = engChar;
}

// special characters (braille to english)
const brailleToEnglishSpecialChars = {}
for (const [engChar, brailleChar] of Object.entries(englishToBrailleSpecialChars)) {
    brailleToEnglishSpecialChars[brailleChar] = engChar;
}

// checks if the input is Braille
const isBraille = (input) => {
    return /^[O.]+$/.test(input);
};

// take the Braille input and translate it to English
const brailleToEnglishTranslator = (brailleInput) => {
    let englishOutput = ""
    let isCapital = false
    let isNumber = false

    for (let i = 0; i < brailleInput.length; i += 6) {
        let brailleChar = brailleInput.substring(i, i + 6)

        // translate a uppercase
        // if the previous Braille char was a "capital follows" char isCapital will be true
        if (isCapital) {
            englishOutput += brailleToEnglishLetters[brailleChar].toUpperCase()
            isCapital = false
        }
        // transalte a space
        // if we were translating a number, encountering a space means the number is complete
        else if (brailleChar == englishToBrailleSpecialChars[" "]) {
            englishOutput += brailleToEnglishSpecialChars[brailleChar]
            isNumber = false
        }
        // translate a number
        else if (isNumber) {
            englishOutput += brailleToEnglishNumbers[brailleChar]
        }
        // if this is the "capital follows" Braille character, set the isCapital flag to true
        // we know that the following character will be uppercase
        else if (brailleChar == englishToBrailleSpecialChars["capital"]) {
            isCapital = true
        }
        // if this is the "number follows" Braille character, set the isNumber flag to true
        // we know that the following characters will be numbers until we hit a space
        else if (brailleChar == englishToBrailleSpecialChars["number"]) {
            isNumber = true
        }
        else {
            englishOutput += brailleToEnglishLetters[brailleChar]
        }
    }
    return englishOutput
}

// take the English input and translate it to Braille
const englishToBrailleTranslator = (englishInput) => {
    let brailleOutput = ""
    let isNumber = false

    for (i = 0; i < englishInput.length; ++i) {
        let englishChar = englishInput[i]

        // translate an upper case letter
        // we want to add the Braille "capital follows", then the Braille character
        if (englishChar >= 'A' && englishChar <= 'Z') {
            brailleOutput += englishToBrailleSpecialChars["capital"] + englishToBrailleLetters[englishChar.toLowerCase()]
        }
        // translate a space
        // we want to add the Braille "space" character 
        // also if we were translating a number, encountering a space means the number is complete
        else if (englishChar == " ") {
            brailleOutput += englishToBrailleSpecialChars[englishChar]
            isNumber = false
        }
        // translate a number
        else if (englishChar >= '0' && englishChar <= '9') {
            if (!isNumber) {
                brailleOutput += englishToBrailleSpecialChars["number"]
                isNumber = true
            }
            brailleOutput += englishToBrailleNumbers[englishChar]
        }
        // translate lowercase alphabet
        else {
            brailleOutput += englishToBrailleLetters[englishChar]
        }
    }

    return brailleOutput
}

const translator = (input) => {
    if (isBraille(input)) {
        return brailleToEnglishTranslator(input);
    } else {
        return englishToBrailleTranslator(input);
    }
}

const input = process.argv.slice(2).join(" ");

const output = translator(input);
console.log(output);
