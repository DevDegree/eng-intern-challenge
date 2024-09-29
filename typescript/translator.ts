type English = string; // length 1 (must enforced in code)
type Braille = string; // length 6 (must enforced in code)
type StrNum = string; // length 1 (must enforced in code) (must identify seperately)

interface Braille_t_Eng { 
  [key: Braille]: English 
};

interface Eng_t_Braille { 
  [key: English]: Braille 
};

interface StrNum_t_Braille { 
  [key: StrNum]: Braille 
};

interface Braille_t_StrNum { 
  [key: Braille]: StrNum 
};

interface Braille_t_Command {
  [key: Braille]: "CAP" | "DECI" | "NUM"
}

const braille_t_eng: Braille_t_Eng = {
  // "..O.. and so on": "eng letter"
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
  "O...O.": "k",
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
  "..OO.O": ".",
  "......": " "
}

const eng_t_braille: Eng_t_Braille = {
  // "eng letter": "..O.. and so on"
  "a": "O.....",
  "b": "O.O...",
  "c": "OO....",
  "d": "OO.O..",
  "e": "O..O..",
  "f": "OOO...",
  "g": "OOOO..",
  "h": "O.OO..",
  "i": ".OO...",
  "j": ".OOO..",
  "k": "O...O.",
  "l": "O.O.O.",
  "m": "OO..O.",
  "n": "OO.OO.",
  "o": "O..OO.",
  "p": "OOO.O.",
  "q": "OOOOO.",
  "r": "O.OOO.",
  "s": ".OO.O.",
  "t": ".OOOO.",
  "u": "O...OO",
  "v": "O.O.OO",
  "w": ".OOO.O",
  "x": "OO..OO",
  "y": "OO.OOO",
  "z": "O..OOO",
  ".": "..OO.O",
  " ": "......",
}

const num_t_braille: StrNum_t_Braille = {
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

const braille_t_num: Braille_t_StrNum = {
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
}

const braille_t_command: Braille_t_Command = {
  ".....O": "CAP",
  ".O...O": "DECI",
  ".O.OOO": "NUM",
}

enum command_t_braille {
  CAP = ".....O",
  DECI = ".O...O",
  NUM = ".O.OOO",
}

function checkBraille(str: string): false|string[] {
  if (str.length % 6 != 0) {
    return false
  }

  const brailleSlice: string[] = []

  for (let i = 0; i < str.length; i++) {
    if (str[i] != "O" && str[i] != ".") {
      return false;
    }

    if ((i % 6 == 0) && (i + 6 <= str.length)) {
      const sample = str.slice(i, i + 6)
      // braille_t_num not included as they're also in eng
      if (!braille_t_eng[sample] && !braille_t_command[sample]) {
        return false;
      }
      brailleSlice.push(sample);
    }
  }

  return brailleSlice;
}

function translateTEng(braille: Braille[]): string {
  let englishStr = "";
  // flags
  let cap = false;
  let num = false;
  let deci = false;
  for (let i = 0; i < braille.length; i++) {
    const brailleSlice = braille[i];

    const command = braille_t_command[brailleSlice] || "";
    if (command?.length > 0) {
      if (command == "CAP") {
        cap = true;
        deci = false;
        num = false;
      } else if (command == "DECI") {
        deci = true;
        cap = false;
        num = false;
      } else if (command == "NUM") {
        num = true;
        cap = false;
        deci = false;
      }
      continue;
    }

    if (cap) {
      englishStr += braille_t_eng[brailleSlice].toUpperCase();
      cap = false;
    } else if (num) {
      englishStr += braille_t_num[brailleSlice];

      if (i + 1 < braille.length && braille_t_num[braille[i + 1]]) {
        num = true; // retain num flag for next digit
      } else {
        num = false;
      }
      
    } else if (deci) {
      englishStr += ".";
      if (i + 1 < braille.length && braille_t_num[braille[i + 1]]) {
        num = true; // set num flag if next digit
      }
      deci = false;
    } else {
      englishStr += braille_t_eng[brailleSlice];
    }
  }
  return englishStr;
}

function translateTBraille(english: English): string {
  let brailleStr = "";
  let lastNum = false;

  for (const symbol of english) {
    const brailleNum = num_t_braille[symbol];
    const brailleLetter = eng_t_braille[symbol.toLowerCase()];
    // console.log(symbol, brailleLetter, brailleNum)

    // Number case
    if (brailleNum?.length > 0) {
      if (lastNum) {
        brailleStr += brailleNum
      } else {
        brailleStr += command_t_braille.NUM + brailleNum;
      }
      lastNum = true;
    }
    // upper/lower case ;)
    else if (brailleLetter?.length > 0) {

      if (symbol == "." && lastNum) {
        brailleStr += (command_t_braille.DECI + brailleLetter)
        continue;
      }
      // upper case
      if (symbol == symbol.toUpperCase() && symbol != " ") {
        brailleStr += (command_t_braille.CAP + brailleLetter);
      }
      // lower case
      else {
        brailleStr += brailleLetter;
      }

      lastNum = false;
    }
  }

  return brailleStr;
}

function work() {
  const argsArr = process.argv;
  if (argsArr.length < 2) {
    console.log("Arg length error");
    return;
  }

  const translationStr = argsArr.slice(2).join(" ");
  // console.log(translationStr);

  if (translationStr?.length <= 0) {
    console.log("Translation str length error");
    return;
  }

  const braille = checkBraille(translationStr);

  if (braille !== false) {
    const eng = translateTEng(braille);
    console.log(eng);
  } else {
    const braille = translateTBraille(translationStr);
    console.log(braille);
  }
}

work();