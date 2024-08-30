# Braille Translator
# author: Andressa Machado
# date: 30-Aug-2.24

class Translator
  private
  attr_reader :format, :input

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

  BRAILLE_DIGITS = {
    'O.....' => '1', 'O.O...' => '2', 'OO....' => '3',
    'OO.O..' => '4', 'O..O..' => '5', 'OOO...' => '6',
    'OOOO..' => '7', 'O.OO..' => '8', '.OO...' => '9',
    '.OOO..' => '0'
  }.freeze

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
    # flag used to indicate that the next sequences are numbers or
    # when set to false, indicate that next sequences are letters
    is_number = false
    index = 0

    # go through the input array and translate each sequence to respective character
    input.reduce([]) do |result, sequence|
      # if the sequence is a rule, check the rule and translate the next sequence accordingly
      # otherwise, translate the sequence to a character
      if (BRAILLE_RULES[sequence])
        case BRAILLE_RULES[sequence]
        when 'uppercase'
          next_sequence = input[index += 1]
          result << BRAILLE_ALPHABET[next_sequence].upcase
        when 'number'
          is_number = true
          result << BRAILLE_DIGITS[input[index]]
        end
      else
        if (is_number)
          result << BRAILLE_DIGITS[input[index]]
        else
          result << BRAILLE_ALPHABET[input[index]]
        end
      end
      index += 1
      result
    end.join
  end

  # Method to translate text to braille
  def text_to_braille
    # variable to store the result of the translation
    result = []

    # go through the input array and translate each char to respective sequence
    input.each_with_index do |char, index|
      # if char is a uppercase letter, add the uppercase rule to the result array
      if (char.match?((/[A-NP-Z]/)))
        result.insert(index, BRAILLE_RULES.key('uppercase'))
      end
      # continue translation of the char to the respective sequence
      index += 1
      result.insert(index, BRAILLE_ALPHABET.key(char.downcase))
    end
      result.join
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

 # translator = Translator.new('.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..')
 # translator = Translator.new('.O.OOOOO.O..O.O...')
 # translator = Translator.new('.....OO.....O.O...OO...........O.OOOO.....O.O...OO....')
 # translator = Translator.new('Hello world')
puts translator.translate
