const { alphabet, numbers } = require("./map");
const { isBraille, isNumber } = require("./utils")

const input = process.argv.slice(2).join(" ");

let output = "";
if (isBraille(input)) {
  // convert to english
} else {
  // convert to braille
}