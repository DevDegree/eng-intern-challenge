const BrailleDictionary = {
  letters: {
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
    " ": "......",
  },
  numbers: {
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
  },
  symbols: {
    capital: ".....O",
    number: ".O.OOO",
  },
};

const reverseMapping = (map) => {
  const reversed = {};
  Object.keys(map).forEach((key) => {
    reversed[map[key]] = key;
  });
  return reversed;
};

const BrailleToEnglishChar = (brailleChar, isCapital, isNumber) => {
  const reversedLetters = reverseMapping(BrailleDictionary.letters);
  const reversedNumbers = reverseMapping(BrailleDictionary.numbers);
  if (isCapital) {
    return reversedLetters[brailleChar].toUpperCase();
  } else if (isNumber) {
    return reversedNumbers[brailleChar];
  } else {
    return reversedLetters[brailleChar];
  }
};

const EnglishToBrailleChar = (englishChar, isNumber) => {
  if (/[A-Z]/.test(englishChar)) {
    return (
      BrailleDictionary.symbols.capital +
      BrailleDictionary.letters[englishChar.toLowerCase()]
    );
  } else if (/[0-9]/.test(englishChar)) {
    return (
      (isNumber ? "" : BrailleDictionary.symbols.number) +
      BrailleDictionary.numbers[englishChar]
    );
  } else {
    return BrailleDictionary.letters[englishChar];
  }
};

const detectType = (input) => (/^[O.]+$/.test(input) ? "braille" : "english");

const translateEnglishToBraille = (input) => {
  let isNumber = false;

  return input
    .split("")
    .map((char) => {
      if (/[0-9]/.test(char)) {
        isNumber = true;
      } else {
        isNumber = false;
      }
      return EnglishToBrailleChar(char, isNumber);
    })
    .join("");
};

const translateBrailleToEnglish = (input) => {
  const brailleChunks = input.match(/.{1,6}/g);

  let isCapital = false;
  let isNumber = false;

  return brailleChunks
    .map((chunk) => {
      if (chunk === BrailleDictionary.symbols.capital) {
        isCapital = true;
        return "";
      }
      if (chunk === BrailleDictionary.symbols.number) {
        isNumber = true;
        return "";
      }

      const translatedChar = BrailleToEnglishChar(chunk, isCapital, isNumber);
      isCapital = false;
      if (chunk === BrailleDictionary.letters[" "]) {
        isNumber = false;
      }

      return translatedChar;
    })
    .join("");
};

const translate = (input) => {
  const type = detectType(input);
  if (type === "english") {
    return translateEnglishToBraille(input);
  } else {
    return translateBrailleToEnglish(input);
  }
};

const inputString = process.argv.slice(2).join(" ");
console.log(translate(inputString));
