
let capital_follows = ".....O"
let number_follows = ".O.OOO"
const {brailleToEngMap, brailleToNumMap, engToBrailleMap, numberToBrailleMap} = require("./maps")
let set = new Set()

function func() {
    let arg = process.argv.slice(2);
    for(let i = 0; i < arg[0].length; i++){
        set.add(arg[0][i]);
    }
    if(arg.length > 1){
        englishToBraille(arg)
    }
    else if(arg[0].length % 6 == 0 && set.size <= 2 && arg.length == 1){
        brailleToEnglish(arg)
    }
    else
        englishToBraille(arg)
    
}

function englishToBraille(arr){
    let ans = "";
    for(let l = 0; l < arr.length; l++){
        let str = arr[l]
        let number = false;
        for(let i = 0; i < str.length; i++){
            let curr = str[i]
            if(curr.charCodeAt(0) >= 65 && curr.charCodeAt(0) <= 90){
                number = false;
                ans += capital_follows
                ans += engToBrailleMap.get(curr.toString().toLowerCase())
            }
            else if(curr.charCodeAt(0) >= 48 && curr.charCodeAt(0) <= 57){
                if(number){
                    ans += numberToBrailleMap.get(curr.toString())
                }
                else{
                    ans += number_follows
                    number = true;
                    ans += numberToBrailleMap.get(curr.toString());
                }
            }
            else{
                number = false;
                ans += engToBrailleMap.get(curr.toString())
            }
        }
        if(l != arr.length - 1){
            ans += "......"
        }
    }
    console.log(ans);
}

function brailleToEnglish(arg){
    let str = arg[0]
    let ans = "";
    let capital = false;
    let number = false;
    for(let i = 0; i < str.length; i+= 6){
        let curr = str.substring(i, i + 6);
        if(curr == capital_follows){
            capital = true
        }
        else if(curr == number_follows){
            number = true;
        }
        else{
            if(number){
                if(brailleToEngMap.get(curr) == " "){
                    number = false;
                }
                else
                    ans += brailleToNumMap.get(curr);
            }
            else{
                if(capital){
                    ans += brailleToEngMap.get(curr).toUpperCase()
                    capital = false;
                }
                else{
                    ans += brailleToEngMap.get(curr)
                }
            }
            
        }
    }
    console.log(ans);
}


func()
