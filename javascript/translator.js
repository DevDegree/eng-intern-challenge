    //basic function
    function translateToEnglish(inputText)
    {
        return "Inside translate to english";
    }
    
    //basic function
    function translateToBraille(inputText)
    {
        return "Inside translate to braille";
    }


    function main() {
    const inputArgs = process.argv.slice(2);
    
    //for user input
    if (inputArgs.length < 1) {
      return;
    }
  
    const inputText = inputArgs.join(" ");
  
    // regex to check if it is braille or not
    if (/^[O. ]+$/.test(inputText)) {
      const translatedText = translateToEnglish(inputText);
      console.log(translatedText);
    } else {
      const translatedText = translateToBraille(inputText);
      console.log(translatedText);
    }
  }
  
  main();