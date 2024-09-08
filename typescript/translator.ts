const brailleMap = new Map([
  ["a", "O....."],
  ["b", "O.O..."],
  ["c", "OO...."],
  ["d", "OO.O.."],
  ["e", "O..O.."],
  ["f", "OOO..."],
  ["g", "OOOO.."],
  ["h", "O.OO.."],
  ["i", ".OO..."],
  ["j", ".OOO.."],
  ["k", "O...O."],
  ["l", "O.O.O."],
  ["m", "OO..O."],
  ["n", "OO.OO."],
  ["o", "O..OO."],
  ["p", "OOO.O."],
  ["q", "OOOOO."],
  ["r", "O.OOO."],
  ["s", ".OO.O."],
  ["t", ".OOOO."],
  ["u", "O...OO"],
  ["v", "O.O.OO"],
  ["w", ".OOO.O"],
  ["x", "OO..OO"],
  ["y", "OO.OOO"],
  ["z", "O..OOO"],
  ["1", "O....."],
  ["2", "O.O..."],
  ["3", "OO...."],
  ["4", "OO.O.."],
  ["5", "O..O.."],
  ["6", "OOO..."],
  ["7", "OOOO.."],
  ["8", "O.OO.."],
  ["9", ".OO..."],
  ["0", ".OOO.."],
  ["capital", ".....O"],
  ["decimal", "...O.O"],
  ["number", ".O.OO."],
  [".", "..OO.O"],
  [",", "..O..."],
  ["?", "..O.OO"],
  ["!", "..OOO."],
  [":", "..OOO."],
  [";", "..O.O."],
  ["/", ".O..O."],
  ["<", ".OO..O"],
  [">", "O..OO."],
  ["(", "O.O..O"],
  [")", ".O.OO."],
  [" ", "......"],
]);

const reverseBrailleMap = new Map(
  [...brailleMap].map(([key, value]) => [value, key])
);

function isBraille(input: string) {
  return /^[O.]+$/.test(input);
}

function brailleToEnglish(braille: string) {
  const chunks = braille.match(/.{1,6}/g);
  let output = "";
  let capitalizeNext = false;
  let isNumber = false;

  for (let chunk of chunks as RegExpMatchArray) {
    if (chunk === brailleMap.get("capital")) {
      capitalizeNext = true;
    } else if (chunk === brailleMap.get("number")) {
      isNumber = true;
    } else if (reverseBrailleMap.has(chunk)) {
      let char = reverseBrailleMap.get(chunk);
      if (isNumber) {
        output += char;
        isNumber = false;
      } else {
        output += capitalizeNext ? char?.toUpperCase() : char;
        capitalizeNext = false;
      }
    }
  }
  return output;
}

function englishToBraille(english: string) {
  let output = "";
  let isNumber = false;

  for (let char of english) {
    if (/[A-Z]/.test(char)) {
      output += brailleMap.get("capital");
      char = char.toLowerCase();
    }
    if (/[0-9]/.test(char) && !isNumber) {
      output += brailleMap.get("number");
      isNumber = true;
    }
    if (/[a-z]/.test(char)) {
      isNumber = false;
    }
    const brailleChar = brailleMap.get(char) || brailleMap.get(" "); // Default to space if character not found
    output += brailleChar;
  }
  return output;
}

function translate(input: string) {
  if (isBraille(input)) {
    return brailleToEnglish(input);
  } else {
    return englishToBraille(input);
  }
}

// Main execution
if (require.main === module) {
  const args = process.argv.slice(2);
  const input = args.join(" ");
  const result = translate(input);
  console.log(result);
}
