// collect input, with "node" and file/path removed
const input = process.argv.slice(2);
console.log("input:", input);

// establish a string to return to user
let output = "";

const notBraile = /[^\.O]/

// handle no input
if (!input.length) {
  console.error("Error: Please add an input of either Braile or English");
  process.exit(1);
}

// determine if input is braile or English
function isItBraile() {
  // only uses . and O characters
  if (notBraile.test(input[0])) {
    console.log("Contains non-Braile characters:", notBraile.exec(input[0]));
    return false;
  }
  // should only be one string
  if (input.length > 1) {
    // add note to user not to use spaces when entering braile?
    console.log("Too long:", input.length);
    return false;
  }
  // should be evenly divisible by 6 (no spaces)
  if (input[0].length % 6 != 0) {
    // add note to user to check all their braile characters are complete?
    console.log("Not divisible by 6:", input[0].length % 6);
    return false;
  }
  return true;
}

const translator = {
  // letters
  a: "O.....",  // ⠁
  b: "OO....",  // ⠃
  c: "O.O...",  // ⠉
  d: "O..O..",  // ⠙
  e: "O..OO.",  // ⠑
  f: "OO.O..",  // ⠋
  g: "O..OOO",  // ⠛
  h: "OOO...",  // ⠓
  i: ".O.O..",  // ⠊
  j: ".O..O.",  // ⠚
  k: "O...O.",  // ⠅
  l: "OO..O.",  // ⠇
  m: "O.O.O.",  // ⠍
  n: "O..OO.",  // ⠝
  o: "O..O.O",  // ⠕
  p: "OO.O.O",  // ⠏
  q: "O..OOO",  // ⠟
  r: "OOO.O.",  // ⠗
  s: ".OO.O.",  // ⠎
  t: ".O..OO",  // ⠞
  u: "O...OO",  // ⠥
  v: "OO..OO",  // ⠧
  w: ".O..OO",  // ⠺
  x: "O.O.OO",  // ⠭
  y: "O..OOO",  // ⠽
  z: "O..O.O",  // ⠵
  // numbers
  "0": ".O..O.",  // ⠚ (same as "j")
  "1": "O.....",  // ⠁
  "2": "OO....",  // ⠃
  "3": "O.O...",  // ⠉
  "4": "O..O..",  // ⠙
  "5": "O..OO.",  // ⠑
  "6": "OO.O..",  // ⠋
  "7": "O..OOO",  // ⠛
  "8": "OOO...",  // ⠓
  "9": ".O.O..",  // ⠊
  // punctuation
  ".": "OOO...",  // Period ⠲
  ",": "OO....",  // Comma ⠂
  "?": ".O.O.O",  // Question Mark ⠦
  "!": ".O..OO",  // Exclamation Mark ⠖
  ":": "OO.O.O",  // Colon ⠒
  ";": "OO.O..",  // Semicolon ⠆
  "-": ".O..O.",  // Dash ⠤
  "/": ".O.OOO",  // Slash ⠌
  "<": "O.OO..",  // Less than ⠣
  ">": "O..O.O",  // Greater than ⠜
  "(": ".O.O.O",  // Left parenthesis ⠶
  ")": "OOO..O",  // Right parenthesis ⠶
  // instructions
  " ": "......", // space
  "capital follows": ".....O",
  "decimal follows": ".O...O",
  "number follows": ".O.OOO",
};

function braileToEnglish() {
  let english = "";
  // break into strings of six characters
  // parse each character into english, allowing for "x follows" modifiers
  // (if character is a space, end "number follows" modifier)
  return english;
}

function englishToBraile() {
  const singleString = input.join(" ");
  const characters = singleString.split("");
  let braile = "";
  // check if next character is a capital or a number, add appropriate braile
  const capital = /[A-Z]/;
  const number = /[0-9]/;
  let numLock = false;
  // parse each character into braile
  characters.forEach((character) => {
    // if character is a space, turn off numLock
    if (character == " ") numLock = false;
    // if character is a number, and numLock is false add "numbers follows";
    // if character is a capital, add "capital follows";
    // shift character from characters array and save
  })
  return braile;
}

if (isItBraile()) output = braileToEnglish();
else output = englishToBraile();

console.log(`${ isItBraile() ? "Braile to English" : "English to Braile"}`, output);
// process.exit(0);
