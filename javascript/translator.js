const brailleToEnglish = {
  "o.....": "a",
  "o.o...": "b",
  "oo....": "c",
  "oo.o..": "d",
  "o..o..": "e",
  "ooo...": "f",
  "oooo..": "g",
  "o.oo..": "h",
  ".oo...": "i",
  ".ooo..": "j",
  "o...o.": "k",
  "o.o.o.": "l",
  "oo..o.": "m",
  "oo.oo.": "n",
  "o..oo.": "o",
  "ooo.o.": "p",
  "ooooo.": "q",
  "o.ooo.": "r",
  ".oo.o.": "s",
  ".oooo.": "t",
  "o...oo": "u",
  "o.o.oo": "v",
  ".ooo.o": "w",
  "oo..oo": "x",
  "oo.ooo": "y",
  "o..ooo": "z",
  "..oo.o": ".",
  "......": " ",
};

const brailleNumbersToEnglish = {
  "o.....": 1,
  "o.o...": 2,
  "oo....": 3,
  "oo.o..": 4,
  "o..o..": 5,
  "ooo...": 6,
  "oooo..": 7,
  "o.oo..": 8,
  ".oo...": 9,
  ".ooo..": 0,
};

const englishToBraille = {
  a: "o.....",
  b: "o.o...",
  c: "oo....",
  d: "oo.o..",
  e: "o..o..",
  f: "ooo...",
  g: "oooo..",
  h: "o.oo..",
  i: ".oo...",
  j: ".ooo..",
  k: "o...o.",
  l: "o.o.o.",
  m: "oo..o.",
  n: "oo.oo.",
  o: "o..oo.",
  p: "ooo.o.",
  q: "ooooo.",
  r: "o.ooo.",
  s: ".oo.o.",
  t: ".oooo.",
  u: "o...oo",
  v: "o.o.oo",
  w: ".ooo.o",
  x: "oo..oo",
  y: "oo.ooo",
  z: "o..ooo",
  1: "o.....",
  2: "o.o...",
  3: "oo....",
  4: "oo.o..",
  5: "o..o..",
  6: "ooo...",
  7: "oooo..",
  8: "o.oo..",
  9: ".oo...",
  0: ".ooo..",
  " ": "......",
  Capital: ".....o",
  Number: ".o.ooo",
};

const capitalFollows = ".....o";
const numberFollows = ".o.ooo";

const translateEnglishToBraille = (englishStr) => {
  let brailleStr = "";
  let isCapital = false;
  let isNumber = false;

  for (let i = 0; i < englishStr.length; i++) {
    if (englishStr[i] === " ") {
      brailleStr += englishToBraille[" "];
      isNumber = false; //Set number flag to false when there is a space. (Technical Requirment)
    } 
    
    else if (!isNaN(englishStr[i])) {
      if (!isNumber) {
        brailleStr += englishToBraille["Number"];
        isNumber = true;
      }
      brailleStr += englishToBraille[englishStr[i]];
    } 
    
    else if (
      englishStr[i] === englishStr[i].toUpperCase()
    ) {
      brailleStr += englishToBraille["Capital"];
      brailleStr += englishToBraille[englishStr[i].toLowerCase()];
      isCapital = true;
    } 
    
    else brailleStr += englishToBraille[englishStr[i]];

  }

  return brailleStr.toUpperCase();
};

const translateBrailleToEnglish = (brailleStr) => {
  let englishStr = "";
  let isNumber = false;
  let isCapital = false;

  for (let i = 0; i < brailleStr.length; i += 6) {
    const slicedBraille = brailleStr.slice(i, i + 6); //Divide string into groups of 6 

    if (slicedBraille === numberFollows) {
      isNumber = true;
    } 
    
    else if (slicedBraille === capitalFollows) {
      isCapital = true;
    } 

    else if (slicedBraille === brailleToEnglish["......"]) {
      englishStr += " ";
      isNumber = false;
    } 
    
    else {
      if (isNumber) {
        englishStr += brailleNumbersToEnglish[slicedBraille];
      } 
      
      else if (isCapital) {
        englishStr += brailleToEnglish[slicedBraille].toUpperCase();
        isCapital = false;
      } 
      
      else englishStr += brailleToEnglish[slicedBraille];

    }
  }

  return englishStr;
};

// Determine if input string is in Braille or English
const isBraille = (inputStr) => {
  return inputStr.length % 6 === 0 && /^[o.]+$/.test(inputStr);
};

const translateInput = (inputStr) => {
  return isBraille(inputStr)
    ? translateBrailleToEnglish(inputStr)
    : translateEnglishToBraille(inputStr);
};

const args = process.argv.slice(2);
const inputStr = args.join(" ");
console.log(translateInput(inputStr));