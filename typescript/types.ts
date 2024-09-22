export type NumberDigit =
    | "0"
    | "1"
    | "2"
    | "3"
    | "4"
    | "5"
    | "6"
    | "7"
    | "8"
    | "9";

export type BrailleSymbol = `${"O" | "."}${"O" | "."}${"O" | "."}${"O" | "."}${
    | "O"
    | "."}${"O" | "."}`;

export type BrailleString = string;

export type BrailleToEnglishMap = {
    [key in BrailleSymbol]?: string;
};

export type BrailleToNumberMap = { [key in BrailleSymbol]?: NumberDigit };

export type EnglishToBrailleMap = { [key: string]: BrailleSymbol };

export function isNumberDigit(char: string): char is NumberDigit {
    return /^[0-9]$/.test(char);
}

export function isBrailleSymbol(symbol: string): symbol is BrailleSymbol {
    return /^[O.]{6}$/.test(symbol);
}

export function isBrailleString(braille: string): braille is BrailleString {
    return /^[O.]+$/.test(braille);
}
