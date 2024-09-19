let braileMap = {
  a: "O.....",
  b: "O.O...",
  c: "OO....",
  d: "OO.O..",
  e: "O..O..",
  f: "OOO...",
  g: "OOOO..",
  h: "O.OO..",
  i: ".O.O..",
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
  O: ".OOO..",
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
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..OO.",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
  captital: ".....O",
  number: ".O.OOO",
};

function toBraile(string) {
  return string
    .split("")
    .map((s) => {
      let braileQ = "";
      let isNumber = false;
      if (/^[A-Z]*$/.test(s)) {
        braileQ = braileMap["captital"];
      }
      if (/^[0-9]*$/.test(s) && isNumber == false) {
        isNumber = true;
        braileQ = braileMap["number"];
      }
      if (s == " ") {
        isNumber == false;
      }

      return [braileQ, braileMap[s]].join("");
    })
    .join("");
}

function toString(braile) {
  let isNumber = false;
  let isCapital = false;
  return braile
    .match(/.{1,6}/g)
    .map((b) => {
      if (b === ".O.OOO") {
        isNumber = true;
        return;
      }
      if (b === "......") {
        isNumber = false;
      }

      if (b === ".....O") {
        isCapital = true;
        return;
      }

      if (isNumber) {
        return Object.keys(braileMap)
          .filter((key) => braileMap[key] === b)
          .filter((s) => /^[0-9]*$/.test(s))
          .join("");
      } else {
        if (isCapital) {
          isCapital = false;
          return Object.keys(braileMap)
            .filter((key) => braileMap[key] === b)
            .filter((s) => /^(?!\d+$)[a-z @&$]*$/.test(s))
            .join("")
            .toUpperCase();
        }
        return Object.keys(braileMap)
          .filter((key) => braileMap[key] === b)
          .filter((s) => /^(?!\d+$)[a-z @&$]*$/.test(s))
          .join("");
      }
    })
    .join("");
}

function convert(text) {
  if (/[^O.]/.test(text)) {
    console.log(toBraile(text));
    return toBraile(text);
  }
  console.log(toString(text));
  return toString(text);
}

const arguments = process.argv;

convert(arguments.splice(2).join(" "));
