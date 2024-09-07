#!/usr/bin/env ruby

english_to_braille = {
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
braille_to_english = english_to_braille.invert
braille_letter_to_digit = {
  "a" => "1", "b" => "2", "c" => "3", "d" => "4", "e" => "5", "f" => "6",
  "g" => "7", "h" => "8", "i" => "9", "j" => "10",
}

def is_braille?(s)
    # return false if the size of the string is not a multiple of 6
    return false unless s.size % 6 == 0

    # return true if string is comprised of only "O" and "."
    s.chars.all? { |c| c == "O" || c == "." }
end

def is_capital_follows?(s)
    # return true if s matches the braille representation for "Capital follows"
    s == ".....O"
end

def is_number_follows?(s)
    # return true if s matches the braille representation for "Number follows"
    s == ".O.OOO"
end

def is_space?(s)
    # return true if s matches the braille representation for "Capital follows"
    s == "......"
end

def translate_to_english(s, braille_to_english, letter_to_digit)
    # Initialize an empty string to hold the translation
    translation = ""

    # Flags to indicate if the next character should be capitalized or is a number
    capital_follows = false
    number_follows     = false

    # Iterate over the string 's', processing it in chunks of 6 characters (representing a braille character)
    s.chars.each_slice(6) do |slice|
        braille_char = slice.join

        case
        when is_capital_follows?(braille_char)
            capital_follows = true
        when is_number_follows?(braille_char)
            number_follows = true
        when is_space?(braille_char)
            translation += " "
            number_follows = false # When a Braille `number follows` symbol is read, assume all following symbols are numbers until the next `space` symbol
        else
            # Convert braille to English using braille_to_english hash
            english_char = braille_to_english[braille_char]

            # Capitalize English letter if capital_follows = true
            english_char = capital_follows ? english_char.capitalize : english_char
            capital_follows = false

            # Convert English letter to its digit equivalent if number_follows = true
            english_char = number_follows ? letter_to_digit[english_char] : english_char

            translation += english_char
        end
    end

    # Print final translation
    puts translation
end

def translate_to_braille(s, english_to_braille)
    translation = ""
    puts translation
end

ARGV.each do|arg|
    if is_braille?(arg)
        translate_to_english(arg, braille_to_english, braille_letter_to_digit)
    else
        translate_to_braille(arg, english_to_braille)
    end
end

