/**
 * This function checks if the input is Braille
 *
 * @param {string[]} inputArray - An array of strings from the input
 * @returns {boolean} - Returns `true` if the input array contains a valid Braille character, otherwise `false`.
 *
 */
function isBrailleCheck(inputArray) {
  // Braille inputs are expected to be a continuous string
  if (inputArray.length !== 1) {
    return false;
  }
  
  const uniqueChatacters = [...new Set(inputArray[0].toLowerCase())];
  
  // It passes as Braille if the unique characters are either . or o
  if (uniqueChatacters.length === 1) {
    return uniqueChatacters[0] === '.' || uniqueChatacters[0] === 'o';
  } else if (uniqueChatacters.length === 2) {
    return uniqueChatacters.every(char => char === '.' || char === 'o');
  }

  return false;
}

/**
 * This function splits the Braille string into chunks of strings in an array
 *
 * @param {string} string - Braille string that will need to be translated
 * @returns chunks - Returns an array of Braille character chunks
 *
 */
function splitEverySixChars(string) {
  const chunks = [];
  for (let i = 0; i < string.length; i += 6) {
    chunks.push(string.slice(i, i + 6));
  }
  return chunks;
}

/**
 * This function returns the english translation of the Braille character
 *
 * @param {string} key - Braille string that will need to be translated
 * @param {object} dict - Translation dictionary defined in constants
 * @returns - Returns the key from the dictionary, otherwise `false`
 *
 */
function getValueFromDict(key, dict) {
  let value;
  value = dict[key];
  return value !== undefined ? value : false;
}

/**
 * This function returns the Braille translation of the English character
 *
 * @param {string} value - character that will need to be translated to Braille
 * @param {object} dict - Translation dictionary defined in constants
 * @returns - Returns the key from the dictionary, otherwise `false`
 *
 */
function getKeyFromDict(value, dict) {
  const key = Object.keys(dict).find((key) => dict[key] === value);
  return key !== undefined ? key : false;
}

const symbolSet = new Set('.,?|:;-/<>()')
/**
 * Checks if the character is a symbol in braille_symbols_dict that can be translated.
 * This is only for English to Braille translation.
 * 
 * @param {string} char - character to be checked
 * @returns {boolean}
 */
function isSymbolInDict(char) {
  return symbolSet.has(char)
}

module.exports = {
  isBrailleCheck,
  splitEverySixChars,
  getKeyFromDict,
  getValueFromDict,
  isSymbolInDict,
};
