"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const process_1 = require("process");
const translatorUtils_1 = require("./translatorUtils");
const args = process_1.argv.slice(2);
function translateBrailleToText(brailleInput) {
    var _a;
    const brailleChars = brailleInput.match(/.{1,6}/g) || [];
    let result = "";
    let isNumber = false;
    for (let i = 0; i < brailleChars.length; i++) {
        const char = translatorUtils_1.brailleToEnglishMap.get(brailleChars[i]);
        switch (char) {
            case "capital":
                result += (_a = translatorUtils_1.brailleToEnglishMap.get(brailleChars[++i])) === null || _a === void 0 ? void 0 : _a.toUpperCase();
                break;
            case "number":
                isNumber = true;
                break;
            case " ":
                result += char;
                isNumber = false;
                break;
            default:
                if (isNumber) {
                    result += translatorUtils_1.brailleToNumberMap.get(brailleChars[i]) || "";
                }
                else {
                    result += char || "";
                }
                break;
        }
    }
    return result;
}
function translateTextToBraille(textInput) {
    const result = [];
    let isNumber = false;
    for (const string of textInput) {
        for (const char of string) {
            if (isNumber && translatorUtils_1.numbersToBrailleMap.has(char)) {
                result.push(translatorUtils_1.numbersToBrailleMap.get(char));
            }
            else if ((0, translatorUtils_1.isNumeric)(char)) {
                isNumber = true;
                result.push(translatorUtils_1.englishToBrailleMap.get("number"));
                result.push(translatorUtils_1.numbersToBrailleMap.get(char));
            }
            else if (char === char.toUpperCase() && char !== " ") {
                result.push(translatorUtils_1.englishToBrailleMap.get("capital"));
                result.push(translatorUtils_1.englishToBrailleMap.get(char.toLowerCase()));
            }
            else {
                result.push(translatorUtils_1.englishToBrailleMap.get(char));
            }
        }
        result.push(translatorUtils_1.englishToBrailleMap.get(" "));
        isNumber = false;
    }
    return result.join("").slice(0, -6); // Remove the last space
}
if (args.length === 1 && translatorUtils_1.brailleInputRegex.test(args[0])) {
    console.log(translateBrailleToText(args[0]));
}
else {
    console.log(translateTextToBraille(args));
}
