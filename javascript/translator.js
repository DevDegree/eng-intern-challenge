const brailleAlphaNum = [
  "O.....",
  "O.O...",
  "OO....",
  "OO.O..",
  "O..O..",
  "OOO...",
  "OOOO..",
  "O.OO..",
  ".OO...",
  ".OOO..",
  "O...O.",
  "O.O.O.",
  "OO..O.",
  "OO.OO.",
  "O..OO.",
  "OOO.O.",
  "OOOOO.",
  "O.OOO.",
  ".OO.O.",
  ".OOOO.",
  "O...OO",
  "O.O.OO",
  ".OOO.O",
  "OO..OO",
  "OO.OOO",
  "O..OOO",
  "..OO.O",
  "..O...",
  "..O.OO",
  "..OOO.",
  "..OO..",
  "..O.O.",
  "....OO",
  ".O..O.",
  ".OO..O",
  "O..OO.", //This is the code for >, but it is the same as o. There is no specification for how they should be differentiated, so it will never translate this character to >
  "O.O..O",
  ".O.OO.",
  "......",
];

const brailleMods = [".....O", ".O...O", ".O.OOO"];

const alphaNum = "abcdefghijklmnopqrstuvwxyz.,?!:;-/<>() ".split("");

let inputString = process.argv.slice(2).join(" ");

translate();

function readBraille() {
  let braillePseudoString = [];
  for (let i = 0; i < inputString.length; i += 6) {
    let sixPips = inputString.slice(i, i + 6);
    braillePseudoString.push(sixPips);
  }
  return braillePseudoString;
}

function brailleToEng() {
  let braillePseudoString = readBraille();
  let caps = false;
  let nums = false;
  let englishString = braillePseudoString.map((brailleCharacter) => {
    if (brailleMods.includes(brailleCharacter)) {
      switch (brailleMods.indexOf(brailleCharacter)) {
        case 0:
          caps = true;
          break;
        case 1:
          if (nums) {
            return ".";
          } else {
            console.error(
              "Decimal signifier must be preceded by a number signifier, or part of a number string"
            );
            //this should not be reached with proper braille grammar. https://uebmath.aphtech.org/lesson2.0
          }
          break;
        case 2:
          nums = true;
          break;
      }
    } else {
      const characterIndex = brailleAlphaNum.indexOf(brailleCharacter);
      if (nums) {
        if (brailleCharacter === "......") {
          nums = false;
          return " ";
        } else {
          if (characterIndex < 10) {
            if (characterIndex === 9) {
              return "0";
            }
            return characterIndex + 1;
          } else {
            return alphaNum[characterIndex];
          }
        }
      }
      const englishEquiv = alphaNum[characterIndex];
      if (caps) {
        caps = false;
        return englishEquiv.toUpperCase();
      }
      return englishEquiv;
    }
  });
  return englishString.join("");
}

function engToBraille(string) {
  const englishArray = string.split("");
  let numberRuns = [-2];
  let capsIndexShift = 0;
  let brailleString = englishArray.flatMap((englishCharacter, index) => {
    if (englishCharacter.match(/[0-9]/)) {
      numberRuns.push(index + capsIndexShift);
      if (englishCharacter.match(/[0]/)) {
        return brailleAlphaNum[9];
      }
      return brailleAlphaNum[englishCharacter - 1];
    }
    if (englishCharacter.match(/[A-Z]/)) {
      capsIndexShift++;
      return [brailleMods[0], brailleAlphaNum[alphaNum.indexOf(englishCharacter.toLowerCase())]];
    }
    return brailleAlphaNum[alphaNum.indexOf(englishCharacter)];
  });
  numberMarkers = numberRuns.filter(
    (number, index, numberRuns) => number - numberRuns[index - 1] > 1
  );
  numberMarkers
    .reverse()
    .forEach((marker) => brailleString.splice(marker, 0, brailleMods[2]));
  return brailleString.join("");
}

function translate() {
  const nonBrailleChar = inputString.search(/[^O.]/);
  //search for a character that is not O or .
  if (nonBrailleChar === -1) {
    //If there are not non braille characters, the string can be interpreted as braille.
    console.log(brailleToEng(inputString));
  } else {
    console.log(engToBraille(inputString));
  }
}
