
const isBraille = require("./isBraille");
const toBraille = require("./toBraille");
const toEnglish = require("./toEnglish");

const string = process.argv.slice(2).join(' ');

if (isBraille(string)) {
  console.log(toEnglish(string));
} else {
  console.log(toBraille(string));
}
