const brailleMap = {
    a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..", e: "O..O..", f: "OOO...", g: "OOOO..", h: "O.OO..", i: ".OO...", j: ".OOO..",
    k: "O...O.", l: "O.O.O.", m: "OO..O.", n: "OO.OO.", o: "O..OO.", p: "OOO.O.", q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.",
    u: "O...OO", v: "O.O.OO", w: ".OOO.O", x: "OO..OO", y: "OO.OOO", z: "O..OOO", " ": "......",
    cap: ".....O", num: ".O.OOO",
    0: ".OOO..", 1: "O.....", 2: "O.O...", 3: "OO....", 4: "OO.O..", 5: "O..O..", 6: "OOO...", 7: "OOOO..", 8: "O.OO..", 9: ".OO..."
  };
  
  const englishMap = Object.fromEntries(Object.entries(brailleMap).map(([key, value]) => [value, key]));
  

function translate(input) {
    let result = '', capMode = false, numMode = false, isBraille = /^[O.\s]+$/.test(input);
  
    if (isBraille) {
      for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i + 6);
        if (brailleChar === brailleMap['cap']) capMode = true;
        else if (brailleChar === brailleMap['num']) numMode = true;
        else {
          let char = englishMap[brailleChar];
          if (capMode) char = char.toUpperCase(), capMode = false;
          if (numMode && /[a-j]/.test(char)) char = (char.charCodeAt(0) - 'a'.charCodeAt(0) + 1) % 10, numMode = false;
          result += char;
        }
      }
    } else {
      for (const char of input) {
        if (/[0-9]/.test(char)) {
          if (!numMode) result += brailleMap['num'], numMode = true;
          result += brailleMap[char];
        } else if (/[A-Z]/.test(char)) result += brailleMap['cap'] + brailleMap[char.toLowerCase()], numMode = false;
        else result += brailleMap[char], numMode = false;
      }
    }
  
    return result;
  }
