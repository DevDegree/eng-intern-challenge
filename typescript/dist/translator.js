"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const charMap_1 = __importDefault(require("./charMap"));
const brailleMap_1 = __importDefault(require("./brailleMap"));
function translator(word) {
    let regexp = /\b(?!\w*[.O])\w+\b/;
    let output = "hello";
    if (regexp.test(word)) {
        return translateToBraille(word);
    }
    else {
        return translateToEnglish(word);
    }
    console.log(output);
    return output;
}
function translateToBraille(word) {
    let output = "";
    const numStr = "1234567890";
    let i = 0;
    while (i < word.length) {
        const char = word[i];
        const translation = charMap_1.default.get(word[i].toLowerCase());
        if (numStr.includes(char)) {
            if (i == 0 || !numStr.includes(word[i - 1])) {
                output += ".O.OOO";
            }
        }
        else if (word.charCodeAt(i) > 64 && word.charCodeAt(i) < 91) {
            output += ".....O";
        }
        output += translation;
        i += 1;
    }
    console.log(output);
    return output;
}
function translateToEnglish(word) {
    var _a;
    let output = "";
    while (word.length > 0) {
        let brailleChar = word.slice(0, 6);
        let translation;
        if (brailleChar == ".O...O") {
            word = word.slice(6);
            continue;
        }
        if (brailleChar == ".O.OOO") {
            word = word.slice(6);
            while (word.length > 0) {
                brailleChar = word.slice(0, 6);
                if (brailleChar == "......") {
                    break;
                }
                translation = brailleMap_1.default.get("n" + brailleChar);
                output += translation;
                word = word.slice(6);
            }
            output += " ";
            word = word.slice(6);
        }
        else if (brailleChar == ".....O") {
            brailleChar = word.slice(6, 12);
            translation = (_a = brailleMap_1.default.get(brailleChar)) === null || _a === void 0 ? void 0 : _a.toUpperCase();
            output += translation;
            word = word.slice(12);
        }
        else {
            translation = brailleMap_1.default.get(brailleChar);
            output += translation;
            word = word.slice(6);
        }
    }
    console.log(output);
    return output;
}
//# sourceMappingURL=translator.js.map