BRAILLE_ALPHABET_LETTERS = {
  'a' => 'O.....',
  'b' => 'O.O...',
  'c' => 'OO....',
  'd' => 'OO.O..',
  'e' => 'O..O..',
  'f' => 'OOO...',
  'g' => 'OOOO..',
  'h' => 'O.OO..',
  'i' => '.OO...',
  'j' => '.OOO..',
  'k' => 'O...O.',
  'l' => 'O.O.O.',
  'm' => 'OO..O.',
  'n' => 'OO.OO.',
  'o' => 'O..OO.',
  'p' => 'OOO.O.',
  'q' => 'OOOOO.',
  'r' => 'O.OOO.',
  's' => '.OO.O.',
  't' => '.OOOO.',
  'u' => 'O...OO',
  'v' => 'O.O.OO',
  'w' => '.OOO.O',
  'x' => 'OO..OO',
  'y' => 'OO.OOO',
  'z' => 'O..OOO'
}

BRAILLE_ALPHABET_NUMBERS = {
  '1' => 'O.....',
  '2' => 'O.O...',
  '3' => 'OO....',
  '4' => 'OO.O..',
  '5' => 'O..O..',
  '6' => 'OOO...',
  '7' => 'OOOO..',
  '8' => 'O.OO..',
  '9' => '.OO...',
  '0' => '.OOO..'
}

BRAILLE_ALPHABET_SPECIAL = {
  '.' => '..OO.O',
  ',' => '..O...',
  '?' => '..O.O.',
  '!' => '..OO..',
  ':' => '..OO.O',
  ';' => '..O.OO',
  '-' => '..O.OO',
  '/' => '.O..O.',
  '<' => '..OO.O',
  '>' => '..OOOO',
  '(' => '.O..OO',
  ')' => '..O.O.',
  ' ' => '......'
}

BRAILLE_INDICATORS = {
  'capital' => '.....O',   # Capital follows
  'number' => '.O.OOO',    # Number follows
  'decimal' => '.O.O..'    # Decimal follows (added)
}

def is_braille?(string)
    # Check if the input is a valid Braille string by verifying it contains only dots (.) and Os 
    # and its length is a multiple of 6
    string.match?(/\A[.O]+\z/) && string.length % 6 == 0
end


def translate(input)
    if is_braille?(input)
        translate_braille_to_english(input)
    else
        translate_english_to_braille(input)
    end
end


def translate_english_to_braille(input)
    output = ""
    number_mode = false  # This flag will indicate if we are in a numeric sequence
  
    input.chars.each do |char|
      if char.match(/[A-Z]/)
        # Handle uppercase letters
        output += BRAILLE_INDICATORS['capital'] + BRAILLE_ALPHABET_LETTERS[char.downcase]
        number_mode = false  # Capital letters break numeric mode
      elsif char.match(/[0-9]/)
        # Handle numbers
        unless number_mode
          output += BRAILLE_INDICATORS['number']
          number_mode = true  # We are now in a numeric sequence
        end
        output += BRAILLE_ALPHABET_NUMBERS[char]
      elsif char == ' '
        # Handle spaces
        output += BRAILLE_ALPHABET_SPECIAL[char]
        number_mode = false  # Spaces break numeric mode
      elsif BRAILLE_ALPHABET_LETTERS.key?(char)
        # Handle lowercase letters
        output += BRAILLE_ALPHABET_LETTERS[char]
        number_mode = false  # Any non-number character breaks numeric mode
      elsif BRAILLE_ALPHABET_SPECIAL.key?(char)
        # Handle special characters
        output += BRAILLE_ALPHABET_SPECIAL[char]
        number_mode = false  # Special characters break numeric mode
      else
        raise "Unexpected character received: '#{char}'"
      end
    end
  
    output
  end
  
  def translate_braille_to_english(input)
    output = ""
    capital_on = false
    number_on = false
  
    # Process each Braille character group (6-dot pattern)
    input.scan(/.{6}/).each do |braille_char|
      if braille_char == BRAILLE_INDICATORS['capital']
        capital_on = true
      elsif braille_char == BRAILLE_INDICATORS['number']
        number_on = true
      else
        if capital_on && BRAILLE_ALPHABET_LETTERS.value?(braille_char)
          output += BRAILLE_ALPHABET_LETTERS.key(braille_char).upcase
          capital_on = false  # Reset capital flag
        elsif number_on && BRAILLE_ALPHABET_NUMBERS.value?(braille_char)
          output += BRAILLE_ALPHABET_NUMBERS.key(braille_char)
          # Keep the number_on flag true, allowing the next numbers to be processed correctly
        elsif BRAILLE_ALPHABET_LETTERS.value?(braille_char)
          output += BRAILLE_ALPHABET_LETTERS.key(braille_char)
          number_on = false  # Reset number flag when a letter is encountered
        elsif BRAILLE_ALPHABET_NUMBERS.value?(braille_char)
          output += BRAILLE_ALPHABET_NUMBERS.key(braille_char)
          number_on = false  # Reset number flag after processing the first number
        elsif BRAILLE_ALPHABET_SPECIAL.value?(braille_char)
          output += BRAILLE_ALPHABET_SPECIAL.key(braille_char)
          number_on = false  # Reset number flag after processing a special character
        else
          puts "Warning: Unrecognized Braille character: #{braille_char}"
        end
      end
    end
  
    output
  end
  
input = ARGV.join(" ")
puts translate(input)
