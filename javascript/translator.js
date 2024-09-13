const englishToBrailleDictionary = {
  a: "0.....",
  b: "0.0...",
  c: "00....",
  d: "00.0..",
  e: "0..0..",
  f: "000...",
  g: "0000..",
  h: "0.00..",
  i: ".00...",
  j: ".000..",
  k: "0...0.",
  l: "0.0.0.",
  m: "00..0.",
  n: "00.00.",
  o: "0..00.",
  p: "000.0.",
  q: "00000.",
  r: "0.000.",
  s: ".00.0.",
  t: ".0000.",
  u: "0...00",
  v: "0.0.00",
  w: ".000.0",
  x: "00..00",
  y: "00.000",
  z: "0..000",
};

const numbersToBrailleDictionary = {
  1: "0.....",
  2: "0.0...",
  3: "00....",
  4: "00.0..",
  5: "0..0..",
  6: "000...",
  7: "0000..",
  8: "0.00..",
  9: ".00...",
  0: ".000..",
};

const capitalizeNext = ".....0";

const numberNext = ".0000.";

const spaceNext = "......";

// reverse objects key and values to convert braille to alphabets & numbers

const brailleToEnglishDictionary = Object.entries(
  englishToBrailleDictionary
).reduce((accumulator, [key, value]) => {
  accumulator[value] = key;
  return accumulator;
}, {});
// console.log(brailleToEnglishDictionary);

const brailleToNumbersDictionary = Object.entries(
  numbersToBrailleDictionary
).reduce((accumulator, [key, value]) => {
  accumulator[value] = key;
  return accumulator;
}, {});
// console.log(brailleToNumbersDictionary);

// function to translate english alphabets & numbers to Braille
function englishToBrailleTranslator(input) {
  const arr = input.split("");

  let capitalSeries = false;
  let numberSeries = false;

  const converted = arr.map((letter) => {
    if (letter === " ") {
      return spaceNext;
    } else if (isNaN(letter) && letter === letter.toUpperCase()) {
      capitalSeries = true;
      // numberSeries = false;
      return capitalizeNext + englishToBrailleDictionary[letter.toLowerCase()];
    } else if (letter >= "0" && letter <= "9") {
      if (numberSeries === false) {
        numberSeries = true;
        return numberNext + numbersToBrailleDictionary[letter];
      } else {
        return numbersToBrailleDictionary[letter];
      }
    } else {
      return englishToBrailleDictionary[letter];
    }
  });
  return converted.join("");
}

// function to translate Braille to english alphabets & numbers
function brailleToEnglishTranslator(input) {}

// translator function to check input language and convert it
function translator(input) {
  if (input.includes(".") && input.includes("0")) {
    console.log(brailleToEnglishTranslator(input));
  } else {
    console.log(englishToBrailleTranslator(input));
  }
}

translator("Hello World 123");
translator(".....0 0..... ");
translator("123");
translator(" ");
