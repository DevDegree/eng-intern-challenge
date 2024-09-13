const ENGLISH_TO_BRAILLE = [
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
    ['.', "..OO.O"],
    [',', "..O..."],
    ['?', "..O.OO"],
    ['!', "..OOO."],
    [':', "..OO.."],
    [';', "..O.O."],
    ['-', "....OO"],
    ['/', ".O..O."],
    ['<', ".OO..O"],
    ['>', "O..OO."],
    ['(', "O.O..O"],
    [')', ".O.OO."],
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
    ['0', ".OOO.."],
]

const CAPITAL_MODIFIER = '.....O';
const NUMBER_MODIFIER = '.O.OOO';
const BRAILLE_REGEX = /^[\.O]+$/;
const CAPITAL_REGEX = /[A-Z]/;
const NUMBER_REGEX = /[0-9]/;
const TEXT_STATE = 'TEXT_STATE';
const NUMBER_STATE = 'NUMBER_STATE';
const OTHER_CHARACTER = 'OTHER_CHARACTER';
const UPPERCASE_CHARACTER = 'UPPERCASE_CHARACTER';
const NUMBER_CHARACTER = 'NUMBER_CHARACTER';

function translate(text) {
    let result = '';
    if (BRAILLE_REGEX.test(text)) {
        let state = TEXT_STATE;
        for (let i = 0; i < text.length; i += 6) {
            let brailleCharacter = text.substring(i, i + 6);
            switch (brailleCharacter) {
                case CAPITAL_MODIFIER: {
                    state = TEXT_STATE;
                    i += 6;
                    let nextBrailleCharacter = text.substring(i, i + 6);
                    result += brailleToEnglish(nextBrailleCharacter, OTHER_CHARACTER).toUpperCase();
                    break;
                }
                case NUMBER_MODIFIER: {
                    state = NUMBER_STATE;
                    break;
                }
                default: {
                    if (brailleCharacter === englishToBraille(' ')) state = TEXT_STATE;
                    if (state === NUMBER_STATE) result += brailleToEnglish(brailleCharacter, NUMBER_CHARACTER);
                    else result += brailleToEnglish(brailleCharacter, OTHER_CHARACTER);

                }
            }
        }
    } else {
        let state = TEXT_STATE;
        for (let character of text) {
            switch (testEnglishCharacter(character)) {
                case OTHER_CHARACTER: {
                    state = TEXT_STATE;
                    result += englishToBraille(character);
                    break;
                }
                case UPPERCASE_CHARACTER: {
                    state = TEXT_STATE;
                    result += CAPITAL_MODIFIER;
                    result += englishToBraille(character.toLowerCase());
                    break;
                }
                case NUMBER_CHARACTER: {
                    if (state !== NUMBER_STATE) {
                        result += NUMBER_MODIFIER;
                        state = NUMBER_STATE;
                    }
                    result += englishToBraille(character);
                    break;
                }
            }
        }
    }
    return result;
}

function testEnglishCharacter(character) {
    if (CAPITAL_REGEX.test(character)) return UPPERCASE_CHARACTER;
    else if (NUMBER_REGEX.test(character)) return NUMBER_CHARACTER;
    else return OTHER_CHARACTER;
}

function englishToBraille(characterToFind) {
    return ENGLISH_TO_BRAILLE.find(([character]) => character === characterToFind)[1];
}

function brailleToEnglish(characterToFind, characterType) {
    return ENGLISH_TO_BRAILLE.find(([englishCharacter, brailleCharacter]) => brailleCharacter === characterToFind && testEnglishCharacter(englishCharacter) === characterType)[0];
}

let input = '';

process.argv.forEach(function (val, index, array) {
    if (index > 1) {
        if (index > 2) {
            input += ' ' + val;
        } else {
            input += val
        }
    }
});

console.log(translate(input));

module.exports = translate;
