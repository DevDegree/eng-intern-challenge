# Translator class to convert english to braille and vice versa
class Translator
  # Constants used for translation
  BRAILLE_SPACE = '......'
  BRAILLE_CAP_FOLLOWS = '.....O'
  BRAILLE_NUM_FOLLOWS = '.O.OOO'

  BRAILLE_TO_ALPHA = {
    'O.....' => 'a',
    'O.O...' => 'b',
    'OO....' => 'c',
    'OO.O..' => 'd',
    'O..O..' => 'e',
    'OOO...' => 'f',
    'OOOO..' => 'g',
    'O.OO..' => 'h',
    '.OO...' => 'i',
    '.OOO..' => 'j',
    'O...O.' => 'k',
    'O.O.O.' => 'l',
    'OO..O.' => 'm',
    'OO.OO.' => 'n',
    'O..OO.' => 'o',
    'OOO.O.' => 'p',
    'OOOOO.' => 'q',
    'O.OOO.' => 'r',
    '.OO.O.' => 's',
    '.OOOO.' => 't',
    'O...OO' => 'u',
    'O.O.OO' => 'v',
    '.OOO.O' => 'w',
    'OO..OO' => 'x',
    'OO.OOO' => 'y',
    'O..OOO' => 'z'
  }

  BRAILLE_TO_NUM = {
    'O.....' => '1',
    'O.O...' => '2',
    'OO....' => '3',
    'OO.O..' => '4',
    'O..O..' => '5',
    'OOO...' => '6',
    'OOOO..' => '7',
    'O.OO..' => '8',
    '.OO...' => '9',
    '.OOO..' => '0'
  }

  ALPHA_TO_BRAILLE = {
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

  NUM_TO_BRAILLE = {
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

  # Translate string English->Braille or Braille->English depending on input
  def self.translate(str)
    if braille?(str)
      to_english(str)
    else
      to_braille(str)
    end
  end

  # Return true if string is braille, false otherwise
  def self.braille?(str)
    str.chars.all? { |c| ['.', 'O'].include?(c) } && (str.length % 6).zero?
  end

  # Convert braille string to english
  def self.to_english(str)
    english = ''
    is_alpha = true
    is_upcase = false

    # Iterate through string indices, moving 6 characters at a time
    0.step(str.length - 6, 6).each do |i|
      braille_char = str[i...i + 6]

      case braille_char
      when BRAILLE_CAP_FOLLOWS
        is_upcase = true
      when BRAILLE_NUM_FOLLOWS
        is_alpha = false
      when BRAILLE_SPACE
        english << ' '
        is_alpha = true
      else
        if is_alpha
          char = BRAILLE_TO_ALPHA[braille_char]
          if is_upcase
            char = char.upcase
            is_upcase = false
          end
        else
          char = BRAILLE_TO_NUM[braille_char]
        end
        english << char
      end
    end

    english
  end

  # Convert english string to braille
  def self.to_braille(str)
    braille = ''
    is_alpha = true

    str.each_char do |c|
      case c
      when /[0-9]/
        braille << BRAILLE_NUM_FOLLOWS if is_alpha
        braille << NUM_TO_BRAILLE[c]
        is_alpha = false
      when ' '
        braille << BRAILLE_SPACE
        is_alpha = true
      when c.upcase
        braille << BRAILLE_CAP_FOLLOWS
        braille << ALPHA_TO_BRAILLE[c.downcase]
      else
        braille << ALPHA_TO_BRAILLE[c]
      end
    end

    braille
  end
end

input_string = ARGV.join(' ')
print Translator.translate(input_string)
