import * as readline from 'readline';

// Dictionary mapping characters to their Braille representations (in binary)
const BRAILLE_MAP: { [key: string]: number } = {
    'a': 0b100000, 'b': 0b101000, 'c': 0b110000, 'd': 0b110100, 'e': 0b100100,
    'f': 0b111000, 'g': 0b111100, 'h': 0b101100, 'i': 0b011000, 'j': 0b011100,
    'k': 0b100010, 'l': 0b101010, 'm': 0b110010, 'n': 0b110110, 'o': 0b100110,
    'p': 0b111010, 'q': 0b111110, 'r': 0b101110, 's': 0b011010, 't': 0b011110,
    'u': 0b100011, 'v': 0b101011, 'w': 0b011101, 'x': 0b110011, 'y': 0b110111,
    'z': 0b100111,
    '1': 0b100000, '2': 0b101000, '3': 0b110000, '4': 0b110100, '5': 0b100100,
    '6': 0b111000, '7': 0b111100, '8': 0b101100, '9': 0b011000, '0': 0b011100,
    '.': 0b001101, ',': 0b001000, '?': 0b001011, '!': 0b001110, '-': 0b000011,
    ':': 0b001100, ';': 0b001010, '(': 0b101001, ')': 0b010110, '/': 0b010010,
    "'": 0b000010, '"': 0b001010, '*': 0b000110, '@': 0b000101, '&': 0b101101,
    ' ': 0b000000,
    'capital': 0b000001,
    'number': 0b010111,
    'decimal': 0b000101,
};

// Reverse mapping of BRAILLE_MAP for easy lookup
const BRAILLE_REVERSE_MAP: { [key: number]: string } = Object.fromEntries(
    Object.entries(BRAILLE_MAP).map(([k, v]) => [v, k])
);

function translateToBraille(text: string): number[] {
    const translated: number[] = [];
    let numberMode = false;

    for (const char of text) {
        if (char === ' ') {
            translated.push(BRAILLE_MAP[' ']);
            numberMode = false;
        } else if (/\d/.test(char)) {
            if (!numberMode) {
                translated.push(BRAILLE_MAP['number']);
                numberMode = true;
            }
            translated.push(BRAILLE_MAP[char]);
        } else if (char === '.') {
            if (numberMode) {
                translated.push(BRAILLE_MAP['decimal']);
            } else {
                translated.push(BRAILLE_MAP[char] || 0);
            }
            numberMode = false;
        } else {
            if (numberMode) {
                numberMode = false;
            }
            if (char === char.toUpperCase()) {
                translated.push(BRAILLE_MAP['capital']);
            }
            translated.push(BRAILLE_MAP[char.toLowerCase()] || 0);
        }
    }

    return translated;
}

function translateToEnglish(brailleBinary: number[]): string {
    const translated: string[] = [];
    let index = 0;
    let numberMode = false;
    let capitalMode = false;

    while (index < brailleBinary.length) {
        const brailleChar = brailleBinary[index];

        if (brailleChar === BRAILLE_MAP[' ']) {
            translated.push(' ');
            numberMode = false;
            capitalMode = false;
        } else if (brailleChar === BRAILLE_MAP['number']) {
            numberMode = true;
        } else if (brailleChar === BRAILLE_MAP['decimal']) {
            translated.push('.');
        } else if (brailleChar === BRAILLE_MAP['capital']) {
            capitalMode = true;
        } else {
            if (numberMode) {
                const char = BRAILLE_REVERSE_MAP[brailleChar] || '?';
                if ('abcdefghij'.includes(char)) {
                    const digit = ((char.charCodeAt(0) - 'a'.charCodeAt(0) + 1) % 10).toString();
                    translated.push(digit);
                } else {
                    translated.push('?');
                }
            } else {
                let char = BRAILLE_REVERSE_MAP[brailleChar] || '?';
                if (capitalMode) {
                    char = char.toUpperCase();
                    capitalMode = false;
                }
                translated.push(char);
            }
        }
        index++;
    }

    return translated.join('');
}

function binaryToBrailleDots(binary: number): string {
    return Array.from({ length: 6 }, (_, i) => (binary & (1 << (5 - i))) ? 'O' : '.').join('');
}

function brailleDotsToBinary(dots: string): number {
    return dots.split('').reduce((acc, char, i) => acc + (char === 'O' ? 1 << (5 - i) : 0), 0);
}

function main() {
    const args = process.argv.slice(2);
    const input = args.join(' ');

    if (/^[O.]+$/.test(input)) {
        const brailleBinary: number[] = [];
        for (let i = 0; i < input.length; i += 6) {
            brailleBinary.push(brailleDotsToBinary(input.slice(i, i + 6)));
        }
        console.log(translateToEnglish(brailleBinary));
    } else {
        const brailleBinary = translateToBraille(input);
        console.log(brailleBinary.map(binaryToBrailleDots).join(''));
    }
}

main();