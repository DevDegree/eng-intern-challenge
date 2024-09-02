process.stdin.setEncoding('utf8');

const BrailleReference = {
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
    CAPITAL: ".....O",
    DECIMAL: "..O.OO",
    NUMBER: "..OO.O",
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
 

const brailleToEnglish = Object.fromEntries(
    Object.entries(BrailleReference).map(([key, value]) => [value, key])
);

function getBrailleToEnglishTranslation(key){
    return BrailleReference[key];
}

function getEnglishToBrailleTranslation(braille) {
    return brailleToEnglish[braille];
}

const input = process.argv.slice(2).join('');
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

    inputLetters.forEach(letter => {
        translation.push(getBrailleToEnglishTranslation(letter))
    })

    console.log(translation.join(""))
}