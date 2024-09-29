const sentence = process.argv.slice(2);
let translatedSentece = '';

const translationObj = {
    a: 'O.....',
    b: 'O.O...',
    c: 'OO....',
    d: 'OO.O..',
    e: 'O..O..',
    f: 'OOO...',
    g: 'OOOO..',
    h: 'O.OO..',
    i: '.OO...',
    j: '.OOO..',
    k: 'O...O.',
    l: 'O.O.O.',
    m: 'OO..O.',
    n: 'OO.OO.',
    o: 'O..OO.',
    p: 'OOO.O.',
    q: 'OOOOO.',
    r: 'O.OOO.',
    s: '.OO.O.',
    t: '.OOOO.',
    u: 'O...OO',
    v: 'O.O.OO',
    w: '.OOO.O',
    x: 'OO..OO',
    y: 'OO.OOO',
    z: 'O..OOO',
    capitalFollows: '.....O',
    numberFollows: '.O.OOO',
    space: '......',
    1: 'O.....',
    2: 'O.O...',
    3: 'OO....',
    4: 'OO.O..',
    5: 'O..O..',
    6: 'OOO...',
    7: 'OOOO..',
    8: 'O.OO..',
    9: '.OO...',
    0: '.OOO..',
};

// Loop all the sentence array
for (const word of sentence) {
    if (sentence.length === 1) {
        // Word is in Braille Alphabet
        let start = 0;
        let capitalFollows = false;
        let numberFollows = false;
        while (start <= word.length) {
            const brailleWord = word.substring(start, start + 6);
            start += 6;
            if (brailleWord === translationObj.capitalFollows) {
                capitalFollows = true;
                continue;
            }
            if (brailleWord === translationObj.numberFollows) {
                numberFollows = true;
                continue;
            }
            if (brailleWord === translationObj.space) {
                translatedSentece += ' ';
                numberFollows = false;
                continue;
            }
            for (const key in translationObj) {
                if (brailleWord === translationObj[key]) {
                    if (numberFollows && !isNaN(key)) {
                        translatedSentece += key;
                    }
                    if (!numberFollows && isNaN(key)) {
                        if (capitalFollows) {
                            translatedSentece += key.toUpperCase();
                        } else {
                            translatedSentece += key;
                        }
                    }
                }
            }
            capitalFollows = false;
        }
    } else {
        // Word is in English Alphabet
        const charArray = word.split('');
        //Verify if the word is not a number
        if (isNaN(word * 1)) {
            for (const char of charArray) {
                // Verify if capital follows
                if (char === char.toUpperCase()) {
                    translatedSentece += translationObj.capitalFollows;
                }
                translatedSentece += translationObj[char.toLowerCase()];
            }
        } else {
            translatedSentece += translationObj.numberFollows;
            for (const char of charArray) {
                translatedSentece += translationObj[char];
            }
        }
        if (word !== sentence[sentence.length - 1]) {
            translatedSentece += translationObj.space;
        }
    }
}

console.log(translatedSentece);
