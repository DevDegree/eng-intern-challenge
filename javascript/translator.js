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
    0: ".OOOO.",
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
};

const capitalIndicator = ".....O";
const numberIndicator = ".O.OOO";

const englishToBraille = (text) => {
    let braille = "";
    let isNumber = false;

    for (let char of text) {
        if (char >= "A" && char <= "Z") {
            braille += capitalIndicator + brailleMap[char.toLowerCase()];
        } else if (char >= "0" && char <= "9") {
            if (!isNumber) {
                braille += numberIndicator;
                isNumber = true;
            }
            braille += brailleMap[char];
        } else {
            if (isNumber && char !== " ") isNumber = false;
            braille += brailleMap[char];
        }
    }

    return braille;
};

const brailleToEnglish = (braille) => {
    let english = "";
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < braille.length; i += 6) {
        const brailleChar = braille.slice(i, i + 6);

        if (brailleChar === capitalIndicator) {
            isCapital = true;
        } else if (brailleChar === numberIndicator) {
            isNumber = true;
        } else {
            let char = Object.keys(brailleMap).find(
                (key) => brailleMap[key] === brailleChar
            );

            if (isNumber) {
                char = Object.keys(brailleMap).find(
                    (key) =>
                        brailleMap[key] === brailleChar &&
                        key >= "0" &&
                        key <= "9"
                );
            }

            if (isCapital) {
                char = char.toUpperCase();
                isCapital = false;
            }

            english += char || "";
            if (isNumber && char === " ") isNumber = false;
        }
    }

    return english;
};

const isBraille = (input) => {
    return /^[O.]+$/.test(input);
};

const translate = () => {
    const args = process.argv.slice(2);
    const input = args.join(" ");

    if (isBraille(input)) {
        console.log(brailleToEnglish(input));
    } else {
        console.log(englishToBraille(input));
    }
};

translate();
