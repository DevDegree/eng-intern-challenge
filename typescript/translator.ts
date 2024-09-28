// This file contains the "dictionaries" for two-way translation between English and Braille

export const brailleToEnglish: Record<string, string> = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "capital",
    ".O...O": "decimal",
    ".O.OOO": "number",
    "......": " "
}

export const brailleNumToEnglish: Record<string, string> = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")"
}

export const englishToBraille: Record<string, string> = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": "......",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    "capital": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO."
}

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