# frozen_string_literal: true

# create the hash of braille to english
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

# create the hash of english to braille numbers
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

# create the hash of braille to english numbers
ENGLISH_NUMBERS_HASH = BRAILLE_NUMBERS_HASH.invert.freeze
# create the hash of english to braille
ENGLISH_HASH = BRAILLE_HASH.invert.freeze

# Create an evaluator to determine if english or braille
def braille_checker?(input_string)
  input_string.include?('.')
end

# If english, translate to braille
def english_translator(input_string)
  number_follows = false
  capital_follows = false

  braille_translation = input_string.chars.map do |character|
    number_follows = false if character == ' '

    if character == character.upcase && character.match(/[a-zA-Z]/)
      capital_follows = true
      character = character.downcase
    end

    if character.match(/\d/) && !number_follows
      number_follows = true
      ".O.OOO#{BRAILLE_NUMBERS_HASH[character]}"
    elsif character.match(/\d/) && number_follows
      BRAILLE_NUMBERS_HASH[character]
    elsif capital_follows
      capital_follows = false
      ".....O#{BRAILLE_HASH[character]}"
    else
      BRAILLE_HASH[character]
    end
  end

  braille_translation.join
end

# If braille, translate to english
def braille_translator(input_string)
  # MAKE SURE TO REMEMBER to account for number follows and capital letter follows
  number_follows = false
  capital_follows = false
  braille_characters = input_string.scan(/.{6}/)

  english_translation = braille_characters.map do |braille_character|
    if braille_character == '.....O'
      capital_follows = true
      next
    end

    if braille_character == '.O.OOO'
      number_follows = true
      next
    end

    number_follows = false if braille_character == '......'

    if capital_follows
      capital_follows = false
      BRAILLE_HASH.key(braille_character).upcase
    elsif number_follows
      BRAILLE_NUMBERS_HASH.key(braille_character)
    else
      BRAILLE_HASH.key(braille_character)
    end
  end

  english_translation.join
end

# Program must work at runtime
def run(input_string)
  puts braille_checker?(input_string) ? braille_translator(input_string) : english_translator(input_string)
end

run(ARGV.join(' '))
