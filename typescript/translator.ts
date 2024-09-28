import { isBraille, englishToBrailleConverter, brailleToEnglishConverter } from "./functions.js"

function brailleTranslator(): void {

    const args = process.argv.slice(2)
    const input = args.join(" ")

    if (!isBraille(input)) {
        console.log(englishToBrailleConverter(input))
    }
    else {
        console.log(brailleToEnglishConverter(input))
    }
}

brailleTranslator()