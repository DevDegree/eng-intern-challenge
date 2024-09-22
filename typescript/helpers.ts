import {
    BRAILLE_TO_ENGLISH_MAP,
    BRAILLE_TO_NUMBER_MAP,
    ENGLISH_TO_BRAILLE_MAP,
} from "./constants";
import { BrailleString, BrailleSymbol, NumberDigit } from "./types";

export const convertBrailleToEnglish = (braille: BrailleString): string => {
    return BRAILLE_TO_ENGLISH_MAP[braille];
};

export const convertBrailleToNumber = (braille: BrailleString): NumberDigit => {
    return BRAILLE_TO_NUMBER_MAP[braille];
};

export const convertEnglishToBraille = (english: string): BrailleSymbol => {
    return ENGLISH_TO_BRAILLE_MAP[english];
};

export const convertNumberToBraille = (
    number: NumberDigit,
    hasPrefix: boolean
): BrailleString => {
    return (
        (hasPrefix ? "" : ENGLISH_TO_BRAILLE_MAP.NUM) +
        ENGLISH_TO_BRAILLE_MAP[number]
    );
};

export const convertCapitalToBraille = (capital: string): BrailleString => {
    return (
        ENGLISH_TO_BRAILLE_MAP.CAPITAL +
        ENGLISH_TO_BRAILLE_MAP[capital.toLowerCase()]
    );
};
