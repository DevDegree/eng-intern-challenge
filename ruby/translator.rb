# Mapping of Braille characters to English letters, numbers, and punctuation
BRAILLE_ALPHABET = {
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
  'z' => 'O..OOO',
  '1' => 'O.....',
  '2' => 'O.O...',
  '3' => 'OO....',
  '4' => 'OO.O..',
  '5' => 'O..O..',
  '6' => 'OOO...',
  '7' => 'OOOO..',
  '8' => 'O.OO..',
  '9' => '.OO...',
  '0' => '.OOO..',
  'capital' => '.....O',   # Capital follows
  'number' => '.O.OOO',    # Number follows
  'decimal' => '.O.O..',   # Decimal follows (added)
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

# Inverted dictionary for translating Braille back to English
ENGLISH_ALPHABET = BRAILLE_ALPHABET.invert

# Function to determine if a given string is Braille
def is_braille?(string)
    # Check if the input is a valid Braille string by verifying it contains only dots (.) and Os
    # and its length is a multiple of 6
    string.match?(/\A[.O]+\z/) && string.length % 6 == 0
end


# Function to determine the direction of translation and perform the translation
def translate(input)
    if is_braille?(input)
        translate_braille_to_english(input)
    else
        translate_english_to_braille(input)
    end
end


# Function to translate English text to Braille
def translate_english_to_braille(input)
    output = ""
    number_mode = false  # This flag will indicate if we are in a numeric sequence
    
    input.chars.each do |char|
        if char.match(/[A-Z]/)
            output += BRAILLE_ALPHABET['capital'] + BRAILLE_ALPHABET[char.downcase]
            number_mode = false  # Capital letters break numeric mode
        elsif char.match(/[0-9]/)
            if !number_mode
                output += BRAILLE_ALPHABET['number']
                number_mode = true  # We are now in a numeric sequence
            end
            output += BRAILLE_ALPHABET[char]
        elsif char == ' '
            output += BRAILLE_ALPHABET[char]
            number_mode = false  # Spaces break numeric mode
        else
            output += BRAILLE_ALPHABET[char]
            number_mode = false  # Any non-number character breaks numeric mode
        end
    end
    output
end

# Function to translate Braille text back to English
def translate_braille_to_english(input)
    input.scan(/.{6}/).map { |braille_char| ENGLISH_ALPHABET[braille_char] }.join
end


input = ARGV.join(" ")
puts translate(input)
