#!/usr/bin/env ts-node

/**
 * When control characters are encountered, a function is returned to transform the next character
 * (and then return the rest of the input string alongside the transformed character). Said function
 * is also responsible for returning another `Control` if the control should still be active.
 */
type Control = (input: string) => [Control | null, string | undefined, string]
export class Character extends String {
  private capital?: string
  private number?: string
  private constructor(Default?: string, capital?: string, number?: number) {
    super(Default)
    this.capital = capital
    this.number = number?.toString()
  }
  private static CHARACTERS: { [key: string]: Character | undefined } = {
    "O.....": new Character("a", "A", 1),
    "O.O...": new Character("b", "B", 2),
    "OO....": new Character("c", "C", 3),
    "OO.O..": new Character("d", "D", 4),
    "O..O..": new Character("e", "E", 5),
    "OOO...": new Character("f", "F", 6),
    "OOOO..": new Character("g", "G", 7),
    "O.OO..": new Character("h", "H", 8),
    ".OO...": new Character("i", "I", 9),
    ".OOO..": new Character("j", "J", 0),
    "O...O.": new Character("k", "K"),
    "O.O.O.": new Character("l", "L"),
    "OO..O.": new Character("m", "M"),
    "OO.OO.": new Character("n", "N"),
    "O..OO.": new Character("o", "O"),
    "OOO.O.": new Character("p", "P"),
    "OOOOO.": new Character("q", "Q"),
    "O.OOO.": new Character("r", "R"),
    ".OO.O.": new Character("s", "S"),
    ".OOOO.": new Character("t", "T"),
    "O...OO": new Character("u", "U"),
    "O.O.OO": new Character("v", "V"),
    ".OOO.O": new Character("w", "W"),
    "OO..OO": new Character("x", "X"),
    "OO.OOO": new Character("y", "Y"),
    "O..OOO": new Character("z", "Z"),
    "......": new Character(" "),
  }

  /**
   * Takes the first six characters of a string and parses them as a `Character` or `Control`.
   *
   * @param input braille-encoded string
   * @throws if there aren't enough characters in `input`
   * @returns two values -- the parsed `Character`/`Control` (or undefined if neither was found),
   *          and the rest of the input string after the first six characters.
   */
  private static take6(input: string): [Character | Control | undefined, string] {
    const six = input.slice(0, 6)
    if (six.length !== 6)
      throw new RangeError(`expected 6 characters, found ${six.length}`)

    let r: Character | Control | undefined = Character.CHARACTERS[six] ?? Character.CONTROLS[six]

    return [r, input.slice(6)]
  }

  private static CONTROLS: { [key: string]: Control | undefined } = {
    ".....O": (input: string) => {
      let result: Character | Control | undefined
      [result, input] = this.take6(input)
      if (!(result instanceof Character && result.capital))
        throw new Error("invalid caps")
      else
        return [null, result.capital, input]
    },
    ".O.OOO": (input: string) => {
      let result: Character | Control | undefined

      if (input.slice(0, 6) === ".O...O") {
        console.error("DECIMALPT")
        return [
          Character.CONTROLS[".O.OOO"] ?? null, ".", input.slice(6)
        ]
      } else if (input.slice(0, 6) === "......") {
        console.error("SPACENUM")
        return [null, " ", input.slice(6)]
      }

      [result, input] = this.take6(input)
      switch (true) {
        case result instanceof Character:
          if (!result.number)
            throw new Error("invalid number")
          else {
            console.error(`DEBUG: ${result.number}`)
            return [Character.CONTROLS[".O.OOO"] ?? null, result.number, input]
          }
        case result === undefined:
          return [null, undefined, ""]
        default:
          throw new Error("double control")
      }
    },
  }


  /**
   * Parses a braille-encoded string and returns the result.
   *
   * @param input braille-encoded string
   * @returns the parsed string, or `undefined` if parsing failed.
   */
  public static read(input: string): string | undefined {
    console.error(`READING "${input}"`)
    let r = ""
    let control: Control | null = null
    while (input.length > 0) {
      console.error("WHILE")
      let result: Character | Control | undefined
      if (control)
        [control, result, input] = control(input)
      else
        [result, input] = Character.take6(input)

      switch (typeof result) {
        case "function":
          console.error("FUNCTION")
          if (control) {
            console.error("DOUBLE CONTROL")
            return undefined
          } else
            control = result
          break
        default:
          console.error(`DEBUG: ${result?.toString()}`)
          r += result?.toString() ?? ""
          break
      }
    }
    return r
  }
}

export class BrailleEncoder extends String {
  private static CHARACTERS: { [key: string]: string | undefined } = {
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
  }

  private static NUMBERS: { [key: string]: string | undefined } = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
  }

  /**
   * Encodes a string into braille.
   *
   * @throws if the input string cannot be represented as a valid braille string.
   * @returns the braille-encoded string
   */
  public static encode(input: string): string {
    let r = ""

    let number = false
    for (const char of input) {
      console.error("FOR")
      switch (true) {
        case char === " ":
          console.error("SPACE")
          r += "......"
          if (number)
            console.error("NUMBER OFF")
          number = false
          break
        case number:
          if (char === ".") {
            console.error("DECIMALPT")
            r += ".O...O"
          } else if (isNaN(parseInt(char)))
            throw new TypeError("malformed number")
          else if (!BrailleEncoder.NUMBERS[char])
            throw new Error("unreachable")
          else {
            console.error(`DEBUG: ${char} -> ${BrailleEncoder.NUMBERS[char]}`)
            r += BrailleEncoder.NUMBERS[char]
          }
          break
        default:
          if (BrailleEncoder.NUMBERS[char] !== undefined) {
            console.error("NUMBER ON")
            number = true
            r += ".O.OOO"
            r += BrailleEncoder.NUMBERS[char]
            console.error(`DEBUG: ${char} -> ${BrailleEncoder.NUMBERS[char]}`)
            continue
          } else if (BrailleEncoder.CHARACTERS[char.toLowerCase()] === undefined)
            throw new Error(`invalid character '${char.toLowerCase()}'`)
          else if (char.toUpperCase() === char) {
            console.error("UPPERCASE")
            r += ".....O"
          }
          console.error(`DEBUG: ${char.toLowerCase()} -> ${BrailleEncoder.CHARACTERS[char.toLowerCase()]}`)
          r += BrailleEncoder.CHARACTERS[char.toLowerCase()]
      }
    }

    return r
  }
}

const input = process.argv.slice(2).join(" ")
let result: string | undefined
try {
  result = Character.read(input)
} catch {
  result = BrailleEncoder.encode(input)
}
console.error(`FINAL: "${result}"`)
console.log(result)
