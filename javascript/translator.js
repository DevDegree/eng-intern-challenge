/*
* This file takes in a series of command line arguments
* and formats those arguments as a string. That string is 
* translated to or from braille.
*/

const inputText = process.argv.slice(2).join(" ");

let capitalFollows = false;
let decimalFollows = false;
let numberFollows = false;

const englishToBrailleMap = new Map([
  ["a", "O....."],
  ["b", "O.O..."],
  ["c", "OO...."],
  ["d", "OO.O.."],
  ["e", "O..O.."],
  ["f", "OOO..."],
  ["g", "OOOO.."],
  ["h", "O.OO.."],
  ["i", ".OO..."],
  ["j", ".OOO.."],
  ["k", "O...O."],
  ["l", "O.O.O."],
  ["m", "OO..O."],
  ["n", "OO.OO."],
  ["o", "O..OO."],
  ["p", "OOO.O."],
  ["q", "OOOOO."],
  ["r", "O.OOO."],
  ["s", ".OO.O."],
  ["t", ".OOOO."],
  ["u", "O...OO"],
  ["v", "O.O.OO"],
  ["w", ".OOO.O"],
  ["x", "OO..OO"],
  ["y", "OO.OOO"],
  ["z", "O..OOO"],
  ["1", "O....."],
  ["2", "O.O..."],
  ["3", "OO...."],
  ["4", "OO.O.."],
  ["5", "O..O.."],
  ["6", "OOO..."],
  ["7", "OOOO.."],
  ["8", "O.OO.."],
  ["9", ".OO..."],
  ["0", ".OOO.."],
  ["capitalFollows", ".....O"],
  ["decimalFollows", ".O...O"],
  ["numberFollows", ".O.OOO"],
  [" ", "......"],
]);
const brailleToEnglishMap = new Map();
englishToBrailleMap.forEach((value, key) => {
  if (isNaN(key) || key === " ") {
    brailleToEnglishMap.set(value, key);   
  }
});

function getBrailleChar(englishChar) {
  let preString = "";

  if (englishChar === " ") {
    decimalFollows = false;
    numberFollows = false;
  } else if (!isNaN(englishChar) && !numberFollows) {
    numberFollows = true;
    preString = englishToBrailleMap.get("numberFollows");
  } else if (englishChar !== englishChar.toLowerCase()) {
    preString = englishToBrailleMap.get("capitalFollows");
    englishChar = englishChar.toLowerCase();
  }

  return preString + englishToBrailleMap.get(englishChar);
}

function getEnglishChar(brailleStr) {
  let char = brailleToEnglishMap.get(brailleStr);
  
  if (char === " ") {
    capitalFollows = false;
    decimalFollows = false;
    numberFollows = false;
  } else if (char === "capitalFollows") {
    capitalFollows = true;
    return "";
  } else if (char === "decimalFollows") {
    decimalFollows = true;
    return "";
  } else if (char === "numberFollows") {
    numberFollows = true;
    return "";
  }
  
  if (numberFollows) {
    if (char === "j") {
      char = "0";
    } else {
      char = String.fromCharCode(char.charCodeAt(0) - 48);
    }
  }
  
  if (capitalFollows) {
    capitalFollows = false;
    char = char.toUpperCase();
  }
  
  return char;
}

function brailleToEnglish(braille) {
  const getNextLetter = (idx) => braille.slice(idx, idx + 6);

  let englishStr = "";

  for (let i = 0; i < braille.length; i += 6) {
    englishStr += getEnglishChar(getNextLetter(i));
  }

  return englishStr;
}

function englishToBraille(english) {
  return english.replaceAll(/./g, (char) => getBrailleChar(char));
}

function isBrailleText(text) {
  return text && text.length % 6 === 0 && text.search(/[^\.O]/g) === -1;
}

function translateBraille(text) {
  return isBrailleText(text) ? brailleToEnglish(text) : englishToBraille(text);
}

// Print out the translation to stout
console.log(translateBraille(inputText))
