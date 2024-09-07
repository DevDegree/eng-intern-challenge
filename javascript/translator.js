
const alpha = {
 'a':'O.....',
 'b':'O.O...', 
 'c':'OO....',
 'd':'OO.O..', 
 'e':'O..O..',
 'f':'OOO...',
 'g':'OOOO..', 
 'h':'O.OO..',
 'i':'.OO...', 
 'j':'.OOO..',
 'k':'O...O.',
 'l':'O.O.O.', 
 'm':'OO..O.',
 'n':'OO.OO.', 
 'o':'O..OO.',
 'p':'OOO.O.', 
 'q':'OOOOO.',
 'r':'O.OOO.', 
 's':'.OO.O.',
 't':'.OOOO.', 
 'u':'O...OO',
 'v':'O.O.OO', 
 'w':'.OOO.O',
 'x':'OO..OO', 
 'y':'OO.OOO',
 'z':'O..OOO', 
 ' ':'......',
 'A':'......OO.....',
 'B':'......OO.O...', 
 'C':'......OOO....',
 'D':'......OOO.O..', 
 'E':'......OO..O..',
 'F':'......OOOO...',
 'G':'......OOOOO..', 
 'H':'......OO.OO..',
 'I':'......O.OO...', 
 'J':'......O.OOO..',
 'K':'......OO...O.',
 'L':'......OO.O.O.', 
 'M':'......OOO..O.',
 'N':'......OOO.OO.', 
 'O':'......OO..OO.',
 'P':'......OOOO.O.', 
 'Q':'......OOOOOO.',
 'R':'......OO.OOO.', 
 'S':'......O.OO.O.',
 'T':'......O.OOOO.', 
 'U':'......OO...OO',
 'V':'......OO.O.OO', 
 'W':'......O.OOO.O',
 'X':'......OOO..OO', 
 'Y':'......OOO.OOO',
 'Z':'......OO..OOO', 
}


const num = {
  '1':'O.....',
  '2':'O.O...',
  '3':'OO....',
  '4':'OO.O..',
  '5':'O..O..',
  '6':'OOO...',
  '7':'OOOO..',
  '8':'O.OO..',
  '9':'.OO...',
  '0':'.OOO..'
}

const modi = {
  capitals:'.....O',
  decimal:'.O...O',
  numbers:'.O.OOO'
}

// const sym = {
//   '.':'..OO.O',
//   ',':'..O...',
//   '?':'..O.OO',
//   '!':'..OOO.',
//   ':':'..OO..',
//   ';':'..O.O.',
//   '-':'....OO',
//   '/':'.O..O.',
//   '<':'.OO..O',
//   '>':'O..OO.',
//   '(':'O.O..O',
//   ')':'.O.OO.',
// }


// one function isn't enough, so multiple will be used.

// braille to english:
//  one funtion to sort between english and braille, one function to split in-coming strings or inputs into 6-characters groups, one function to translate each 6-character group into the correct word or number of the opposite languge, and lastly one to concatinate all the seperated letter or numbers into one text output. 

// englsih to braille:
// one function to iiterate over the string or input value, one function to itterate over the correct object as dictated by key:value pairs and the modi object keys, and lastly one function to combine all of it and output the correct braille. 


let translator = function(input) {
  
  const x = `${input}`
  
  let lang = '';

  const sorter = () => {
    

    const y = x.toLowerCase()

    for (let i = 0; i < y.length; i++) {
      

      if (y[i] === 'a' || y[i] === 'e' || y[i] === 'i' || y[i] === 'u' || y[i] === 'y' || y[i] === 'k' || y[i] === 'l' || y[i] === 'm' || y[i] === 'n' || y[i] === 'g' || y[i] === 'p' || y[i] === 't' || y[i] === 'b' || y[i] === '1' || y[i] === '2' || y[i] === '3' || y[i] === '4' || y[i] === '5' || y[i] === '6' || y[i] === '7' || y[i] === '8' || y[i] === '9' || y[i] === 'h' || y[i] === 'z' || y[i] === 'r') {
        lang = 'english'; 
        console.log(lang + ' sorted');
        englishToBraille(x)
        break;
      } 

    }

    if (lang === '') {
    lang = 'braille';
    console.log(lang + ' sorted');
    brailleSpliter()
    }
  }

  const brailleSpliter = () => {

    let result = x.match(/[\s\S]{1,6}/g) || [];
    console.log('after spliting:')
    console.log(result)
    brailleToEnglsih(result)

  }
  
  const brailleToEnglsih = (arr) => {

    console.log('Braille To English:')
    let arr2 = [];

    let object = '';
        object = alpha;


for (let i = 0; i < arr.length; i++) {  

    if (modi.numbers === arr[i]){
            object = num
          }

    if ('......' === arr[i]) {
      object = alpha
    }
  
function getKeyByValue(object, value) {
    for (let prop in object) {
        if (object.hasOwnProperty(prop)) {
          if ( modi.capitals === value) {
            return '*';
          } 

          if (modi.numbers === arr[i]){
             return '';
          }
        
            if (object[prop] === value)
                return prop;
        }
    }
}

ans = getKeyByValue(object, arr[i]);

 arr2 = arr2 + ans


    }
    
    let str2 = ''
    for (let i = 0; i < arr2.length; i++) {
    str2 = arr2.replace(/\*(\w)/g, (_, letter) => letter.toUpperCase())
  }
  
  console.log(str2);
  }
  
  const englishToBraille = () => {
    console.log('Englsih to Braille:')
    let input = x;
    let record = [];
    let ans = '';

    for (let i = 0; i < input.length; i++){
      
      key = `${input[i]}`
    
        if (num[key]) {
          ans = num[key]
          
          if(typeof input[i - 1] !== 'number'){
            ans = modi.numbers + num[key]
          }

          record = record + ans
        }

    else {ans = alpha[key]
  
      record = record + ans
    }
    
    }
    console.log(record)
  }

    

  sorter(x);
  console.log('end');
}





// test cases 

// translator('army')
// translator('u')
// translator('cookie')
// translator('425')
// translator('Hello world')
// translator('.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..') // output: Hello world
// translator('.....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O..') // output: Hello World
// translator('.....OO.....O.OOO.OO..O.OO.OOO') // output: Army
// translator('O.....O.OOO.OO..O.OO.OOO') // output: army
// translator('.O.OOOOO.O..O.O..............OO.....O.OOO.OO..O......OOO.OOO') // output: 42 ArmY 
// translator('42 ArmY 42') // output: '.O.OOOOO.O..O.O..............OO.....O.OOO.OO..O......OOO.OOO.O.OOOOO.O..O.O...'
// translator('.O.OOOOO.O..O.O...') // output: 42
// translator('42') // output: .O.OOOOO.O..O.O...

