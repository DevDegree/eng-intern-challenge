const BrailleCapitalFollows = '.....O'
const BrailleNumberFollows = '.O.OOO'

const BrailleToEnglish: Record<string, string> = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' '
}

const BrailleNumberToEnglish: Record<string, string> = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
}

const EnglishToBraille: Record<string, string> = {}
for(const [key, value] of Object.entries(BrailleToEnglish)) {
    EnglishToBraille[value] = key
}
for(const [key, value] of Object.entries(BrailleNumberToEnglish)) {
    EnglishToBraille[value] = key
}

function isLowerAlpha(char: string): boolean {
    return /^[a-z]$/.test(char)
}

function isUpperAlpha(char: string): boolean {
    return /^[A-Z]$/.test(char)
}

function isNumeric(char: string): boolean {
    return /^[0-9]$/.test(char)
}

function convertToEnglish(str: string): string {
    if(str.length % 6 != 0) {
        throw new Error('Braille string must have length divisible by 6')
    }
    let isCapital = false
    let isNumber = false
    let result = ''
    for(let i = 0; i < str.length; i += 6) {
        const segment = str.slice(i, i + 6)
        if(segment == BrailleCapitalFollows) {
            isCapital = true
        } else if(segment == BrailleNumberFollows) {
            isNumber = true
        } else if(segment in BrailleToEnglish) {
            const char = BrailleToEnglish[segment]
            if(isCapital) {
                result += isLowerAlpha(char) ? char.toUpperCase() : char
                isCapital = false
            } else if(isNumber) {
                if(char == ' ') {
                    result += ' '
                    isNumber = false
                } else {
                    result += BrailleNumberToEnglish[segment]
                }
            } else {
                result += char
            }
        } else {
            throw new Error('Invalid Braille character')
        }
    }
    return result
}

function convertToBraille(str: string) {
    let isNumber = false
    let result = ''
    for(const char of str) {
        let braille = EnglishToBraille[char]
        if(isNumeric(char)) {
            if(!isNumber) {
                result += BrailleNumberFollows
                isNumber = true
            }
        } else if(isUpperAlpha(char)) {
            result += BrailleCapitalFollows
            braille = EnglishToBraille[char.toLowerCase()]
        } else {
            isNumber = false
        }
        result += braille
    }
    return result
}

function main() {
    const inputString = process.argv.slice(2).join(' ')
    try {
        console.log(convertToEnglish(inputString))
    } catch {
        console.log(convertToBraille(inputString))
    }
}

main()
