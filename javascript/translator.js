class Braille{

    static eToB_Map =new Map([
        ['a','O.....'],
        ['b','O.O...'],
        ['c','OO....'],
        ['d','OO.O..'],
        ['e','O..O..'],
        ['f','OOO...'],
        ['g','OOOO..'],
        ['h','O.OO..'],
        ['i','.OO...'],
        ['j','.OOO..'],
        ['k','O...O.'],
        ['l','O.O.O.'],
        ['m','OO..O.'],
        ['n','OO.OO.'],
        ['o', 'O..OO.'],
        ['p', 'OOO.O.'], 
        ['q', 'OOOOO.'], 
        ['r', 'O.OOO.'], 
        ['s', '.OO.O.'], 
        ['t', '.OOOO.'],
        ['u', 'O...OO'], 
        ['v', 'O.O.OO'], 
        ['w', '.OOO.O'], 
        ['x', 'OO..OO'], 
        ['y', 'OO.OOO'],
        ['z', 'O..OOO'], 
        ['1', 'O.....'], 
        ['2', 'O.O...'], 
        ['3', 'OO....'], 
        ['4', 'OO.O..'], 
        ['5', 'O..O..'],
        ['6', 'OOO...'], 
        ['7', 'OOOO..'], 
        ['8', 'O.OO..'], 
        ['9', '.OO...'], 
        ['0', '.OOO..'],
        ['space', '......'],
        ['capital', '.....O'],
        ['number', '.O.OOO'],
    ]);

    static bToE_Map = new Map([
        ['O.....', 'a'], 
        ['O.O...', 'b'], 
        ['OO....', 'c'], 
        ['OO.O..', 'd'], 
        ['O..O..', 'e'],
        ['OOO...', 'f'], 
        ['OOOO..', 'g'], 
        ['O.OO..', 'h'], 
        ['.OO...', 'i'], 
        ['.OOO..', 'j'],
        ['O...O.', 'k'], 
        ['O.O.O.', 'l'], 
        ['OO..O.', 'm'], 
        ['OO.OO.', 'n'], 
        ['O..OO.', 'o'],
        ['OOO.O.', 'p'], 
        ['OOOOO.', 'q'], 
        ['O.OOO.', 'r'], 
        ['.OO.O.', 's'], 
        ['.OOOO.', 't'],
        ['O...OO', 'u'], 
        ['O.O.OO', 'v'], 
        ['.OOO.O', 'w'], 
        ['OO..OO', 'x'], 
        ['OO.OOO', 'y'],
        ['O..OOO', 'z'], 
        ['O.....', '1'], 
        ['O.O...', '2'], 
        ['OO....', '3'], 
        ['OO.O..', '4'], 
        ['O..O..', '5'],
        ['OOO...', '6'], 
        ['OOOO..', '7'], 
        ['O.OO..', '8'], 
        ['.OO...', '9'], 
        ['.OOO..', '0'],
        ['......', 'space'],
        ['.....O', 'capital'],
        ['.O.OOO', 'number'],
    ]);
    
    static isBraille(text){
        //check if text is braille, braille=>true, english=>false
        return (/^[O. ]+$/.test(text));
    }

    static toBraille(text){
        let brailleText='';
        let isNumber=false;

        for(let char of text){
            //check if char is alphabet letter
            if (char.toLowerCase != char.toUpperCase()){
                //check for uppercase letter
                if (char === char.toUpperCase()){
                    brailleText+=this.eToB_Map.get('capital');
                }
                brailleText+=this.eToB_Map.get(char.toLowerCase());
            }else if (!isNaN(char*1)){
                //check for number
                if (!isNumber){
                    //first number
                    brailleText+=this.eToB_Map.get('number');
                    isNumber=true;
                }
                brailleText+=this.eToB_Map.get(char);
            }else if (char===' '){
                //space
                isNumber=false;
                brailleText+=this.eToB_Map.get('space');
            }
        }
        return brailleText;
    }

    static toEnglish(brailleText){
        let englishText='';
        let brailleChar=[];
        let isCapital=false;
        let isNumber=false;

        for (let i=0;i<brailleText.length;i+=6){
            brailleChar.push(brailleText.substring(i, i + 6));
        }
        for (let char of brailleChar){
            if (char==this.bToE_Map.get('.O.OOO')){
                isNumber=true;
            }else if (char==this.eToB_Map.get('.....O')){
                isCapital=true;
            }else if (char==this.bToE_Map.get('......')){
                englishText+=' ';
            }
            if (isNumber){
                englishText+=this.eToB_Map.get(char);
            }
            if (isCapital){
                englishText+=this.eToB_Map.get(char).toUpperCase();
                isCapital=false;
            }else{
                englishText+=this.eToB_Map.get(char);
            }
            return englishText;
        }
    }

    static translate(text){
        if (this.isBraille(text)){
            return this.toEnglish(text);
        }else{
            return this.toBraille(text);
        }
    }

}

const args = process.argv.slice(2);
const input = args.join(' ');

console.log(translate(input));