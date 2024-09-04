# Define the Braille Dictionary
BRAILLE_DICT = {
  "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..", "e" => "O..O..",
  "f" => "OOO...", "g" => "OOOO..", "h" => "O.OO..", "i" => ".OO...", "j" => ".OOO..",
  "k" => "O...O.", "l" => "O.O.O.", "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.",
  "p" => "OOO.O.", "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.",
  "u" => "O...OO", "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO", "y" => "OO.OOO",
  "z" => "O..OOO",
  " " => "......",
  "capital" => ".....O",
  "number" => ".O.OOO",
  "0" => ".OOO..", "1" => "O.....", "2" => "O.O...", "3" => "OO....", "4" => "OO.O..",
  "5" => "O..O..", "6" => "OOO...", "7" => "OOOO..", "8" => "O.OO..", "9" => ".OO..."
}

# Reverse Dictionary for English Translation
ENGLISH_DICT = BRAILLE_DICT.invert

# Determine if the input string is Braille
def braille?(input_string)

  # if the string contains all 0s and .s then it is Braille
  # TO DO: Logic out if it makes sense to check all values - I think it does
  input_string.chars.all? { |c| c == 'O' || c == '.' }

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
    puts "Braille"
  else
    puts "English"
  end

end

# Execute main for when file is run directly
main if __FILE__ == $PROGRAM_NAME
