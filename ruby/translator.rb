#!/usr/bin/env ruby

class Translator
    ENGLISH_TO_BRAILLE = {
      "a" => "O.....",
      "b" => "O.O...",
      "c" => "OO....",
      "d" => "OO.O..",
      "e" => "O..O..",
      "f" => "OOO...",
      "g" => "OOOO..",
      "h" => "O.OO..",
      "i" => ".OO...",
      "j" => ".OOO..",
      "k" => "O...O.",
      "l" => "O.O.O.",
      "m" => "OO..O.",
      "n" => "OO.OO.",
      "o" => "O..OO.",
      "p" => "OOO.O.",
      "q" => "OOOOO.",
      "r" => "O.OOO.",
      "s" => ".OO.O.",
      "t" => ".OOOO.",
      "u" => "O...OO",
      "v" => "O.O.OO",
      "w" => ".OOO.O",
      "x" => "OO..OO",
      "y" => "OO.OOO",
      "z" => "O..OOO"
    }
    BRAILLE_TO_ENGLISH = ENGLISH_TO_BRAILLE.invert
    BRAILLE_LETTER_TO_DIGIT = {
      "a" => "1", "b" => "2", "c" => "3", "d" => "4", "e" => "5", "f" => "6",
      "g" => "7", "h" => "8", "i" => "9", "j" => "10",
    }
    BRAILLE_CAPITAL_FOLLOWS = ".....O"
    BRAILLE_NUMBER_FOLLOWS  = ".O.OOO"
    BRAILLE_SPACE           = "......"

    def is_braille?(s)
        # return false if the size of the string is not a multiple of 6
        return false unless s.size % 6 == 0

        # return true if string is comprised of only "O" and "."
        s.chars.all? { |c| c == "O" || c == "." }
    end

    def translate_to_english(braille_string)
        # Initialize an empty string to hold the translation
        translation = ""

        # Flags to indicate if the next character should be capitalized or is a number
        capital_follows = false
        number_follows  = false

        # Iterate over the string 's', processing it in chunks of 6 characters (representing a braille character)
        braille_string.chars.each_slice(6) do |slice|
            braille_char = slice.join

            case
            when braille_char == BRAILLE_CAPITAL_FOLLOWS
                capital_follows = true
            when braille_char == BRAILLE_NUMBER_FOLLOWS
                number_follows = true
            when braille_char == BRAILLE_SPACE
                translation += " "
                number_follows = false # When a Braille `number follows` symbol is read, assume all following symbols are numbers until the next `space` symbol
            else
                # Convert braille to English using braille_to_english hash
                english_char = BRAILLE_TO_ENGLISH[braille_char]

                # Capitalize English letter if capital_follows = true
                english_char = capital_follows ? english_char.capitalize : english_char
                capital_follows = false

                # Convert English letter to its digit equivalent if number_follows = true
                english_char = number_follows ? BRAILLE_LETTER_TO_DIGIT[english_char] : english_char

                translation += english_char
            end
        end

        # Print final translation
        puts translation
    end

    def translate_to_braille(english_string)
        translation = ""
        puts translation
    end
end

translator= Translator.new
ARGV.each do|arg|
    if translator.is_braille?(arg)
        translator.translate_to_english(arg)
    else
        translator.translate_to_braille(arg)
    end
end

