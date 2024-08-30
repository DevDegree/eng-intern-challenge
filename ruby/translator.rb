# Braille Translator
# author: Andressa Machado
# date: 30-Aug-2.24

class Translator
  private
  attr_reader :format, :input

  # Braille alphabet dictionary
  BRAILLE_ALPHABET = {
    'O.....' => 'a', 'O.O...' => 'b', 'OO....' => 'c',
    'OO.O..' => 'd', 'O..O..' => 'e', 'OOO...' => 'f',
    'OOOO..' => 'g', 'O.OO..' => 'h', '.OO...' => 'i',
    '.OOO..' => 'j', 'O...O.' => 'k', 'O.O.O.' => 'l',
    'OO..O.' => 'm', 'OO.OO.' => 'n', 'O..OO.' => 'o',
    'OOO.O.' => 'p', 'OOOOO.' => 'q', 'O.OOO.' => 'r',
    '.OO.O.' => 's', '.OOOO.' => 't', 'O...OO' => 'u',
    'O.O.OO' => 'v', '.OOO.O' => 'w', 'OO..OO' => 'x',
    'OO.OOO' => 'y', 'O..OOO' => 'z', '......' => ' '
  }.freeze

  # Braille digits dictionary
  BRAILLE_DIGITS = {
    '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....',
    '4' => 'OO.O..', '5' => 'O..O..', '6' => 'OOO...',
    '7' => 'OOOO..', '8' => 'O.OO..', '9' => '.OO...',
    '0' => '.OOO..'
  }.freeze

  # Braille punctuation dictionary
  BRAILLE_PUNCTUATION = {
    '.' => '..OO.O', ',' => '..O...', '?' => '..O.OO',
    '!' => '..OOO.', ':' => '..OO..', ';' => '..O.O.',
    '-' => '....OO', '/' => '.O..O.', '<' => '.OO..O',
    '>' => 'O..OO.', '(' => 'O.O..O', ')' => '.O.OO.',
    ' ' => '......'
  }.freeze

  # Braille rules dictionary containing sentence building directions
  BRAILLE_RULES = {
    '.....O' => 'uppercase', '.O...O' => 'decimal', '.O.OOO' => 'number'
  }.freeze

  # Method to check if it is a braille or text input
  def check_format(input)
    input.match?(/[A-NP-Z0-9]/i) ? 'text' : 'braille'
  end

  # Method to prepare input for translation
  def prepare_input(input)
    # if braille, slice the input into an array of strings of 6 characters long
    # if text, split the input into an array of characters
    format == 'braille' ? input.scan(/.{6}/) : input.chars
  end

  # Method to translate braille to text
  def braille_to_text
    has_uppercase = false

    # go through the input array and translate each sequence to respective character
    # input.map {|sequence| BRAILLE_ALPHABET[sequence]}.join
    input.map.with_index {|sequence, index|
    # if the sequence is a rule, check the rule and translate the next sequence accordingly
    # otherwise, translate the sequence to a character
    if (BRAILLE_RULES[sequence])
      case BRAILLE_RULES[sequence]
      when 'uppercase'
        has_uppercase = true
        BRAILLE_ALPHABET[input[index + 1]].upcase
      end
    else
      has_uppercase ? BRAILLE_ALPHABET[input[index + 1]] : BRAILLE_ALPHABET[input[index]]
    end
    }.join
  end

  public
  def initialize(input)
    @format = check_format(input)
    @input = prepare_input(input)
  end

  def translate
    format == 'braille' ? braille_to_text : text_to_braille
  end
end

translator = Translator.new('O.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O......OOO.O..')
translator.translate
