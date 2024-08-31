const BRAILLE_MAP: { [key: string]: string } = {
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
  " ": "......",
  capitalizationFollows: ".....O",
  numberFollows: ".O.OOO",
};

export function translateToBraille(text: string): string {
  let result: string[] = [];
  let isNumber = false;

  for (const char of text) {
    if (char >= "A" && char <= "Z") {
      if (!isNumber) {
        result.push(BRAILLE_MAP["capitalizationFollows"]);
      }
      result.push(BRAILLE_MAP[char.toLowerCase()]);
      isNumber = false;
    } else if (char >= "a" && char <= "z") {
      result.push(BRAILLE_MAP[char]);
      isNumber = false;
    } else if (char >= "0" && char <= "9") {
      if (!isNumber) {
        result.push(BRAILLE_MAP["numberFollows"]);
        isNumber = true;
      }
      result.push(BRAILLE_MAP[char]);
    } else {
      result.push(BRAILLE_MAP[char] || "");
      isNumber = false;
    }
  }

  return result.join("");
}

if (require.main === module) {
  const input = process.argv.slice(2).join(" ");
  console.log(translateToBraille(input));
}
