class BrailleTranslator
  BRAILLE_MAPPING = {
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
    ' ' => '......',
    'capital' => '.....O',
    'number' => '.O.OOO'
  }

  NUMBERS = {
    'a' => '1', 'b' => '2', 'c' => '3', 'd' => '4', 'e' => '5',
    'f' => '6', 'g' => '7', 'h' => '8', 'i' => '9', 'j' => '0'
  }

  def translate(input)
    if is_braille?(input)
      braille_to_english(input)
    else
      english_to_braille(input)
    end
  end

  private

  def is_braille?(input)
    return input.match?(/\A[O.]+\z/) && input.length % 6 == 0 && input.length != 1
  end

  def english_to_braille(text)
    result = []
    number_mode = false
  
    text.each_char do |char|
      if char =~ /[A-Za-z]/
        if number_mode
          result << BRAILLE_MAPPING[' ']
          number_mode = false
        end
        result << BRAILLE_MAPPING['capital'] if char =~ /[A-Z]/
        result << BRAILLE_MAPPING[char.downcase]
      elsif char =~ /[0-9]/
        result << BRAILLE_MAPPING['number'] unless number_mode
        number_mode = true
        result << BRAILLE_MAPPING[NUMBERS.key(char)]
      else
        result << BRAILLE_MAPPING[char]
        number_mode = false
      end
    end

    result.join
  end

  def braille_to_english(braille)
    result = []
    braille_chars = braille.scan(/.{6}/)
    capitalize_next = false
    number_mode = false

    braille_chars.each do |char|
      if char == BRAILLE_MAPPING['capital']
        capitalize_next = true
      elsif char == BRAILLE_MAPPING['number']
        number_mode = true
      elsif char == BRAILLE_MAPPING[' ']
        result << ' '
        number_mode = false
      else
        letter = BRAILLE_MAPPING.key(char)
        if number_mode
          result << NUMBERS[letter]
        else
          letter = letter.upcase if capitalize_next
          result << letter
        end
        capitalize_next = false
      end
    end

    result.join
  end
end

translator = BrailleTranslator.new
input = ARGV.join(' ')
output =  translator.translate(input)
print output
