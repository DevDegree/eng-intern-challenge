import { CAPITAL_FOLLOWS, NUMBER_FOLLOWS, rules, SPACE } from "./rules";
import { ASCII_0_CODE, ASCII_a_CODE, charIsUpperCase, isalpha, isnum, strHasNum } from "./util";
export class Translator {
    private englishToBraille: Map<string, string> = new Map();
    private brailleToEnglish: Map<string, string> = new Map();
    
    constructor() {
        // add rules
        for (const {english, braille} of rules) {
            if (!this.addRule(english, braille)) {
                console.error(`duplicate rule [${english}] to [${braille}]`);
            }
        }
    }
    // tries to translate the string from braille to english, if not possible, then we translate to braille instead
    public translate(words: string[]): string {
        console.log(words);
        if (words.length === 0) {
            return "";
        }
        if (words.length > 1) { // braille will only contain one argument
            return this.translateToBraille(words);
        }

        const str = words[0];
        let result: string = "";
        let capitalizeFlag = false;
        let numberFlag = false;

        if (str.length % 6 !== 0) { // all braille words should be multiples of 6
            return this.translateToBraille(words);
        }

        for (let i = 0; i < str.length; i += 6) {
            const chunk = str.substring(i, i+6);
            const rule = this.brailleToEnglish.get(chunk);

            if (!rule) {
                return this.translateToBraille(words);
            }
            
            if (rule === CAPITAL_FOLLOWS) {
                capitalizeFlag = true;
            } else if (rule === NUMBER_FOLLOWS) {
                numberFlag = true;
            } else {
                if (rule === SPACE) {
                    numberFlag = false;
                }
                if (numberFlag) {
                    let code = rule.charCodeAt(0) - ASCII_a_CODE + 1;
                    if (code === 10) {
                        code = 0;
                    }
                    code += ASCII_0_CODE;
                    result += String.fromCharCode(code);
                } else if (isalpha(rule) && capitalizeFlag) {
                    result += rule.toUpperCase();
                    capitalizeFlag = false;
                } else {
                    result += rule;
                }
            }
        }
        return result;
    }
    private translateToBraille(words: string[]): string {
        let result: string = "";
        for (let i = 0; i < words.length; i++) {
            const word = words[i];

            if (strHasNum(word)) {
                result += this.englishToBraille.get(NUMBER_FOLLOWS);
            }

            for (const char of word) {
                if (isnum(char)) {
                    let code = char.toLowerCase().charCodeAt(0) - ASCII_0_CODE;
                    if (code === 0) {
                        code = 10;
                    }
                    code += ASCII_a_CODE - 1;
                    result += this.englishToBraille.get(String.fromCharCode(code));
                } else if (charIsUpperCase(char) && isalpha(char)) {
                    result += this.englishToBraille.get(CAPITAL_FOLLOWS);
                    result += this.englishToBraille.get(char.toLowerCase());
                } else {
                    result += this.englishToBraille.get(char.toLowerCase());
                }
            }

            if (i !== words.length - 1) { // not the last word, should separate with space
                result += this.englishToBraille.get(SPACE);
            }
        }
        return result;
    }
    // adds a rule to our dictionaries
    // if rule exists, return false
    // otherwise, return true
    private addRule(english: string, braille: string): Boolean {
        if (this.englishToBraille.has(english) || this.brailleToEnglish.has(braille)) {
            return false;
        }
       
        this.englishToBraille.set(english, braille);
        this.brailleToEnglish.set(braille, english);
        return true;
    }
}