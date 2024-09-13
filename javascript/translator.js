#!/usr/bin/env node

const brailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', ' ': '......'
}


const reverseBrailleDict = Object.keys(brailleDict).reduce((obj, key) => {
    obj[brailleDict[key]] = key
    return obj
}, {});


const CAPITAL_FOLLOWS = '.....O'
const NUMBER_FOLLOWS = '.O.OOO'

function englishToBraille(text) {
    let brailleOutput = []
    let isNumber = false
    
    for (let char of text) {
        if (char >= '0' && char <= '9') {
            if (!isNumber) {
                brailleOutput.push(NUMBER_FOLLOWS)
                isNumber = true;
            }
            brailleOutput.push(brailleDict[char])
        } else {
            if (isNumber) {
                isNumber = false
            }
            if (char === ' ') {
                brailleOutput.push(brailleDict[char])
            } else if (char >= 'A' && char <= 'Z') {
                brailleOutput.push(CAPITAL_FOLLOWS)
                brailleOutput.push(brailleDict[char.toLowerCase()]);
            } else {
                brailleOutput.push(brailleDict[char] || '......')
            }
        }
    }
    return brailleOutput.join('')
}

function brailleToEnglish(brailleText) {
    let englishOutput = []
    let isCapital = false
    let isNumber = false
    
    const brailleChars = brailleText.match(/.{1,6}/g)
    
    for (let brailleChar of brailleChars) {
        if (brailleChar === CAPITAL_FOLLOWS) {
            isCapital = true
            continue
        }
        if (brailleChar === NUMBER_FOLLOWS) {
            isNumber = true
            continue
        }

        let char = reverseBrailleDict[brailleChar] || ' '
        if (isNumber) {
            englishOutput.push(char)
            isNumber = false
        } else {
            if (isCapital) {
                englishOutput.push(char.toUpperCase())
                isCapital = false
            } else {
                englishOutput.push(char)
            }
        }
    }
    return englishOutput.join('')
}


function translate(inputString) {

    if (/^[O.]+$/.test(inputString)) {

        console.log(brailleToEnglish(inputString))
    } else {
        console.log(englishToBraille(inputString))
    }
}


function main() {
    const args = process.argv.slice(2);
    if (args.length === 0) {
        return
    }
    const inputString = args.join(' ')
    translate(inputString)
}

main()
