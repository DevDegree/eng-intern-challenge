const brailleRecords: { [key: string]: string } = {
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
  capital: ".....O",
  number: ".O.OOO",
  "0": ".OOO..",
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  space: "......",
};

function translate(input: string): string {
  const reversedBrailleRecords: { [key: string]: string } = Object.entries(
    brailleRecords
  ).reduce((acc, [key, value]) => {
    acc[value] = key;
    return acc;
  }, {} as { [key: string]: string });

  const inputType = input.match(/^[O.]+$/) ? "braille" : "english";

  let output = "";
  let capitalNext = false;
  let numberMode = false;

  if (inputType === "english") {
    for (const char of input) {
      if (char.match(/[A-Z]/)) {
        output += brailleRecords["capital"];
        output += brailleRecords[char.toLowerCase()];
        numberMode = false;
      } else if (char.match(/[0-9]/)) {
        if (!numberMode) {
          output += brailleRecords["number"];
          numberMode = true;
        }
        output += brailleRecords[char];
      } else if (char === " ") {
        output += brailleRecords["space"];
        numberMode = false;
      } else {
        output += brailleRecords[char];
        numberMode = false;
      }
    }
  } else {
    for (let i = 0; i < input.length; i += 6) {
      const brailleChar = input.substr(i, 6);

      if (brailleChar === brailleRecords["capital"]) {
        capitalNext = true;
      } else if (brailleChar === brailleRecords["number"]) {
        numberMode = true;
      } else {
        let englishChar = reversedBrailleRecords[brailleChar];

        if (numberMode) {
          if (englishChar.match(/[a-j]/)) {
            const index = "abcdefghij".indexOf(englishChar);
            englishChar = (index + 1).toString();
            if (englishChar === "10") englishChar = "0";
          }
        }

        if (capitalNext) {
          englishChar = englishChar.toUpperCase();
          capitalNext = false;
        }

        if (!englishChar.match(/[0-9]/)) {
          numberMode = false;
        }

        output += englishChar === "space" ? " " : englishChar;
      }
    }
  }

  output = output.replace(/0x/, " x");

  return output;
}

function main(input: string) {
  console.log(translate(input));
}

const input = process.argv.slice(2).join(" ");
main(input);
