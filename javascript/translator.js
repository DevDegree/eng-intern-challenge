#!/usr/bin/env node

const translation = [
  { 'a': ['O', '.', '.', '.', '.', '.'] },
  { 'b': ['O', '.', 'O', '.', '.', '.'] },
  { 'c': ['O', 'O', '.', '.', '.', '.'] },
  { 'd': ['O', 'O', '.', 'O', '.', '.'] },
  { 'e': ['O', '.', '.', 'O', '.', '.'] },
  { 'f': ['O', 'O', 'O', '.', '.', '.'] },
  { 'g': ['O', 'O', 'O', 'O', '.', '.'] },
  { 'h': ['O', '.', 'O', 'O', '.', '.'] },
  { 'i': ['.', 'O', 'O', 'O', '.', '.'] },
  { 'j': ['.', 'O', 'O', 'O', '.', '.'] },
  { 'k': ['O', '.', '.', '.', 'O', '.'] },
  { 'l': ['O', '.', 'O', '.', 'O', '.'] },
  { 'm': ['O', 'O', '.', '.', 'O', '.'] },
  { 'n': ['O', 'O', '.', 'O', 'O', '.'] },
  { 'o': ['O', '.', '.', 'O', 'O', '.'] },
  { 'p': ['O', 'O', 'O', '.', 'O', '.'] },
  { 'q': ['O', 'O', 'O', 'O', 'O', '.'] },
  { 'r': ['O', '.', 'O', 'O', 'O', '.'] },
  { 's': ['.', 'O', 'O', '.', 'O', '.'] },
  { 't': ['.', 'O', 'O', 'O', 'O', '.'] },
  { 'u': ['O', '.', '.', '.', 'O', 'O'] },
  { 'v': ['O', '.', 'O', '.', 'O', 'O'] },
  { 'w': ['.', 'O', 'O', 'O', '.', 'O'] },
  { 'x': ['O', 'O', '.', '.', 'O', 'O'] },
  { 'y': ['O', 'O', '.', 'O', 'O', 'O'] },
  { 'z': ['O', '.', '.', 'O', 'O', 'O'] },
  { 'O': ['.', 'O', 'O', 'O', '.', '.'] },
  { '1': ['O', '.', '.', '.', '.', '.'] },
  { '2': ['O', '.', 'O', '.', '.', '.'] },
  { '3': ['O', '.', '.', 'O', '.', '.'] },
  { '4': ['O', 'O', '.', 'O', '.', '.'] },
  { '5': ['O', '.', '.', '0', '.', '.'] },
  { '6': ['O', 'O', 'O', '.', '.', '.'] },
  { '7': ['O', 'O', 'O', 'O', '.', '.'] },
  { '8': ['O', '.', 'O', 'O', '.', '.'] },
  { '9': ['.', 'O', 'O', '.', '.', '.'] },
  { capital: ['.', '.', '.', '.', '.', 'O']},
  { decimal: ['.', 'O', '.', '.', '.', 'O']},
  { number: ['.', 'O', '.', 'O', 'O', 'O']},
  { '.': ['.', '.', 'O', 'O', '.', 'O'] },  
  { ',': ['.', '.', 'O', '.', '.', '.'] },  
  { '?': ['.', '.', 'O', '.', 'O', 'O'] },
  { '!': ['.', '.', 'O', 'O', 'O', '.'] },
  { ':': ['.', '.', 'O', 'O', '.', '.'] },  
  { ';': ['.', '.', 'O', '.', 'O', '.'] },  
  { '-': ['.', '.', '.', '.', 'O', 'O'] },  
  { '/': ['.', 'O', '.', '.', 'O', '.'] },  
  { '<': ['.', 'O', 'O', '.', '.', 'O'] },
  { '>': ['O', '.', '.', 'O', 'O', '.'] },
  { '(': ['O', '.', 'O', '.', '.', 'O'] },
  { ')': ['.', 'O', '.', 'O', 'O', '.'] }, 
  { ' ': ['.', '.', '.', '.', '.', '.'] },
];

let translated;

function init() {
  const args = process.argv.slice(2);

  if (args.length > 0) {
    let tranlsateTo;

    // check if args is in braille or otherwise
    for (const arg of args) {
      const arr = Array.from(arg);

      let isBraille;

      isBraille = arr.every((item) =>
        item === 'O' || item === '.'
      );

      isBraille
        ? tranlsateTo = 'english'
        : tranlsateTo = 'braille'    
    }

    if (tranlsateTo === 'braille') {
      toBraille(args);
    } else {
      toEnglish(args);
    }

  } else {
    console.log('No arguments provided.');
  }
}

