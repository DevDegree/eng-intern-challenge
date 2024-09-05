
const inputString = formatInput();

console.log(inputString);
idLang();

function formatInput() {
  return process.argv.slice(2).join(' ');
}

function readBraille() {

}

function readEnglish() {

}

function idLang() {
  const nonBrailleChar = inputString.search(/[^O.]/);
  //search for a character that is not O or .
  if(nonBrailleChar === -1) {
    //If there are not non braille characters, the string can be interpreted as braille.
    console.log("String is Braille")
  } else {
    console.log("String is not Braille")
  }
}

const brailleAlphanum = [
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
  "O.OO..",
  "O.O.OO",
  ".OOO.O",
  "OO..OO",
  "OO.OOO",
  "O..OOO"
];

const brailleMod = [
  ".....O",
  ".O...O",
  ".O.OOO"
];

const brailleSmyb = [
  "..OO.O",
  "..O...",
  "..O.OO",
  "..OOO.",
  "..OO..",
  "..O.O.",
  "....OO",
  ".O..O.",
  ".OO..O",
  "O..OO.",
  "O.O..O",
  ".O.OO.",
  "......"
];


