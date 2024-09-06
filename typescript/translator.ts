const input = process.argv.slice(2).join(" ");

const brailleToLettersOrSpecial: { [braille: string]: string } = {
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
  "..OO.O": ".",
  "..O...": ",",
  "..O.OO": "?",
  "..OOO.": "!",
  "..OO..": ":",
  "..O.O.": ";",
  "....OO": "-",
  ".O..O.": "/",
  ".OO..O": "<",
  // "O..OO.": ">",
  "O.O..O": "(",
  ".O.OO.": ")",
  "......": " ",
};

const brailleToNumber: { [braille: string]: string } = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
};

const lettersOrSpecialToBraille: { [braille: string]: string } = {
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
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  // ">": "O..OO.",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
};

const numberToBraille: { [braille: string]: string } = {
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  "0": ".OOO..",
};

if (/^[O.]+$/.test(input)) {
  // Braille is inputted
  let beginning: number = 0;
  let end: number = 6;
  let output: string = "";
  let isNumber: boolean = false;

  while (end <= input.length) {
    const currentSlice: string = input.slice(beginning, end);

    if (currentSlice === ".O.OOO") {
      // Number follows indicator
      isNumber = true;
    } else if (isNumber && currentSlice === "......") {
      // isNumber is true and currentSlice is space
      isNumber = false;
      output += " ";
    } else if (isNumber) {
      // If isNumber process as number
      output += brailleToNumber[currentSlice];
    } else if (currentSlice === ".....O") {
      // Capital follows indicator
      beginning += 6;
      end += 6;
      const nextSlice: string = input.slice(beginning, end);
      output += brailleToLettersOrSpecial[nextSlice]?.toUpperCase();
    } else {
      // Regular character
      output += brailleToLettersOrSpecial[currentSlice];
    }

    beginning += 6;
    end += 6;
  }
  console.log(output);
} else {
  // Regular character inputted
  let counter: number = 0;
  let output: string = "";
  let isNumber: boolean = false;

  while (counter < input.length) {
    const currentChar: string = input[counter];

    if (currentChar === " ") {
      output += "......";
      isNumber = false;
    } else if (isNumber) {
      output += numberToBraille[currentChar];
    } else if (/^[0-9]$/.test(currentChar)) {
      isNumber = true;
      output += ".O.OOO";
      output += numberToBraille[currentChar];
    } else if (currentChar === currentChar.toUpperCase()) {
      output += ".....O";
      output += lettersOrSpecialToBraille[currentChar.toLowerCase()];
    } else {
      output += lettersOrSpecialToBraille[currentChar.toLowerCase()];
    }
    counter++;
  }
  console.log(output);
}
