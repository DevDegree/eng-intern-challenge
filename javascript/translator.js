class TwoWayMap {
    constructor(map) {
       this.map = new Map(map)
       this.reverseMap = new Map()

       for(const [key, value] of map) {
          this.reverseMap.set(value, key)
       }
    }
    get(key) { return this.map.get(key) }
    reverseGet(key) { return this.reverseMap.get(key) }
}

const alphabetMap = new TwoWayMap(new Map([
  ['a', 'O.....'],
  ['b', 'O.O...'],
  ['c', 'OO....'],
  ['d', 'OO.O..'],
  ['e', 'O..O..'],
  ['f', 'OOO...'],
  ['g', 'OOOO..'],
  ['h', 'O.OO..'],
  ['i', '.OO...'],
  ['j', '.OOO..'],
  ['k', 'O...O.'],
  ['l', 'O.O.O.'],
  ['m', 'OO..O.'],
  ['n', 'OO.OO.'],
  ['o', 'O..OO.'],
  ['p', 'OOO.O.'],
  ['q', 'OOOOO.'],
  ['r', 'O.OOO.'],
  ['s', '.OO.O.'],
  ['t', '.OOOO.'],
  ['u', 'O...OO'],
  ['v', 'O.O.OO'],
  ['w', '.OOO.O'],
  ['x', 'OO..OO'],
  ['y', 'OO.OOO'],
  ['z', 'O..OOO'],
  [' ', '......'],
  ['CAPS', '.....O'],
  ['DEC', '.O...O'],
  ['NUM', '.O.OOO'],
]))
const symbolMap = new TwoWayMap(new Map([
  ['1', 'O.....'],
  ['2', 'O.O...'],
  ['3', 'OO....'],
  ['4', 'OO.O..'],
  ['5', 'O..O..'],
  ['6', 'OOO...'],
  ['7', 'OOOO..'],
  ['8', 'O.OO..'],
  ['9', '.OO...'],
  ['0', '.OOO..'],
  ['.', '..OO.O'],
  [',', '..O...'],
  ['?', '..O.OO'],
  ['!', '..OOO.'],
  [':', '..OO..'],
  [';', '..O.O.'],
  ['-', '....OO'],
  ['/', '.O..O.'],
  ['<', '.OO..O'],
  ['>', 'O..OO.'],
  ['(', 'O.O..O'],
  [')', '.O.OO.'],
]))

function brailleToEnglish(str){
  let capsLock = false
  let numMode = false

  let result = ""
  for(let i=0; i<str.length; i+=6){
    const braille = str.substring(i, i+6)

    let translation
    if(numMode==true){
      if(alphabetMap.reverseGet(braille)=="DEC") translation = "DEC" //decimal point
      else translation = symbolMap.reverseGet(braille) //num
    } else {
      if(alphabetMap.reverseGet(braille)) translation = alphabetMap.reverseGet(braille)
      else translation = symbolMap.reverseGet(braille)
    }

    if(translation=="CAPS"){
      capsLock=true
    }else if(translation=="NUM"){
      numMode=true
    }else if(translation=="DEC"){
      result += '.'
    }else{
      if(capsLock==true) translation = translation.toUpperCase()
      if(translation==' ') numMode=false

      result += translation
      capsLock = false
    }
  }
  return result;
}

function englishToBraille(english){
  let result = ""
  let numFound = false

  for(let i=0; i<english.length; i++){
    let char = english.charAt(i)
    if(isLetter(char)){
        if(isUpperCase(char)){
          result += alphabetMap.get("CAPS")
        }
        result += alphabetMap.get(char.toLowerCase())
    }else if(char==" "){
      result += alphabetMap.get(char)
      numFound = false
    }else if(isNumeric(char)){
      if(numFound==false){
        result += alphabetMap.get("NUM")
        numFound = true
      }
      result += symbolMap.get(char)
    }else if(!isLetter(char)){
      //next char is num means cur char is decimal
      if(char=='.' && i+1<english.length && isNumeric(english.charAt(i+1))){ 
        result += alphabetMap.get("DEC")
      }else{
        result += symbolMap.get(char)
      }
    }
  }
  return result
}

function isNumeric(value) {
    return /^-?\d+$/.test(value);
}
function isUpperCase(str){
  return str == str.toUpperCase()
}
function isLetter(str){
  return str.length === 1 && str.match(/[a-z]/i);
}

function isEnglish(text){
  if(text.length%6!=0) return true//braille text must have 6 sections per character

  for(let char of text){
    if(char!='.' && char!='O') return true
  }
  return false
}

function brailleTranslator(text){
  if(isEnglish(text)){
    return englishToBraille(text)
  }
  return brailleToEnglish(text)
}

(function main(){
  const input = process.argv.slice(2).join(" ");
  if(input.length > 0) {
    console.log(brailleTranslator(input))
  } else {
    console.log('No input provided. Usage: node translator.js <input>');
  }
})()
