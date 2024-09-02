const brailleToEnglishMap: { [key: string]: string } = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '.O.OOO': 'number', '.....O': 'capital'
};

const englishToBrailleMap: { [key: string]: string } = Object.fromEntries(
    Object.entries(brailleToEnglishMap).map(([key, value]) => [value, key])
);

const numbersMap: { [key: string]: string } = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
};

const reverseNumbersMap: { [key: string]: string } = Object.fromEntries(
    Object.entries(numbersMap).map(([key, value]) => [value, key])
);

function translateToBraille(text: string): string {
    let result: string[] = [];
    let numberMode = false;

    for (let i = 0; i < text.length; i++) {
        let char = text[i];

        if (char >= 'A' && char <= 'Z') {
            result.push(englishToBrailleMap['capital']);
            char = char.toLowerCase();
            numberMode = false;
        } else if (char >= '0' && char <= '9') {
            if (!numberMode) {
                result.push(englishToBrailleMap['number']);
                numberMode = true;
            }
            char = reverseNumbersMap[char];
        } else {
            numberMode = false;
        }

        result.push(englishToBrailleMap[char] || '......');
    }

    return result.join('');
}

function translateToEnglish(braille: string): string {
    let result: string[] = [];
    let capitalNext = false;
    let numberMode = false;

    for (let i = 0; i < braille.length; i += 6) {
        let chunk = braille.slice(i, i + 6);

        if (chunk === '.....O') {
            capitalNext = true;
            continue;
        } else if (chunk === '.O.OOO') {
            numberMode = true;
            continue;
        } else if (chunk === '......') {
            result.push(' ');
            numberMode = false;
            continue;
        }

        let char = brailleToEnglishMap[chunk] || ' ';

        if (numberMode) {
            char = numbersMap[char] || char;
            if (!char) numberMode = false;
        }

        if (capitalNext) {
            char = char.toUpperCase();
            capitalNext = false;
        }

        result.push(char);
    }

    return result.join('');
}

function main() {
    const input = process.argv.slice(2).join(' ');
    
    if (/^[O.]+$/.test(input)) {
        console.log(translateToEnglish(input));
    } else {
        console.log(translateToBraille(input));
    }
}

main();
