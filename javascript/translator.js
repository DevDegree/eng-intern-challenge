const engBraille = {
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
  cap: ".....O",
  num: ".O.OOO",
};

const brailleEng = Object.keys(engBraille).reduce((acc, key) => {
  acc[engBraille[key]] = key;
  return acc;
}, {});

function translate(input) {
  if (input.match(/^[O.]+$/)) {
    let result = "";
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < input.length; i += 6) {
      const brailleChar = input.slice(i, i + 6);
      if (brailleChar === engBraille["cap"]) {
        isCapital = true;
      } else if (brailleChar === engBraille["num"]) {
        isNumber = true;
      } else if (brailleChar === engBraille[" "]) {
        isNumber = false; 
        result += " ";
      } else {
        let char = brailleEng[brailleChar];
        if (isNumber && char >= "a" && char <= "j") {
          char = String.fromCharCode(
            char.charCodeAt(0) - "a".charCodeAt(0) + "1".charCodeAt(0)
          );
        } else if (isCapital) {
          char = char.toUpperCase();
          isCapital = false;
        }
        result += char;
      }
    }
    return result;
  } else {
    let result = "";
    let isNumber = false;

    for (const char of input) {
      if (char >= "A" && char <= "Z") {
        result += engBraille["cap"] + engBraille[char.toLowerCase()];
      } else if (char >= "0" && char <= "9") {
        if (!isNumber) {
          result += engBraille["num"];
          isNumber = true;
        }
        result +=
          engBraille[
            String.fromCharCode(
              char.charCodeAt(0) - "1".charCodeAt(0) + "a".charCodeAt(0)
            )
          ];
      } else {
        if (isNumber && (char < "0" || char > "9")) {
          isNumber = false;
        }
        result += engBraille[char];
      }
    }
    return result;
  }
}

const args = process.argv.slice(2);
if (args.length > 0) {
  const input = args.join(" ");
  console.log(translate(input));
}
