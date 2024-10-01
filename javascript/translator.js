function isBraille(input) {
    if (input.includes("O") ||input.includes(".") ) {
        return true;
    }
    return false;
}

const braille = new Map([['a','O.....'],['b','O.O...'],['c','OO....'],['d','OO.O..'],
['e','O..O..'],['f','OOO...'],['g','OOOO..'],['h','O.OO..'],['i','.OO...'],['j','.OOO..'],
['k','O...O.'],['l','O.O.O.'],['m','OO..O.'],['n','OO.OO.'],['o','O..OO.'],['p','OOO.O.'],
['q','OOOOO.'],['r','O.OOO.'],['s','.OO.O.'],['t','.OOOO.'],['u','O...OO'],['v','O.O.OO'],
['w','.OOO.O'],['x','OO..OO'],['y','OO.OOO'],['z','O..OOO'],['1','O.....'],['2','O.O...'],
['3','OO....'],['4','OO.O..'],['5','O..O..'],['6','OOO...'],['7','OOOO..'],['8','O.OO..'],
['9','.OO...'],['0','.OOO..'],['.','..OO.O'],[',','..O...'],['?','..O.OO'],['!','..OOO.'],
[':','..OO..'],[';','..O.O.'],['-','....OO'],['/','.O..O.'],['<','.OO..O'],['>','O..OO.'],
['(','O.O..O'],[')','.O.OO.'],[' ','......']
])

const reverseBraille = new Map();
braille.forEach((value, key) => {
    if (!reverseBraille.has(value)) {
        reverseBraille.set(value, []);
    }
    reverseBraille.get(value).push(key); 
});

function translateEnglish(string) {
    let translateE = '';
    let firstNumber = true;
    let numbers = false;
    for (let i = 0; i< string.length; i++) {
        let s = string[i];
        
        if ( s >= "A" && s<= "Z") {
            translateE += '.....O';
            translateE += braille.get(s.toLowerCase());
            firstNumber = true;
            numbers = false;
        }

        else if (s >= '0' && s<= "9") {
            if (firstNumber) {
                translateE += '.O.OOO';
                firstNumber = false;
                numbers = true;
            }
            translateE += braille.get(s);
        }

        else if (s === '.' && numbers) {
            translateE += '.O...O';
            translateE += braille.get(s);
        }

        else {
        numbers = false;
        translateE += braille.get(s);
        }
    }

    return translateE;

}

function translateBraille(string) {
    let translateB = '';
    let numbers = false;
    let capital = false;
    let i = 0
    
    while(i < string.length) {
        let b = string.substring(i,i+6)
        
        if (b === '.....O') {
            capital = true;
            
        } else if (b === '.O.OOO') {
            numbers = true;
           
        } else if (b === '.O...O' && numbers) {
            
        }

        let s = reverseBraille.get(b);

        if (s && s.length > 0) {
            if (capital ) {
                translateB += s[0].toUpperCase();
                capital = false;
            } else if (numbers) {
                
                translateB += s[1]|| s[0];
            } else {
                
                translateB += s[0];
            }
        }
        i += 6;
    }
    return translateB;
}

function main() {
    const args = process.argv.slice(2).join(' ');
    let translation;
    if (isBraille(args)) {
        translation = translateBraille(args);
    } else {
        translation = translateEnglish(args);
    }
    
    console.log(translation);
}

if (require.main === module) {
    main();
}


module.exports = { translateEnglish, translateBraille };

// console.log(translateEnglish("4.2. 4"));