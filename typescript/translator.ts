// Use TypeScript's Record type for better type safety
const toBraille: Record<string, string> = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    'cap': '.....O',
    'num': '.O.OOO',
    ' ': '......',
};

// Reverse mapping using Object.entries for clarity
const toEng: Record<string, string> = Object.fromEntries(
    Object.entries(toBraille).map(([key, value]) => [value, key])
);

function englishToBraille(input: string): string {
    let output = '';
    let numMode = false;

    for (let c of input) {
        if (numMode && c === ' ') {
            numMode = false;
        }

        if (!numMode && /\d/.test(c)) {
            output += toBraille['num'];
            numMode = true;
        }

        if (!numMode) {
            if (c >= 'A' && c <= 'Z') {
                output += toBraille['cap'];
                c = c.toLowerCase();
            }
        }

        const brailleChar = toBraille[c];
        if (brailleChar) {
            output += brailleChar;
        } else {
            // Handle unknown characters
            console.warn(`Warning: Character '${c}' cannot be translated to Braille.`);
        }
    }
    return output;
}

function brailleToEnglish(input: string): string {
    let output = '';
    let capMode = false;
    let numMode = false;

    // Split the input into chunks of 6 characters
    const chars = input.match(/.{1,6}/g) || [];

    for (const brailleChar of chars) {
        const symbol = toEng[brailleChar];

        if (!symbol) {
            // Handle unknown Braille patterns
            console.warn(`Warning: Braille pattern '${brailleChar}' cannot be translated to English.`);
            continue;
        }

        if (symbol === 'cap') {
            capMode = true;
            continue;
        }

        if (symbol === 'num') {
            numMode = true;
            continue;
        }

        let ch = symbol;

        if (numMode) {
            const digitsMap: Record<string, string> = {
                'a': '1',
                'b': '2',
                'c': '3',
                'd': '4',
                'e': '5',
                'f': '6',
                'g': '7',
                'h': '8',
                'i': '9',
                'j': '0',
            };
            if (ch in digitsMap) {
                ch = digitsMap[ch];
            } else if (ch === ' ') {
                numMode = false;
            } else {
                console.warn(`Warning: Character '${ch}' is not a valid digit in num mode.`);
            }
        } else {
            if (capMode) {
                ch = ch.toUpperCase();
                capMode = false;
            }
        }
        output += ch;
    }
    return output;
}

function main() {
    const args = process.argv.slice(2);

    if (args.length < 1) {
        console.error("Error: Must pass at least 1 argument.");
        process.exit(1);
    }

    let result = '';

    for (let i = 0; i < args.length; i++) {
        const input = args[i];
        if (input.includes('.') || input.includes('O')) {
            // Treat input as Braille
            if (i > 0) result += ' ';
            result += brailleToEnglish(input);
        } else {
            // Treat input as English
            if (i > 0) result += toBraille[' '];
            result += englishToBraille(input);
        }
    }

    console.log(result);
}

main();
