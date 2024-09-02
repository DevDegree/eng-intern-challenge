// Isabelle Choi 
// IsabelleLissina@gmail.com

const BrailleAlphabet = {
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
    CAPITAL: ".....O",
    DECIMAL: "..O.OO",
    NUMBER: ".O.OOO",
    DOT: "O.....",
    COMMA: ".O....",
    QUESTION_MARK: ".O..O.",
    EXCLAMATION_MARK: ".O.O.O",
    COLON: "O..O.O",
    SEMICOLON: "OO....",
    HYPHEN: ".O..O.",
    SLASH: ".O.O..",
    LESS_THAN: "O...OO",
    GREATER_THAN: "O..O.O",
    OPEN_PAREN: "O..OOO",
    CLOSE_PAREN: ".O.OO.",
    SPACE: "......"
};

const BrailleNumbers = {
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


function getBrailleToEnglishTranslation(key){
    return BrailleAlphabet[key];
}

function getBrailleNumberTranslation(key){
    return BrailleNumbers[key];
}

function getEnglishToBrailleTranslation(braille) {
    const brailleToEnglish = Object.fromEntries(
        Object.entries(BrailleAlphabet).map(([key, value]) => [value, key])
    );
    return brailleToEnglish[braille];
}

function isUpperCase(letter) {
    return letter === letter.toUpperCase() && letter !== letter.toLowerCase();
}

const input = process.argv.slice(2).join(' ');
const isEnglish = input.split('').some(letter => letter !== 'O' && letter !== '.');

if (!isEnglish) {
    getBrailleToEnglish(input)
}
getEnglishFromBraille(input)

function getBrailleToEnglish(input) {
    const inputSize = 6;
    let brailleInputSplit = [];
    let brailleTranslation = [];
    let translation = [];

    for(let i = 0; i < input.length; i+= inputSize){
        brailleInputSplit.push(input.slice(i, i + inputSize))
    }

    brailleInputSplit.forEach(letter => {
        brailleTranslation.push(getEnglishToBrailleTranslation(letter));
    })

    for(let i = 0; i < brailleTranslation.length; i++) {
        if (brailleTranslation[i] === "CAPITAL"){
            translation.push(brailleTranslation[i + 1].toUpperCase())
            i++;
            i++;
        }
        if(brailleTranslation[i] === "SPACE"){
            translation.push(" ")
        }
        else {
            translation.push(brailleTranslation[i])
        }
    }
    console.log(translation.join(""));
}

function getEnglishFromBraille(input){
    let translation = [];
    const inputLetters = input.split("");
    let previousWasNumber = false;
    let previousWasCapital = false;

    inputLetters.forEach(letter => {
        let isNumber = !isNaN(parseInt(letter, 10));

        if (isNumber) {
            if (!previousWasNumber) {
                translation.push(BrailleAlphabet.NUMBER);
            }
            translation.push(getBrailleNumberTranslation(letter));
            previousWasNumber = true; 
        } 
        else {
            if (letter === " ") {
              translation.push(BrailleAlphabet.SPACE);
            }
            if(isUpperCase(letter)){
                if(!previousWasCapital){
                    translation.push(BrailleAlphabet.CAPITAL)
                }
                translation.push(getBrailleToEnglishTranslation(letter.toLowerCase()));
                previousWasCapital = true;
            }
            else{
                previousWasCapital = false;
                previousWasNumber = false;
                translation.push(getBrailleToEnglishTranslation(letter.toLowerCase()));
            }
        }
    });

    console.log(translation.join(""))
}