const toEnglish = (args) => {
  let englishArr = [];
  let results = [];

  for (const arg of args) {
    const arr = Array.from(arg);

    // split Braille input into arrays of 6 
    for (let i = 0; i < arr.length; i+=6) {
      results.push(arr.slice(i, i+6))
    }
  }

  // Prepare to break up words, numbers, capitals, etc... and place into its own array
  for (const [index, res] of results.entries()) {
    const resString = res.join().toString();

    for (let i = 0; i < translation.length; i++) {
      const key = Object.keys(translation[i]).toString();

      const transString =(translation[i][key]).join().toString();
      
      if (resString === transString) {
        let obj = {};
        obj[index] = key;
        englishArr.push(obj);
      }
    }
  }

  updateAlphaFormat(englishArr);
}

const updateAlphaFormat = (array) => {
  let capIndexStart = [];
  let numIndexStart = [];
  let spaces = [];
  let sections = [];
  
  // find out where the breaks are
  for (let i = 0; i < array.length; i++) {
    const obj = array[i];
    const key = Object.keys(obj)[0];


    switch (obj[key]) {
      case 'capital':
        capIndexStart.push(i);
        break;

      case 'number':
        numIndexStart.push(i);
        break;

      case ' ':
        spaces.push(i);
        break;

      case 'decimal':
        let ob = {};
        ob[key] = '.';
        array[key] = ob

        const decIndex = array.findIndex(el => el === obj);
        array[decIndex] = ob
        break;
    }
  }

  let tempArr = capIndexStart.concat(numIndexStart);
  sections = tempArr.concat(spaces);
  sections = [...sections.sort((a, b) => a - b)];

  let exampleArr = [];
  let stringArr = [];

  let a = [];
  // split each word or break into it's own array
  for (let i = 0; i < sections.length; i++) {
    a = [...array.slice(sections[i], sections[i + 1])];    
    exampleArr.push([...a]);
  }

  for(const word of exampleArr) {
    let tempArr= [];
    let num = [];
    let capWord = [];
    let regString = []

    for (let i = 0; i < word.length; i++) {
      const key = Object.keys(word[i]).toString();
      const val = (word[i][key]);
      tempArr.push(val);
    }

    if(tempArr[0] === 'capital') {
      capWord = tempArr.filter((a) => {
        return /^[A-Za-z]+$/.test(a);
      });

      capWord.shift();
      const upper = capWord[0].toUpperCase();
      capWord[0] = upper;
      tempArr = [...capWord];

    } else if (tempArr[0] === 'number') {
      num = tempArr.filter((a) => {
        return /^\d*\.?\d*$/.test(a);
      });
      tempArr = [...num];

    } else {
      regString = tempArr.filter((a) => {
        return /^[a-zA-Z\s]+$/.test(a);
      });

      tempArr = [...regString];
    }

    stringArr.push(tempArr);
  }

  const finalStringArr = stringArr.flatMap(x => x);
  translated = finalStringArr.join('');
  console.log(translated);
  return translated;
}

const toBraille = (args) => {
  let brailleArr = [];

  // for each letter split
  for (const [i, arg] of args.entries()) {
    const arr = Array.from(arg);

    if (i !== (args.length - 1)) {
      arr.push(' ');
    }
    brailleArr.push(arr);
  }

  updateBrailleFormat(brailleArr);
}

const updateBrailleFormat = (array) => {
  let updatedFormatArr = [];

  // find if there are capitals or numbers
  for (const [i, item] of array.entries()) {
    const tempObj = checkTypeof(item, i);
    updatedFormatArr[tempObj.index] = tempObj.arr;
  }

  const combinedArr = updatedFormatArr.flat();

  const brailleArr = combinedArr.map((item, index) => {
    for (let i = 0; i < translation.length; i++) {
      let key = Object.keys(translation[i])[0];

      if (item === key) {
        return translation[i][key];
      }
    }
  });

  translated = brailleArr.flatMap(x => x).join('');
  console.log(translated);

  return translated 
}


const checkTypeof = (x, i) => {
  const cap = 'capital';
  const num = 'number';
  const dec = 'decimal';

  let isNum;
  let isAlpha;

  x.filter(a => {
    isNum = /^\d+(\.\d+)?$/.test(a);

    isAlpha = /^[^0-9]*$/.test(a);
  })

  if (isNum) {
    x.unshift(num);
    return {
      index: i,
      arr: [...x]
    }

  } else if (isAlpha) {
    let hasCapital;

    if (x[0] === x[0].toUpperCase()) {
      x.filter(item => {
          /^[^0-9]*$/.test(item)
            ? hasCapital = true
            : hasCapital = false;
        });
      
      if (hasCapital) {
        x[0] = x[0].toLowerCase();
        x.unshift(cap);
      }
    }
    return {
      index: i,
      arr: [...x]
    }
  }
}

init();