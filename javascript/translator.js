#!/usr/bin/env node

// this function assumes that all CLI arguments are of the same type
// ie: three arguments provided in either all english, or all braille
const braille = /^[\.O]+$/;
const english = /[a-zA-Z0-9\.\,\?\!\:\;\-\<\>\(\)\/\\\s ]/g;
const uppercase = /^[A-Z]*$/;
const numeric = /^[+-]?\d+(\.\d+)?$/;

const dictionary = [
    ["a", "O....."], ["b", "O.O..."], ["c", "OO...."], ["d", "OO.O.."], ["e", "O..O.."], ["f", "OOO..."], ["g", "OOOO.."],
    ["h", "O.OO.."], ["i", ".OO..."], ["j", ".OOO.."], ["k", "O...O."], ["l", "O.O.O."], ["m", "OO..O."], ["n", "OO.OO."],
    ["o", "O..OO."], ["p", "OOO.O."], ["q", "OOOOO."], ["r", "O.OOO."], ["s", ".OO.O."], ["t", ".OOOO."], ["u", "O...OO"],
    ["v", "O.O.OO"], ["w", ".OOO.O"], ["x", "OO..OO"], ["y", "OO.OOO"], ["z", "O..OOO"], ["1", "O....."], ["2", "O.O..."],
    ["3", "OO...."], ["4", "OO.O.."], ["5", "O..O.."], ["6", "OOO..."], ["7", "OOOO.."], ["8", "O.OO.."], ["9", ".OO..."],
    ["0", ".OOO.."], [".", "..OO.O"], [",", "..O..."], ["?", "..O.OO"], ["!", "..OOO."], [":", "..OO.."], [";", "..O.O."],
    ["-", "....OO"], ["/", ".O..O."], ["<", ".OO..O"], [">", "O..OO."], ["(", "O.O..O"], [")", ".O.OO."], [" ", "......"]
]

// Access command-line arguments
var args = process.argv.splice(2);
var input = args.join(" ");

function lang(input) {
    if (input.length == 0) {
        console.log("\nPlease input a string to translate. \n");
    } else if (braille.test(input)) {
        if (input.length % 6 !== 0) {
            console.log("\nAmbiguous input. Please try again.\n");
        } else {
            cluster(input);
        }
    } else if (english.test(input)) {
        engToBraille(input);
    } else {
        console.log("\nUndefined error.");
    }
}

function cluster(input) {
    const inpArr = [];

    for (i = 0; i < input.length; i += 6) {
        inpArr.push(input.substring(i, i + 6));
    }

    brailleToEng(inpArr);
}

function engToBraille(input) {
    var message = "";

    var mode = 0;

    for (i = 0; i < input.length; i++) {

        if (!uppercase.test(input[i - 1]) && uppercase.test(input[i])) {
            mode = 0;
            message += ".....O";
            message += dictionary.slice(mode).find(defn => defn[0] === input[i].toLowerCase())[1];
        } else if (!numeric.test(input[i - 1]) && numeric.test(input[i])) {
            mode = 26;
            message += ".O.OOO";
            message += dictionary.slice(mode).find(defn => defn[0] === input[i])[1];
        } else if (!numeric.test(input[i]) && mode !== 0) {
            mode = 0;
            message += dictionary.slice(mode).find(defn => defn[0] === input[i])[1];
        } else if (mode === 26 && input[i + 1] === "." && numeric.test(input[i + 2])) {
            message += dictionary.slice(mode).find(defn => defn[0] === input[i])[1];
            message += ".O...O";
            i++;
        } else {
            message += dictionary.slice(mode).find(defn => defn[0] === input[i])[1];
        }

    }

    console.log(message);
}

function brailleToEng(inpArr) {
    var message = "";

    var mode = 0;

    for (i = 0; i < inpArr.length; i++) {
        if (inpArr[i] === ".....O") {
            mode = 0;
            message += dictionary.slice(mode).find(defn => defn[1] === inpArr[i + 1])[0].toUpperCase();
            i++;
        } else if (inpArr[i] === ".O.OOO") {
            mode = 26;
        } else if (mode === 26 && (dictionary.slice(mode).find(defn => defn[1] === inpArr[i]) === undefined)) {
            mode = 0;
            message += dictionary.slice(mode).find(defn => defn[1] === inpArr[i])[0];
        } else {
            message += dictionary.slice(mode).find(defn => defn[1] === inpArr[i])[0];
        }
    }

    console.log(message);
}

lang(input); 