const enBrMap = new Map([
    ['a', "O....."],
    ['b', "O.O..."],
    ['c', "OO...."],
    ['d', "OO.O.."],
    ['e', "O..O.."],
    ['f', "OOO..."],
    ['g', "OOOO.."],
    ['h', "O.OO.."],
    ['i', ".OO..."],
    ['j', ".OOO.."],
    ['k', "O...O."],
    ['l', "O.O.O."],
    ['m', "OO..O."],
    ['n', "OO.OO."],
    ['o', "O..OO."],
    ['p', "OOO.O."],
    ['q', "OOOOO."],
    ['r', "O.OOO."],
    ['s', ".OO.O."],
    ['t', ".OOOO."],
    ['u', "O...OO"],
    ['v', "O.O.OO"],
    ['w', ".OOO.O"],
    ['x', "OO..OO"],
    ['y', "OO.OOO"],
    ['z', "O..OOO"],
    [' ', "......"],
    ['1', "O....."],
    ['2', "O.O..."],
    ['3', "OO...."],
    ['4', "OO.O.."],
    ['5', "O..O.."],
    ['6', "OOO..."],
    ['7', "OOOO.."],
    ['8', "O.OO.."],
    ['9', ".OO..."],
    ['0', ".OOO.."]
]);
const brEnMap = new Map([
    ["O.....", 'a'],
    ["O.O...", 'b'],
    ["OO....", 'c'],
    ["OO.O..", 'd'],
    ["O..O..", 'e'],
    ["OOO...", 'f'],
    ["OOOO..", 'g'],
    ["O.OO..", 'h'],
    [".OO...", 'i'],
    [".OOO..", 'j'],
    ["O...O.", 'k'],
    ["O.O.O.", 'l'],
    ["OO..O.", 'm'],
    ["OO.OO.", 'n'],
    ["O..OO.", 'o'],
    ["OOO.O.", 'p'],
    ["OOOOO.", 'q'],
    ["O.OOO.", 'r'],
    [".OO.O.", 's'],
    [".OOOO.", 't'],
    ["O...OO", 'u'],
    ["O.O.OO", 'v'],
    [".OOO.O", 'w'],
    ["OO..OO", 'x'],
    ["OO.OOO", 'y'],
    ["O..OOO", 'z'],
    ["......", ' '],
]);
const brEnNumMap = new Map([
    ["O.....", '1'],
    ["O.O...", '2'],
    ["OO....", '3'],
    ["OO.O..", '4'],
    ["O..O..", '5'],
    ["OOO...", '6'],
    ["OOOO..", '7'],
    ["O.OO..", '8'],
    [".OO...", '9'],
    [".OOO..", '0'],
]);
const CAP_FOLLOWS = ".....O";
const NUM_FOLLOWS = ".O.OOO";
const SPACE = "......";

/*
 * As stated in the technical spec, this translator will only include alphanumerical
 * characters and spaces for the english strings. Since every braille encoding has at
 * least one non-raised area (i.e., represented as a period), the input is in braille
 * if and only if it contains a period -- otherwise, the precondition as detailed in
 * spec has failed.
 *
 * As a disclaimer, I made extensive use of outside documentation to complete this task,
 * as I am not familiar with JavaScript in the context of command-line tools, such as
 * getting execution arguments. I would've done without using Java, C, or C++.
 *
 * Further, we note that because of how node processes arguments, any whitespace
 * between words of the input string are treated as a single space; some shells may not
 * support process.execArgv and thus I have opted to do with otherwise.
*/

function toEnglish(str) {
    var ret = "";
    var cap = false;
    var num = false;

    for (var i = 0; i < str.length; i += 6) {
        var segment = str.substring(i, i + 6);

        // End of number; reset num flag
        if (segment == SPACE) num = false;

        // Set caps flag
        if (segment == CAP_FOLLOWS) cap = true;

        // Set num flag
        else if (segment == NUM_FOLLOWS) num = true;

        // Get character
        else {
            var nextChar = num ?
                brEnNumMap.get(segment) :
                brEnMap.get(segment);

            // Apply capitalization
            if (cap) nextChar = nextChar.toUpperCase();

            // Reset caps flag
            cap = false;

            // Append to return
            ret += nextChar;
        }
    }

    return ret;
}

function toBraille(str) {
    var ret = "";
    var num = false;

    for (var i = 0; i < str.length; i++) {
        var cur = str.charAt(i);

        // First digit of a number; add num flag
        if (!num && '0' <= cur && cur <= '9') {
            ret += NUM_FOLLOWS;
            num = true;
        }
        if ('A' <= cur && cur <= 'Z') ret += CAP_FOLLOWS;

        // Next number will require a num flag
        if (cur == ' ') num = false;

        // Append encoding
        ret += enBrMap.get(cur.toLowerCase());
    }

    return ret;
}

// Entry point
var input = process.argv.slice(2).join(' ');

if (input.includes(".")) console.log(toEnglish(input));
else console.log(toBraille(input));
