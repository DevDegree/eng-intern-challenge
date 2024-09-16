eng_to_braille = {
  'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..', 'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..',
  'i' => '.OO...', 'j' => '.OOO..', 'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.', 'p' => 'OOO.O.',
  'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.', 'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO',
  'y' => 'OO.OOO', 'z' => 'O..OOO', ' ' => '......'
}

number_to_braille = {
  '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..', '5' => 'O..O..', '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..',
  '9' => '.OO...', '0' => '.OOO..'
}

braille_to_eng = eng_to_braille.invert
braille_to_number = number_to_braille.invert

CAPITAL = '.....O'
NUMBER = '.O.OOO'
LETTER = '.O.O.O'

def eng_to_braille(input_str, eng_to_braille, number_to_braille, capital, number, letter)
  braille_output = []
  num_mode = false

  input_str.each_char do |char|
    if char.match?(/\d/)
      unless num_mode
        braille_output << number
        num_mode = true
      end
      braille_output << number_to_braille[char]
    elsif char.match?(/[a-zA-Z]/)
      if num_mode
        braille_output << letter
        num_mode = false
      end
      if char.match?(/[A-Z]/)
        braille_output << capital
        char = char.downcase
      end
      braille_output << eng_to_braille[char]
    else
      braille_output << (eng_to_braille[char] || '')
      num_mode = false
    end
  end
  braille_output.join
end

def braille_to_eng(input_str, braille_to_eng, braille_to_number, capital, number, letter)
  return "Error: Invalid Braille input" if input_str.length % 6 != 0

  english_output = []
  braille_blocks = input_str.scan(/.{6}/)
  num_mode = false
  capitalize_next = false

  braille_blocks.each do |char|
    case char
    when number
      num_mode = true
    when letter
      num_mode = false
    when capital
      capitalize_next = true
    else
      translated_char = if num_mode
                          braille_to_number[char] || braille_to_eng[char] || '?'
                        else
                          braille_to_eng[char] || '?'
                        end

      if capitalize_next && translated_char.match?(/[a-z]/i)
        translated_char = translated_char.upcase
        capitalize_next = false
      end

      english_output << translated_char
      num_mode = false if translated_char == ' ' || !translated_char.match?(/[0-9]/)
    end
  end
  english_output.join
end

def check_language(input_str)
  input_str.match?(/\A[O.]+\z/) && (input_str.length % 6 == 0)
end

def translate(input_str, eng_to_braille, number_to_braille, braille_to_eng, braille_to_number, capital, number, letter)
  if check_language(input_str)
    braille_to_eng(input_str, braille_to_eng, braille_to_number, capital, number, letter)
  else
    eng_to_braille(input_str, eng_to_braille, number_to_braille, capital, number, letter)
  end
end

if ARGV.empty?
  puts "Usage: ruby translator.rb <text_to_translate>"
  exit
end

input = ARGV.join(' ')
output = translate(input, eng_to_braille, number_to_braille, braille_to_eng, braille_to_number, CAPITAL, NUMBER, LETTER)
puts output