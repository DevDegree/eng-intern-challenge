// okay lets see here: I need to make a cmd line app that:
//1 translates braille to english
//2 translates english back to braille.

// the app should determine if the argument passed at runtime is braille or english and convert appropriately.

// 0 = raised dot
// . = er, an unraised dot
//include english alphabet, capitalization, spaces, and 0-9

//then after converting, print to terminal the direct translation and nothing else


//initial thoughts
//braille is always six characters it seems. so probably just slice every 6 characters if its braille. 
//but what if its english? how can i determine its english? i suppose if theres a bunch of dots and Os. 
//what if it was blank? return nothing i suppose.

//might as well start with what i have though. 
// .....0 = capitalize. so is that read left to right on the lexicon? row by row i mean?
// well, 0.00.. translates to h, meaning yes, its read row by row.

//so i could start with just a big fat object for each character.
// const brailleLibrary = {
//   a: "0.....",
//   b: "0.0...",
//   c: "00....",
//   d: "00.0..",
//   e: "0..0..",
//   f: "000...",
//   g: "0000..",
//   h: "0.00..",
//   i: ".00...",
//   j: ".000..",
//   k: "0...0.",
//   l: "0.0.0.",
//   m: "00..0.",
//   n: "00.00.",
//   o: "0..00.",
//   p: "000.0.",
//   q: "00000.",
//   r: "0.000.",
//   s: ".00.0.",
//   t: ".0000.",
//   u: "0...00",
//   v: "0.0.00",
//   w: ".000.0",
//   x: "00..00",
//   y: "00.000",
//   z: "0..000",
//   1: "0.....",
//   2: "0.0...",
//   3: "00....",
//   4: "00.0..",
//   5: "0..0..",
//   6: "000...",
//   7: "0000..",
//   8: "0.00..",
//   9: ".00...",
//   0: ".000..",
//   caps: ".....0",
//   decimal: ".0...0",
//   numberFollows: ".0.000",
//   period: "..00.0",
//   comma: "..0...",
//   question: "..0.00",
//   exclamation: "..000.",
//   colon: "..00..",
//   semicolon: "..0.0.",
//   hyphen: "....00",
//   slash: ".0..0.",
//   left: ".00..0",
//   right: "0..00.",
//   openBracket: "0.0..0",
//   closeBracket: ".0.00.",
//   space: "......",
//   capitalize: (character) => {
//     character.toUppercase()
//   }
// }
//threw in a capitalize method for now.
//numberFollows is interesting. All following characters are numbers until space follows. whys that? 
//ah. cause its the exact same in braille. i could probably refactor the code here so i dont double repeat f and 6.

//Also, it would be easier if the keys were the actual characters themselves. lets try this again:

const engToBrailleLibrary = {
  "a": "O.....", 
  "b": "O.O...", 
  "c": "OO....", 
  "d": "OO.O..", 
  "e": "O..O..", 
  "f": "OOO...", 
  "g": "OOOO..", 
  "h": "O.OO..", 
  "i": ".OO...", 
  "j": ".OOO..", 
  "k": "O...O.", 
  "l": "O.O.O.", 
  "m": "OO..O.", 
  "n": "OO.OO.", 
  "o": "O..OO.", 
  "p": "OOO.O.", 
  "q": "OOOOO.", 
  "r": "O.OOO.", 
  "s": ".OO.O.", 
  "t": ".OOOO.", 
  "u": "O...OO", 
  "v": "O.O.OO", 
  "w": ".OOO.O", 
  "x": "OO..OO", 
  "y": "OO.OOO", 
  "z": "O..OOO", 
  ",": "..O...", 
  "?": "..O.OO", 
  "!": "..OOO.", 
  ":": "..OO..", 
  ";": "..O.O.", 
  "-": "....OO", 
  "/": ".O..O.", 
  "<": ".OO..O", 
  ">": "O..OO.", 
  "(": "O.O..O", 
  ")": ".O.OO.", 
  " ": "......", 
  "caps": ".....O",
  ".": ".O...O",
  "numberFollows": ".O.OOO",
  "period": "..OO.O",
}
const numberToBraille = {
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  "0": ".OOO..",
}


//reverse the library for braille to english
const brailleToEngLibrary = {
  "O.....": "a", 
  "O.O...": "b", 
  "OO....": "c", 
  "OO.O..": "d", 
  "O..O..": "e", 
  "OOO...": "f", 
  "OOOO..": "g", 
  "O.OO..": "h", 
  ".OO...": "i", 
  ".OOO..": "j", 
  "O...O.": "k", 
  "O.O.O.": "l", 
  "OO..O.": "m", 
  "OO.OO.": "n", 
  "O..OO.": "o", 
  "OOO.O.": "p", 
  "OOOOO.": "q", 
  "O.OOO.": "r", 
  ".OO.O.": "s", 
  ".OOOO.": "t", 
  "O...OO": "u", 
  "O.O.OO": "v", 
  ".OOO.O": "w", 
  "OO..OO": "x", 
  "OO.OOO": "y", 
  "O..OOO": "z", 
  "..O...": ",", 
  "..O.OO": "?", 
  "..OOO.": "!", 
  "..OO..": ":", 
  "..O.O.": ";", 
  "....OO": "-", 
  ".O..O.": "/", 
  ".OO..O": "<", 
  ".OO..O": ">", 
  "O.O..O": "(", 
  ".O.OO.": ")", 
  "......": " ",  
  "..OO.O": ".", //period
}

