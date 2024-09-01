import {
  BrailleEnglishMap,
  DictionaryTypes,
  BrailleDictionaryEntry,
} from './BrailleEnglishMap'
import { BrailleCharacter, English } from './types'
import { isEnglish, isBrailleCharacter } from './utils'
import brailleMappings from './dictionaryEntries.json'

export class BrailleDictionary {
  private brailleMap: BrailleEnglishMap
  addDictionaryEntries =
    (dictionaryEntries: any[]) => (type: DictionaryTypes) =>
      dictionaryEntries.forEach(([englishEntry, brailleEntry]) =>
        isEnglish(englishEntry)
          ? isBrailleCharacter(brailleEntry)
            ? this.brailleMap.setEntry(englishEntry, brailleEntry)(type)
            : console.warn(`Invalid entry: ${brailleEntry}`)
          : console.warn(`Invalid entry: ${englishEntry}`),
      )

  constructor() {
    this.brailleMap = new BrailleEnglishMap()
    this.addDictionaryEntries(brailleMappings.modifiers)(
      DictionaryTypes.Modifier,
    )
    this.addDictionaryEntries(brailleMappings.lowerCaseAlphabet)(
      DictionaryTypes.Lowercase,
    )
    this.addDictionaryEntries(brailleMappings.upperCaseAlphabet)(
      DictionaryTypes.Uppercase,
    )
    this.addDictionaryEntries(brailleMappings.numbers)(DictionaryTypes.Number)
    this.addDictionaryEntries(brailleMappings.specialCharacters)(
      DictionaryTypes.Special,
    )
    this.addDictionaryEntries(brailleMappings.space)(DictionaryTypes.Space)
  }
  lookupEnglish = (
    entryType: DictionaryTypes,
    braille: BrailleCharacter,
  ): English | undefined => this.brailleMap.getEnglish(entryType, braille)

  lookupBraille = (english: English): BrailleDictionaryEntry | undefined =>
    this.brailleMap.getBraille(english)
}
