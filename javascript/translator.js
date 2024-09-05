// Time complexity: O(N). Space complexity: O(N). 

// Initializing hash map with braille to english definitions
const ENGLISH_TO_BRAILLE_LETTER = new Map([
  ["a", "O....."], ["b", "O.O..."], ["c", "OO...."], ["d", "OO.O.."], ["e", "O..O.."], ["f", "OOO..."],
  ["g", "OOOO.."], ["h", "O.OO.."], ["i", ".OO..."], ["j", ".OOO.."], ["k", "O...O."], ["l", "O.O.O."],
  ["m", "OO..O."], ["n", "OO.OO."], ["o", "O..OO."], ["p", "OOO.O."], ["q", "OOOOO."], ["r", "O.OOO."],
  ["s", ".OO.O."], ["t", ".OOOO."], ["u", "O...OO"], ["v", "O.O.OO"], ["w", ".OOO.O"], ["x", "OO..OO"],
  ["y", "OO.OOO"], ["z", "O..OOO"], [".", "..OO.O"], [",", "..O..."], ["?", "..O.OO"], ["!", "..OOO."],
  [":", "..OO.."], [";", "..O.O."], ["-", "....OO"], ["/", ".O..O."], ["<", ".OO..O"], [">", "O..OO."],
  ["(", "O.O..O"], [")", ".O.OO."], [" ", "......"], ["CAPITAL_FOLLOWS", ".....O"], 
  ["DECIMAL_FOLLOWS", ".O...O"], ["NUMBER_FOLLOWS", ".O.OOO"]
])
const ENGLISH_TO_BRAILLE_NUMBER = new Map([
  ["1", "O....."], ["2", "O.O..."], ["3", "OO...."], ["4", "OO.O.."], ["5", "O..O.."], ["6", "OOO..."],
  ["7", "OOOO.."], ["8", "O.OO.."], ["9", ".OO..."], ["0", ".OOO.."],
])

// Initializing hash map with english to braille definitions
const BRAILLE_TO_ENGLISH_LETTER = new Map(
  [...ENGLISH_TO_BRAILLE_LETTER].map(([key, value]) => [value, key])
)
const BRAILLE_TO_ENGLISH_NUMBER = new Map(
  [...ENGLISH_TO_BRAILLE_NUMBER].map(([key, value]) => [value, key])
)

// Translate from English to Braille
const translate_english_to_braille = (english) => {
    let number_enabled = false, result = ""
    for (let i = 0; i < english.length; i++) {
        if (english.charAt(i) >= "0" && english.charAt(i) <= "9") {
            // Output the string of numbers, and prepend "number follows" code for the first number 
            if (!number_enabled) {
                result += ".O.OOO"
                number_enabled = true
            }
            result += ENGLISH_TO_BRAILLE_NUMBER.get(english.charAt(i))
        } else {
            number_enabled = false
            if (english.charAt(i) >= "A" && english.charAt(i) <= "Z") {
                result += ".....O"
            }
            result += ENGLISH_TO_BRAILLE_LETTER.get(english.charAt(i).toLowerCase())
        }
    }
    return result
}

const translate_braille_to_english = (braille) => {
    let i = 0, result = ""
    while(i < braille.length){
        let current_letter = BRAILLE_TO_ENGLISH_LETTER.get(braille.substring(i, i + 6))
        if(current_letter === "NUMBER_FOLLOWS"){
            i += 6

            // Repeatedly output the string of numbers until it reaches a space or the end. 
            while(i < braille.length){
                if(braille.substring(i, i + 6) === "......"){
                    result += " "
                    break
                }
                result += BRAILLE_TO_ENGLISH_NUMBER.get(braille.substring(i, i + 6))
                i += 6
            }
        } else if(current_letter === "CAPITAL_FOLLOWS"){
            i += 6
            result += BRAILLE_TO_ENGLISH_LETTER.get(braille.substring(i, i + 6)).toUpperCase()
        } else if(current_letter !== "DECIMAL_FOLLOWS") result += current_letter

        i += 6
    }
    return result
}

const input_string = process.argv.slice(2).join(' ')

// The condition for a braille string is the length must be a multiple of 6, and each letter is either '.' or 'O'
let is_braille = input_string.length % 6 === 0

for(let i = 0; i < input_string.length; i++)
    is_braille &= (input_string.charAt(i) === '.' || input_string.charAt(i) === 'O')

if(is_braille) console.log(translate_braille_to_english(input_string))
else console.log(translate_english_to_braille(input_string))