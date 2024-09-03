let englishToBrailleMap = {};

// Add key-value pairs to the map
englishToBrailleMap['A'] = 'O.....';
englishToBrailleMap['B'] = 'O.O...';
englishToBrailleMap['C'] = 'OO....';
englishToBrailleMap['D'] = 'OO.O..';
englishToBrailleMap['E'] = 'O..O..';
englishToBrailleMap['F'] = 'OOO...';
englishToBrailleMap['G'] = 'OOOO..';
englishToBrailleMap['H'] = 'O.OO..';
englishToBrailleMap['I'] = '.OO...';
englishToBrailleMap['J'] = '.OOO..';
englishToBrailleMap['K'] = 'O...O.';
englishToBrailleMap['L'] = 'O.O.O.';
englishToBrailleMap['M'] = 'OO..O.';
englishToBrailleMap['N'] = 'OO.OO.'; 
englishToBrailleMap['O'] = 'O..OO.';
englishToBrailleMap['P'] = 'OOO.O.';
englishToBrailleMap['Q'] = 'OOOOO.';
englishToBrailleMap['R'] = 'O.OOO.';
englishToBrailleMap['S'] = '.OO.O.';
englishToBrailleMap['T'] = '.OOOO.';
englishToBrailleMap['U'] = 'O...OO';
englishToBrailleMap['V'] = 'O.O.OO';
englishToBrailleMap['W'] = '.OOO.O';
englishToBrailleMap['X'] = 'OO..OO';
englishToBrailleMap['Y'] = 'OO.OOO';
englishToBrailleMap['Z'] = 'O..OOO';
englishToBrailleMap['1'] = 'O.....';
englishToBrailleMap['2'] = 'O.O...';
englishToBrailleMap['3'] = 'OO....';
englishToBrailleMap['4'] = 'OO.O..';
englishToBrailleMap['5'] = 'O..O..';
englishToBrailleMap['6'] = 'OOO...';
englishToBrailleMap['7'] = 'OOOO..';
englishToBrailleMap['8'] = 'O.OO..';
englishToBrailleMap['9'] = '.OO...';
englishToBrailleMap['0'] = '.OOO..';
englishToBrailleMap[' '] = '......'; //space
englishToBrailleMap['CapitalFollows'] = '.....O';
englishToBrailleMap['DecimalFollows'] = '.O...O';
englishToBrailleMap['NumberFollows'] = '.O.OOO';

let brailleToEnglishMap = {};

Object.entries(englishToBrailleMap).forEach((entry) => {
    brailleToEnglishMap[entry[1]] = entry[0]
})


function isBraille(inputtedString) {
    if(inputtedString.length < 6){
        return false;
    }
    
   const firstSix = inputtedString.substring(0,6)

   const foundInBrailleToEnglishMap = brailleToEnglishMap[firstSix]

   if (foundInBrailleToEnglishMap) {
     return true
   }

   return false
}

function isCharNumber(c) {
    return c >= '0' && c <= '9';
}

function isLetter(c) {
    return c.toLowerCase() != c.toUpperCase();
}

function convertEnglishNumberToBraille(englishNumberString) {
    let brailleNumber = englishToBrailleMap['NumberFollows']
    for (const c of englishNumberString) {
        brailleNumber += englishToBrailleMap[c]
    }

    brailleNumber += englishToBrailleMap[' ']

    return brailleNumber
}


function convertEnglishToBraille(englishString) {
    let brailleString = ""
    for (let i = 0; i < englishString.length; i++) {
        const englishChar = englishString[i]
        const isCharLetter = isLetter(englishChar)

        const isNumber = isCharNumber(englishChar)

        if (isNumber) {
            let numIdxEnd = i

            while (isCharNumber(englishString[numIdxEnd])) {
                numIdxEnd++
            }

            const numberSubStr = englishString.substring(i, numIdxEnd)

            const brailleNumber = convertEnglishNumberToBraille(numberSubStr)

            brailleString = brailleString + brailleNumber

            i = numIdxEnd
        }

        else if (isCharLetter) {
            let braille = ""
            const isUpper = englishChar == englishChar.toUpperCase()
            
            if (isUpper) {
                braille +=  englishToBrailleMap['CapitalFollows']
            }

            braille += englishToBrailleMap[englishChar.toUpperCase()]

            brailleString += braille
        }

        else {
            brailleString += englishToBrailleMap[englishChar]
        }
    }

    return brailleString
}

//convertEnglishToBraille("Abc 123")

function convertBrailleToEnglish(brailleString) {

    let englishString = ""
    let capsOn = false
    for (let i = 0; i < brailleString.length; i += 6) {
        if (i == brailleString.length) {
            break
        }
        const brailleInput = brailleString.substring(i, i + 6)

        const english = brailleToEnglishMap[brailleInput]
        
        if (english === "CapitalFollows") {
            capsOn = true
            continue
        }

        if (capsOn) {
            englishString += english.toUpperCase()
            capsOn = false
        }
        else {
            englishString += english.toLowerCase()
        }
    }

    return englishString

}


const inputtedString = process.argv.slice(2, process.argv.length).join(" ")


const isInputBraille = isBraille(inputtedString)

if (isInputBraille) {
    console.log(convertBrailleToEnglish(inputtedString))
}

else {
    console.log(convertEnglishToBraille(inputtedString))
}

