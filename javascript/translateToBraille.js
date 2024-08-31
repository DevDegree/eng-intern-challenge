const { brailleSpecials } = require("./brailleSpecials");
const { brailleAlphabet } = require("./brailleAlphabets");
const { brailleNumbers } = require("./brailleNumbers");
function translateToBraille(val) {
    let str = "";
    let isNum = false;
    // function to check the string's case
    const isUpperCase = str => str !== " " && str === str.toUpperCase();

    // for loop that iterates through all the characters
    for (let i = 0; i < val.length; i++) {
        // getting the current value based on current index
        const value = val.charAt(i) || "";

        if (value.match(/\d+/) && !isNum) {
            // only storing the number sign when number is found
            str += brailleSpecials['number']
            str += brailleNumbers[value]
            isNum = true;
        } else if (value !== " " && isNum) {
            // assuming all the values to be a number until space is entered
            str += brailleNumbers[value] || ""
        } else if (isUpperCase(value)) {
            str += brailleSpecials['capital']
            str += brailleAlphabet[value.toLowerCase()]
        } else if (value === " ") {
            isNum = false;
            str += brailleSpecials[value]
        } else {
            str += brailleAlphabet[value]
        }
    }
    return str;
}

module.exports = { translateToBraille }