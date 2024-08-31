import { brailleToEnglish } from "./utils/brailleToEnglish";
import { englishToBraille } from "./utils/englishToBraille";
import { isBraille } from "./utils/isBraille";

const translate = (input: string): string => {
    if (isBraille(input)) {
        return brailleToEnglish(input);
    } else {
        return englishToBraille(input);
    }
}

const input = process.argv.slice(2).join(' ');
console.log(translate(input));