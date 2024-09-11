// get input argument
const arg = process.argv;
const input = arg.slice(2).join(" ");

const b_letter_key = {
  "O.....": "a",
  "O.O...": "b",
  "OO....": "c",
  "OO.O..": "d",
  "O..O..": "e",
  "OOO...": "f",
  "OOOO..": "g",
  "O.OO..": "h",
  ".OO...": "i",
  ".OOO..": "j",
  "O..O.": "k",
  "O.O.O.": "l",
  "OO..O.": "m",
  "OO.OO.": "n",
  "O..OO.": "o",
  "OOO.O.": "p",
  "OOOOO.": "q",
  "O.OOO.": "r",
  ".OO.O.": "s",
  ".OOOO.": "t",
  "O...OO": "u",
  "O.O.OO": "v",
  ".OOO.O": "w",
  "OO..OO": "x",
  "OO.OOO": "y",
  "O..OOO": "z",
  ".....O": "CAPS",
  ".O.OOO": "NUM",
  ".O...O": "DOT",
  "......": " ",
};

const b_number_key = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
  "..OO.O": ".",
  "..O...": ",",
  "..O.OO": "?",
  "..OOO.": "!",
  "..OO..": ":",
  "....OO": "-",
  ".O..O.": "/",
  ".OO..O": "<",
  "O..OO.": ">",
  "O.O..O": "(",
  ".O.OO.": ")",
};

const e_letter_key = {
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
  k: "O..O.",
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
  CAPS: ".....O",
  NUM: ".O.OOO",
  DOT: ".O...O",
  " ": "......",
};

const e_number_key = {
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
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..OO.",
  "(": "O.O..O",
  ")": ".O.OO.",
};

function english_to_brail(str) {
  let num_state = false;
  let str_arr = str.split("");
  let res = "";
  str_arr.forEach((el) => {
    if (el == " ") {
      num_state = false;
    }

    if (parseInt(el)) {
      if (!num_state) {
        res += e_letter_key["NUM"];
      }
      res += e_number_key[el];
      num_state = true;
    } else {
      let char = e_letter_key[el.toLowerCase()];
      if (el.toLowerCase() !== el) {
        res += e_letter_key["CAPS"];
      }

      res += char;
    }
  });

  return res;
}

function brail_to_english(str) {
  let capital_state = false;
  let num_state = false;

  let res = "";
  let corr_key;

  for (let i = 0; i < str.length; i += 6) {
    let char = str.slice(i, i + 6);

    if (b_letter_key[char] == "CAPS") {
      capital_state = true;
      corr_key = b_letter_key;
      continue;
    }

    if (b_letter_key[char] == "NUM") {
      num_state = true;
      corr_key = b_number_key;
      continue;
    }

    if (capital_state || num_state) {
      if (capital_state) {
        res += corr_key[char].toUpperCase();
        capital_state = false;
      } else if (num_state) {
        res += corr_key[char];
        if (b_letter_key[char] == " ") {
          res += " ";
          num_state = false;
          corr_key = b_letter_key;
        }
      }
    } else {
      res += corr_key[char];
    }
  }
  return res;
}

// Check if input is braile or english
function translate_text(str) {
  const regex = /[O.]/g;
  let refinedStr = str.replace(regex, "");

  if (refinedStr.length == 0) {
    return brail_to_english(str);
  } else {
    return english_to_brail(str);
  }
}

console.log(translate_text(input));
