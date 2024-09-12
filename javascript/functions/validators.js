const validateInput = (input) => {
    // This program only supports alphanumeric, '.' (period), and ' ' (space) characters.
    if (/[^A-Za-z0-9 .]/.test(input)) { throw new Error('Invalid input.'); } 
}

const validateBrailleInputLength = (input) => {
    // A Braille input must be divisible by 6.
    if (input.length % 6 !== 0) { throw new Error('Invalid input.'); }
}

module.exports = {
    validateInput,
    validateBrailleInputLength
}