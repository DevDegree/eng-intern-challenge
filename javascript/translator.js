//get args
const input = process.argv.slice(2)

//define braille alphabet
const alphabet = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO."
}
const brailleAlpa = {
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
    "O.OO..": "l",
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
    "......": " ",
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")"
}

//check if there is only 1 arg and it is only made up of "O" or "." characters + check if length is multiple of 6 to be safe
if (input.length === 1 && input[0].match(/^[O.]+$/) && input[0].length % 6 === 0) {
    //process braille into array of 6 characters
    const braille = input[0].match(/.{1,6}/g)
    //initialize result + flags
    let result = ""
    let capFollows = false
    let numFollows = false

    //translate braille to alphabet
    braille.forEach(brailleChar => {
        //check for capital follows or number follows braille

        //consume captial follows braille
        if (brailleChar === ".....O") {
            capFollows = true
            return
        }
        //consume number follows braille
        if (brailleChar === ".O.OOO") {
            numFollows = true
            return
        }

        //if space detected, set num follows to false
        if (brailleChar === "......") {
            numFollows = false
        }
        //translate braille to alphabet
        if (capFollows) {
            let char = brailleAlpa[brailleChar]
            //check if char is an a-z letter, if yes, capitlize it
            if (/^[a-z]$/.test(char)) {
                char = char.toUpperCase()
            }
            result += char
            capFollows = false
        } else if (numFollows) { //convert letters to numbers
            result += (brailleAlpa[brailleChar].charCodeAt(0) - 96) % 10
        } else {//convert other chars to alphabet directly from map
            result += brailleAlpa[brailleChar]
        }

    })
    console.log(result)

} else { //if input is a non-braille string
    let result = ""
    input.forEach((word, idx) => {
        let numMode = false;
        word.split("").forEach(char => {
            //check if char is a-z and uppercase
            if (/^[A-Z]$/.test(char)) {
                result += ".....O"
                char = char.toLowerCase()
                result += alphabet[char]
            } else if (/^[0-9]$/.test(char)) { //convert numbers to letters
                if (numMode) {//if number mode is on, add number directly
                    result += alphabet[String.fromCharCode(parseInt(char) + 96)]
                } else {//if number mode is off, turn it on and add number follows + number
                    result += ".O.OOO"
                    numMode = true
                    result += alphabet[String.fromCharCode(parseInt(char) + 96)]
                }
            } else {//convert other chars to braille
                result += alphabet[char]
            }
        })
        if (idx !== input.length - 1) result += "......" //add space between words, but not after the last word
    })
    console.log(result)

}