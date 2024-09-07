# TypeScript Instructions
General Approach

Use Map() objects to store mappings between English letters, numbers, special characters, and their corresponding Braille representations. These maps are created for:

English letters to Braille (letterToBraille) and vice versa (brailleToLetter).

Numbers to Braille (numberToBraille) and vice versa (brailleToNumber).

Special characters to Braille (specialCharToBraille) and vice versa (brailleToSpecialChar).

if a charater that doesn't exist on my map is inputted an error is thrown.

brailleToEnglishFunction(text: string): Converts a string of Braille dots into English characters. It uses the relevant map based on the Braille sequence and handles special cases for capital letters, numbers, and special characters.

englishToBrailleFunction(text: string): Converts a string of English text into Braille. It processes each character and uses maps to convert letters, numbers, and special characters. It handles uppercase characters and sequences of numbers with appropriate Braille prefixes.

getEnglishCapChar: Handles the conversion of a Braille capital letter sequence to an uppercase English character.

getBrailleFromCapChar: Converts an uppercase English character to its Braille equivalent, preceded by the Braille capital letter prefix.

getNumberSequenceFromBraille: Extracts a sequence of numbers from Braille, handling number delimiters and special characters like decimals.

getBrailleFromNumberSequence: Converts a sequence of numbers in English to Braille, adding the number prefix and ensuring correct conversion.

getSpecialCharFromBraille and getBrailleFromSpecialChar: Translate special characters between Braille and English.

isBraille(text: string): This function checks whether the input is Braille by ensuring it only contains O and . characters and has a valid Braille length (a multiple of 6). If true, the program proceeds with Braille to English conversion, otherwise with English to Braille.

translator(text: string): This function determines whether the input is Braille or English and directs the input to the appropriate translation function (brailleToEnglishFunction or englishToBrailleFunction).

There is an edge case where the Braille sequence 'O..OO.' maps to both the letter 'o' and the symbol '>'. 
Since they share the same Braille pattern, I went with a solution that retuns '>' only when we are in a number squence returns 'o'.

