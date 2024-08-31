const BRAILE_MAPPING = {
    // letters
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    // Special Char
    '.....O': 'CAPS', '.O.OOO': 'NUM', '......': ' '
};

const ENGLISH_MAPPING = Object.fromEntries(
    Object.entries(BRAILE_MAPPING).map(([k, v]) => [v, k])
);

const NUMBER_MAPPING = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
};

const NUMBER_REV_MAPPING = Object.fromEntries(
    Object.entries(NUMBER_MAPPING).map(([k, v]) => [v, k])
);

function isBraile(phrase) {
    return [...phrase].every(char => char === 'O' || char === '.');
}

function braileToEng(phrase) {
    let curr = 0;
    let capslock = false;
    let numSwitch = false;
    const english = [];
    
    for (let i = 0; i < phrase.length / 6; i++) {
        const segment = phrase.slice(curr, curr + 6);
        if (segment in BRAILE_MAPPING) {
            const mappedChar = BRAILE_MAPPING[segment];
            if (mappedChar === 'CAPS') {
                capslock = true;
            } else if (mappedChar === 'NUM') {
                numSwitch = true;
            } else if (mappedChar === ' ') {
                numSwitch = false;
                english.push(' ');
            } else {
                if (capslock) {
                    english.push(mappedChar.toUpperCase());
                    capslock = false;
                } else if (numSwitch) {
                    english.push(NUMBER_MAPPING[segment]);
                } else {
                    english.push(mappedChar);
                }
            }
        }
        curr += 6;
    }
    return english.join('');
}

function engToBraile(phrase) {
    const braile = [];
    let isNum = false;

    for (const char of phrase) {
        if (char in NUMBER_REV_MAPPING) {
            if (!isNum) {
                braile.push(ENGLISH_MAPPING['NUM']);
            }
            isNum = true;
            braile.push(NUMBER_REV_MAPPING[char]);
        } else if (char.toLowerCase() in ENGLISH_MAPPING) {
            isNum = false;
            if (char === char.toUpperCase() && char !== char.toLowerCase()) {
                braile.push(ENGLISH_MAPPING['CAPS']);
            }
            braile.push(ENGLISH_MAPPING[char.toLowerCase()]);
        } else if (char === ' ') {
            braile.push('......');
        }
    }
    return braile.join('');
}

function main() {
    const args = process.argv.slice(2);
    if (args.length > 0) {
        const phrase = args.join(' ');
        if (isBraile(phrase)) {
            const word = braileToEng(phrase);
            console.log(word);
        } else {
            const braile = engToBraile(phrase);
            console.log(braile);
        }
    } else {
        console.log("");
    }
}

if (require.main === module) {
    main();
}
