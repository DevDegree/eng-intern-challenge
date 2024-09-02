const brailleToEnglish = {
  "O.....": "a",
  "O.O...": "b",
  "OO....": "c",
  "OO.O..": "d",
  "O..O..": "e",
  "OOO...": "f",
  "OOOO..": "g",
  "O.OO..": "h",
  ".OO...": "i",
  ".OOO..": "j",
  "O...O.": "k",
  "O.O.O.": "l",
  "OO..O.": "m",
  "OO.OO.": "n",
  "O..OO.": "o",
  "OOO.O.": "p",
  "OOOOO.": "q",
  "O.OOO.": "r",
  ".OO.O.": "s",
  ".OOOO.": "t",
  "O...OO": "u",
  "O.O.OO": "v",
  ".OOO.O": "w",
  "OO..OO": "x",
  "OO.OOO": "y",
  "O..OOO": "z",
  "......": " ",
  ".O.OOO": "number",
  ".....O": "capitalize",
};

const numbers = {
  1: "a",
  2: "b",
  3: "c",
  4: "d",
  5: "e",
  6: "f",
  7: "g",
  8: "h",
  9: "i",
  0: "j",
};

// Create the reverse mapping for English to Braille, including numbers
const englishToBraille = {
  ...Object.fromEntries(
    Object.entries(brailleToEnglish).map(([braille, english]) => [
      english,
      braille,
    ])
  ),
  ...Object.fromEntries(
    Object.entries(numbers).map(([num, letter]) => [
      num,
      brailleToEnglish[letter],
    ])
  ),
  // Explicitly add mappings for numbers 0-9
  0: ".OOO..",
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
};

function isBraille(input) {
  return /^[O.]+$/.test(input);
}

function translateToEnglish(braille) {
  let english = "";
  let isNumberMode = false;
  let isCapitalMode = false;

  for (let i = 0; i < braille.length; i += 6) {
    const symbol = braille.slice(i, i + 6);

    if (symbol === ".O.OOO") {
      isNumberMode = true;
      continue;
    }

    if (symbol === ".....O") {
      isCapitalMode = true;
      continue;
    }

    if (symbol === ".....O") {
      english += " ";
      isNumberMode = false; // Reset number mode after space
      continue;
    }

    let letter = brailleToEnglish[symbol] || "";

    if (isNumberMode) {
      letter =
        Object.keys(numbers).find((key) => numbers[key] === letter) || "";
    }

    if (isCapitalMode) {
      letter = letter.toUpperCase();
      isCapitalMode = false; // Reset capital mode after using it
    }

    english += letter;
  }

  return english;
}

function translateToBraille(english) {
  let braille = "";
  let prevType = ""; // To handle multiple numbers

  for (let char of english) {
    if (char === " ") {
      braille += englishToBraille[" "];
      prevType = "space";
      continue;
    }

    if (char >= "0" && char <= "9") {
      if (prevType !== "number") {
        braille += englishToBraille["number"];
        prevType = "number";
      }
      braille += englishToBraille[char];
      continue;
    } else {
      prevType = "letter";
    }

    if (char >= "A" && char <= "Z") {
      braille += englishToBraille["capitalize"];
      char = char.toLowerCase();
    }

    braille += englishToBraille[char] || ""; // Ignore undefined characters
  }

  return braille;
}

function main() {
  const input = process.argv.slice(2).join(" ");

  if (isBraille(input)) {
    console.log(translateToEnglish(input));
  } else {
    console.log(translateToBraille(input));
  }
}

main();
