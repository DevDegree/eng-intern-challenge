"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.isNumeric = exports.numbersToBrailleMap = exports.englishToBrailleMap = exports.brailleToEnglishMap = exports.brailleToNumberMap = exports.brailleInputRegex = void 0;
exports.brailleInputRegex = /^([OO.]{6})+$/;
exports.brailleToNumberMap = new Map([
    ["O.....", "1"],
    ["O.O...", "2"],
    ["OO....", "3"],
    ["OO.O..", "4"],
    ["O..O..", "5"],
    ["OOO...", "6"],
    ["OOOO..", "7"],
    ["O.OO..", "8"],
    [".OO...", "9"],
    [".OOO..", "0"]
]);
exports.brailleToEnglishMap = new Map([
    ["O.....", "a"],
    ["O.O...", "b"],
    ["OO....", "c"],
    ["OO.O..", "d"],
    ["O..O..", "e"],
    ["OOO...", "f"],
    ["OOOO..", "g"],
    ["O.OO..", "h"],
    [".OO...", "i"],
    [".OOO..", "j"],
    ["O...O.", "k"],
    ["O.O.O.", "l"],
    ["OO..O.", "m"],
    ["OO.OO.", "n"],
    ["O..OO.", "o"],
    ["OOO.O.", "p"],
    ["OOOOO.", "q"],
    ["O.OOO.", "r"],
    [".OO.O.", "s"],
    [".OOOO.", "t"],
    ["O...OO", "u"],
    ["O.O.OO", "v"],
    [".OOO.O", "w"],
    ["OO..OO", "x"],
    ["OO.OOO", "y"],
    ["O..OOO", "z"],
    ["......", " "],
    [".....O", "capital"],
    [".O.OOO", "number"]
]);
exports.englishToBrailleMap = new Map(Array.from(exports.brailleToEnglishMap.entries()).map(([braille, english]) => [english, braille]));
exports.numbersToBrailleMap = new Map(Array.from(exports.brailleToNumberMap.entries()).map(([braille, numbers]) => [numbers, braille]));
const isNumeric = (value) => {
    return !isNaN(parseFloat(value)) && isFinite(Number(value));
};
exports.isNumeric = isNumeric;
