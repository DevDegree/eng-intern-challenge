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
        ['......', 'space'],
        ['.....O', 'capital'],
        ['.O.OOO', 'number'],
    ]);

    static number_map = new Map([
        ['O.....', '1'], 
        ['O.O...', '2'], 
        ['OO....', '3'], 
        ['OO.O..', '4'], 
        ['O..O..', '5'],
        ['OOO...', '6'], 
        ['OOOO..', '7'], 
        ['O.OO..', '8'], 
        ['.OO...', '9'], 
        ['.OOO..', '0']
    ]);
    
    static isBraille(text){
        return (/^[O. ]+$/.test(text));
    }

    static toBraille(text){
        let brailleText='';
        let isNumber=false;

        for(let char of text){
            //check if char is alphabet letter
            if (char===' '){
                //space
                isNumber=false;
                brailleText+=this.eToB_Map.get('space');
            }else if (char >= '0' && char <= '9'){
                //check for number
                if (!isNumber){
                    //first number
                    brailleText+=this.eToB_Map.get('number');
                    isNumber=true;
                }
                brailleText+=this.eToB_Map.get(char);
            }else{
                //check for uppercase letter
                if (char === char.toUpperCase() && char.toLowerCase() !== char.toUpperCase()){
                    brailleText+=this.eToB_Map.get('capital');
                }
                brailleText+=this.eToB_Map.get(char.toLowerCase());
            }
        }
        return brailleText;
    }

    static toEnglish(text){
        let englishText='';
        let brailleChar=[];
        let isCapital=false;
        let isNumber=false;

        for (let i=0;i<text.length;i+=6){
            brailleChar.push(text.substring(i, i + 6));
        }
        
        for (let char of brailleChar){
            let englishChar=this.bToE_Map.get(char);
            
            if (englishChar==='capital'){
                isCapital=true;
                continue; 
            }else if (englishChar==='number'){
                isNumber=true;
                continue;          
            }else if (englishChar==='space'){
                englishText+=' ';
                isNumber=false;
                continue;
            }
            
            if (isNumber){
                englishText+=this.number_map.get(char);
                continue;
            }
            
            if (isCapital){
                englishText+=englishChar.toUpperCase();
                isCapital=false;
            }else{
                englishText+=englishChar;
            }
            
            
                       
        }
        return englishText;

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

console.log(Braille.translate(input));