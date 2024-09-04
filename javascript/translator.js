// mvp
// import maps
import { englishToBrailleMap, brailleToEnglishMap } from './maps';
import englishToBraille from './englishToBraille';
import brailleToEnglish from './brailleToEnglish';

// create conversion function
function translator() {
  // store user arguments
  const args = process.argv.slice(2).join(' ');

  // determine whether to translate into braille or english
  // if args is divisible by 6 and contains only "O" or ".", it's braille
  // otherwise, it's an alphanumeric string

  // translate from english to braille
  // translate from braille to english
  // account for numbers, capital letters, and spaces

  // stretch
  // return an error message if arguments contain invalid characters
  // if argument is braille and contains characters other than "O" or ".", and if argument is not divisible by 6, return an error message
  // if argument is english and contains characters other than letters, numbers, or space, return an error message
}
