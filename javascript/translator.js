const brailleDict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", 
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", 
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", "cap": ".....O", "num": ".O.OOO", " ": "......", "1": "O.....", 
    "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", 
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};

const reverseBrailleDict = Object.fromEntries(Object.entries(brailleDict).map(([k, v]) => [v, k]));

function isBraille(input) 
{
    return input.split('').every(ch => ch === 'O' || ch === '.');
}

function englishToBraille(englishStr) 
{
    let brailleStr = '';
    let isNum = false;

    for(let i = 0; i < englishStr.length; i++) 
    {
        let char = englishStr[i];

        if (char === ' ') 
        {
            brailleStr += brailleDict[' '];
            isNum = false;
        } 
        else if (/[A-Z]/.test(char)) 
        { 
            brailleStr += brailleDict['cap'];
            brailleStr += brailleDict[char.toLowerCase()];
            isNum = false;
        } 
        else if (/[0-9]/.test(char)) 
        { 
            if (!isNum) {
                brailleStr += brailleDict['num'];
                isNum = true;
            }
            brailleStr += brailleDict[char];
        } 
        else 
        { 
            brailleStr += brailleDict[char];
            isNum = false;
        }
    }

    return brailleStr;
}

function brailleToEnglish(brailleStr) 
{
    let englishStr = '';
    let isCap = false;
    let isNum = false;

    for (let i = 0; i < brailleStr.length; i += 6) 
    {
        const symbol = brailleStr.slice(i, i + 6);

        if (symbol === brailleDict['cap']) 
        {
            isCap = true;
            continue;
        } 
        else if (symbol === brailleDict['num']) 
        {
            isNum = true;
            continue;
        } 
        else if (symbol === brailleDict[' ']) 
        {
            englishStr += ' ';
            isCap = false;
            isNum = false;
            continue;
        }

        const translatedChar = reverseBrailleDict[symbol];

        if (isNum) 
        {
            englishStr += translatedChar;
        } 
        else if (isCap) 
        {
            englishStr += translatedChar.toUpperCase();
            isCap = false;
        } 
        else 
        {
            englishStr += translatedChar;
        }
    }

    return englishStr;
}
function translate(input) 
{
    if (isBraille(input)) 
    {
        return brailleToEnglish(input);
    } 
    else 
    {
        return englishToBraille(input);
    }
}

const input = process.argv.slice(2).join(" ");
console.log(translate(input));
