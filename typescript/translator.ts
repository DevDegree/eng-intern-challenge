const { ENGLISH_TO_BRAILLE, BRAILLE_TO_ENGLISH, BRAILLE_TO_ENGLISH_NUMBERS } = require("./constants");

const chunkString = (str: string): string[] => {
    // The match function returns an array of chunks , each containing 6 symbols
    return str.match(/.{1,6}/g) as string[];
}

const translateBrlToEng = (braille: string) => {
    // Split the braille string into chunks
    const brailleChunks = chunkString(braille);

    let isNextNumber = false;
    let result = "";

    for (let i = 0; i < brailleChunks.length; i++) {
        // Get the English symbol
        const currentSymbol = BRAILLE_TO_ENGLISH[brailleChunks[i]];

        switch (currentSymbol) {
            case "capital":
                // If it's a capital indicator, capitalize the next symbol
                result += BRAILLE_TO_ENGLISH[brailleChunks[i + 1]].toUpperCase();
                // Skip the next chunk since it has been processed as capitalized
                i++;
                break;
            case "number":
                // If it's a number indicator, set the flag to interpret the next symbols as numbers
                isNextNumber = true;
                break;
            case " ":
                // If it's a space, reset the number flag and add the space to the result
                isNextNumber = false;
                result += currentSymbol;
                break;
            default:
                // For all other cases, add the current symbol to the result
                // If the flag is set, treat the current symbol as a number
                result += isNextNumber
                    ? BRAILLE_TO_ENGLISH_NUMBERS[brailleChunks[i]]
                    : currentSymbol;
        }
    }

    // Log the final translated result
    console.log(result);
}

const translateEngToBrl = (text: string) => {
    let isNextNumber = false;

    // Split the input text into individual characters 
    // and map each character to its Braille equivalent
    const result = text.split("").map((char) => {
        // Get the Braille representation for the current character
        const currentBrailleChunk = ENGLISH_TO_BRAILLE[char.toLowerCase()];

        // Check if the character is a number
        if (/[0-9]/.test(char)) {
            if (!isNextNumber) {
                // Prepend number indicator only for the first number in a sequence
                isNextNumber = true;
                return ENGLISH_TO_BRAILLE["number"] + currentBrailleChunk;
            }
            return currentBrailleChunk;
        }

        // If the character is a space, reset the number flag,
        // return the Braille representation for space
        if (char === " ") {
            isNextNumber = false;
            return currentBrailleChunk;
        }

        // If the character is uppercase, prepend the Braille capital indicator
        if (char === char.toUpperCase()) {
            return ENGLISH_TO_BRAILLE["capital"] + currentBrailleChunk;
        }

        return currentBrailleChunk;
    }).join("");

    // Log the final translated result
    console.log(result);
};


const translator = () => {
    // Combine all arguments passed after `npx ts-node translator.ts` into a single string
    const inputText = process.argv.slice(2).join(" ").trim();

    // Check if the input consists only of Braille symbols
    if (/^[O.]+$/.test(inputText)) {
        translateBrlToEng(inputText);
    } else {
        // Otherwise, translate from English to Braille
        translateEngToBrl(inputText);
    }
}

export default translator();