let brailleAlphabet = [
    ['A', "O....."],
    ['B', "O.O..."],
    ['C', "OO...."],
    ['D', "OO.O.."],
    ['E', "O..O.."],
    ['F', "OOO..."],
    ['G', "OOOO.."],
    ['H', "O.OO.."],
    ['I', ".OO..."],
    ['J', ".OOO.."],
    ['K', "O...O."],
    ['L', "O.O.O."],
    ['M', "OO..O."],
    ['N', "OO.OO."],
    ['O', "O..OO."],
    ['P', "OOO.O."],
    ['Q', "OOOOO."],
    ['R', "O.OOO."],
    ['S', ".OO.O."],
    ['T', ".OOOO."],
    ['U', "O...OO"],
    ['V', "O.O.OO"],
    ['W', ".OOO.O"],
    ['X', "OO..OO"],
    ['Y', "OO.OOO"],
    ['Z', "O..OOO"]
]

function translate(text) {
    text = text.toUpperCase();
    let result = '';

    for (let character of text) {
        let braille = brailleAlphabet.find(([letter]) => letter === character);
        if (braille) {
            result += braille[1];
        } else {
            result += 'not in the alphabet yet';
        }
    }

    return result.trim();
}

let input = '';

process.argv.forEach(function (val, index, array) {
    if (index > 1) {
        input += val;
    }
});

console.log(translate(input));

module.exports = translate;
