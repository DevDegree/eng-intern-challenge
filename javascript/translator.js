const brailleMap = {
  // Lowercase letters
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
  'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
  'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
  'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
  'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',

  // Capital indicator
  'CAP': '.....O',

  // Numbers (requires number sign first)
  'NUM': '.O.OOO', // Number follows
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
  '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

  // Space
  ' ': '......',
};

const englishMap = Object.fromEntries(Object.entries(brailleMap).map(([k,v]) => [v,k]));

function isBraille(str){
    return /^[O.]+$/.test(str);
}

function englishToBraille(eng){
    let braille = '';
    let inNumberMode = false;

    for (const char of eng){
        if (char >= 'A' && char <= 'Z'){
            braille += brailleMap['CAP'];
            braille += brailleMap[char.toLowerCase()];
            inNumberMode = false;
        } else if(char >= 'a' && char <= 'z'){
            braille += brailleMap[char];
            inNumberMode = false;
        } else if (char >= '0' && char <= '9'){
            if (!inNumberMode){
                braille += brailleMap['NUM'];
                inNumberMode = true;
            }
            braille += brailleMap[char];
        } else if (char === ' '){
            braille += brailleMap[' '];
            inNumberMode = false;
        }
    }
    return braille;
}

function brailleToEnglish(braille){
    const cells = braille.match(/.{1,6}/g) || [];
    let english = '';
    let capitalizeNext = false;
    let inNumberMode = false;

    for (const cell of cells){
        if (cell === brailleMap['CAP']){
            capitalizeNext = true;
        } else if (cell === brailleMap['NUM']){
            inNumberMode = true;
        } else if (cell === brailleMap[' ']){
            english += ' ';
            inNumberMode = false;
        } else {
            const char = englishMap[cell];
            if (capitalizeNext && char){
                english += char.toUpperCase();
                capitalizeNext = false;
            } else if (inNumberMode && char >= 'a' && char <= 'j'){
                english += '1234567890'['abcdefghij'.indexOf(char)];
                inNumberMode = false;
            } else {
                english += char;
            }
        }
    }
    return english;
}

const main = () => {
    const str = process.argv.splice(2).join(" ").trim();
    if(str.length < 1) return process.exit(1);

    if(isBraille(str)){
        console.log(brailleToEnglish(str));
    } else {
        console.log(englishToBraille(str));
    }
}

main();
