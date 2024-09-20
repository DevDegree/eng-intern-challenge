# frozen_string_literal: true

BRAILLE_HASH = {
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
  ' ' => '......'
}.freeze

BRAILLE_NUMBERS_HASH = {
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
}.freeze

ENGLISH_NUMBERS_HASH = BRAILLE_NUMBERS_HASH.invert.freeze

ENGLISH_HASH = BRAILLE_HASH.invert.freeze

# Create an evaluator to determine if input is english or braille
def braille_checker?(input_string)
  # Specs indicate that braille will include periods and english won't
  input_string.include?('.')
end

# If english, translate input to braille
def english_translator(input_string)
  # track capital letters and numbers
  number_follows = false
  capital_follows = false

  braille_translation = input_string.chars.map do |character|
    # numbers persist until first space
    number_follows = false if character == ' '

    # if character is a capital letter, set flag and downcase
    if character.match(/[A-Z]/)
      capital_follows = true
      character = character.downcase
    end

    # if character is a number, set flag or add number braille
    if character.match(/\d/)
      if number_follows
        BRAILLE_NUMBERS_HASH[character]
      else
        number_follows = true
        ".O.OOO#{BRAILLE_NUMBERS_HASH[character]}"
      end
      # add capital_follows + braille character
    elsif capital_follows
      capital_follows = false
      ".....O#{BRAILLE_HASH[character]}"
    else
      # add braille characters and spaces
      BRAILLE_HASH[character]
    end
  end

  # create the final output string
  braille_translation.join
end

# If braille, translate to english
def braille_translator(input_string)
  # track capital letters and numbers
  number_follows = false
  capital_follows = false

  # separate braille characters
  braille_characters = input_string.scan(/.{6}/)

  english_translation = braille_characters.map do |braille_character|
    # if braille character is a space, set flag and skip itereation
    if braille_character == '.....O'
      capital_follows = true
      next
    end

    # evaluate end of numbers
    number_follows = false if braille_character == '......'

    # if braille character is a number, set flag and skip iteration
    if braille_character == '.O.OOO'
      number_follows = true
      next
    end

    # if capital letter, set flag to false and return upcase
    if capital_follows
      capital_follows = false
      BRAILLE_HASH.key(braille_character).upcase
    # if number follows, return number
    elsif number_follows
      BRAILLE_NUMBERS_HASH.key(braille_character)
    else
      # add english characters and spaces
      BRAILLE_HASH.key(braille_character)
    end
  end

  # create the ifnal output string
  english_translation.join
end

# Program must work at runtime
def run(input_string)
  # evaluate type of string and call appropriate translator, then output
  puts braille_checker?(input_string) ? braille_translator(input_string) : english_translator(input_string)
end

# Run the program
run(ARGV.join(' '))
