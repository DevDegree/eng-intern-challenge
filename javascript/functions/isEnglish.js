const allowedEnglishChars = /[A-NP-Za-z0-9]/;

const isEnglish = (input) => {
    for (let i = 0; i < input.length; i++) {
        const char = input[i];

        if (char === '.') { return false; }
        else if (allowedEnglishChars.test(char)) { return true; }
    }

    return true;
}

module.exports = isEnglish;