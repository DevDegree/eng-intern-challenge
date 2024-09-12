// Take CLI arguments
const userInput = process.argv.slice(2);

// determine if given arguments are English or Braille
const languageType = (language) => {
  // Braille will ALWAYS include a period .
  if (language.includes('.')) {
    console.log("Braille");
  } else {
    console.log("English");
  }
  return;
};

languageType(userInput[0]);



