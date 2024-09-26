const brailleLetters = {
    'A': 'O.....','B': 'O.O...','C': 'OO....','D': 'OO.O..','E': 'O..O..','F': 'OOO...','G': 'OOOO..','H': 'O.OO..','I': '.OO...','J': '.OOO..','K': 'O...O.','L': 'O.O.O.','M': 'OO..O.',
    'N': 'oo.oo.','O': 'O..OO.','P': 'OOO.O.','Q': 'OOOOO.','R': 'O.OOO.','S': '.00.0.','T': '.OOOO.','U': 'O...OO','V': '0.0.00','W': '.OOO.O','X': 'OO..OO','Y': 'OO.OOO','Z': 'O..OOO',

    'CAPITAL_FOLLOWS': '.....O',

    ' ': '......'
};

const brailleNumbers = {
    '0': '.OOO..','1': 'O.....','2': 'O.O...','3': 'OO....','4': 'OO.O..','5': 'O..O..','6': 'OOO...','7': 'OOOO..','8': 'O.OO..','9': '.OO...',

    'NUMBER_FOLLOWS': '.O.OOO'
};




function textToBraille (text) {
    let braille = '';
    let number = false;

    for (let i = 0; i < text.length; i++) {
        let char = text[i];
        //console.log(braille);
        if(char >= 'A' && char <= 'Z') {
            braille += brailleLetters['CAPITAL_FOLLOWS'] + brailleLetters[char];
        }
        else if (char >= '0' && char <= '9') {
            if(!number){
                braille += brailleNumbers['NUMBER_FOLLOWS']
                number = true;
            }
            braille += brailleNumbers[char]
        }
        else if (brailleLetters[char]){
            number = false;
            braille += brailleLetters[char] || '';
        }
        else {
            number =false
            braille += brailleLetters[char.toUpperCase()] || '';
        }

    }
    return braille;
}

const reverseBL = Object.entries(brailleLetters).reduce((acc, [key, value]) => {
    acc[value] = key;
    return acc;
}, {});

const reverseBN = Object.entries(brailleNumbers).reduce((acc, [key, value]) => {
    acc[value] = key;
    return acc;
}, {});

function brailleToText(braille) {
    let splitBraille = braille.match(/.{1,6}/g);
    let text = '';
    let capital = false;
    let number = false;

    for(let i = 0; i < splitBraille.length; i++) {
        let char = splitBraille[i];
        //console.log(text);
        if (char === brailleLetters['CAPITAL_FOLLOWS']) {
            capital = true;
        }
        else if (char === brailleNumbers['NUMBER_FOLLOWS']) {
            number = true;
        }
        else if (number && reverseBN[char] >= '1' && reverseBN[char] <= '9') {
            text += reverseBN[char];
        }
        else {
            if (capital && reverseBL[char] >= 'A' && reverseBL[char] <= 'Z') {
                text += reverseBL[char];
                capital = false;

            }
            else {
                text += reverseBL[char].toLowerCase();
            }

            if (reverseBL[char] === ' ') {
                number = false;
            }
        }
    }
    return text;

}


if (require.main === module) {
    const input = process.argv.slice(2).join(' ');
    if (input.includes('O') || input.includes('.')) {
        console.log(brailleToText(input));
    } else {
        console.log(textToBraille(input));
    }
}
module.exports = { textToBraille, brailleToText};