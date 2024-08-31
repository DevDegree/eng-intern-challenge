import { alphabetToBraille, brailleToAlphabet, brailleToNumber, CAPITALIZE, NUMBER, numberToBraille, SPACE } from "./constants";

const isBraille = (message: string): boolean => {
    return message.split('').every(char => char === 'O' || char === '.');
}

const englishToBraille = (message: string): string => {
    const result: string[] = [];
    let numberMode = false;

    for (const char of message) {
        if (/[a-zA-Z]/.test(char)) {
            if (/[A-Z]/.test(char)) {
                result.push(CAPITALIZE);
            }
            result.push(alphabetToBraille[char.toLowerCase()]);
            numberMode = false;
        } else if (/\d/.test(char)) {
            if (!numberMode) {
                result.push(NUMBER);
                numberMode = true;
            }
            result.push(numberToBraille[char]);
        } else if (/\s/.test(char)) {
            result.push(alphabetToBraille[char]);
            numberMode = false;
        }
    }

    return result.join('');
}

    const brailleToEnglish = (message: string): string => {
    const result: string[] = [];
    let numberMode = false;
    let i = 0;

    while (i < message.length) {
        const symbol = message.slice(i, i + 6);

        if (symbol === SPACE) {
            numberMode = false;
        }

        if (symbol === CAPITALIZE) {
            i += 6;
            const nextSymbol = message.slice(i, i + 6);
            result.push(brailleToAlphabet[nextSymbol].toUpperCase());
        } else if (symbol === NUMBER) {
            numberMode = true;
            i += 6;
            continue;
        } else if (symbol in brailleToAlphabet && !numberMode) {
            result.push(brailleToAlphabet[symbol]);
            numberMode = false;
        } else if (symbol in brailleToNumber) {
            result.push(brailleToNumber[symbol]);
        } else {
            result.push(' ');
        }

        i += 6;
    }

    return result.join('');
}

const translate = (input: string): string => {
    if (isBraille(input)) {
        return brailleToEnglish(input);
    } else {
        return englishToBraille(input);
    }
}

const input = process.argv.slice(2).join(' ');
console.log(translate(input));

