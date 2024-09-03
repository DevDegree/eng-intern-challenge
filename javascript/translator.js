#!/usr/bin/env node

// white = . ;  black = 0
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

function init() {
  const args = process.argv.slice(2);

  if (args.length > 0) {
    let tranlsateTo;

    // check if args is in braille or otherwise
    for (const arg of args) {
      const arr = Array.from(arg);

      const isBraille = arr.filter((item) =>
        item === 'O' || item === '.'
      );

      isBraille.length === 0
        ? tranlsateTo = 'braille'
        : tranlsateTo = 'english'    
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
  console.log('to English');
  let englishArr = [];
  let results = [];

  for (const arg of args) {
    const arr = Array.from(arg);

    // split Braille input into arrays of 6 
    for (let i = 0; i < arr.length; i+=6) {
      results.push(arr.slice(i, i+6))
    }
  }

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

  sortToEnglish(englishArr);
}

const sortToEnglish = (array) => {
  // console.log('arr', array);
  let capIndexStart = [];
  let numIndexStart = [];
  let breaks = [];
  let sections = [];
  
  
  // find out where the spaces are
  for (let i = 0; i < array.length; i++) {
    const obj = array[i];
    const key = Object.keys(obj)[0];

    switch (obj[key]) {
      case 'capital':
        capIndexStart.push(i);
        break

      case 'number':
        numIndexStart.push(i);
        break

      case ' ':
        breaks.push(i);
        break
    }
  }

  let tempArr = capIndexStart.concat(numIndexStart);
  sections = tempArr.concat(breaks);
  sections = [...sections.sort((a, b) => a - b)];

  console.log(sections);

  let stringed = [];

  for (const [i, item] of array.entries()) {
    let index = i.toString();
    console.log(item);
    
  }

}



const toBraille = (args) => {
  console.log('to braille', args);

  // for each letter split
  for (const arg of args) {
    const arr = Array.from(arg);

    console.log(arr);
  }
}

init();