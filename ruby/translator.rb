# Define Braille Dictionaries
BRAILLE_LETTER_DICT = {
  "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..", "e" => "O..O..",
  "f" => "OOO...", "g" => "OOOO..", "h" => "O.OO..", "i" => ".OO...", "j" => ".OOO..",
  "k" => "O...O.", "l" => "O.O.O.", "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.",
  "p" => "OOO.O.", "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.",
  "u" => "O...OO", "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO", "y" => "OO.OOO",
  "z" => "O..OOO",
  " " => "......",
  "capital" => ".....O"
}

# Seperate dictionary for numbers as to avoid confusion when converting from braille to english a = 1, b = 2, etc.
BRAILLE_NUMBER_DICT = {
  "0" => ".OOO..", "1" => "O.....", "2" => "O.O...", "3" => "OO....", "4" => "OO.O..",
  "5" => "O..O..", "6" => "OOO...", "7" => "OOOO..", "8" => "O.OO..", "9" => ".OO...", "number" => ".O.OOO"
}

# Reverse Dictionaries for English Translation
ENGLISH_LETTER_DICT = BRAILLE_LETTER_DICT.invert
ENGLISH_NUMBER_DICT = BRAILLE_NUMBER_DICT.invert

# Determine if the input string is Braille
def braille?(input_string)

  # if the string contains all Os and .s then it is Braille
  # TO DO: Logic out if it makes sense to check all values - I think it does
  input_string.chars.all? { |c| c == 'O' || c == '.' }

end

# Convert Braille to English
def braille_to_english(braille_translation)

  # Store the translated characters
  english_translation = []
  i = 0
  
  # Flags to track whether the next character should be capitalized or if it's a number
  is_capital = false
  is_number = false

  # Loop through the braille string, processing 6 characters (one Braille symbol) at a time
  while i < braille_translation.length

    # Extract the next 6 characters to form a Braille symbol
    symbol = braille_translation[i, 6]
    
    # Check if the symbol is the Braille "capital" indicator
    if symbol == BRAILLE_LETTER_DICT["capital"]

      is_capital = true
    
    # Check if the symbol is the Braille "number" indicator
    elsif symbol == BRAILLE_NUMBER_DICT["number"]

      is_number = true

    else

      # Search number dictionary for the conversion if it exists
      if is_number

        # TO DO: decide if adding "" makes sense if a symbol isn't in dictionary
        char = ENGLISH_NUMBER_DICT[symbol] || ""
        if char.match?(/\d/)
          english_translation << char
        else
          is_number = false
          english_translation << char
        end

      else

        char = ENGLISH_LETTER_DICT[symbol] || ""
        if is_capital
          char = char.upcase
          is_capital = false
        end

        english_translation << char

      end

    end
    
    i += 6

  end

  english_translation.join

end

# Convert English to Braille
def english_to_braille(english_string)
  braille_translation = []
  is_number = false

  english_string.each_char do |char|
    if char.match?(/[A-Z]/)
      # Add capital indicator and convert to lowercase
      braille_translation << BRAILLE_LETTER_DICT["capital"]
      char = char.downcase
    end

    if char.match?(/\d/)
      # Add number indicator if it's not already added
      unless is_number
        braille_translation << BRAILLE_NUMBER_DICT["number"]
        is_number = true
      end
      braille_translation << BRAILLE_NUMBER_DICT[char]
    else
      # set flag to false, if a letter or space is encountered
      is_number = false
      braille_translation << BRAILLE_LETTER_DICT[char] || ""
    end
  end

  braille_translation.join
end


def main

  # Join all arguments into a single string
  input_string = ARGV.join(" ")

  # Verifies that there is at least something to translate
  if input_string.empty?
    puts "Usage: ruby translator.rb <input_string>"
    return
  end

  # Check if input is braille or english
  if braille?(input_string)
    puts braille_to_english(input_string)
  else
    puts english_to_braille(input_string)
  end

end

# Execute main for when file is run directly
main if __FILE__ == $PROGRAM_NAME
