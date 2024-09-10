const letters = {
    "a":"O.....",
    "b":"O.O...",
    "c":"OO....",
    "d":"OO.O..",
    "e":"O..O..",
    "f":"OOO...",
    "g":"OOOO..",
    "h":"O.OO..",
    "i":".OO...",
    "j":".OOO..",
    "k":"O...O.",
    "l":"O.O.O.",
    "m":"OO..O.",
    "n":"OO.OO.",
    "o":"O..OO.",
    "p":"OOO.O.",
    "q":"OOOOO.",
    "r":"O.OOO.",
    "s":".OO.O.",
    "t":".OOOO.",
    "u":"O...OO",
    "v":"O.O.OO",
    "w":".OOO.O",
    "x":"OO..OO",
    "y":"OO.OOO",
    "z":"O..OOO",
    " ":"......",
    "cap":".....O",
    "num":".O.OOO", 
    "dec":".O...O"  
}
const specialChars = {
    ".":"..OO.O",
    ",":"..O...",
    "?":"..O.OO",
    "!":"..OOO.",
    ":":"..OO..",
    ";":"..O.O.",
    "-":"....OO",
    "/":".O..O.",
    "<":".OO..O",
    ">":"O..OO.",
    "(":"O.O..O",
    ")":".O.OO.",
}
const numbers = {
    "1": "O.....",
    "2": "O.O...",
    
}

function toBraille(text) {
    let result = "";
    let isCap = false;
    let isNum = false;
    for (let i = 0; i < text.length; i++) {
        if (text[i] === text[i].toUpperCase()) {
            isCap = true;
        }
        let char = text[i].toLowerCase();
        if (letters[char] && isCap) {
            result += letters["cap"];
            result += letters[char];
            isCap = false;
        }
        else {
            result += char;
        }
    }
    return result;
}

function toText(text){
    let result = "";
    for (let i = 0; i < text.length; i+=6) {
        let isCap = false;
        let char = text.slice(i, i+6);
        for (let key in letters) {
            if (letters[key] === char && key !== "cap" && !isCap) {
                result += key;
            }
            else if (key==="cap"){
                isCap = true;
            }
            else if(letters[key] === char && key !== "cap" && isCap){
                result += key.toUpperCase();
                isCap = false;
            }
        }
    }
    return result;
}
console.log(toText("O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O.OOOOO.O.OOO..OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO")); // hello world
console.log(toBraille("aBcdefghijklmnopqrstuvwxyz")); // O.....O.O...OO....OO.O..O..OOO...OOOO..O.OO...OO...O..O.OO..O...O.O.OO.O.OO.OO..OO.OOOO..OOO