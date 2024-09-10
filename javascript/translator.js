let BRAILLE_STATE = {
    CAPITAL_FOLLOWS: ".....O",
    DECIMAL_FOLLOWS: ".O...O",
    NUMBER_FOLLOWS: ".O.OOO",
  };
  let BRAILLE_SPACE = "......";
  let CAPITAL_ENGLISH_TO_BRAILLE = {
    a: "O.....",b: "O.O...",c: "OO....",d: "OO.O..",e: "O..O..",
    f: "OOO...",g: "OOOO..",h: "O.OO..",i: ".OO...",j: ".OOO..",
    k: "O...O.",l: "O.O.O.",m: "OO..O.",n: "OO.OO.",o: "O..OO.",
    p: "OOO.O.",q: "OOOOO.",r: "O.OOO.",s: ".OO.O.",t: ".OOOO.",
    u: "O...OO",v: "O.O.OO",w: ".OOO.O",x: "OO..OO",y: "OO.OOO",
    z: "O..OOO",
  };
  let NUMERIC_ENGLISH_TO_BRAILLE = {
    1: "O.....",2: "O.O...",3: "OO....",4: "OO.O..",5: "O..O..",
    6: "OOO...",7: "OOOO..",8: "O.OO..",9: ".OO...",0: ".OOO..",
  };
  function isNumeric(ch) {
    return /^[0-9]$/.test(ch);
  }
  function isLowerCaseAlphabetic(ch) {
    return /^[a-z]$/.test(ch);
  }
  function isUpperCaseAlphabetic(ch) {
    return /^[A-Z]$/.test(ch);
  }
  function isAlphabetic(ch) {
    return /^[a-zA-Z]$/.test(ch);
  }
  function keyValueSwapper(record) {
    let swapped = {};
    Object.entries(record).forEach(function (_a) {
      let k = _a[0],
        v = _a[1];
      swapped[v] = k;
    });
    return swapped;
  }
  function getCapitalBrailleToEnglish() {
    return keyValueSwapper(CAPITAL_ENGLISH_TO_BRAILLE);
  }
  function getNumericBrailleToEnglish() {
    return keyValueSwapper(NUMERIC_ENGLISH_TO_BRAILLE);
  }
  function isState(str) {
    return Object.values(BRAILLE_STATE).find(function (v) {
      return v === str;
    });
  }
  function getState(state) {
    if (!isState) {
      throw new Error("Invalid braille state");
    }
    return {
      isAlphabetic: state === BRAILLE_STATE.CAPITAL_FOLLOWS,
      isNumeric: state === BRAILLE_STATE.NUMBER_FOLLOWS,
      isDecimal: state === BRAILLE_STATE.DECIMAL_FOLLOWS,
    };
  }
  function isBraille(input) {
    return /^[O.]+$/.test(input);
  }
  function isEnglish(input) {
    return /^[a-zA-Z0-9]+$/.test(input);
  }


  function brailleToEnglish(text) {
    let BRAILLE_LEN = 6;
    if (text.length === 0 || text.length % BRAILLE_LEN !== 0 || !isBraille(text))
      throw new Error("Invalid braille");
    let translate = "";
    let state = {
      isAlphabetic: false,
      isNumeric: false,
      isDecimal: false,
    };
    let CAPITAL_BRAILLE_TO_ENGLISH = getCapitalBrailleToEnglish();
    let NUMERIC_BRAILLE_TO_ENGLISH = getNumericBrailleToEnglish();
    let prevBraille = "";
    for (let i = 0; i < text.length; i += BRAILLE_LEN) {
      let braille = text.substring(i, i + BRAILLE_LEN);
      if (braille === BRAILLE_SPACE) {
        translate += " ";
        state.isAlphabetic = true;
      } else if (isState(braille)) {
        state = getState(braille);
      } else if (state.isAlphabetic) {
        let ch = CAPITAL_BRAILLE_TO_ENGLISH["".concat(braille)];
        translate += isState(prevBraille) ? ch.toUpperCase() : ch;
      } else if (state.isNumeric) {
        translate += NUMERIC_BRAILLE_TO_ENGLISH["".concat(braille)];
        state.isAlphabetic = false;
      }
      prevBraille = braille;
    }
    return translate;
  }
  
  function englishToBraille(text) {
    let translate = "";
    // if (!text) return translate;
    text = String(text);
    let prevCh = "";
    for (let i = 0; i < text.length; i++) {
      let ch = text[i];
      if (ch === " ") {
        translate += BRAILLE_SPACE;
      } else if (isNumeric(ch)) {
        if (isAlphabetic(prevCh) || prevCh === " " || prevCh === "") {
          translate += BRAILLE_STATE.NUMBER_FOLLOWS;
        }
        translate += NUMERIC_ENGLISH_TO_BRAILLE["".concat(ch)];
      } else if (isAlphabetic(ch)) {
        if (isUpperCaseAlphabetic(ch)) {
          translate += BRAILLE_STATE.CAPITAL_FOLLOWS;
        }
        translate += CAPITAL_ENGLISH_TO_BRAILLE["".concat(ch.toLowerCase())];
      }
      prevCh = ch;
    }
    return translate;
  }
  function translate(text) {
    if (isBraille(text)) {
      return brailleToEnglish(text);
    } else {
      return englishToBraille(text);
    }
  }
  let args = process.argv.slice(2).join(" ");
  console.log(translate(args));
  