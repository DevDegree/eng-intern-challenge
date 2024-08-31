const braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO.....', 'd': 'OOO....',
    'e': 'OO.O...', 'f': 'OOO....', 'g': 'OOOO....', 'h': 'O.OO...',
    'i': '.O.O...', 'j': '.O.OO..', 'k': 'O..O...', 'l': 'O.O.O..',
    'm': 'OO..O..', 'n': 'OOO..O.', 'o': 'OOO.O..', 'p': 'OOOOO..',
    'q': 'OOOOOO.', 'r': 'OOOOO.O', 's': 'OOOO.O.', 't': 'OOOOO.O',
    'u': 'O..O..', 'v': 'O.O.O.', 'w': '.O.OOO.', 'x': 'OO..OO.',
    'y': 'OOO..OO', 'z': 'OO..O.', ' ': '......',
    '0': '.O.OOO.', '1': '.O....', '2': '.O.O..', '3': '.OO...', 
    '4': '.OOO..', '5': '.O.O..', '6': '.OOOO.', '7': '.OOOOO',
    '8': '.OOOO.', '9': '.O.O..'
};

 const convertToBraille = (str) => {
    let result = '';
    let isNumber = false;

    for (let s of str) {
        if (s === ' ') {
            result += braille_dict[' '];
        } else if (s >= '0' && s <= '9') {
            if (!isNumber) {
                result += braille_dict['0']; 
                 isNumber = true;
            }
            result += braille_dict[s];
        } else if (s >= 'A' && s <= 'Z') {
            result += braille_dict[' ']; 
            result += braille_dict[s.toLowerCase()];
            isNumber = false;
        } else if (s >= 'a' && s <= 'z') {
            result += braille_dict[s];
            isNumber = false;
        } else {
            result += '?'; 
        }
    }

    return result;
}

 const convertToEnglish = (str) => {
    let result = '';
    const braille_length = 6;
    let i = 0;

    while (i < str.length) {
        let braille_char = str.substring(i, i + braille_length);
        i += braille_length;

        if (braille_char === braille_dict['0']) { 
            continue; 
        } else if (braille_char === braille_dict[' ']) { 
            
            continue; 
        } else {
            const entry = Object.entries(braille_dict).find(([key, val]) => val === braille_char);
            if (entry) {
                result += entry[0];
            } else {
                result += '?'; 
            }
        }
    }

    return result;
}

 const input = process.argv.slice(2).join(" ");
const isBraille = input.includes('O') || input.includes('.');
const output = isBraille ? convertToEnglish(input) : convertToBraille(input);
console.log(output);
