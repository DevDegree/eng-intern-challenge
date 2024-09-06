
const alpha = {
 a:'O.....',
 b:'O.O...', 
 c:'OO....',
 d:'OO.O..', 
 f:'OOO...',
 g:'OOOO..', 
 h:'O.OO..',
 i:'.OO...', 
 j:'.OOO..',
 l:'O.O.O.', 
 m:'OO..O.',
 n:'OO.OO.', 
 o:'O..OO.',
 p:'OOO.O.', 
 q:'OOOOO.',
 r:'O.OOO.', 
 s:'.OO.O.',
 t:'.OOOO.', 
 u:'O...OO',
 v:'O.O.OO', 
 w:'.OOO.O',
 x:'OO..OO', 
 y:'OO.OOO',
 z:'O..OOO', 
}

const num = {
  1:'O.....',
  2:'O.O...',
  3:'OO....',
  4:'OO.O..',
  5:'O..O..',
  6:'OOO...',
  7:'OOOO..',
  8:'O.OO..',
  9:'.OO...',
  0:'.OOO..'
}

const modi = {
  capitals:'.....O',
  decimal:'.O...O',
  numbers:'.O.OOO'
}

const sym = {
  '.':'..OO.O',
  ',':'..O...',
  '?':'..O.OO',
  '!':'..OOO.',
  ':':'..OO..',
  ';':'..O.O.',
  '-':'....OO',
  '/':'.O..O.',
  '<':'.OO..O',
  '>':'O..OO.',
  '(':'O.O..O',
  ')':'.O.OO.',
}

const spa = {
  ' ':'......'
}


// one function isn't enough, so multiple will be used. one funtion to sorta between english and braille, one function to split in coming strings or inputs into 6-characters groups, one function to translate each 6-character group into the correct word or number of the opposite languge, and lastly one to concatinate all the seperated letter or numbers into one text. 

let translator = function(input) {
  
  const x = `${input}`

  const sorter = () => {
    
    let lang = '';

    const y = x.toLowerCase()

    let i = 0; 
    
    while (i < y.length) {

      console.log(y[i])

      if (y[i] === 'a' || y[i] === 'e' || y[i] === 'i' || y[i] === 'u' || y[i] === 'y' || y[i] === 'k' || y[i] === 'l' || y[i] === 'm' || y[i] === 'n' || y[i] === 'g' || y[i] === 'p' || y[i] === 't' || y[i] === 'b' || y[i] === '1' || y[i] === '2' || y[i] === '3' || y[i] === '4' || y[i] === '5' || y[i] === '6' || y[i] === '7' || y[i] === '8' || y[i] === '9' || y[i] === 'h' || y[i] === 'z') {
        lang = 'english'; 
        console.log(lang);
        break;
      } 
      if (i === y.length) {
        lang = 'braille';
        console.log(lang);
        
      }
      
      i++
    }
    
  }

  sorter(x);
  console.log(x);
}





// test cases 

// translator('army')
// translator('O.....OO....')
// translator('u')
// translator('cookie')
// translator('425')
