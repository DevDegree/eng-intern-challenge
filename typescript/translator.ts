//Sarah Qiao - Shopify Winter 2025 Eng Intern Challenge (September 7, 2024)

interface CharHash {
  [key: string] : string;
}

// Index 0: Capital, Index 1: Decimal, Index 2: Number
const hashOptions: string[] = [".....O", ".O...O", ".O.OOO"];
let hashSelector: number = -1;

const letterHash: CharHash = { // hashSelector < 1
  a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..",
  e: "O..O..", f: "OOO...", g: "OOOO..", h: "O.OO..",
  i: ".OO...", j: ".OOO..", k: "O...O.", l: "O.O.O.",
  m: "OO..O.", n: "OO.OO.", o: "O..OO.", p: "OOO.O.",
  q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.",
  u: "O...OO", v: "O.O.OO", w: ".OOO.O", x: "OO..OO",
  y: "OO.OOO", z: "O..OOO",
};

const numberHash: CharHash = { // hashSelector >= 1
  1: "O.....", 2: "O.O...", 3: "OO....", 4: "OO.O..",
  5: "O..O..", 6: "OOO...", 7: "OOOO..", 8: "O.OO..",
  9: ".OO...", 0: ".OOO..",
};

const punctuationHash: CharHash = { // Assume that 0..00. is "o" unless the "number follow" sequence is used
  ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", 
  ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
  "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.",
  " ": "......"
};

function isBraille(str: string): boolean {
  for(let i = 0; i < str.length; i++) { //O(n) time where n is number of chars in the braille expression
    if(str[i] !== "." && str[i] !== "O") {
      return false;
    }
  }
  return true;
}

// Encode from English to Braille
function encode(words: string[]): string {
  return words
    .map((word: string) => {
      let brailleWord = "";
      hashSelector = -1;
      for(let i = 0; i < word.length; i++) {
        if(isNaN(+word[i])) { //Use Letter Hash
          if (hashSelector === 2 && word[i] === ".") { // Decimal number
            brailleWord = brailleWord.concat(hashOptions[1]);
          } else {
            hashSelector = -1;
            if (word[i].match(/[a-zA-Z]/i)) { // Use Letter Hash
              if(word[i].toLowerCase() !== word[i]) { // Capitalized
                brailleWord = brailleWord.concat(hashOptions[0]);
              }
              brailleWord = brailleWord.concat(letterHash[word[i].toLowerCase()]);
            } else if (punctuationHash[word[i]] !== undefined) { // Use Punctuation Hash
              brailleWord = brailleWord.concat(punctuationHash[word[i]]);
            } else { // undefined character
              brailleWord = brailleWord.concat("");
            }
          }
        } else { // Use Number Hash
          if (hashSelector !== 2) {
            brailleWord = brailleWord.concat(hashOptions[2]);
            hashSelector = 2;
          }
          brailleWord = brailleWord.concat(numberHash[word[i]]);
        }
      }
      return brailleWord;
    })
    .join("......");
}

// Decode from Braille into English
function decode(braille: string): string {
  let output = braille
    .match(/.{1,6}/g)
    ?.map((char: string) => {
      if (hashOptions.includes(char)) {
        hashSelector = hashOptions.indexOf(char);
        if (hashSelector === 1) {
          hashSelector = 2; // Use number hash
          return ".";
        }
        return "";
      } else {
        // Check for punctuation or space (resets hashSelector)
        let keyChar = Object.keys(punctuationHash).find(key => punctuationHash[key] === char);
        if (keyChar) {
          if (keyChar === " ") {
            hashSelector = -1;
          } else if (keyChar === ">" && hashSelector < 1) {
            return hashSelector === 0 ? "O" : "o"; // Special case because 'o' and '>' they have the same pattern
          }
          return keyChar;
        } else {
          // Letter or Number
          if (hashSelector < 1) { // Use Letter Hash
            keyChar = Object.keys(letterHash).find(key => letterHash[key] === char);
            if (hashSelector === 0) { // Capitalized
              hashSelector = -1;
              return keyChar?.toUpperCase();
            } 
            return keyChar; // Lowercase
          } else { // Use Number Hash
            return Object.keys(numberHash).find(key => numberHash[key] === char);
          }
        }
      }
    })
    .join("");

  return output || "";
}

if (process.argv.length > 2) {
  let words: string[] = process.argv.slice(2);

  if (words.length > 1 || words[0].length % 6 !== 0) { // English sentence to encode
    console.log(encode(words));
  } else {
    if(!isBraille(words[0])) { // contains non-braille character
      console.log(encode(words));
    } else { // Braille string to decode
      console.log(decode(words[0]));
    }
  }
} else { // No argument passed
  console.log("");
}