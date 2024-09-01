// Mappings for English to Braille Translation
const englishToBraille = {
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
    " ": "......",
    CAPITAL: ".....O",
    NUMBER: ".O.OOO",
};

const numberToBraille = {
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
};

// Reverse mappings
const brailleToEnglish = {};
for (const [key, value] of Object.entries(englishToBraille)) {
    if (key !== "CAPITAL" && key !== "NUMBER") {
        brailleToEnglish[value] = key;
    }
}

const brailleToNumber = {};
for (const [key, value] of Object.entries(numberToBraille)) {
    brailleToNumber[value] = key;
}

// Check if the input is Braille (or English)
const isBraille = (text) => {
    if (text.length % 6 !== 0) {
        return false;
    }

    for (let char of text) {
        // only '0' and '.' are valid Braille characters
        if (char !== "O" && char !== ".") {
            return false;
        }
    }

    return true;
};

// CLI
const main = () => {
    const args = process.argv.slice(2);
    if (args.length < 1) {
        console.log("ERROR: Missing arguments | Usage: node translator.js <str>");
        return;
    }

    const inputText = args.join(' ');
    console.log('inputText is: ', inputText);

    if (isBraille(inputText)) {
        console.log('Translating Braille to English.');
    } else {
        console.log('Translating English to Braille.');
    }
}

if (require.main === module) {
    main();
}
