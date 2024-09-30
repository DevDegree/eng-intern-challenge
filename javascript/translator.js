function translate(msg) {
    let ans = "";
    // if (msg.search(/\./) > 0) {
        
    //
    //alphabet case
    if (msg.search(/[^a-zA-Z ]+/) === -1) {
        for (i=0; i<= msg.length; i++) {
            let curAns = [];
            let curCode = "";
            let char = msg.slice(i, i+1)
            let pattern = /[A-Z]/
            let capitalMatch = pattern.test(char);
            if (capitalMatch) {
                ans = ans + ".....O";
            }
            let charNum = char.charCodeAt(0)-96;
            switch(charNum%10) {
                case 1: //a case
                curAns = [1];
                break;

                case 2: //b case
                curAns = [1, 2];
                break;

                case 3: //c case
                curAns = [1, 4];
                break;

                case 4: //d case
                curAns = [1, 4, 5];
                break;

                case 5: //e case
                curAns = [1, 5];
                break;

                case 6: //f case
                curAns = [1, 2, 4];
                break;

                case 7: //g case
                curAns = [1, 2, 4, 5];
                break;

                case 8: //h case
                curAns = [1, 2, 5];
                break;

                case 9: //i case
                curAns = [2, 4];
                break;

                case 0: //j case
                curAns = [2, 4, 5];
                break;
            }
           
            //next set of alphabets (k-t)
            if (Math.floor(charNum / 10) == 1) {
                curAns.push(3);
            } //next set (u-z)
            else if (Math.floor(charNum / 10) == 2) {
                curAns.push(6);
            }
            
            if(char == "w" || char == "W") {
                curAns = [2, 4, 5, 6]
            }
            
            // translate number codes
            for (a=1; a<=6; a++) {
                if(curAns.find((e) => e = a)) {
                    const check = (e) => e == a;
                    if(curAns.some(check)) {
                        curCode = curCode + "O";
                    } else {
                        curCode = curCode + ".";
                    }
                }
            }
            if (char == " ") {
                curCode="......";
            }
             ans = ans + curCode;
        }
    }
}
