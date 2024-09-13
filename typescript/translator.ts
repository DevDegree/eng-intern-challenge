class Braille {
    private text: string;
    private brailleCharMap: { [key: string]: string } = {
        a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..", e: "O..O..", f: "OOO...", g: "OOOO..", h: "O.OO..",
        i: ".OO...", j: ".OOO..", k: "O...O.", l: "O.O.O.", m: "OO..O.", n: "OO.OO.", O: "O..OO.", p: "OOO.O.",
        q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.", u: "O...OO", v: "O.O.OO", w: ".OOO.O", x: "OO..OO",
        y: "OO.OOO", z: "O..OOO", 

        ".": "..OO.O", ",": ".O....", "?": ".O..OO", "!": ".O.OO.", ":": ".OO...", ";": ".O.O..", 
        "-": "..O.O.", "/": "..O..O", "<": "O..OO.", ">": "OO..OO", "(": ".O..O.", ")": ".O..O.",

    };
    private brailleNumMap: { [key: string]: string} = {
        0: ".OOO..", 1: "O.....", 2: "O.O...", 3: "OO....", 4: "OO.O..", 5: "O..O..", 
        6: "OOO...", 7: "OOOO..", 8: "O.OO..", 9: ".OO..."
    }
    private brailleSpecialMap: { [key: string]: string } = {
        "capital": '.....O', "decimal": '.O...O', "number": '.O.OOO', "space": "......" 
    }

    constructor(text: string) {
        this.text = text;
    }

    translate(): string {
        if (this.isBraille(this.text)) { 
            return this.toEnglish(); 
        }
        return this.toBraille();
    }

    isBraille(text: string): boolean {
        const brailleChars = ['O', '.'];

        if (text.length % 6 !== 0) {
            return false;
        }
        for (const char of text) {
            if (!brailleChars.includes(char)) {
                return false;
            }
        }
        return true;
    }
    
    findMapKey(value: string): string | undefined {
        for (const [key, val] of Object.entries(this.brailleCharMap)) {
            if (val === value) {
                return key; 
            }
        }
        for (const [key, val] of Object.entries(this.brailleNumMap)) {
            if (val === value) {
                return key; 
            }
        }
        for (const [key, val] of Object.entries(this.brailleSpecialMap)) {
            if (val === value) {
                return key; 
            }
        }
        return undefined; 
    }

    toBraille(): string {
        let output = '';
        let lastWasNumber = false;

        for (const char of this.text) {
            if (char === ' ') {
                output += this.brailleSpecialMap.space;
            } else if (char === '.') {
                if (lastWasNumber) { 
                    output += this.brailleSpecialMap.decimal;
                }
                output += this.brailleCharMap['.'];
   
            } else if (char >= '0' && char <= '9') {
                if (!lastWasNumber) {
                    output += this.brailleSpecialMap.number;
                }
                output += this.brailleNumMap[parseInt(char, 10)];
                lastWasNumber = true;

            } else if (char.toUpperCase() === char) {
                output += this.brailleSpecialMap.capital;
                output += this.brailleCharMap[char.toLowerCase()];
                lastWasNumber = false;
            } else if (char in this.brailleCharMap) {
                output += this.brailleCharMap[char.toLowerCase()];
                lastWasNumber = false;
            } else {
                output += '?';
            }
        }
        return output;
    }
    
    toEnglish(): string {
        let pos = 0;
        let output = '';
        let numFollows = false;
        let decFollows = false;
        let capFollows = false;
    
        while (pos + 6 <= this.text.length) {
            let brailleChar = this.text.slice(pos, pos + 6);

            if (brailleChar === this.brailleSpecialMap.capital) {
                capFollows = true;
                numFollows = false;
                decFollows = false;
                pos += 6;
                continue;
            } else if (brailleChar === this.brailleSpecialMap.number) {
                capFollows = false;
                numFollows = true;
                decFollows = false;
                pos += 6;
                continue;
            } else if (brailleChar === this.brailleSpecialMap.decimal) {
                capFollows = false;
                numFollows = false;
                decFollows = true;
                output += '.';
                pos += 6;
                continue;
            } else if (brailleChar === this.brailleSpecialMap.space) {
                capFollows = false;
                numFollows = false;
                decFollows = false;
                output += ' ';
                pos += 6;
                continue;
            }
    
            if (numFollows) {
                const num = Object.keys(this.brailleNumMap).find(key => this.brailleNumMap[Number(key)] === brailleChar);
                if (num !== undefined) {
                    output += num;
                    if (decFollows) {
                        decFollows = false;
                    }
                } else {
                    output += '?';
                }
            } else {
                let engChar = this.findMapKey(brailleChar);
                if (capFollows && engChar) {
                    engChar = engChar.toUpperCase();
                    capFollows = false;
                }
                output += engChar;
            }
            pos += 6;
        }
        return output;
    }
    
}

function main() {
    const input = process.argv.slice(2).join(' ');
    
    if (!input) {
        console.error("No input detected.");
        return;
    }

    const brailleConverter = new Braille(input);
    const output = brailleConverter.translate();
    console.log(output);
}

main();
