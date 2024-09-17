ALPHABET_BRAILLE = {
  a: 'O.....', b: 'O.O...', c: 'OO....', d: 'OO.O..', e: 'O..O..',
  f: 'OOO...', g: 'OOOO..', h: 'O.OO..', i: '.OO...', j: '.OOO..',
  k: 'O...O.', l: 'O.O.O.', m: 'OO..O.', n: 'OO.OO.', o: 'O..OO.',
  p: 'OOO.O.', q: 'OOOOO.', r: 'O.OOO.', s: '.OO.O.', t: '.OOOO.',
  u: 'O...OO', v: 'O.O.OO', w: '.OOO.O', x: 'OO..OO', y: 'OO.OOO',
  z: 'O..OOO',
  :'.' => '.O.O.O', :',' => 'O.....', :'!' => 'OOO...', :'?' => '.O.OO.',
  :'-' => 'O....O', :':' => 'OO.O..', :';' => 'O.O...', :"'" => 'O....O',
  :' ' => '......', :capital => '.....O', :number => '.O.OOO'
}

BRAILLE_ALPHABET = {}
SPECIAL_CHARS = {}

ALPHABET_BRAILLE.each do |k, v|
  if k.to_s.match?(/[a-zA-Z]/)
    BRAILLE_ALPHABET[v] = k.to_s
  end
  if ['.', ',', '-', ':', ';', '!', '?', "'"].include?(k.to_s)
    SPECIAL_CHARS[v] = k.to_s
  end
end

# number -> braille
NUMBER_DICT = {
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

def translate_to_braille(text)
  solution = []
  number_mode = false # store if in number mode
  text.each_char do |char|
    if char =~ /[A-Z]/
      solution << ALPHABET_BRAILLE[:capital]
      solution << ALPHABET_BRAILLE[char.downcase.to_sym]
      number_mode = false
    elsif char =~ /\d/
      unless number_mode
        solution << ALPHABET_BRAILLE[:number]
        number_mode = true
      end
      solution << NUMBER_DICT[char]
    else
      if number_mode && char == ' '
        number_mode = false
      end
      solution << (ALPHABET_BRAILLE[char.to_sym] || '......')
    end
  end
  solution.join
end

def translate_to_english(braille)
  solution = []
  check_capital = false
  number_mode = false
  braille_buffer = ''
  braille.each_char do |char|
    braille_buffer += char
    if braille_buffer.length == 6
      if braille_buffer == ALPHABET_BRAILLE[:capital]
        check_capital = true
      elsif braille_buffer == ALPHABET_BRAILLE[:number]
        number_mode = true
      elsif braille_buffer == '......'
        solution << ' '
        number_mode = false
      else
        if number_mode
          char = NUMBER_DICT.key(braille_buffer) || ''
        else
          char = BRAILLE_ALPHABET[braille_buffer] || SPECIAL_CHARS[braille_buffer] || ''
        end
        if check_capital
          char = char.upcase
          check_capital = false
        end
        solution << char
      end
      braille_buffer = ''
    end
  end
  solution.join
end

def main
  input_str = ARGV.join(' ')
  
  if is_braille(input_str.gsub(' ', ''))
    puts translate_to_english(input_str)
  else
    puts translate_to_braille(input_str)
  end
end

def is_braille(text)
  # check if the input consists only of 'O' and '.' characters
  all_valid_chars = text.chars.all? { |c| c == 'O' || c == '.' }
  
  # check if the input length is a multiple of 6 (Braille characters are 6 dots)
  valid_length = text.length % 6 == 0
  
  # the input is Braille if it only contains 'O' and '.' AND its length is a multiple of 6
  all_valid_chars && valid_length
end

main