const brailleOperators = {
  ".....O": "capitalFollows",
  ".O.OOO": "numberFollows",
  ".O...O": "decimalFollows"
}

const brailleToNumber = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
}




// const brailleToEngLibrary = {
//   '.O..': 'j',
//   'O.....': 'a',
//   '0.O...': 'b',
//   '00....': 'c',
//   '00.0..': 'd',
//   '0..0..': 'e',
//   '000...': 'f',
//   '0000..': 'g',
//   '0.00..': 'h',
//   '.00...': 'i',
//   '0...0.': 'k',
//   '0.0.0.': 'l',
//   '00..0.': 'm',
//   '00.00.': 'n',
//   '0..00.': '>',
//   '000.0.': 'p',
//   '00000.': 'q',
//   '0.000.': 'r',
//   '.00.0.': 's',
//   '.0000.': 't',
//   '0...00': 'u',
//   '0.0.00': 'v',
//   '.000.0': 'w',
//   '00..00': 'x',
//   '00.000': 'y',
//   '0..000': 'z',
//   '.....0': 'caps',
//   '.0...0': '.',
//   '.0.000': 'numberFollows',
//   '..00.0': 'period',
//   '..0...': ',',
//   '..0.00': '?',
//   '..000.': '!',
//   '..00..': ':',
//   '..0.0.': ';',
//   '....00': '-',
//   '.0..0.': '/',
//   '.00..0': '<',
//   '0.0..0': '(',
//   '.0.00.': ')',
//   '......': ' '
// } 


const brailleString = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO...OOO.......O.....O.O...OO...............O.OOOO.O.OO...OO....OO.O........OO....OO.O.......O............OOOO.O..O...OO.O..OOOO.......O.....O.O...OO...."
const englishString = "Hello, 123 World!"

const brailleToEnglishTranslator = (message) => {

  //prep variables
  let messageBox = [] //where strings are translated
  let capitalFollowsFlag = false //flag next braille chunk to be capitalized
  let numberFollowsFlag = false //flag for turning stuff into numbers

  //turn string message into an array so i can loop through it every 6 chars
  const messageArray = message.split("")
  for (let i = 0; i < messageArray.length; i += 6) {
    const chunk = messageArray.slice(i, i + 6).join("")
    messageBox.push(chunk)
  }


  //translate the message

  //for each chunk
  const translatedMessage = messageBox.map((chunk) => {
    console.log(chunk, 'chunk here')
    let translatedChar

    //check if its a capitalizer first. 
    if (brailleOperators[chunk] === "capitalFollows") {
      console.log('caps here')
      capitalFollowsFlag = true
      return ""
    } 
      //if its not a capitalizer check if its a numberFollows.
      else if (brailleOperators[chunk] === "numberFollows") {
        numberFollowsFlag = true
        return ""
    } 

    //check if the numberFollows flag is on. if it is, check if the chunk is a space. if it is, add it and unflag the numberFollows.
    if (numberFollowsFlag){
      
      if(brailleToEngLibrary[chunk] === " ") {
        console.log('space found', brailleToEngLibrary[chunk], chunk)
        translatedChar = brailleToEngLibrary[chunk]
        numberFollowsFlag = false
        return translatedChar
      }
      //if its not, then just use the number library 
      else {
        translatedChar = brailleToNumber[chunk]
        return translatedChar
      }
    }


    //get the translated character
    translatedChar = brailleToEngLibrary[chunk]

    //if capitalizer is flagged, uppercase the character and unflag.
    if(capitalFollowsFlag) {
      translatedChar = translatedChar.toUpperCase();
      capitalFollowsFlag = false
    }
    return translatedChar
  })
  
  console.log(translatedMessage.join(""), 'translated message')

}

const englishToBrailleTranslator = (message) => {

  let messageBox = []
  let numberize = false
  //break the message into single characters
  const chars = message.split("")

  //for each character, translate it to braille
  chars.forEach((char) => {
    console.log(char)
  
    //check if this character is uppercase. use regex to ensure its not flagged true for non alphabet stuff.
    if (char.match(/[a-zA-Z]/) && char === char.toUpperCase()){
      messageBox.push(engToBrailleLibrary['caps'])
      messageBox.push(engToBrailleLibrary[char.toLowerCase()])
      numberize = false

    } else if (char.match(/[0-9]/)) {
        if (!numberize) {
          messageBox.push(engToBrailleLibrary['numberFollows']);  // Add number marker if not already in number mode
          numberize = true;
        }
        messageBox.push(numberToBraille[char]);  // Add nraille for the number
    } else {
        const brailleChar = engToBrailleLibrary[char] || "?";  // Fallback for unrecognized characters
        messageBox.push(brailleChar);
        numberize = false;  // Exit number mode for non-number characters
    }
    
      

  })
  const finalMessage = messageBox.join("")

  console.log(finalMessage, 'message here')
  brailleToEnglishTranslator(finalMessage)
}

//? to do
//? get decimal follows working
//? then get engtoBraille() working and its operators (if any are needed)
//? return ? if its nonbraille

brailleToEnglishTranslator(brailleString)
// englishToBrailleTranslator(englishString)
