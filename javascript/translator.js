const { alphabet, numbers, markers } = require("./map");
const { isBraille, isNumber, isCapital, isSpace, invertObject } = require("./utils")

const input = process.argv.slice(2).join(" ");

let output = "";
if (isBraille(input)) {
  // convert to english
  const braille = Array.from({ length: Math.ceil(input.length / 6) }, (_, i) => {
    return input.slice(i * 6, 6 + i * 6);
  });
  const brailleAlphabet = invertObject(alphabet);
  const brailleMarkers = invertObject(markers);
  let addingNumbers = false;
  let capital = false;
  for (let char of braille) {
    if (char in brailleMarkers) {
      // found a marker
      let marker = brailleMarkers[char];
      if (marker === "capital") {
        // capital marker
        capital = true;
      } else {
        // number marker
        addingNumbers = true;
      }
    } else {
      // letter, number or space
      // handle space
      if (char === "......") {
        addingNumbers = false;
        output += " ";
      } else if (addingNumbers) {
        let num = numbers.findIndex((val) => val === char);
        output += num;
      } else {
        if (capital) {
          output += brailleAlphabet[char];
          capital = false;
        } else {
          output += brailleAlphabet[char].toLowerCase();
        }
      }
    }
  }
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