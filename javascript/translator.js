
const inputString = formatInput();
idLang();

function formatInput() {
  return process.argv.slice(2).join(' ');
}

function readBraille() {

}

function readEnglish() {

}

function idLang() {
  const nonBrailleChar = inputString.search(/[^O.]/);
  //search for a character that is not O or .
  if(nonBrailleChar === -1) {
    //If there are not non braille characters, the string can be interpreted as braille.
    console.log("String is Braille")
  } else {
    console.log("String is not Braille")
  }
}
