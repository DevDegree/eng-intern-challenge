BRAILLE = {
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..',
  'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..',
  'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.',
  'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.',
  'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO',
  'z' => 'O..OOO', ' ' => '......', '#' => '.O.OOO', 'upcase' => '.....O'
}

ENGLISH = BRAILLE.invert

def is_braille?(input)
  input.delete('.O ').empty?
end

def english_to_braille(input)
  result = ''
  in_number_mode = false
  input.each_char do |char|
    if char == ' '
      in_number_mode = false
      result += BRAILLE[char]
    elsif char.match?(/[1-9]/)
      result += BRAILLE['#'] unless in_number_mode
      in_number_mode = true
      result += BRAILLE[('a'.ord + char.to_i - 1).chr]
    elsif char == '0'
      result += BRAILLE['#'] unless in_number_mode
      in_number_mode = true
      result += BRAILLE['j']
    else
      in_number_mode = false
      result += BRAILLE['upcase'] if char.match?(/[A-Z]/)
      result += BRAILLE[char.downcase]
    end
  end
  result
end

def braille_to_english(input)
  result = ''
  in_number_mode = false
  capitalize_next = false
  input.scan(/.{6}/).each do |char|
    if char == BRAILLE['#']
      in_number_mode = true
    elsif char == BRAILLE['upcase']
      capitalize_next = true
    elsif char == BRAILLE[' ']
      result += ' '
      in_number_mode = false
    else
      letter = ENGLISH[char]
      if in_number_mode
        number = (letter.ord - 'a'.ord + 1).to_s
        number = '0' if number == '10'
        result += number
      else
        letter = letter.upcase if capitalize_next
        result += letter
        capitalize_next = false
      end
    end
  end
  result
end

def main
  input = ARGV.join(" ")
  puts is_braille?(input) ? braille_to_english(input) : english_to_braille(input)
end

main