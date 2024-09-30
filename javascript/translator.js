// Braille keys and values
const brailleMap = {
  // Alphabet
  alphabet: {
    A: "O.....",
    B: "O.O...",
    C: "OO....",
    D: "OO.O..",
    E: "O..O..",
    F: "OOO...",
    G: "OOOO..",
    H: "O.OO..",
    I: ".OO...",
    J: ".OOO..",
    K: "O...O.",
    L: "O.O.O.",
    M: "OO..O.",
    N: "OO.OO.",
    O: "O..OO.",
    P: "OOO.O.",
    Q: "OOOOO.",
    R: "O.OOO.",
    S: ".OO.O.",
    T: ".OOOO.",
    U: "O...OO",
    V: "O.O.OO",
    W: ".OOO.O",
    X: "OO..OO",
    Y: "OO.OOO",
    Z: "O..OOO",
  },

  // Numbers
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

  // Following Elements and Others
  capital_follows: ".....O",
  number_follows: ".O.OOO",
  space: "......",
};

let result = "";
let numberFollowCounter = 0;

function checkInput(input) {
  const braillePattern = /([O.]{6})/;
  if (!braillePattern.test(input)) {
    return englishToBraille(input);
  } else {
    return brailleToEnglish(input);
  }
}

function englishToBraille(input) {
  const upperCasePattern = /[A-Z]/;
  const spacePattern = /^\s*$/;

  const splitInput = input.split("");

  for (let i = 0; i < splitInput.length; i++) {
    if (isNaN(splitInput[i])) {
      numberFollowCounter = 0;

      if (upperCasePattern.test(splitInput[i])) {
        result +=
          brailleMap["capital_follows"] + brailleMap["alphabet"][splitInput[i]];
        continue;
      }

      result += brailleMap["alphabet"][splitInput[i].toUpperCase()];
      continue;
    } else {
      if (spacePattern.test(splitInput[i])) {
        result += brailleMap["space"];
        continue;
      }

      numberFollowCounter++;
      if (numberFollowCounter == 1) {
        result += brailleMap["number_follows"] + brailleMap[splitInput[i]];
        numberFollowCounter++;
        continue;
      } else if (numberFollowCounter > 1) {
        result += brailleMap[splitInput[i]];
        continue;
      }
    }
  }

  return result;
}

function brailleToEnglish(input) {
  const splitInput = input.match(/.{1,6}/g);

  let numberSequence = false;

  for (let i = 0; i < splitInput.length; i++) {
    if (getObjectKey(brailleMap, splitInput[i]) == "capital_follows") {
      i++;
      result += getObjectKey(brailleMap["alphabet"], splitInput[i]);
      continue;
    }

    if (
      !numberSequence &&
      getObjectKey(brailleMap, splitInput[i]) == "number_follows"
    ) {
      i++;
      result += getObjectKey(brailleMap, splitInput[i]);
      numberSequence = true;
      continue;
    }

    if (getObjectKey(brailleMap, splitInput[i]) == "space") {
      result += " ";
      numberSequence = false;
      continue;
    }

    if (!numberSequence) {
      result += getObjectKey(
        brailleMap["alphabet"],
        splitInput[i]
      ).toLowerCase();
      continue;
    }

    result += getObjectKey(brailleMap, splitInput[i]);
  }

  return result;
}

function getObjectKey(object, valueToFindKey) {
  return Object.keys(object).find((key) => object[key] === valueToFindKey);
}

if (require.main === module) {
  const args = process.argv.slice(2);
  const inputString = args.join(" ");
  const result = checkInput(inputString);
  console.log(result);
}