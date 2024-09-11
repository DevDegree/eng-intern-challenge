
const braille = {
    alphabet : {
        a: "O.....",
        b: "O.O...",
        c: "OO....",
        d: "OO.O..",
        e: "O..O..",
        f: "OOO...",
        g: "OOOO..",
        h: "O.OO..",
        i: ".OO...",
        j: ".OOO..",
        k: "O...O.",
        l: "O.O.O.",
        m: "OO..O.",
        n: "OO.OO.",
        o: "O..OO.",
        p: "OOO.O.",
        q: "OOOOO.",
        r: "O.OOO.",
        s: ".OO.O.",
        t: ".OOOO.",
        u: "O...OO",
        v: "O.O.OO",
        w: ".OOO.O",
        x: "OO..OO",
        y: "OO.OOO",
        z: "O..OOO",
    },
    numbers:{
        0: ".OOO..",
        1: "O.....",
        2: "O.O...",
        3: "OO....",
        4: "OO.O..",
        5: "O..O..",
        6: "OOO...",
        7: "OOOO..",
        8: "O.OO..",
        9: ".OO...",
    },
    punctuation:{
        " ": "......",
        ".":"..OO.O",
        ",":"..O...",
        "?":"..O.OO",
        "!":"..OOO.",
        ":":"..OO..",
        ";":"..O.O.",
        "_":"....OO",
        "/":".O..O.",
        "<": "O.O..O",
        ">": "O.O.O.",
        "(": ".O..OO",
        ")": "O..OO.",
    },
    follow:{
        numberFollow: ".O.OOO",
        decimalFollow:".O...O",
        capitalFollow:".....O"
    }
};

const translate = () => {
    const input = process.argv.slice(2).join(" ");
    if (!input) {
        console.log("no input");
        return;
    }

    const inputAr = [...input];  // break input down to a character an element

    const isBraille = inputAr.every(char => char === '.' || char === 'O');     // checking braille or english

    if (isBraille) {
        // Braille to English translation
        const groupsOfSixArray = []; // break the brailles into groups of 6 since each braille segment is 6 units
        for (let i = 0; i < input.length; i += 6) {
            groupsOfSixArray.push(input.slice(i, i + 6)); // 
        }

        let isNumber = false;
        let isUpperCase = false;
        let result = '';

        // section is the keys in the braille object
        const locateBraille = (section, value) => {
            return Object.keys(braille[section]).find(key => braille[section][key] === value) || '';
        };

        for (let i = 0; i < groupsOfSixArray.length; i++) {
            const item = groupsOfSixArray[i];
            if (item === braille.follow.capitalFollow) {
                isUpperCase = true;
         
            }
            if (item === braille.follow.numberFollow) {
                isNumber = true;
            
            }

            let character = '';
            if (isNumber) {
                character = locateBraille('numbers', item);
                if (!character) {
                    isNumber = false;
                    character = locateBraille('alphabet', item) || locateBraille('punctuation', item);
                }
            } else if (isUpperCase) {
                character = locateBraille('alphabet', item);
                if (character) {
                    character = character.toUpperCase();
                    isUpperCase = false;
                }
            } else {
                character = locateBraille('punctuation', item) || locateBraille('alphabet', item);
            }

            if (character) {
                result += character;
            }
        }

        console.log(result);
    } else {
        // English to Braille translation
        const brailleResult = inputAr.map((item, index) => {
            const code = item.charCodeAt(0);
            if (code >= 65 && code <= 90) { // uppercase
                return braille.follow.capitalFollow + braille.alphabet[item.toLowerCase()];
            } else if (code >= 97 && code <= 122) { // lowercase
                return braille.alphabet[item];
            } else if (code >= 48 && code <= 57) { // numbers
                const prevNumber = inputAr[index-1];
                if (index > 0 && prevNumber.charCodeAt(0) >= 48 && prevNumber.charCodeAt(0) <= 57) {
                    return braille.numbers[item];
                } else {
                    return braille.follow.numberFollow + braille.numbers[item];
                }
            } else if (item === " ") { // space
                return braille.punctuation[item];
            } else if (item === ".") { // decimal
                return braille.follow.decimalFollow + braille.punctuation[item];
            } else {
                return braille.punctuation[item] || '';
            }
        }).join('');

        console.log(brailleResult);
    }
};

translate();