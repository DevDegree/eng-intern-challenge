const HashTable = require("./hashTable");
const Helper = require("./helper");

function main() {
  // initilizing characters as well as Braille in HashSet
  const alphabets = new HashTable();
  const numbers = new HashTable();
  numberInitilizing(numbers);
  alphabetsInilization(alphabets);
  const helper = new Helper(alphabets, numbers);

  // reading data from command prompt
  let inputString = "";
  for (let i = 2; i < process.argv.length; i++) {
    if (i + 1 == process.argv.length) {
      inputString += process.argv[i];
    } else {
      inputString += process.argv[i] + " ";
    }
  }

  let result = helper.convert(inputString);
  console.log(result);
}

// function help to initlize all the numbers
function numberInitilizing(numbers) {
  let data = {
    " ": "......", // Space
    0: ".OOO..",
    1: "O.....",
    2: "O.O...",
    3: "OO....",
    4: "OO.O..",
    5: "O..O..",
    6: "OOO...",
    7: "OOOO..",
    8: "O.OO..",
    9: ".OO...",
    C: ".....O", //for capital
    N: ".O.OOO", // for numbers
  };

  for (const [key, value] of Object.entries(data)) {
    numbers.set(value, key + "");
    numbers.set(key + "", value);
  }
}

function alphabetsInilization(alphabets) {
  let data = {
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
    C: ".....O", //for capital
    N: ".O.OOO", // for numbers
    " ": "......", // for space
  };
  for (const [key, value] of Object.entries(data)) {
    alphabets.set(value, key + "");
    alphabets.set(key + "", value);
  }
}

if (require.main === module) {
  main();
}
