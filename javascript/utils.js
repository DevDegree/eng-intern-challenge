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
        return false
    }

    const uniqueChatacters = [...new Set(inputArray[0].toLowerCase())];

    // It passes as Braille if there is . or o present
    if (uniqueChatacters.includes(".") || uniqueChatacters.includes("o")) {
        return true;
    }
    
    return false;
};

/**
 * This function checks if the input is Braille
 * 
 * @param {string} string - Braille string that will need to be translated
 * @returns {string[]} - Returns an array of Braille characters
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
function getKeyFromDict(key, dict) {
    let value;
    value = dict[key];

    if (value === undefined) {
        return false;
    }

    return value;
}


/**
 * This function returns the Braille translation of the English character
 * 
 * @param {string} value - character that will need to be translated to Braille
 * @param {object} dict - Translation dictionary defined in constants
 * @returns - Returns the key from the dictionary, otherwise `false`
 * 
 */
function getValueFromDict(value, dict) {
    const key = Object.keys(dict).find(key => dict[key] === value);


    if (key === undefined) {
        return false;
    }

    return key
}


module.exports = { isBrailleCheck, splitEverySixChars, getKeyFromDict, getValueFromDict };