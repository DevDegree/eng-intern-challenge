const brailleToAlpha = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' ',

    '.....O': 'capital follows',
    '.O...O': 'decimal follows',
    '.O.OOO': 'number follows',

    '..OO.O': '.',
    '..O...': ',', 
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';', 
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..OO.': '>',
    '.O.OO.': '(',
    '.O.OO.': ')',
}

const brailleToNumber = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
    '......': ' '
}

const alphaToBraille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',

    '.': '..OO.O',
    ',': '..O...', 
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',  
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': '.O.OO.',
    ')': '.O.OO.',
}

const numberToBraille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    ' ': '......',
}

const capitalMap = {
    'A': 'a',
    'B': 'b',
    'C': 'c',
    'D': 'd',
    'E': 'e',
    'F': 'f',
    'G': 'g',
    'H': 'h',
    'I': 'i',
    'J': 'j',
    'K': 'k',
    'L': 'l',
    'M': 'm',
    'N': 'n',
    'O': 'o',
    'P': 'p',
    'Q': 'q',
    'R': 'r',
    'S': 's',
    'T': 't',
    'U': 'u',
    'V': 'v',
    'W': 'w',
    'X': 'x',
    'Y': 'y',
    'Z': 'z',
}

function getArgs() {
    return process.argv.slice(2).join(' ')
}

function mainFunc() {
    const input = getArgs()
    let output = ''
    if (isBraille(input)) {
        output = parseBraille(input)
    } else {
        output = parseEnglish(input)
    }
    console.log(output)
}

// Returns true if Braille string 
function isBraille(str) {
    if (str.length % 6 !== 0) {
        return false
    }
    const firstSix = str.slice(0, 6)
    // Check if first 6 chars together exist in our Braille maps
    if (brailleToAlpha[firstSix] || brailleToNumber[firstSix]) {
        return true
    } else {
        return false
    }
}

// Parses Braille to English
function parseBraille(input) {
    let output = []

    for (let i = 0; i + 5 < input.length; i += 6) { 
        output.push(input.slice(i, i+6))
    }
 
    let result = ''
    let capitalFollows = false
    let decimalFollows = false
    let numberFollows = false

    for (let y = 0; y < output.length; y++) {
        // Capital
        if (output[y] === '.....O') {
            capitalFollows = true
            // decimal
        } else if (output[y] === '.O...O') {
            decimalFollows = true
            // number
        } else if (output[y] === '.O.OOO') {
            numberFollows = true
        } else if (capitalFollows) {
            let capitalized = brailleToAlpha[output[y]].toUpperCase()
            result += capitalized
            capitalFollows = false
        } else if (decimalFollows || numberFollows) {
            result += brailleToNumber[output[y]]
            if (output[y] === '......') {
                decimalFollows = false
                numberFollows = false
            }
        } else {
            result += brailleToAlpha[output[y]]
        }
    }
    return result
}

// Parses English to Braille
function parseEnglish(input) {
    let splitString = input.split('')

    let mapToUse = alphaToBraille
    let arr = []
    let numberFollows = false

    for (let i = 0; i < splitString.length; i++) {
        if (!Number.isNaN(Number.parseInt(splitString[i]))) {
            if (!numberFollows) {
                mapToUse = numberToBraille
                arr.push('.O.OOO', mapToUse[splitString[i]])
                numberFollows = true
            } else {
                arr.push(mapToUse[splitString[i]])
            }
        } else if (splitString[i] === '.') {
            arr.push('.O...O', mapToUse[splitString[i]])
        } else if (splitString[i] === ' ') {
            arr.push('......')
            numberFollows = false
            mapToUse = alphaToBraille
        } else if (capitalMap[splitString[i]]) {
            arr.push('.....O', mapToUse[capitalMap[splitString[i]]])
        } else {
            arr.push(mapToUse[splitString[i]])
        }
    }
    return arr.join('')
}

mainFunc()