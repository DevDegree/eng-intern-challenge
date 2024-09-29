const userInput = [];
process.argv.forEach((val, index) => {
    if (index > 1) userInput.push(val);
})
const message = userInput.join(' ');

const brailleToEnglish = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z'
}
const brailleToNumbers = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
}

const englishToBraille = Object.fromEntries(Object.entries(brailleToEnglish).map(([key, value]) => [value, key]));
const numberToBraille = Object.fromEntries(Object.entries(brailleToNumbers).map(([key, value]) => [value, key]));

const isBraille = (str) => {
   return /^[O.]+$/.test(str); 
}
const isAcceptedEnglish = (str) => {
    return /^[a-zA-z0-9 ]+$/.test(str);
}

var result = '';
if (isBraille(message)) {
    const brailleCharacters = message.match(/.{1,6}/g);
    var chars = []
    for (i = 0; i < brailleCharacters.length; i++) {
        if (brailleCharacters[i] === '.....O'){
            i++
            try {
                chars.push((brailleToEnglish[brailleCharacters[i]]).toUpperCase())
            } catch {
                chars.push('*')
            }
        }
        else if (brailleCharacters[i] === '.O.OOO') {
            i++
            for(i; i < brailleCharacters.length && brailleCharacters[i] != '......' ; i++) {
                try {
                    chars.push(brailleToNumbers[brailleCharacters[i]]);
                } catch {
                    chars.push('*');
                }
            }
        }
        else if (brailleCharacters[i] === '......') {
            try {
                chars.push(' ');
            } catch {
                chars.push('*');
            }
        }
        else {
            try {
                chars.push(brailleToEnglish[brailleCharacters[i]]);
            } catch {
                chars.push('*');
            }
        }
    }
    result = chars.join('');
}
else if (isAcceptedEnglish(message)) {
    const englishCharacters = message.split('');
    var chars = [];
    for (i = 0; i < englishCharacters.length; i++) {
        if (/^[A-Z]$/.test(englishCharacters[i])) {
            chars.push('.....O');
            chars.push(englishToBraille[englishCharacters[i].toLowerCase()]);
        }
        else if (/^[a-z]$/.test(englishCharacters[i])) {
            chars.push(englishToBraille[englishCharacters[i]]);
        }
        else if (/^[1-9]$/.test(englishCharacters[i])) {
            chars.push('.O.OOO');
            for (i; i < englishCharacters.length && englishCharacters[i] != ' '; i++) {
                chars.push(numberToBraille[englishCharacters[i]]);
            }
            if (englishCharacters[i] === ' ') chars.push('......')
        }
        else {
            chars.push('......');
        }
    }
    result = chars.join('');
}
else {
    result = 'invalid input';
}

console.log(result)
