const {
  letterToBraille,
  numberToBraille,
  signalsToBraille,
  signsToBraille,
  brailleToLetter,
  brailleToNumber,
  brailleToSignals,
  brailleToSigns,
} = require("./alphabets.js");

function translator() {
  const args = process.argv.slice(2);
  const input = args.join(" ");

  let translated;
  if (isBraille(input)) {
    translated = translateBraille(input);
  } else {
    translated = translateEnglish(input);
  }
  console.log(translated);
}

const isBraille = (str) => {
  const regex = /^([.O]{6})+$/;
  return regex.test(str);
};

const translateBraille = (brailleString) => {
  const chunkSize = 6;
  let english = "";
  let isCap = false;
  let isNum = false;
  let toAdd;
  for (let i = 0; i < brailleString.length; i += chunkSize) {
    const braille = brailleString.substring(i, i + chunkSize);
    if (!isNum && braille in brailleToLetter) {
      toAdd = brailleToLetter[braille];
      if (isCap) {
        toAdd = toAdd.toUpperCase();
        isCap = false;
      }
    } else if (braille in brailleToSigns) {
      toAdd = brailleToSigns[braille];
    } else if (braille in brailleToNumber) {
      toAdd = brailleToNumber[braille];
    } else {
      const signal = brailleToSignals[braille];
      if (signal == "capital") {
        isCap = true;
      } else if (signal == "number") {
        isNum = true;
      } else if (signal == "space") {
        toAdd = " ";
        isNum = false;
      }
    }
    if (toAdd) english = english + toAdd;
  }
  return english;
};

const translateEnglish = (englishString) => {
  let braille = "";
  let isNum = false;
  for (let char of englishString) {
    let toAdd = "";
    if (char.toLowerCase() in letterToBraille) {
      if (isUppercase(char)) {
        toAdd += signalsToBraille["capital"];
        char = char.toLowerCase();
      }
      toAdd += letterToBraille[char];
    } else if (char in numberToBraille) {
      if (!isNum) {
        isNum = true;
        toAdd += signalsToBraille["number"];
      }
      toAdd += numberToBraille[char];
    } else if (char in signsToBraille) {
      toAdd = signsToBraille[char];
    } else {
      if (char == " ") {
        toAdd += signalsToBraille["space"];
        isNum = false;
      }
    }
    braille += toAdd;
  }
  return braille;
};

const isUppercase = (char) => {
  return /^[A-Z]$/.test(char);
};

translator();
