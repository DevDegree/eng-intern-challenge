const brailleMap = {
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
    0: ".OOO..",
    1: "O.....",
    2: "O.O...",
    3: "OO....",
    4: "OO.O..",
    5: "O..O..",
    6: "OOO...",
    7: "OOOO..",
    8: "O.OO..",
    9: ".OO...",
    " ": "......",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OO..",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",


    // next char modifiers 
    'capital': '.....O', 
    'decimal': '.O...O', 
    'number': '.O.OOO',
};

const reverseBrailleMap = Object.entries(brailleMap).reduce((acc, [k, v]) => {
    acc[v] = k;
    return acc;
}, {});


const isBraille = str => /^[O.\s]+$/.test(str) && str.replace(/\s/g, '').length % 6 === 0;

const toBraille = text => {
    let res = '';
    let isNumber = false;
    for (const char of text) {
        if (/[A-Z]/.test(char)) {
            res += brailleMap['capital'] + brailleMap[char.toLowerCase()];
            isNumber = false;
        } else if (/[0-9]/.test(char)) {
            if (!isNumber) {
                res += brailleMap['number'];
                isNumber = true;
            }
            res += brailleMap[char];
        } else if (char === '.') {
            if (isNumber) {
                res += brailleMap['decimal'];
            } else {
                res += brailleMap[char];
            }
        } else {
            isNumber = false;
            res += brailleMap[char.toLowerCase()] || '';
        }
    }
    return res;
};

const toEnglish = brailleStr => {
    const characters = brailleStr.match(/.{6}/g) || [];
    let result = '';
    let isCapital = false;
    let isNumber = false;

    for (const char of characters) {
        if (char === brailleMap['capital']) {
            isCapital = true;
        } else if (char === brailleMap['number']) {
            isNumber = true;
        } else if (char === brailleMap['decimal']) {
            if (isNumber) {
                result += '.';
            } else {
                result += '.'; // what do we do when we get a decimal modifier without a number modifier?
            }
        } else {
            let translated = reverseBrailleMap[char];

            if (translated === undefined) {
                throw new Error('Invalid braille character');
            }

            if (isNumber) {
                if (translated >= 'a' && translated <= 'j') { // a-j share the same braille pattern a=1, b=2, ..., i=9, j=0
                    translated = String((translated.charCodeAt(0) - 'a'.charCodeAt(0) + 1) % 10);
                } else if (translated === ' ') {
                    isNumber = false;
                } 
            }

            if (isCapital) {
                translated = translated.toUpperCase();
                isCapital = false;
            }

            result += translated;
        }
    }
    return result;
};


const main = () => {
    const input = process.argv.slice(2).join(' ');
    return isBraille(input) ? toEnglish(input) : toBraille(input);
};

console.log(main());

