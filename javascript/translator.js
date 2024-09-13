const toBraille = {
  a: "O.....",
  b: "O.O...",
  c: "OO....",
  d: "OO.O..",
  e: "O..O..",
  f: "OOO...",
  g: "OOOO..",
  h: "O.OO..",
  i: ".OO...",
  j: ".OOO..",
  k: "O...O.",
  l: "O.O.O.",
  m: "OO..O.",
  n: "OO.OO.",
  o: "O..OO.",
  p: "OOO.O.",
  q: "OOOOO.",
  r: "O.OOO.",
  s: ".OO.O.",
  t: ".OOOO.",
  u: "O...OO",
  v: "O.O.OO",
  w: ".OOO.O",
  x: "OO..OO",
  y: "OO.OOO",
  z: "O..OOO",
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
  0: ".OOO..",
  " ": "......",
  capitalFollows: ".....O",
  numberFollows: ".O.OOO",
};

const fromBraille = Object.fromEntries(
  Object.entries(toBraille).map(([char, pattern]) => [pattern, char])
);

const fromBrailleNum = Object.fromEntries(
  Object.entries(toBraille)
    .filter(([char]) => !isNaN(char))
    .map(([char, pattern]) => [pattern, char])
);

function translator(input) {
  let output = "";
  let isValidBraille = false;
  let isValidChar = false;

  const capitalFollows = toBraille.capitalFollows;
  const numberFollows = toBraille.numberFollows;
  const spaceBreak = toBraille[" "];
  const lowerCaseInput = input.toLowerCase();

  // check if the input is valid braille
  if (input.length % 6 === 0) {
    isValidBraille = true;
    for (let i = 0; i < input.length; i += 6) {
      const chunk = input.slice(i, i + 6);
      if (
        !fromBraille.hasOwnProperty(chunk) &&
        !fromBrailleNum.hasOwnProperty(chunk)
      ) {
        isValidBraille = false;
        break;
      }
    }
  }

  // check if the input is valid char
  if (!isValidBraille) {
    isValidChar = true;
    for (let char of lowerCaseInput) {
      if (!toBraille.hasOwnProperty(char)) {
        isValidChar = false;
        break;
      }
    }
  }

  if (isValidBraille) {
    // handle brailles here
    let isNumber = false;
    for (let i = 0; i < input.length; i += 6) {
      let braillePattern = input.slice(i, i + 6);
      let character;
      switch (braillePattern) {
        case capitalFollows:
          // When a Braille capital follows symbol is read, assume only the next symbol should be capitalized
          braillePattern = input.slice(i + 6, i + 12);
          i += 6;
          character = fromBraille[braillePattern].toUpperCase();
          break;

        case numberFollows:
          // When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol
          isNumber = true;
          braillePattern = input.slice(i + 6, i + 12);
          i += 6;
          character = fromBrailleNum[braillePattern];
          break;

        case spaceBreak:
          // Space symbol encountered, reset the isNumber flag
          isNumber = false;
          character = fromBraille[braillePattern];
          break;

        default:
          if (isNumber) {
            character = fromBrailleNum[braillePattern];
          } else {
            character = fromBraille[braillePattern];
          }
          break;
      }
      output += character;
    }
  } else if (isValidChar) {
    //need to determine if the input is a number or not
    let firstNumAppearance = false;

    for (let char of input) {
      if (char >= "0" && char <= "9") {
        if (!firstNumAppearance) {
          firstNumAppearance = true;
          output += numberFollows;
          output += toBraille[char];
        } else {
          output += toBraille[char];
        }
      } else if (char === " " || char === "\t" || char === "\b") {
        //reset the firstNumAppearance flag when a space is encountered
        firstNumAppearance = false;
        output += toBraille[char];
      } else if (char === char.toUpperCase()) {
        output += capitalFollows;
        output += toBraille[char.toLowerCase()];
      } else {
        output += toBraille[char];
      }
    }
  } else {
    // handle anything other than the existing keys included in the two objects here by not doing any modification
    output = input;
  }

  return output;
}

// Read input from command line
const args = process.argv.slice(2);
const input = args.join(" ");

//log output to the console
console.log(translator(input));
