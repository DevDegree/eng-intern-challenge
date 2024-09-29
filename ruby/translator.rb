# Braille alphabet mappings
BRAILLE_TO_ENGLISH = {
  'O.....' => 'a', 'O.O...' => 'b', 'OO....' => 'c', 'OO.O..' => 'd', 'O..O..' => 'e',
  'OOO...' => 'f', 'OOOO..' => 'g', 'O.OO..' => 'h', '.OO...' => 'i', '.OOO..' => 'j',
  'O...O.' => 'k', 'O.O.O.' => 'l', 'OO..O.' => 'm', 'OO.OO.' => 'n', 'O..OO.' => 'o',
  'OOO.O.' => 'p', 'OOOOO.' => 'q', 'O.OOO.' => 'r', '.OO.O.' => 's', '.OOOO.' => 't',
  'O...OO' => 'u', 'O.O.OO' => 'v', '.OOO.O' => 'w', 'OO..OO' => 'x', 'OO.OOO' => 'y',
  'O..OOO' => 'z',
  '.....O' => 'capital follows',   
  '.O.OOO' => 'number follows',   
  '.O...O' => 'decimal follows',   
}

SPECIAL_BRAILLE_TO_ENGLISH = {
  '......' => ' ',                
  '..OO.O' => '.',                
  '..O...' => ',',              
  '..O.OO' => '?',                
  '..OOO.' => '!',                 
  '..OO..' => ':',                
  '..O.O.' => ';',                 
  '....OO' => '-',                 
  '.O..O.' => '/',                
  '.OO..O' => '<',                
  'O..OO.' => '>',                 
  'O.O..O' => '(',                 
  '.O.OO.' => ')',                 
}

ENGLISH_TO_BRAILLE = {
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..',
  'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..',
  'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.',
  'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.',
  'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO',
  'z' => 'O..OOO', 'capital follows' => '.....O', 'number follows' => '.O.OOO', 'decimal follows' => '.O...O',
}


SPECIAL_ENGLISH_TO_BRAILLE = {
  ' ' => '......',
  '.' => '..OO.O', ',' => '..O...', '?' => '..O.OO', '!' => '..OOO.', ':' => '..OO..',
  ';' => '..O.O.', '-' => '....OO', '/' => '.O..O.', '<' => '.OO..O', '>' => 'O..OO.',
  '(' => 'O.O..O', ')' => '.O.OO.',
}

# Braille digits (following 'number follows' marker)
BRAILLE_DIGITS = {
  'O.....' => '1', 'O.O...' => '2', 'OO....' => '3', 'OO.O..' => '4', 'O..O..' => '5',
  'OOO...' => '6', 'OOOO..' => '7', 'O.OO..' => '8', '.OO...' => '9', '.OOO..' => '0'
}

ENGLISH_DIGITS = {
  '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..', '5' => 'O..O..',
  '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..', '9' => '.OO...', '0' => '.OOO..'
}

def is_braille?(input)
  input.match?(/^[O.]+$/) && (input.length % 6).zero?
end

def translate_braille_to_english(braille_string)
  characters = braille_string.scan(/.{6}/)
  english_output = ''
  capitalize_next = false
  number_mode = false
  punctuation_mode = false
  greater_than_mode = false

  characters.each_with_index do |char, index|
    if char == '.....O'
      capitalize_next = true
    elsif char == '.O.OOO'
      number_mode = true
    elsif char == '..O.OO'
      english_output << '.'
    elsif BRAILLE_DIGITS.key?(char) && number_mode
      english_output << BRAILLE_DIGITS[char]
    elsif SPECIAL_BRAILLE_TO_ENGLISH.key?(char) 
      if char == 'O..OO.'
        if number_mode
          english_output << '>'
        else
          english_output << 'o'
        end
      else
        english_output << SPECIAL_BRAILLE_TO_ENGLISH[char]
      end
      number_mode = false
    elsif BRAILLE_TO_ENGLISH.key?(char)
      letter = BRAILLE_TO_ENGLISH[char]
      if capitalize_next
        letter = letter.upcase
        capitalize_next = false
      end
      english_output << letter
      number_mode = false
    else
      raise "Unsupported Braille character: #{char}"
    end
  end

  english_output
end

def translate_english_to_braille(english_string)
  braille_output = ''
  number_mode = false

  english_string.chars.each do |char|
    if char =~ /[A-Z]/
      braille_output << ENGLISH_TO_BRAILLE['capital follows']
      braille_output << ENGLISH_TO_BRAILLE[char.downcase]
    elsif char =~ /[0-9]/
      unless number_mode
        braille_output << ENGLISH_TO_BRAILLE['number follows']
        number_mode = true
      end
      braille_output << ENGLISH_DIGITS[char]
    elsif SPECIAL_ENGLISH_TO_BRAILLE.key?(char)
      braille_output << SPECIAL_ENGLISH_TO_BRAILLE[char]
      number_mode = false
    elsif ENGLISH_TO_BRAILLE.key?(char)
      braille_output << ENGLISH_TO_BRAILLE[char]
      number_mode = false if char == ' '
    else
      raise "Unsupported character: #{char}"
    end
  end

  braille_output
end

def translate(input)
  if is_braille?(input)
    translate_braille_to_english(input)
  else
    translate_english_to_braille(input)
  end
end

input = ARGV.join(" ")
puts translate(input)