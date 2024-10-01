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
  "o.ooo.": "s",
  ".oooo.": "t",
  "o...oo": "u",
  "o.o.oo": "v",
  ".ooo.o": "w",
  "oo..oo": "x",
  "oo.ooo": "y",
  "o..ooo": "z",

  // note 0-9 braille same as a-j braille
  "o.....": "1",
  "o.o...": "2",
  "oo....": "3",
  "oo.o..": "4",
  "o..o..": "5",
  "ooo...": "6",
  "oooo..": "7",
  "o.oo..": "8",
  ".oo...": "9",
  ".ooo..": "0",

  "..oo.o": ".",
  "..o...": ",",
  "..o.oo": "?",
  "..ooo.": "!",
  "..oo..": ":",
  "..o.o.": ";",
  "....oo": "-",
  ".o..o.": "/",
  ".oo..o": "<",
  "o..oo.": ">",
  "o.o..o": "(",
  ".o.oo.": ")",
  "......": " ",

  ".....o": "Capital",
  ".o...o": "Decimal",
  ".o.ooo": "Number",
};

const englishToBraille = {
  "a": "o.....",
  "b": "o.o...",
  "c": "oo....",
  "d": "oo.o..",
  "e": "o..o..",
  "f": "ooo...",
  "g": "oooo..",
  "h": "o.oo..",
  "i": ".oo...",
  "j": ".ooo..",
  "k": "o...o.",
  "l": "o.o.o.",
  "m": "oo..o.",
  "n": "oo.oo.",
  "o": "o..oo.",
  "p": "ooo.o.",
  "q": "ooooo.",
  "r": "o.ooo.",
  "s": "o.ooo.",
  "t": ".oooo.",
  "u": "o...oo",
  "v": "o.o.oo",
  "w": ".ooo.o",
  "x": "oo..oo",
  "y": "oo.ooo",
  "z": "o..ooo",

  // note 0-9 braille same as a-j braille
  "1": "o.....",
  "2": "o.o...",
  "3": "oo....",
  "4": "oo.o..",
  "5": "o..o..",
  "6": "ooo...",
  "7": "oooo..",
  "8": "o.oo..",
  "9": ".oo...",
  "0": ".ooo..",

  ".": "..oo.o",
  ",": "..o...",
  "?": "..o.oo",
  "!": "..ooo.",
  ":": "..oo..",
  ";": "..o.o.",
  "-": "....oo",
  "/": ".o..o.",
  "<": ".oo..o",
  ">": "o..oo.",
  "(": "o.o..o",
  ")": ".o.oo.",
  " ": "......",

  "Capital": ".....o",
  "Decimal": ".o...o",
  "Number": ".o.ooo",
};

const translateEnglishToBraille = (englishStr) => {
  let brailleStr = "";
  let isCapital = false;
  let isNumber = false;

  for (let i = 0; i < englishStr.length; i++) {
    
    // checking for space
    if (englishStr[i] === " ") {
      brailleStr += englishToBraille[" "];
      isNumber = false
    } 

    // checking for number
    else if (!isNaN(englishStr[i])) {
        if (!isNumber) {
            brailleStr += englishToBraille["Number"];
            isNumber = true;
        }
      brailleStr += englishToBraille[englishStr[i]]
    } 

    // checking for capitals
    else if (englishStr[i] === englishStr[i].toUpperCase() && englishStr[i] !== englishStr.toLowerCase()) {
      brailleStr += englishToBraille["Capital"];
      brailleStr += englishToBraille[englishStr[i].toLowerCase()]
      isCapital = true;
    } 

    // checking for decimals
    else if (englishStr[i] === ".") {
      brailleStr += englishToBraille["Decimal"];
    } 

    else (brailleStr += englishToBraille[englishStr[i]])
  }

  return brailleStr
};

console.log(translateEnglishToBraille("Hello2 world1"))