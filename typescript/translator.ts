
const BRAILLE_CAPITAL_FOLLOWS = ".....O";
const BRAILLE_NUMBER_FOLLOWS = ".O.OOO";
const BRAILLE_SPACE = "......";

const englishToBrailleMap: Map<string, string> = new Map([
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
  ["z", "O..OOO"]
]);

const englishToBrailleNumberMap: Map<string, string> = new Map([
  ["1", "O....."],
  ["2", "O.O..."],
  ["3", "OO...."],
  ["4", "OO.O.."],
  ["5", "O..O.."],
  ["6", "OOO..."],
  ["7", "OOOO.."],
  ["8", "O.OO.."],
  ["9", ".OO..."],
  ["0", ".OOO.."]
]);

const brailleToEnglishMap: Map<string, string> = new Map(
  Array.from(englishToBrailleMap.entries()).map(([k, v]) => [v, k])
);

const brailleToEnglishNumberMap: Map<string, string> = new Map(
  Array.from(englishToBrailleNumberMap.entries()).map(([k, v]) => [v, k])
);

function isValidBraille(input: string): boolean {
  return /^[O.]+$/.test(input) && input.length % 6 === 0;
}

function brailleToEnglish(brailleText: string): string {
  let result = '';
  let isCapital = false;
  let isNumber = false;

  const brailleCells = brailleText.match(/.{1,6}/g);
  if (!brailleCells) return '';

  for (const cell of brailleCells) {
    if (cell === BRAILLE_SPACE) {
      isNumber = false;
      result += ' ';
      continue;
    }
    if (cell === BRAILLE_CAPITAL_FOLLOWS) {
      isCapital = true;
      continue;
    }

    if (cell === BRAILLE_NUMBER_FOLLOWS) {
      isNumber = true;
      continue;
    }

    let translated = '';

    if (isNumber) {
      translated = brailleToEnglishNumberMap.get(cell) || '';
      if (translated === '') {
        // Fallback to letters if symbol not found in numbers
        translated = brailleToEnglishMap.get(cell) || '';
      }
    } else {
      translated = brailleToEnglishMap.get(cell) || '';
    }

    if (translated === '') {
      continue;
    }

    if (isCapital) {
      result += translated.toUpperCase();
      isCapital = false;
    } else {
      result += translated;
    }
  }

  return result;
}

function englishToBraille(englishText: string): string {
  let result = '';
  let isNumber = false;

  for (const char of englishText) {
    if (char >= 'A' && char <= 'Z') {
      result += BRAILLE_CAPITAL_FOLLOWS;
      result += englishToBrailleMap.get(char.toLowerCase()) || '';
      isNumber = false;
    } else if (char >= 'a' && char <= 'z') {
      result += englishToBrailleMap.get(char) || '';
      isNumber = false;
    } else if (char >= '0' && char <= '9') {
      if (!isNumber) {
        result += BRAILLE_NUMBER_FOLLOWS;
        isNumber = true;
      }
      result += englishToBrailleNumberMap.get(char) || '';
    } else if (char === ' ') {
      result += BRAILLE_SPACE;
      isNumber = false;
    }
    // TODO: handle other special characters
  }

  return result;
}

function main(args: string[]) {
  const text = args.slice(2).join(' ');
  if (!text) {
    console.log('Usage: translator <English Text or Braille>');
    return;
  }
  if (isValidBraille(text)) {
    console.log(brailleToEnglish(text));
  } else {
    console.log(englishToBraille(text));
  }
}

main(process.argv);