const brailleAlphabet = [
  { brl: 'O.....', eng: 'a', type: 'letter' },
  { brl: 'O.O...', eng: 'b', type: 'letter' },
  { brl: 'OO....', eng: 'c', type: 'letter' },
  { brl: 'OO.O..', eng: 'd', type: 'letter' },
  { brl: 'O..O..', eng: 'e', type: 'letter' },
  { brl: 'OOO...', eng: 'f', type: 'letter' },
  { brl: 'OOOO..', eng: 'g', type: 'letter' },
  { brl: 'O.OO..', eng: 'h', type: 'letter' },
  { brl: '.OO...', eng: 'i', type: 'letter' },
  { brl: '.OOO..', eng: 'j', type: 'letter' },
  { brl: 'O...O.', eng: 'k', type: 'letter' },
  { brl: 'O.O.O.', eng: 'l', type: 'letter' },
  { brl: 'OO..O.', eng: 'm', type: 'letter' },
  { brl: 'OO.OO.', eng: 'n', type: 'letter' },
  { brl: 'O..OO.', eng: 'o', type: 'letter' },
  { brl: 'OOO.O.', eng: 'p', type: 'letter' },
  { brl: 'OOOOO.', eng: 'q', type: 'letter' },
  { brl: 'O.OOO.', eng: 'r', type: 'letter' },
  { brl: '.OO.O.', eng: 's', type: 'letter' },
  { brl: '.OOOO.', eng: 't', type: 'letter' },
  { brl: 'O...OO', eng: 'u', type: 'letter' },
  { brl: 'O.O.OO', eng: 'v', type: 'letter' },
  { brl: '.OOO.O', eng: 'w', type: 'letter' },
  { brl: 'OO..OO', eng: 'x', type: 'letter' },
  { brl: 'OO.OOO', eng: 'y', type: 'letter' },
  { brl: 'O..OOO', eng: 'z', type: 'letter' },
  { brl: 'O.....', eng: '1', type: 'number' },
  { brl: 'O.O...', eng: '2', type: 'number' },
  { brl: 'OO....', eng: '3', type: 'number' },
  { brl: 'OO.O..', eng: '4', type: 'number' },
  { brl: 'O..O..', eng: '5', type: 'number' },
  { brl: 'OOO...', eng: '6', type: 'number' },
  { brl: 'OOOO..', eng: '7', type: 'number' },
  { brl: 'O.OO..', eng: '8', type: 'number' },
  { brl: '.OO...', eng: '9', type: 'number' },
  { brl: '.OOO..', eng: '0', type: 'number' },
  { brl: '.....O', eng: 'capitalFollows', type: 'follows' },
  { brl: '.O.OOO', eng: 'numberFollows', type: 'follows' },
  { brl: '......', eng: ' ', type: 'space' },
];

const brailleLettersMap = new Map();
brailleAlphabet.forEach(({ brl, eng, type }) => {
  if (type === 'letter' || type === 'space') {
    brailleLettersMap.set(brl, eng);
  }
});

const brailleNumbersMap = new Map();
brailleAlphabet.forEach(({ brl, eng, type }) => {
  if (type === 'number' || type === 'space') {
    brailleNumbersMap.set(brl, eng);
  }
});

const englishMap = new Map();
brailleAlphabet.forEach(({ brl, eng, type }) => {
  if (type === 'letter' || type === 'number' || type === 'space') {
    englishMap.set(eng, brl);
  }
});

const isCharALetter = (char) => {
  return char.toLowerCase() !== char.toUpperCase();
};

const engToBrl = (str) => {
  const capitalFollows = '.....O';
  const numberFollows = '.O.OOO';
  let numberMode = false;
  let output = '';

  for (let i = 0; i < str.length; i++) {
    if (str[i] >= '0' && str[i] <= '9') {
      // str[i] is a number
      if (!numberMode) {
        numberMode = true;
        output += numberFollows;
      }
      output += englishMap.get(str[i]);
    } else if (isCharALetter(str[i])) {
      if (str[i] === str[i].toUpperCase()) {
        // str[i] is a capital letter
        output += capitalFollows;
        output += englishMap.get(str[i].toLowerCase());
      } else {
        output += englishMap.get(str[i]);
      }
    } else {
      // str[i] must be a space
      numberMode = false;
      output += englishMap.get(str[i]);
    }
  }

  return output;
};

const brlToEng = (str) => {
  const capitalFollows = '.....O';
  const numberFollows = '.O.OOO';
  const space = '......';
  let isCapital = false;
  let isNumber = false;
  let output = '';
  for (let i = 0; i < str.length; i += 6) {
    const currSymbol = str.slice(i, i + 6);

    if (isCapital) {
      output += brailleLettersMap.get(currSymbol).toUpperCase();
      isCapital = false;
      continue;
    }

    if (isNumber) {
      output += brailleNumbersMap.get(currSymbol);
      continue;
    }

    if (currSymbol === capitalFollows) {
      isCapital = true;
    } else if (currSymbol === numberFollows) {
      isNumber = true;
    } else if (currSymbol === space) {
      isNumber = false;
      output += brailleLettersMap.get(currSymbol);
    } else {
      output += brailleLettersMap.get(currSymbol);
    }
  }

  return output;
};

const translator = (str) => {
  if (str.length < 6) {
    console.log(engToBrl(str));
  } else {
    const firstSixChars = str.slice(0, 6);
    if (
      brailleLettersMap.has(firstSixChars) ||
      brailleNumbersMap.has(firstSixChars)
    ) {
      console.log(brlToEng(str));
    } else {
      console.log(engToBrl(str));
    }
  }
};

translator(process.argv.slice(2).join(' '));
