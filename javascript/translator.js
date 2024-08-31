
const braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO.....', 'd': 'OOO....',
    'e': 'OO.O...', 'f': 'OOO....', 'g': 'OOOO....', 'h': 'O.OO...',
    'i': '.O.O...', 'j': '.O.OO..', 'k': 'O..O...', 'l': 'O.O.O..',
    'm': 'OO..O..', 'n': 'OOO..O.', 'o': 'OOO.O..', 'p': 'OOOOO..',
    'q': 'OOOOOO.', 'r': 'OOOOO.O', 's': 'OOOO.O.', 't': 'OOOOO.O',
    'u': 'O..O..', 'v': 'O.O.O.', 'w': '.O.OOO.', 'x': 'OO..OO.',
    'y': 'OOO..OO', 'z': 'OO..O.', ' ': '......',
}

const convertToBraille = (str) => {
    let result = '';
    for(let s of str){
        if(braille_dict[s])
        result = result + braille_dict[s];
     }
     return result;
}


const convertToEnglish = (str) => {
    let result = '';
    let j = []
      for(i = 0; i < str.length; i++){
       result = str.substring(i, i + 7);
       const entry = Object.entries(braille_dict).find(([key, val]) => val === result);
       if(entry){
        j.push(entry[0]);
       }
    }
    return j.join('');
}

if (require.main === module) {
    const input = process.argv.slice(2).join(" ");
    const isBraille = input.includes('O') || input.includes('.');
    const output = isBraille ? translateToEnglish(input) : translateToBraille(input);
    console.log(output);
}
