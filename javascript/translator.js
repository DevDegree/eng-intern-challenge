const brailleLetters = {
    a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..", e: "O..O..",
    f: "OOO...", g: "OOOO..", h: "O.OO..", i: ".OO...", j: ".OOO..",
    k: "O...O.", l: "O.O.O.", m: "OO..O.", n: "OO.OO.", o: "O..OO.",
    p: "OOO.O.", q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.",
    u: "O...OO", v: "O.O.OO", w: ".OOO.O", x: "OO..OO", y: "OO.OOO", z: "O..OOO"
};

const brailleNumbers = {
    1: "O.....", 2: "O.O...", 3: "OO....", 4: "OO.O..", 5: "O..O..",
    6: "OOO...", 7: "OOOO..", 8: "O.OO..", 9: ".OO...", 0: ".OOO.."
};

const brailleSpecial = {
    space: "......", period: "O.O.OO", comma: "O.....",
    question: ".OOO.O", exclamation: ".OO.OO", colon: "OO....",
    semicolon: "O.O...", hyphen: "O....O", slash: "O...OO",
    lessThan: "OO..OO", greaterThan: ".O.OOO", leftParen: "O.OO..",
    rightParen: "O.OO..", quotation: "O.O.O.", apostrophe: "O.....",
    atSymbol: "O.OO.O", ampersand: "O.OO..", capital: ".....O",
    number: ".O.OOO"
};