let braille_obj = {
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
    1: "O.....",
    2: "O.O...",
    3: "OO....",
    4: "OO.O..",
    5: "O..O..",
    6: "OOO...",
    7: "OOOO..",
    8: "O.OO..",
    9: ".OO...",
    0: ".OOO..",
    " ": "......",
    ".": ".....O",
    ",": ".....O",
    "?": "OO..O.",
    "!": "O.OOO.",
    ":": ".OO...",
    ";": ".OO.O.",
    "-": "O...O.",
    "(": "O...O.",
    ")": "O...O.",
    '"': "O.O.O.",
    "'": "O.....",
    "@": "O.OO.O",
    "&": "O.OO..",
    capital: ".....O",
    number: ".O.OOO",
  };
  
  let english_obj = {};
  
  for (let key in braille_obj) {
    english_obj[braille_obj[key]] = key;
  }
  
  function brailleTranslator(inputText) {
    return /^[O.]+$/.test(inputText)
      ? translateToEnglish(inputText)
      : translateToBraille(inputText);
  }
  
  function translateToBraille(text) {
    let brailleOutput = "";
    for (let char of text) {
      if (char >= "A" && char <= "Z") {
        brailleOutput += braille_obj["capital"];
        char = char.toLowerCase();
      } else if (char >= "0" && char <= "9") {
        if (!brailleOutput.endsWith(braille_obj["number"])) {
          brailleOutput += braille_obj["number"];
        }
      }
      brailleOutput += braille_obj[char] || braille_obj[" "]; // Ensure that missing characters are handled
    }
    return brailleOutput;
  }
  
  function translateToEnglish(braille) {
    let englishOutput = "";
    let i = 0;
  
    while (i < braille.length) {
      let brailleChar = braille.slice(i, i + 6);
  
      // Check for capital indicator
      if (brailleChar === braille_obj["capital"]) {
        i += 6; // Move past the capital indicator
        brailleChar = braille.slice(i, i + 6);
        englishOutput += (english_obj[brailleChar] || "").toUpperCase();
        i += 6; // Move past the current character
      }
      // Check for number indicator
      else if (brailleChar === braille_obj["number"]) {
        i += 6; // Move past the number indicator
        brailleChar = braille.slice(i, i + 6);
        if (brailleChar in english_obj && !isNaN(english_obj[brailleChar])) {
          englishOutput += english_obj[brailleChar];
        }
        i += 6; // Move past the current character
      }
      // Handle regular Braille characters
      else {
        englishOutput += english_obj[brailleChar] || "";
        i += 6; // Move to the next Braille character
      }
    }
   
    return englishOutput;
  }
  
  const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  
  function main() {
    readline.question("Enter text to translate: ", (inputText) => {
      const result = brailleTranslator(inputText);
      console.log(result);
      readline.close();
    });
  }a
  
  main();
  