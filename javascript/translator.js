/**
 * @author Geoff Scornaienchi
 * Sept 2024
 */

const charLookup = {
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
  '1': "O.....",
  '2': "O.O...",
  '3': "OO....",
  '4': "OO.O..",
  '5': "O..O..",
  '6': "OOO...",
  '7': "OOOO..",
  '8': "O.OO..",
  '9': ".OO...",
  '0': ".OOO.."
}

const brailleLookup = {
  "......": ' ',
  "O.....": 'a',
  "O.O...": 'b',
  "OO....": 'c',
  "OO.O..": 'd',
  "O..O..": 'e',
  "OOO...": 'f',
  "OOOO..": 'g',
  "O.OO..": 'h',
  ".OO...": 'i',
  ".OOO..": 'j',
  "O...O.": 'k',
  "O.O.O.": 'l',
  "OO..O.": 'm',
  "OO.OO.": 'n',
  "O..OO.": 'o',
  "OOO.O.": 'p',
  "OOOOO.": 'q',
  "O.OOO.": 'r',
  ".OO.O.": 's',
  ".OOOO.": 't',
  "O...OO": 'u',
  "O.O.OO": 'v',
  ".OOO.O": 'w',
  "OO..OO": 'x',
  "OO.OOO": 'y',
  "O..OOO": 'z',
}

const brailleNumsLookup = {
  "......": ' ',
  "O.....": '1',
  "O.O...": '2',
  "OO....": '3',
  "OO.O..": '4',
  "O..O..": '5',
  "OOO...": '6',
  "OOOO..": '7',
  "O.OO..": '8',
  ".OO...": '9',
  ".OOO..": '0'
}

const processArgs = () => {
  let input = "";
  for (let i = 2; i < process.argv.length; i++){
    input = input.concat(process.argv[i] + ((i < process.argv.length - 1) ? " " : ""))
  }
  return input
}

const detectBraille = (word) => {
  for (let c of word){
    if (c !== '.' && c !== 'O'){
      return false
    }
  }
  return true
}

const translateTextToBraille = (word) => {

  function isUpperCase(s) {
    return (s !== s.toLowerCase() && s === s.toUpperCase());
  }

  function isNumber(s) {
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'].includes(s)
  }

  let textToTranslate = word
  let numberSequence = false
  let newWord = "";

  for (c of word){

    if (c == ' '){
      newWord = newWord.concat('......')
      numberSequence = false
    }
    else if (isNumber(c)){
      if (!numberSequence){
        newWord = newWord.concat('.O.OOO' + charLookup[c])
        numberSequence = true
      }
      else{
        newWord = newWord.concat(charLookup[c])
      }
    }
    else if (isUpperCase(c)){
      newWord = newWord.concat('.....O' + charLookup[c.toLowerCase()])
    }
    else{
      newWord = newWord.concat(charLookup[c])
    }
  }

  return newWord
}

const translateBrailleToText = (braille) => {
  let textToTranslate = braille
  let capitalFollows = false;
  let numberFollows = false;
  let newWord = "";

  while (textToTranslate.length >= 6){
    let currentWord = textToTranslate.substring(0, 6);

    if (currentWord == ".....O"){
      capitalFollows = true
      textToTranslate = textToTranslate.substring(6);
      continue
    }
    else if (currentWord == ".O.OOO"){
      numberFollows = true
      textToTranslate = textToTranslate.substring(6);
      continue
    }
    if (currentWord == "......"){
      numberFollows = false
    }
  
    if (capitalFollows){
      newWord = newWord.concat(brailleLookup[currentWord].toUpperCase())
      capitalFollows = false;
    }
    else if (numberFollows){
      newWord = newWord.concat(brailleNumsLookup[currentWord])
    }
    else{
      newWord = newWord.concat(brailleLookup[currentWord])
    }
    textToTranslate = textToTranslate.substring(6);
      
  }
  return newWord
}

let argsAsString = processArgs();
let isBraille = detectBraille(argsAsString);

let answer = isBraille ? translateBrailleToText(argsAsString) : translateTextToBraille(argsAsString)
console.log(answer)
