const brailMap = {
    "a":"o.....", "b":"o.o...", "c":"oo....", "d":"oo.o..", "e":"o..o..", "f":"ooo...", "g":"oooo..", "h":"o.oo..",
    "i":".oo...", "j":".ooo..", "k":"o...o.", "l":"o.o.o.", "m":"oo..o.", "n":"oo.oo.", "o":"o..oo.", "p":"ooo.o.", 
    "q":"ooooo.", "r":"o.ooo.", "s":".oo.o.", "t":".oooo.", "u":"o...oo", "v":"o.o.oo", "w":".ooo.o", "x":"oo..oo", 
    "y":"oo.ooo", "z":"o..ooo", "cap":".....o", "num":".o.ooo", "decimal":".o...o", "1":"o.....",
    "2":"o.o...", "3":"oo....", "4":"oo.o..", "5":"o..o..", "6":"ooo...", "7":"oooo..", "8":"o.oo..", "9":".oo...",
    "0":".ooo..", ".":"..oo.o", ",":"..o...", "?":"..o.oo", "!":"..ooo.", ":":"..oo..", ";":"..o.o.", "-":"....oo",
    "/":".o..o.", "<":".oo..o", ">":"o..oo.", "(":"o.o..o", ")":".o.oo.", " ":"......"
}
const reverseBrailleMap = {};
for (const [key, value] of Object.entries(brailleMap)) {
    reverseBrailleMap[value] = key;
}
function isBraille(input) {
    return /^[oO\.]+$/.test(input);
}
function translateToBraille(text) {
    let braille = "";
    let numberMode = false;

    for (let i = 0; i < text.length; i++) {
        let char = text[i].toLowerCase();

        if (char >= "0" && char <= "9") {
            if (!numberMode) {
                braille += brailleMap["num"];
                numberMode = true;
            }
            braille += brailleMap[char];
        } else if (char >= "a" && char <= "z") {
            if (numberMode) {
                braille += " ";
                numberMode = false;
            }
            if (text[i] !== char) {
                braille += brailleMap["cap"];
            }
            braille += brailleMap[char];
        } else {
            braille += brailleMap[char] || "";
        }
    }
    return braille;
}
function translateToEnglish(braille) {
    let english = "";
    let numberMode = false;
    let capMode = false;
    const brailleChars = braille.match(/.{1,6}/g) || [];

    for (let i = 0; i < brailleChars.length; i++) {
        const char = brailleChars[i].replace(/O/g, "o");
        if (char === brailleMap["cap"]) {
            capMode = true;
        } else if (char === brailleMap["num"]) {
            numberMode = true;
        } else if (char === brailleMap[" "]) {
            english += " ";
            numberMode = false;
        } else {
            let translatedChar = reverseBrailleMap[char] || "";
            if (numberMode && translatedChar.match(/[a-j]/)) {
                translatedChar = (Object.keys(brailleMap).find(key => brailleMap[key] === char)) || translatedChar;
                translatedChar = parseInt(translatedChar);
            }
            if (capMode) {
                english += translatedChar.toUpperCase();
                capMode = false;
            } else {
                english += translatedChar;
            }
            if (numberMode && !/[0-9]/.test(translatedChar)) {
                numberMode = false;
            }
        }
    }
    return english;
}
function main() {
    const input = process.argv.slice(2).join(" ");
    if (!input) {
        console.log("Please provide a string to translate.");
        return;
    }
    if (isBraille(input)) {
        const remainder = input.length % 6;
        if (remainder !== 0) {
            console.log("Error: Braille input length is not a multiple of 6. Please provide a valid Braille input.");
            return;
        }
        console.log(translateToEnglish(input));
    } else {
        console.log(translateToBraille(input));
    }
}
main();