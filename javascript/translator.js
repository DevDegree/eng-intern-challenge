const BRAILLE_TO_ALPHANUMERIC = {
   'O.....': ['a', '1'],
   'O.O...': ['b', '2'],
   'OO....': ['c', '3'],
   'OO.O..': ['d', '4'],
   'O..O..': ['e', '5'],
   'OOO...': ['f', '6'],
   'OOOO..': ['g', '7'],
   'O.OO..': ['h', '8'],
   '.OO...': ['i', '9'],
   '.OOO..': ['j', '0'],
   'O...O.': ['k'],
   'O.O.O.': ['l'],
   'OO..O.': ['m'],
   'OO.OO.': ['n'],
   'O..OO.': ['o'],
   'OOO.O.': ['p'],
   'OOOOO.': ['q'],
   'O.OOO.': ['r'],
   '.OO.O.': ['s'],
   '.OOOO.': ['t'],
   'O...OO': ['u'],
   'O.O.OO': ['v'],
   '.OOO.O': ['w'],
   'OO..OO': ['x'],
   'OO.OOO': ['y'],
   'O..OOO': ['z']
}

const CAPTAL_FOLLOWS = '.....O';
const DECIMAL_FOLLOWS = '.O...O'; 
const NUMBER_FOLLOWS = '.O.OOO';
const SPACE = '......'

/*
Function to check if the string is English
str: a string to be checked
returns true or false
*/
const isEnglish = (str) =>{
   for (let i = 0; i < str.length; i++){
      if(str[i] != '.' && str[i] != 'O'){
         return true;
      }
   }
   return false;
}

/*
Function to convert all the characters of a string (English) to Braille symbol
str: a string to be converted
returns a string converted to Braille symbol
*/
const englishToBraille = (str) =>{
   let chars = [];
   let res = '';
   let isNum = false;
   for (let i = 0; i < str.length; i++){
      chars.push(str.substring(i,i+1));
   }
   for (let i = 0; i < str.length; i++){
      if(isAlpha(chars[i])){
         if(isCapital(chars[i])){
            res += CAPTAL_FOLLOWS;
            chars[i] = chars[i].toLowerCase()
         }
      } else if (isNumber(chars[i]) && !isNum){
         res += NUMBER_FOLLOWS;
         isNum = true;
      } else if (isNum){
         if(chars[i] == '.'){
            res += DECIMAL_FOLLOWS;
         }
         if(chars[i] == ' '){
            isNum = false;
         }
      }
      if (chars[i] == ' '){
         res += SPACE;
      } else if (chars[i] == '.'){
         // Do nothing as it is already dealt
      } else {
         res += getKeyByValue(BRAILLE_TO_ALPHANUMERIC, chars[i]);
      }
   }
   return res;
}

/*
Function to check if the character is an alphabet
ch: a character to be checked
returns true or false
*/
const isAlpha = (ch) =>{
   return typeof ch === "string" && ch.length === 1
          && (ch >= "a" && ch <= "z" || ch >= "A" && ch <= "Z");
}

/*
Function to check if the character is capitalized
ch: a character to be checked
returns true or false
*/
const isCapital = (ch) =>{
   return (ch >= "A" && ch <= "Z")
}

/*
Function to check if the character is a number
ch: a character to be checked
returns true or false
*/
const isNumber = (ch) =>{
   return (ch >= "0" && ch <= "9")
}

/*
Function to get the key by value
object: an object to be searched from
value: a value to search
returns the key
*/
const getKeyByValue = (object, value) =>{
   return Object.keys(object).find(key =>
      object[key][0] == value || BRAILLE_TO_ALPHANUMERIC[key][1] == value );
}

/*
Function to convert a string (Braille) to English
str: a string to be converted
returns a string converted to English
*/
const brailleToEnglish = (str) =>{
   let len = str.length;
   let numOfChars = len/6;
   let chars = [];
   for (let i = 0; i < len; i +=6){
      chars.push(str.substring(i,i+6));
   }
   let isCapital = false;
   let isNum = false;
   let res = '';
   for (let i = 0; i < numOfChars; i++){
      switch(chars[i]){
         case CAPTAL_FOLLOWS:
            isCapital = true;
            break;
         case NUMBER_FOLLOWS:
            isNum  = true;
            break;
         default:
            if(isNum){
               if(chars[i] == DECIMAL_FOLLOWS){
                  res += '.'
               } else if(chars[i] == SPACE) {
                  isNum = false;
                  res += ' ';
               } else {
                  temp = convertToEnglish(chars[i])
                  res += temp[1];
               }
            } else if(isCapital) {
               temp = convertToEnglish(chars[i])
               res += temp[0].toUpperCase();
               isCapital = false;
            } else if(chars[i] == SPACE){
               res += ' ';
            } else {
               temp = convertToEnglish(chars[i])
               res += temp[0];
            }
      }
   }
   return res;
}

/*
Function to convert a character (Braille string) to an English letter
ch: a string to be converted (represents a charactor)
returns a character converted to English letter
*/
const convertToEnglish = (ch) =>{
   return BRAILLE_TO_ALPHANUMERIC[ch];
}

/*
Function to determine English or Braille to convert
input: a string to be converted 
returns a string converted to either English or Braille
*/
const translate = (input) =>{
   if(isEnglish(input)){
      return englishToBraille(input)
   } else {
      return brailleToEnglish(input)
   }
}

// main
const INPUT = process.argv.slice(2).join(' ');
if (!INPUT) process.exit(1);

try{
   console.log(translate(INPUT));
} catch (error){
   console.log(error.message);
   process.exit(1);
}