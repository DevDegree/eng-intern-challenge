export{}

// collect input, with node and file/path removed
const input = process.argv.slice(2);

// establish a string to return to user
let output = "";

const notBraile = /[^\.O]/

// handle no input
if (!input.length) {
  console.error("Error: Please add a valid input of either Braile or English");
  process.exit(1);
}

// determine if input is braile or English
function isItBraile() {
  // only uses . and O characters
  if (notBraile.test(input[0])) return false;
  // should only be one string
  if (input.length > 1) return false; // add note to user not to use spaces when entering braile?
  // should be evenly divisible by 6 (no spaces)
  if (input[0].length % 6 != 0) return false; // add note to user to check all their braile characters are complete?
  else return true;
}

const instructions: { [key: string]: string } = {
  "capital follows": ".....O",
  "number follows": ".O.OOO",
}

const numbers: { [key: string]: string } = {
  // (same as a-j)
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  "0": ".OOO..",
}

const letters: { [key: string]: string } = {
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
  " ": "......", // space
}

// establish regex to identify letters or numbers
const capital = /[A-Z]/;
const number = /[0-9]/;
// establish variables to hold modifier status
let capsLock = true;
let numLock = false;

function braileToEnglish() {
  let english = "";
  // break input into strings of six characters
  let characters: string[] = [];
  const braileLetters = input[0].matchAll(/[O\.]{6}/g);
  for(let match of braileLetters) characters.push(match[0]);
  // parse each character into english, allowing for "x follows" modifiers
    characters.forEach((char) => {
    // if character is a space, end "number follows" modifier and add space
    if (char == letters[" "]) {
      numLock = false;
      english += " ";
      return;
    }
    // if it's "number follows", set numLock to true
    if (char == instructions["number follows"]) numLock = true;
    // if it's "capital follows", set capsLock to true (otherwise reset to false)
    if (char == instructions["capital follows"]) capsLock = true;
    // if numLock is true, translate from number definitions
    if (numLock) {
      // let number: string = "";
      for(let n in numbers) if (char == numbers[n]) english += n;
      // english += number;
    } else {
      // otherwise, translate from letter definitions
      // let letter: string = "";
      for (let l in letters) {
        if (char == letters[l]) {
          if (capsLock) {
            english += l.toUpperCase();
            capsLock = false;
          } else english += l;
        }
      }
      // english += letter;
    }
  });
  return english;
}

function englishToBraile() {
  // convert input into array of individual characters
  const characters = input.join(" ").split("");
  // create an empty string to return;
  let braile = "";
  // check if next character is a capital or a number, add appropriate braile
  characters.forEach((character) => {
    // if character is a space, turn off numLock
    if (character == " ") numLock = false;
    // if character is a number, and numLock is false add "numbers follows";
    if (number.test(character)) {
      if (!numLock) {
        braile += instructions["number follows"];
        numLock = true;
      }
      // parse the number into braile
      braile += numbers[character];
    }
    else {
      // if character is a capital, add "capital follows";
      if (capital.test(character)) braile += instructions["capital follows"];
      // parse the character into braile
      if (letters[character.toLowerCase()] !== undefined) braile += letters[character.toLowerCase()];
      // add a flag for undefined characters (e.g. punctuation)
    }
  })
  return braile;
}

if (isItBraile()) output = braileToEnglish();
else output = englishToBraile();

console.log(output);
process.exit(0);
