# translator.rb

# Braille mappings: English letters, numbers, and special control characters
braille_alphabet = {
  "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..",
  "e" => "O..O..", "f" => "OOO...", "g" => "OOOO..", "h" => "O.OO..",
  "i" => ".OO...", "j" => ".OOO..", "k" => "O...O.", "l" => "O.O.O.",
  "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.", "p" => "OOO.O.",
  "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.",
  "u" => "O...OO", "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO",
  "y" => "OO.OOO", "z" => "O..OOO", " " => "......",
  "capital" => ".....O", "number" => ".O.OOO",
  "0" => ".OOO..", "1" => "O.....", "2" => "O.O...", "3" => "OO....",
  "4" => "OO.O..", "5" => "O..O..", "6" => "OOO...", "7" => "OOOO..",
  "8" => "O.OO..", "9" => ".OO..."
}

# Function to convert English to Braille
def english_to_braille(text, braille_alphabet)
  output = ""
  in_number_mode = false  # Tracks if we are in number mode
  text.each_char do |char|
    # Check for uppercase characters
    if char =~ /[A-Z]/
      output += braille_alphabet["capital"]
      output += braille_alphabet[char.downcase]
    # Check for digits
    elsif char =~ /\d/
      unless in_number_mode  # Only switch to number mode if not already in it
        output += braille_alphabet["number"]
        in_number_mode = true
      end
      output += braille_alphabet[char]
    else
      in_number_mode = false if char == " "  # Reset number mode on space
      output += braille_alphabet[char] || ''  # Default to empty if char not found
    end
  end
  output
end

# Function to convert Braille to English
def braille_to_english(braille, braille_alphabet)
  reversed_alphabet = braille_alphabet.invert
  english = ""
  i = 0
  capitalize_next = false  # Tracks if the next letter should be capitalized
  in_number_mode = false   # Tracks if we are in number mode

  # Process the Braille string 6 characters at a time
  while i < braille.length
    current_symbol = braille[i, 6]

    # Handle special symbols for capitalization and numbers
    if current_symbol == braille_alphabet["capital"]
      capitalize_next = true
      i += 6
      next  # Skip to the next character after setting capitalize
    elsif current_symbol == braille_alphabet["number"]
      in_number_mode = true
      i += 6
      next  # Skip to the next character after setting number mode
    elsif current_symbol == braille_alphabet[" "]
      english += " "
      in_number_mode = false  # Reset number mode on space
    else
      # Append the translated character to the result
      char = reversed_alphabet[current_symbol] || ''
      char = char.upcase if capitalize_next  # Capitalize if needed
      english += char
      capitalize_next = false  # Reset capitalization after use
    end
    i += 6  # Move to the next Braille character (6 positions ahead)
  end
  english
end

# Entry point: Detect input type (Braille or English) and translate
input = ARGV[0]

# Simple input check: Braille contains only 'O' and '.'
if input =~ /^[O.]+$/
  puts braille_to_english(input, braille_alphabet)
else
  puts english_to_braille(input, braille_alphabet)
end
