const brailleLookup = {
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
  " ": "......",
  capital: ".....O",
  number: ".O.OOO",
};

const isCapitalLetter = (c) => {
  return c >= "A" && c <= "Z";
};

const isNumber = (c) => {
  return c >= "0" && c <= "9";
};

const reverseBrailleLookup = Object.entries(brailleLookup).reduce(
  (m, [key, value]) => {
    m[value] = key;
    return m;
  },
  {},
);

const reverseBrailNumberLookup = Object.entries(brailleLookup).reduce(
  (m, [key, value]) => {
    if (isNumber(key)) {
      m[value] = key;
    }
    return m;
  },
  {},
);

const isBraile = (text) => {
  const items = text.split("");
  return (
    items.length >= 2 &&
    !items.every((x) => x === "O") &&
    items.every((c) => c === "." || c === "O")
  );
};

const processBraille = (text) => {
  const chunks = [];
  for (let i = 0; i < text.length; i += 6) {
    chunks.push(text.slice(i, i + 6));
  }

  if (!chunks.every((chunk) => chunk.length === 6)) {
    process.exit();
  }

  let res = [];
  let isCapital = false;
  let isNumber = false;

  chunks.forEach((c) => {
    if (c === brailleLookup.capital) {
      isCapital = true;
    } else if (c === brailleLookup.number) {
      isNumber = true;
    } else if (c === brailleLookup[" "]) {
      isNumber = false;
      res.push(" ");
    } else {
      let curr = reverseBrailleLookup[c];
      if (curr) {
        if (isNumber) {
          curr = reverseBrailNumberLookup[c];
        } else if (isCapital) {
          curr = curr.toUpperCase();
          isCapital = false;
        }
        res.push(curr);
      }
    }
  });

  return res.join("");
};

const processWords = (text) => {
  let res = [];
  let prevIsNumber = false;

  text.split("").forEach((c) => {
    if (isCapitalLetter(c)) {
      if (prevIsNumber) {
        res.push(brailleLookup[" "]);
      }
      res.push(brailleLookup.capital + brailleLookup[c.toLowerCase()]);
      prevIsNumber = false;
    } else if (isNumber(c)) {
      if (!prevIsNumber) {
        res.push(brailleLookup.number + brailleLookup[c]);
        prevIsNumber = true;
      } else {
        res.push(brailleLookup[c]);
      }
    } else {
      res.push(brailleLookup[c]);
      prevIsNumber = false;
    }
  });

  return res.join("");
};

const main = () => {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.log("Please provide input to convert to braile/english!");
    process.exit();
  }

  const text = args.join(" ");

  isBraile(text)
    ? console.log(processBraille(text))
    : console.log(processWords(text));
};

main();
