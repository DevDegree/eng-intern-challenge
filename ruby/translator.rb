# Define Braille mappings for lowercase letters, numbers, and special symbols
ENGLISH_TO_BRAILLE = {
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..', 
  'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..',
  'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.',
  'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.',
  'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO', 
  'z' => 'O..OOO', ' ' => '......',  # Space
  'capital' => '.....O',              # Capitalization indicator
  'number' => '.O.OOO'                # Number indicator
}

# Numbers are encoded using letters 'a' to 'j'
NUMBER_TO_BRAILLE = {
  '0' => '.OOO..', '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..',
  '5' => 'O..O..', '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..', '9' => '.OO...'
}

# Reverse mapping from Braille to English (includes both lowercase and capital indicator logic)
BRAILLE_TO_ENGLISH = ENGLISH_TO_BRAILLE.invert.merge(NUMBER_TO_BRAILLE.invert)

# Determine if the input is Braille by checking if it only contains 'O' and '.' characters
def is_braille?(input)
  input.match?(/\A[O\.]+\z/) && (input.length % 6 == 0)
end

# Function to translate English to Braille
def translate_to_braille(text)
  braille_output = ''
  is_number_mode = false

  text.each_char do |char|
    if char =~ /[A-Z]/
      braille_output += ENGLISH_TO_BRAILLE['capital']  # Add capital indicator for uppercase letters
      char = char.downcase
    end

    if char =~ /[0-9]/
      unless is_number_mode
        braille_output += ENGLISH_TO_BRAILLE['number']  # Add number indicator when switching to numbers
        is_number_mode = true
      end
      braille_output += NUMBER_TO_BRAILLE[char]
    elsif char =~ /[a-z]/
      is_number_mode = false  # Reset number mode when returning to letters
      braille_output += ENGLISH_TO_BRAILLE[char]
    elsif char == ' '
      is_number_mode = false  # Reset number mode for spaces
      braille_output += ENGLISH_TO_BRAILLE[' ']
    end
  end

  braille_output
end

# Function to translate Braille to English
def translate_to_english(braille)
  english_output = ''
  is_capital = false
  is_number_mode = false

  braille.scan(/.{6}/).each do |braille_char|
    if braille_char == ENGLISH_TO_BRAILLE['capital']
      is_capital = true
      next
    elsif braille_char == ENGLISH_TO_BRAILLE['number']
      is_number_mode = true
      next
    end

    if is_number_mode
      english_output += BRAILLE_TO_ENGLISH[braille_char].to_s
      is_number_mode = false if braille_char == ' '
    else
      letter = BRAILLE_TO_ENGLISH[braille_char].to_s
      english_output += is_capital ? letter.upcase : letter
      is_capital = false
    end
  end

  english_output
end

# Main program execution
input_string = ARGV[0]  # Read the input passed from command line

if is_braille?(input_string)
  # Translate Braille to English
  puts translate_to_english(input_string)
else
  # Translate English to Braille
  puts translate_to_braille(input_string)
end
