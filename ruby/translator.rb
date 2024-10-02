BRAILLE_MAP = {
  'a' => 0b100000, 'b' => 0b101000, 'c' => 0b110000, 'd' => 0b110100, 'e' => 0b100100,
  'f' => 0b111000, 'g' => 0b111100, 'h' => 0b101100, 'i' => 0b011000, 'j' => 0b011100,
  'k' => 0b100010, 'l' => 0b101010, 'm' => 0b110010, 'n' => 0b110110, 'o' => 0b100110,
  'p' => 0b111010, 'q' => 0b111110, 'r' => 0b101110, 's' => 0b011010, 't' => 0b011110,
  'u' => 0b100011, 'v' => 0b101011, 'w' => 0b011101, 'x' => 0b110011, 'y' => 0b110111,
  'z' => 0b100111,
  '1' => 0b100000, '2' => 0b101000, '3' => 0b110000, '4' => 0b110100, '5' => 0b100100,
  '6' => 0b111000, '7' => 0b111100, '8' => 0b101100, '9' => 0b011000, '0' => 0b011100,
  '.' => 0b001101, ',' => 0b001000, '?' => 0b001011, '!' => 0b001110, '-' => 0b000011,
  ':' => 0b001100, ';' => 0b001010, '(' => 0b101001, ')' => 0b010110, '/' => 0b010010,
  "'" => 0b000010, '"' => 0b001010, '*' => 0b000110, '@' => 0b000101, '&' => 0b101101,
  ' ' => 0b000000,
  'capital' => 0b000001,
  'number' => 0b010111,
  'decimal' => 0b000101
}

BRAILLE_REVERSE_MAP = BRAILLE_MAP.invert

def translate_to_braille(text)
  translated = []
  number_mode = false

  text.each_char do |char|
    if char == ' '
      translated << BRAILLE_MAP[' ']
      number_mode = false
    elsif char =~ /\d/
      translated << BRAILLE_MAP['number'] unless number_mode
      translated << BRAILLE_MAP[char]
      number_mode = true
    elsif char == '.'
      if number_mode
        translated << BRAILLE_MAP['decimal']
      else
        translated << BRAILLE_MAP['.']
      end
      number_mode = false
    else
      number_mode = false
      translated << BRAILLE_MAP['capital'] if char =~ /[A-Z]/
      translated << BRAILLE_MAP[char.downcase]
    end
  end

  translated
end

def translate_to_english(braille_binary)
  translated = []
  number_mode = false
  capital_mode = false

  braille_binary.each do |braille_char|
    if braille_char == BRAILLE_MAP[' ']
      translated << ' '
      number_mode = false
      capital_mode = false
    elsif braille_char == BRAILLE_MAP['number']
      number_mode = true
    elsif braille_char == BRAILLE_MAP['decimal']
      translated << '.'
    elsif braille_char == BRAILLE_MAP['capital']
      capital_mode = true
    else
      if number_mode
        char = BRAILLE_REVERSE_MAP[braille_char]
        if 'abcdefghij'.include?(char)
          digit = (char.ord - 'a'.ord + 1) % 10
          translated << digit.to_s
        else
          translated << '?'
        end
      else
        char = BRAILLE_REVERSE_MAP[braille_char]
        char = char.upcase if capital_mode
        translated << char
        capital_mode = false
      end
    end
  end

  translated.join
end

def binary_to_braille_dots(binary)
  (0..5).map { |i| binary[5 - i] == 1 ? 'O' : '.' }.join
end

def braille_dots_to_binary(dots)
  dots.chars.each_with_index.sum { |char, i| char == 'O' ? 1 << (5 - i) : 0 }
end

input = ARGV.join(' ')

if input.match?(/^[O.]+$/)
  braille_binary = input.scan(/.{6}/).map { |dots| braille_dots_to_binary(dots) }
  puts translate_to_english(braille_binary)
else
  braille_binary = translate_to_braille(input)
  puts braille_binary.map { |char| binary_to_braille_dots(char) }.join
end