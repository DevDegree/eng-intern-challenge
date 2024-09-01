import { BrailleDictionary } from './src/BrailleDictionary'
import { DictionaryTypes } from './src/BrailleEnglishMap'
import { Braille, English } from './src/types'
import { chunkBrailleCharacters, isBraille } from './src/utils'
import yargs, { Arguments } from 'yargs'
import { hideBin } from 'yargs/helpers'

const brailleDictionary = new BrailleDictionary()

// Is it english or braille
const translator = (text: string[]) =>
  isBraille(text[0]) ? brailleToEnglish(text[0]) : englishToBraille(text)

const brailleToEnglish = (input: Braille): void => {
  var translation: string = ''

  // break input into array of Braille
  const brailleCharacters = chunkBrailleCharacters(input)
  var isNumber = false
  var capitalFollow = false

  for (const brailleCharacter of brailleCharacters) {
    // Check if the first char is a modifier, if so, lookup the next char using the correct dictionary
    var translatedCharacter: string | undefined
    if (isNumber) {
      const numberValue = brailleDictionary.lookupEnglish(
        DictionaryTypes.Number,
        brailleCharacter,
      )
      numberValue
        ? (translation += numberValue)
        : console.error('Invalid number')
    } else if (capitalFollow) {
      translatedCharacter = brailleDictionary.lookupEnglish(
        DictionaryTypes.Uppercase,
        brailleCharacter,
      )
      translation += translatedCharacter
      capitalFollow = false
    } else {
      const space = brailleDictionary.lookupEnglish(
        DictionaryTypes.Space,
        brailleCharacter,
      )
      if (space) {
        translation += ' '
        isNumber = false
      } else {
        const modifier = brailleDictionary.lookupEnglish(
          DictionaryTypes.Modifier,
          brailleCharacter,
        )
        if (modifier) {
          switch (modifier) {
            case 'capital-follows': {
              translatedCharacter = brailleDictionary.lookupEnglish(
                DictionaryTypes.Uppercase,
                brailleCharacter,
              )
              capitalFollow = true
              break
            }
            case 'number-follows': {
              isNumber = true
              translatedCharacter = brailleDictionary.lookupEnglish(
                DictionaryTypes.Number,
                brailleCharacter,
              )
              translatedCharacter
                ? (translation += translatedCharacter)
                : console.error('Invalid character')
              break
            }
            // @TODO Add support for decimals
          }
        } else {
          translatedCharacter = brailleDictionary.lookupEnglish(
            DictionaryTypes.Lowercase,
            brailleCharacter,
          )
          if (translatedCharacter) translation += translatedCharacter

          translatedCharacter = brailleDictionary.lookupEnglish(
            DictionaryTypes.Special,
            brailleCharacter,
          )
          if (translatedCharacter) translation += translatedCharacter
        }
      }
    }
  }
  console.log(translation)
}

const englishToBraille = (words: string[]): void => {
  var translatedWords: string[] = []

  for (const word of words) {
    const characters = word.split('')
    var translatedWord = ''

    for (const [index, character] of characters.entries()) {
      const brailleChar = brailleDictionary.lookupBraille(character)

      if (brailleChar) {
        switch (brailleChar.type) {
          case DictionaryTypes.Uppercase: {
            translatedWord += `${brailleDictionary.lookupBraille('capital-follows')?.value}${brailleChar.value}`
            break
          }
          case DictionaryTypes.Lowercase:
            translatedWord += brailleChar.value
            break
          case DictionaryTypes.Special:
            translatedWord += brailleChar.value
            break
          case DictionaryTypes.Number: {
            index === 0
              ? (translatedWord += `${brailleDictionary.lookupBraille('number-follows')?.value}${brailleChar.value}`)
              : (translatedWord += brailleChar.value)
            break
          }
          // @TODO Add support for decimals
        }
      } else {
        throw new Error(`Character ${character} not found in dictionary`)
      }
    }
    translatedWords.push(translatedWord)
  }

  const spaceBrailleChar = brailleDictionary.lookupBraille(' ')
  const translation = translatedWords.join(spaceBrailleChar?.value)

  console.log(translation)
}

const argv = yargs(hideBin(process.argv))
  .command('$0 <text...>', 'Translate text between English and Braille')
  .positional('text', {
    describe:
      'String written in plain English or Braille that you want to translate',
    demandOption: true,
    type: 'string',
    array: true,
  })
  .parseSync()
argv.text

translator(argv.text)
