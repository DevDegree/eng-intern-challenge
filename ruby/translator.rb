#!/usr/bin/env ruby

##
#
class Translator
    LETTERS_ENGLISH_TO_BRAILLE = {
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
    NUMBERS_ENGLISH_TO_BRAILLE = {
      "1" => "O.....",
      "2" => "O.O...",
      "3" => "OO....",
      "4" => "OO.O..",
      "5" => "O..O..",
      "6" => "OOO...",
      "7" => "OOOO..",
      "8" => "O.OO..",
      "9" => ".OO...",
      "0" => ".OOO.."
    }
    LETTERS_BRAILLE_TO_ENGLISH = LETTERS_ENGLISH_TO_BRAILLE.invert
    NUMBERS_BRAILLE_TO_ENGLISH = NUMBERS_ENGLISH_TO_BRAILLE.invert
    BRAILLE_CAPITAL_FOLLOWS = ".....O"
    BRAILLE_NUMBER_FOLLOWS  = ".O.OOO"
    BRAILLE_SPACE           = "......"

    ##
    # Checks if a string is a valid representation of Braille.
    # A valid Braille string has a length that is a multiple of 6, and only contains the characters "O" and "."
    #
    # @param s [String] The string to be checked
    # @return [Boolean] Returns true if the string is a valid Braille representation, otherwise return false
    def is_braille?(s)
        # return false if the size of the string is not a multiple of 6
        return false unless s.size % 6 == 0

        # return true if string is comprised of only "O" and "."
        s.chars.all? { |c| c == "O" || c == "." }
    end

    ##
    # Prints the English translation of a given Braille string
    #
    # @param braille_string [String] The Braille string to be translated to English
    def translate_to_english(braille_string)
        # Initialize an empty string to hold the translation
        translation = ""

        # Flags to indicate if the next character should be capitalized or is a number
        capital_follows = false
        number_follows  = false

        # Process chunks of 6 characters in braille_string (representing one braille character)
        braille_string.chars.each_slice(6) do |slice|
            braille_char = slice.join

            case braille_char
            when BRAILLE_CAPITAL_FOLLOWS
                capital_follows = true
            when BRAILLE_NUMBER_FOLLOWS
                number_follows = true
            when BRAILLE_SPACE
                translation << " "
                number_follows = false # When a Braille `number follows` symbol is read, assume all following symbols are numbers until the next `space` symbol
            else
                # Convert braille to English using braille_to_english hash
                english_char = LETTERS_BRAILLE_TO_ENGLISH[braille_char]

                # Capitalize English letter if capital_follows = true
                english_char = capital_follows ? english_char.capitalize : english_char
                capital_follows = false

                # Convert English letter to its digit equivalent if number_follows = true
                english_char = number_follows ? NUMBERS_BRAILLE_TO_ENGLISH[braille_char] : english_char

                translation << english_char
            end
        end

        # Print final translation
        puts translation
    end

    ##
    # Prints the Braille translation of a given English string
    #
    # @param english_string [String] The English string to be translated to Braille
    def translate_to_braille(english_string)

        # Checks if a given English character is a capitalized letter (A - Z)
        def is_capitalized?(char)
            char.ord.between?(65, 90)
        end

        # Checks if a given English character is a digit (0 - 9)
        def is_digit?(char)
            char.ord.between?(48, 57)
        end

        # Initialize an empty string to hold the translation
        translation = ""

        # Flag to indicate if the braille character for `number_follows` needs to be added to the translation
        # If true, then BRAILLE_NUMBER_FOLLOWS must not be added to the translation (i.e., BRAILLE_NUMBER_FOLLOWS is already included. Only append the braille number to the translation)
        # If false, then BRAILLE_NUMBER_FOLLOWS must be added to the translation (i.e., BRAILLE_NUMBER_FOLLOWS not yet included. Must append BRAILLE_NUMBER_FOLLOWS and the braille number to the translation)
        number_follows_active = false

        # Iterate through each character of the English string
        english_string.each_char do |english_char|
            case
            when is_capitalized?(english_char)
                translation << BRAILLE_CAPITAL_FOLLOWS + LETTERS_ENGLISH_TO_BRAILLE[english_char.downcase]
            when is_digit?(english_char)
                unless number_follows_active
                    translation << BRAILLE_NUMBER_FOLLOWS
                    number_follows_active = true
                end
                translation << NUMBERS_ENGLISH_TO_BRAILLE[english_char]
            when english_char == " "
                translation << BRAILLE_SPACE
                number_follows_active = false # When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.
            else
                translation << LETTERS_ENGLISH_TO_BRAILLE[english_char]
            end
        end

        # Print final translation
        puts translation
    end
end

if __FILE__ == $0
    translator= Translator.new
    string_to_translate = ARGV.join(" ")

    if translator.is_braille?(string_to_translate)
        translator.translate_to_english(string_to_translate)
    else
        translator.translate_to_braille(string_to_translate)
    end
end