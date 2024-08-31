const { brailleSpecials, reverseBrailleSpecials } = require("./brailleSpecials");
const { reverseBrailleAlphabet } = require("./brailleAlphabets");
const { reverseBrailleNumbers } = require("./brailleNumbers");
function translateToEnglish(val, length) {
    let str = "";
    // flags to skip the character signs
    let isCapital = false;
    let isNum = false;
    for (let i = 0; i < val.length; i += length) {
        const value = val.substring(i, i + length) || "";
        if (value === brailleSpecials['capital']) {
            isCapital = true;
            continue;
        } else if (value === brailleSpecials['number']) {
            isNum = true;
            continue;
        } else if (isCapital) {
            // storing the character as capital after capital sign
            const capitalVal = reverseBrailleAlphabet[value].toUpperCase();
            str += capitalVal;
            isCapital = false;
        } else if (value !== brailleSpecials[' '] && isNum) {
            str += reverseBrailleNumbers[value] || ""
        } else if (value === brailleSpecials[' ']) {
            isNum = false;
            str += reverseBrailleSpecials[value]
        } else {
            str += reverseBrailleAlphabet[value]
        }
    }
    return str;
}

module.exports = { translateToEnglish }