const letterToBraille = {
    'a': "O.....", 'b': "O.O...",  
    'c': "OO....", 'd': "OO.O..", 
    'e': "O..O..", 'f': "OOO...", 
    'g': "OOOO..", 'h': "O.OO..", 
    'i': ".OO...", 'j': ".OOO..", 
    'k': "O...O.", 'l': "O.O.O.", 
    'm': "OO..O.", 'n': "OO.OO.", 
    'o': "O..OO.", 'p': "OOO.O.", 
    'q': "OOOOO.", 'r': "O.OOO.", 
    's': ".OO.O.", 't': ".OOOO.", 
    'u': "O...OO", 'v': "O.O.OO", 
    'w': ".OOO.O", 'x': "OO..OO", 
    'y': "OO.OOO", 'z': "O..OOO",
    ' ': "......"
};

const brailleToLetter = Object.fromEntries(
    Object.entries(letterToBraille).map(([key, value]) => [value, key])
);

function letterToNum(letter) {
    const firstTen = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'];
    const num = letter !== 'j' ? firstTen.indexOf(letter) + 1 : 0;
    return String(num);
}

function numToLetter(num) {
    const letterOrder = ['j', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'];
    return letterOrder[num];
}

function brailleToText(braille) {
    const SPACE = "......";
    const CAP_FOLLOW = ".....O";  
    const NUM_FOLLOW = ".O.OOO";

    const brailleChars = [...braille.match(/.{1,6}/g)];
    let result = [];
    let i = 0;

    while (i < brailleChars.length) {
        if (brailleChars[i] === CAP_FOLLOW) {
            i++;
            result.push(brailleToLetter[brailleChars[i]].toUpperCase());
        } else if (brailleChars[i] === NUM_FOLLOW) {
            i++;
            while (i < brailleChars.length && brailleChars[i] !== SPACE) {
                const char = brailleToLetter[brailleChars[i]];
                if (char && "abcdefghij".includes(char)) {
                    result.push(letterToNum(char));
                }
                i++;
            }
        } else {
            result.push(brailleToLetter[brailleChars[i]]);
        }
        i++;
    }

    return result.join('').trim();  // Ensure to trim any extra spaces
}

function textToBraille(text) {
    const CAP_FOLLOW = ".....O"; 
    const NUM_FOLLOW = ".O.OOO";

    const textChars = [...text];
    let result = [];

    textChars.forEach((char, index) => {
        if (/\d/.test(char)) {
            if (index === 0 || !/\d/.test(textChars[index - 1])) {
                result.push(NUM_FOLLOW);
            }
            result.push(letterToBraille[numToLetter(char)]);
        } else if (char === char.toUpperCase() && char.match(/[A-Za-z]/)) {
            result.push(CAP_FOLLOW);
            result.push(letterToBraille[char.toLowerCase()]);
        } else {
            result.push(letterToBraille[char]);
        }
    });

    return result.join('');
}

function translateInput(input) {
    const englishPattern = /^[A-Za-z0-9\s]+$/;
    const braillePattern = /^(?:[O.]{6})+$/;

    if (braillePattern.test(input)) {
        console.log(brailleToText(input));
    } else if (englishPattern.test(input)) {
        console.log(textToBraille(input));
    } else {
        console.log(`Error! => Input: ${input}`);
    }
}

function main() {
    const inputText = process.argv.slice(2).join(' ');
    if (inputText) {
        translateInput(inputText);
    }
}

// Execute main function
if (require.main === module) {
    main();
}
