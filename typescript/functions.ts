import { brailleNumToEnglish, brailleToEnglish, englishToBraille } from "./dictionary.js"

// Checking whether the input is Braille or English
export function isBraille(input: string): boolean {
    return /^[O.]+$/.test(input)
}

// Handles translation from Braille to English
export function brailleToEnglishConverter(braille: string): string {
    // State management declarations
    let english: string = ""
    let capital: boolean = false
    let int: boolean = false
    let decimal: boolean = false

    // Iterates over the argument
    for (let i = 0; i < braille.length; i += 6) {
        const brailleChar = braille.slice(i, i + 6)
        const translatedChar = brailleToEnglish[brailleChar]
        const translatedNum = brailleNumToEnglish[brailleChar]

        // Set var states based on type of char. If false, falls into else and runs a new conditioning.
        if (translatedChar === "capital") {
            capital = true
            int = false
        }
        else if (translatedChar === "number") {
            int = true
        }
        else if (translatedChar === "decimal") {
            decimal = true
        }
        else {
            if (capital) {
                english += translatedChar.toUpperCase()
                capital = false
            }
            else if (int && /[a-j]/.test(translatedChar)) {
                english += translatedNum
            }
            else if (decimal) {
                english += translatedChar
                decimal = false
            }
            else {
                english += translatedChar
            }
        }
    }

    return english
}

// Handles English translation to Braille
export function englishToBrailleConverter(text: string): string {
    // State management declarations
    let braille = ""
    let number = false

    // Iterates over the continuous string argument
    for (let char of text) {
        // Uppercase test
        if (/[A-Z]/.test(char)) {
            braille += englishToBraille["capital"] // capital follows
            braille += englishToBraille[char.toLowerCase()]
        }
        // Number test
        else if (/[0-9]/.test(char)) {
            if (!number) {
                number = true
                braille += englishToBraille["number"]
            }
            braille += englishToBraille[char]
        }
        else {
            braille += englishToBraille[char]
            number = false
        }
    }

    return braille
}