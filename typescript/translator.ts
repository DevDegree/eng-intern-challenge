import {
    convertBrailleToEnglish,
    convertBrailleToNumber,
    convertCapitalToBraille,
    convertEnglishToBraille,
    convertNumberToBraille,
} from "./helpers";
import { BrailleString, isBrailleString, isNumberDigit } from "./types";

const translateBrailleToEnglish = (braille: BrailleString): string => {
    let index = 0;
    let result = "";
    let isNumber = false;
    while (index + 6 <= braille.length) {
        const currentLetter = braille.slice(index, index + 6);
        index += 6;
        const conversion = convertBrailleToEnglish(currentLetter);
        if (conversion === "NUM") {
            isNumber = true;
        } else if (conversion === "CAPITAL") {
            const letterString = braille.slice(index, index + 6);
            index += 6;
            result += convertBrailleToEnglish(letterString).toUpperCase();
        } else if (isNumber) {
            if (conversion === " ") {
                result += " ";
                isNumber = false;
            } else {
                result += convertBrailleToNumber(currentLetter);
            }
        } else {
            result += conversion;
        }
    }
    return result;
};

const translateEnglishToBraille = (english: string): BrailleString => {
    let index = 0;
    let result = "";
    let isNumber = false;
    while (index < english.length) {
        const currentLetter = english.slice(index, index + 1);
        index += 1;
        if (currentLetter === " ") {
            isNumber = false;
        }
        if (isNumberDigit(currentLetter)) {
            result += convertNumberToBraille(currentLetter, isNumber);
            isNumber = true;
        } else if (
            currentLetter === currentLetter.toUpperCase() &&
            currentLetter !== currentLetter.toLowerCase()
        ) {
            result += convertCapitalToBraille(currentLetter);
        } else if (currentLetter == " ") {
            isNumber = false;
            result += convertEnglishToBraille(currentLetter);
        } else {
            result += convertEnglishToBraille(currentLetter);
        }
    }
    return result;
};

// Merge CLI arguments into space-separated string
const input = process.argv.slice(2).join(" ");
if (isBrailleString(input)) {
    console.log(translateBrailleToEnglish(input));
} else {
    console.log(translateEnglishToBraille(input));
}
