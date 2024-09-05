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
  "O..OO.",
  "O.O..O",
  ".O.OO.",
  "......",
];

const brailleMod = [".....O", ".O...O", ".O.OOO"];

const alphNum = "abcdefghijklmnopqrstuvwxyz.x?!:;-/<>() ".split("");

let inputString = formatInput();

console.log(inputString);
idLang();

function formatInput() {
  return process.argv.slice(2).join(" ");
}

function readBraille() {
  let braille = [];
  for (let i = 0; i < inputString.length; i += 6) {
    let char = inputString.slice(i, i + 6);
    braille.push(char);
  }
  return brailleToEng(braille);
}

function brailleToEng(arr) {
  console.debug(arr);
  let eng = "";
  while (arr.length > 0) {
    //could cut off last character?
    let char = arr.shift();
    let mod = brailleMod.indexOf(char);
    console.debug(mod);
    if (mod === -1) {
      eng += alphNum[brailleAlphanum.indexOf(char)];
      console.debug(eng);
    }
    if (mod === 0) {
      eng += alphNum[brailleAlphanum.indexOf(arr.shift())].toUpperCase();
    }
    if (mod === 1) {
      // Not Technically within spec to do anything with a decimal BUT DO MAKE THIS DO SOMETHING ANYWAY
    }
    if (mod === 2) {
      while (arr.length > 0 && char !== "......") {
        char = arr.shift();
        console.debug(char);

        eng += (brailleAlphanum.indexOf(char) + 1 );
      }
    }
    console.debug(eng);
  }
  return eng;
}

function engToBraille(string) {
  for( i = 0 ; i < string.length; i++){
    //is the characer a number?

  }
}

function idLang() {
  const nonBrailleChar = inputString.search(/[^O.]/);
  //search for a character that is not O or .
  if (nonBrailleChar === -1) {
    //If there are not non braille characters, the string can be interpreted as braille.
    console.log("String is Braille");

    console.log("outputting English:\n" + readBraille());
  } else {
    console.log("String is not Braille");
  }
}
