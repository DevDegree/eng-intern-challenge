
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

module.exports = { isBrailleCheck, splitEverySixChars };