BRAILLE_MAP = {
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..',
  'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..',
  'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.',
  'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.',
  'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO',
  'z' => 'O..OOO', '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..',
  '5' => 'O..O..', '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..', '9' => '.OO...',
  '0' => '.OOO..', '.' => '..OO.O', ',' => '..O...', '?' => '..O.O.', '!' => '..OO..',
  ':' => '..OO.O', ';' => '..O.OO', '-' => '..O.OO', '/' => '.O..O.', '<' => '..OO.O',
  '>' => '..OOOO', '(' => '.O..OO', ')' => '..O.O.', ' ' => '......', 'capital' => '.....O',
  'number' => '.O.OOO'
}

ENGLISH_MAP = BRAILLE_MAP.invert

def is_braille?(text)
  text.match?(/\A[.O]+\z/) && text.length % 6 == 0
end

def convert(input)
  is_braille?(input) ? braille_to_english(input) : english_to_braille(input)
end

def english_to_braille(text)
  output = ""
  is_numeric = false

  text.each_char do |ch|
    if ch =~ /[A-Z]/
      output += BRAILLE_MAP['capital'] + BRAILLE_MAP[ch.downcase]
      is_numeric = false
    elsif ch =~ /[0-9]/
      output += BRAILLE_MAP['number'] unless is_numeric
      output += BRAILLE_MAP[ch]
      is_numeric = true
    elsif BRAILLE_MAP.key?(ch)
      output += BRAILLE_MAP[ch]
      is_numeric = false
    else
      raise "Unexpected character: #{ch}"
    end
  end

  output
end

def braille_to_english(braille)
  output = ""
  is_capital = false
  is_numeric = false

  braille.scan(/.{6}/).each do |braille_ch|
    if braille_ch == BRAILLE_MAP['capital']
      is_capital = true
    elsif braille_ch == BRAILLE_MAP['number']
      is_numeric = true
    elsif ENGLISH_MAP.key?(braille_ch)
      char = ENGLISH_MAP[braille_ch]
      output += is_capital ? char.upcase : char
      is_capital = false
      is_numeric = false
    end
  end

  output
end

if __FILE__ == $PROGRAM_NAME
  input_text = ARGV.join(' ')
  puts convert(input_text)
end
