const englishToBrailleMap = {
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
    " ": "......"  
};

const brailleToEnglishMap = Object.fromEntries(Object.entries(englishToBrailleMap).map(([englishChar, brailleCode]) => [brailleCode, englishChar]));

const numberToBrailleMap = {
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
};

const brailleToNumberMap = Object.fromEntries(Object.entries(numberToBrailleMap).map(([numberChar, brailleCode]) => [brailleCode, numberChar]));

const specialBrailleSymbols = {
    "capital": ".....O",
    "number": ".O.OOO"
};

function textToBraille(inputText) {
    let brailleResult = [];
    let isNumberMode = false;

    for (let character of inputText) {
        if (/\d/.test(character)) {   
            if (!isNumberMode) {
                isNumberMode = true;
                brailleResult.push(specialBrailleSymbols.number);
            }
            brailleResult.push(numberToBrailleMap[character]);
        } else if (character === ' ') {  
            isNumberMode = false;
            brailleResult.push(englishToBrailleMap[character]);
        } else if (character.toUpperCase() === character && character.toLowerCase() in englishToBrailleMap) {   
            brailleResult.push(specialBrailleSymbols.capital);
            brailleResult.push(englishToBrailleMap[character.toLowerCase()]);
        } else {
            brailleResult.push(englishToBrailleMap[character.toLowerCase()]);
        }
    }

    return brailleResult.join('');
}

function brailleToText(brailleInput) {
    let englishResult = [];
    let i = 0;
    const brailleLength = brailleInput.length;
    let isNumberMode = false;

    while (i < brailleLength) {
        let brailleChunk = brailleInput.slice(i, i + 6);
        if (brailleChunk === specialBrailleSymbols.capital) {
            i += 6;
            brailleChunk = brailleInput.slice(i, i + 6);
            englishResult.push(brailleToEnglishMap[brailleChunk].toUpperCase());
        } else if (brailleChunk === specialBrailleSymbols.number) {
            isNumberMode = true;
        } else if (brailleChunk === '......') {  
            isNumberMode = false;
            englishResult.push(brailleToEnglishMap[brailleChunk]);
        } else {
            if (isNumberMode) {
                englishResult.push(brailleToNumberMap[brailleChunk]);
            } else {
                englishResult.push(brailleToEnglishMap[brailleChunk]);
            }
        }

        i += 6;
    }
    return englishResult.join('');
}

function isBrailleInput(inputText) {
    return /^[.O]+$/.test(inputText);
}

function main() {
    const inputText = process.argv.slice(2).join(' ');

    if (isBrailleInput(inputText)) {
        console.log(brailleToText(inputText));
    } else {
        console.log(textToBraille(inputText));
    }
}

if (require.main === module) {
    main();
}
