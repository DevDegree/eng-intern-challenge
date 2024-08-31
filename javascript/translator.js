const { assert } = require("node:console");
const { translateToEnglish } = require("./translateToEnglish");
const { translateToBraille } = require("./translateToBraille");

function showResult(val) {
    if (val === "") {
        return ""
    } else if (!val.includes(".")) {
        return translateToBraille(val);
    } else {
        // providing 6 as length to get the braille input
        return translateToEnglish(val, 6);
    }
}

// to run the app using command line args
const args = process.argv.slice(2);
const input = args.join(" ");
if (input) {
    console.log(showResult(input));
    process.exit();
}





