import engToBraille from "./engToBraille.json" assert { type: "json" };

function convertEnglishToBraille(input) {
  let brailleOutput = "";
  let numberMode = false;

  for (let i = 0; i < input.length; i++) {
    const character = input[i];

    // if character is capital, then add capital braille
    if (character === character.toUpperCase() && isNaN(character)) {
      brailleOutput += engToBraille["capital"];
    }

    // if character is number, then add number braille
    if (!isNaN(character) && character !== " ") {
      if (!numberMode) {
        brailleOutput += engToBraille["number"];
        numberMode = true;
      }
    } else {
      brailleOutput += engToBraille[" "];
      numberMode = false;
    }

    let braille = engToBraille[character.toLowerCase()];
    brailleOutput += braille;
  }

  return brailleOutput;
}

let result = convertEnglishToBraille("hello123");
console.log(result);
