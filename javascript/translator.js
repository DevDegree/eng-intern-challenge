const { alphabet, numbers, markers } = require("./map");
const { isBraille, isNumber, isCapital, isSpace } = require("./utils")

const input = process.argv.slice(2).join(" ");

let output = "";
if (isBraille(input)) {
  // convert to english
  const braille = Array.from({ length: Math.ceil(input.length / 6) }, (_, i) => {
    return input.slice(i * 6, 6 + i * 6);
  });
  
} else {
  // convert to braille
  let addingNumbers = false;
  for (let char of input) {
    if (isNumber(char)) {
      if (!addingNumbers) {
        output += markers.number;
        addingNumbers = true;
      }
      output += numbers[parseInt(char)];
    } else if (isSpace(char)) {
      if (addingNumbers) {
        addingNumbers = false;
      }
      output += "......";
    } else if (isCapital(char)) {
      output += markers.capital;
      output += alphabet[char.toUpperCase()];
    } else {
      output += alphabet[char.toUpperCase()];
    }
  }
}

console.log(output);