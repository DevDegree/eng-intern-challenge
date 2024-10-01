const brailleLettersDict = {
  ".....O": "capital follows",
  ".O...O": "decimal follows",
  ".O.OOO": "number follows",
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
  "O..OO.": ">",
  "O.O..O": "(",
  ".O.OO.": ")",
  "......": " ",
};

const brailleNumbersDict = {
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

const englishLettersDict = {
  "capital follows": ".....O",
  "decimal follows": ".O...O",
  "number follows": ".O.OOO",
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
  ">": "O..OO.",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
};

const englishNumbersDict = {
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
};

// function will convert braille to english
// function argument is the user input
const brailleToEnglish = (input) => {
  let english = "";
  let capitalFollows = false;
  let numberFollows = false;
  let decimalFollows = false;

  let i = 0;
  while (i < input[2].length) {
    let braille = input[2].substring(i, i + 6); // storing the 6 character braille symbol
    switch (braille) {
      case ".....O":
        // if a capital follows
        capitalFollows = true;
        break;
      case ".O.OOO":
        // if a number follows
        numberFollows = true;
        break;
      case ".O...O":
        // if a decimal follows
        decimalFollows = true;
        break;
      case "......":
        // if theres a space, add it
        // since there is a space, we will assume that the following symbols are no longer numbers
        english += brailleLettersDict[braille];
        numberFollows = false;
        break;
      default:
        if (decimalFollows) {
          // if a decimal follows
          english += brailleLettersDict[braille];
          decimalFollows = false;
        } else if (numberFollows) {
          // if a number follows
          english += brailleNumbersDict[braille];
        } else if (brailleLettersDict[braille]) {
          // if the next symbol is a letter
          if (capitalFollows) {
            // check if the letter is a capital letter
            english += brailleLettersDict[braille].toUpperCase();
            capitalFollows = false;
          } else {
            // if not a capital letter
            english += brailleLettersDict[braille];
          }
        }
    }

    i += 6;
  }

  console.log(english);
};

// function will convert english to braille
// function arguments are the user input, and a boolean value that is true if there are more than 3 arguments, false otherwise
const englishToBraille = (input, multipleArgs) => {
  let braille = "";
  let numberHasFollowed = false;
  for (let i = 2; i < input.length; i++) {
    for (letr of input[i]) {
      // if the character is a letter
      if (englishLettersDict[letr.toLowerCase()]) {
        // Checks if it is a capital letter
        if (65 <= letr.charCodeAt(0) && letr.charCodeAt(0) <= 90) {
          braille += englishLettersDict["capital follows"];
        }
        braille += englishLettersDict[letr.toLowerCase()];
      }

      // if the character is a number
      if (englishNumbersDict[letr.toLowerCase()]) {
        // this will check if number follows
        if (!numberHasFollowed) {
          braille += englishLettersDict["number follows"];
          numberHasFollowed = true;
        }
        braille += englishNumbersDict[letr.toLowerCase()];
      }
    }

    if (multipleArgs) {
      braille += englishLettersDict[" "];
      numberHasFollowed = false; //once the next space symbol is added, set this back to false
    }
  }

  // this will remove the added extra space to the braille string
  if (multipleArgs) {
    braille = braille.substring(0, braille.length - 6);
  }

  console.log(braille);
};

// function that will check if the input argument is braille or english
const brailleOrEnglish = (value) => {
  // if there are more than 3 arguments in the command line, then it is english
  if (value.length > 3) {
    englishToBraille(value, true);
  } else {
    // if there are only 3 arguments, then we have to check if the input argument is braille or english
    // first check if the first six characters in the argument are in the braille letters dictionary or the braille numbers dictionary
    // if it is, then its braille, otherwise it is english
    if (
      brailleLettersDict[value[2].substring(0, 6)] ||
      brailleNumbersDict[value[2].substring(0, 6)]
    ) {
      brailleToEnglish(value);
    } else {
      englishToBraille(value, false);
    }
  }
};

const inputs = process.argv; // get the user input

// If there is an input argument, check if its braille or english, otherwise remind the user to enter an input next time
if (inputs[2]) {
  brailleOrEnglish(inputs);
} else {
  console.log(
    "No argument provided by user. Please include an input in Braille or English"
  );
}
