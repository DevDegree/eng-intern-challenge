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
end
