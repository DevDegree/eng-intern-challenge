 Define Braille mapping
BRAILLE = {
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..', 
  'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..', 
  'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.', 
  'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.', 
  'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO', 
  'z' => 'O..OOO', ' ' => '......', '#' => '.O.OOO', 'upcase' => '.....O'
}

# Reverse the Braille map for English to Braille translation
ENGLISH = BRAILLE.invert

# Function to translate a Braille number to English
def get_english_number(char)
  ENGLISH.keys.index(char)
end

# Function to translate an English number to Braille
def get_braille_number(char)
  BRAILLE.values[char.to_i]
end

# Function to determine if input is Braille
def is_braille?(input)
  input.delete('.O ').empty?
end

# Function to translate English to Braille
def english_to_braille(input)
  in_number_mode = false  # Flag to track if the current context is numeric.
  input.chars.map do |char|
    if char == ' '
      in_number_mode = false  # Reset number mode on encountering a space.
      BRAILLE[char]
    elsif char =~ /\d/
      if !in_number_mode
        in_number_mode = true  # Set number mode when a digit is first encountered.
        BRAILLE['#'] + get_braille_number(char)
      else
        get_braille_number(char)
      end
    else
      in_number_mode = false
      is_capital = char.upcase == char && char.downcase != char  # Check if the character is a capital letter.
      char = BRAILLE[char.downcase] || ''  # Translate to Braille or use an empty string if no mapping exists.
      is_capital ? BRAILLE['upcase'] + char : char  # Prefix with upcase Braille if the character is capital.
    end
  end.join
end

# Function to translate Braille to English
def braille_to_english(input)
  result = ''
  in_number_mode = false  # Flag to track numeric context.
  i = 0
  while i < input.length
    char = input[i, 6]  # Extract a segment of 6 characters which represents one Braille character.
    if char == BRAILLE['upcase']
      i += 6  # Skip the next 6 characters as they represent an uppercase letter.
      next_char = input[i, 6]
      result += (ENGLISH[next_char] || '').upcase  # Convert the next Braille character to uppercase.
    elsif char == BRAILLE['#']
      in_number_mode = true  # Enter number mode on encountering the number sign.
    elsif char == BRAILLE[' ']
      in_number_mode = false  # Exit number mode on space.
      result += ' '
    else
      result += in_number_mode ? get_english_number(char).to_s : ENGLISH[char]  # Append the translated character or number.
    end
    i += 6
  end
  result
end

# Main function to handle the translation based on the input type.
def main
  input = ARGV.join(" ")  # Combine command line arguments into a single string.

  # Output the translation based on whether the input is Braille or English.
  puts is_braille?(input) ? 
    braille_to_english(input) 
    : english_to_braille(input)
end

main
