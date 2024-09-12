const allowedEnglishChars = /[A-NP-Za-z0-9]/;

const isEnglish = (input) => {
    for (let i = 0; i < input.length; i++) {
        const char = input[i];

        // If string has '.', it is a Braille string.
        if (char === '.') { return false; }

        // If string has 'A-NP-Za-z0-9', it is an English string.
        else if (allowedEnglishChars.test(char)) { return true; }
    }

    // A string of length 6 with all O's 'OOOOOO' may be ambiguous; however, no such Braille character is equivalent to 'OOOOOO'.
    // Therefore, a string consisting of only O's at any length may be inferred as an English string.
    return true;
}

module.exports = isEnglish;