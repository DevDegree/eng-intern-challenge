import { English, BrailleCharacter } from './types'

export enum DictionaryTypes {
  Lowercase = 'Lowercase',
  Uppercase = 'Uppercase',
  Number = 'Number',
  Special = 'SpecialChar',
  Modifier = 'Modifier',
  Space = 'Space',
}
export interface BrailleDictionaryEntry {
  type: DictionaryTypes
  value: BrailleCharacter
}

export interface DictionaryEntry {
  type: DictionaryTypes
  value: BrailleCharacter
}

export interface EnglishDictionaryEntry {
  type: BrailleCharacter
  value: English
}

export class BrailleEnglishMap extends Map {
  private englishToBrailleMap: Map<English, BrailleDictionaryEntry> = new Map<
    English,
    BrailleDictionaryEntry
  >()
  private brailleToEnglishMap = new Map<
    DictionaryTypes,
    Map<BrailleCharacter, English>
  >([
    [DictionaryTypes.Lowercase, new Map<BrailleCharacter, English>()], // no modifiers
    [DictionaryTypes.Uppercase, new Map<BrailleCharacter, English>()],
    [DictionaryTypes.Number, new Map<BrailleCharacter, English>()],
    [DictionaryTypes.Special, new Map<BrailleCharacter, English>()], // no modifiers
    [DictionaryTypes.Modifier, new Map<BrailleCharacter, English>()],
    [DictionaryTypes.Space, new Map<BrailleCharacter, English>()], // no modifiers
  ])

  public setEntry =
    (english: English, braille: BrailleCharacter) =>
    (entryType: DictionaryTypes) => {
      {
        const brailleCharacter = braille as BrailleCharacter
        this.englishToBrailleMap.set(english, {
          type: entryType,
          value: brailleCharacter,
        })
        this.brailleToEnglishMap.set(
          entryType,
          this.brailleToEnglishMap
            .get(entryType)
            ?.set(brailleCharacter, english) ??
            new Map<BrailleCharacter, English>().set(brailleCharacter, english),
        )
        return this
      }
    }

  public getEnglish = (
    entryType: DictionaryTypes,
    braille: BrailleCharacter,
  ): English | undefined =>
    this.brailleToEnglishMap.get(entryType)?.get(braille)

  public getBraille = (english: English): BrailleDictionaryEntry | undefined =>
    this.englishToBrailleMap.get(english)
}
