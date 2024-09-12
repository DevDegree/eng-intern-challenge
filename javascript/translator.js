// Take CLI arguments
const userInput = process.argv.slice(2);

// determine if given arguments are English or Braille
const languageType = (language) => {
  // Braille will ALWAYS include a period .
  if (language[0].includes('.')) {
    let brailleArray = splitBrailleCharacters(language[0]);
    console.log(brailleArray);
    return;
  } else {
    console.log('English');
    return;
  }
};

const splitBrailleCharacters = (braille) => {
  return braille.match(/.{1,6}/g);
}

languageType(userInput);



