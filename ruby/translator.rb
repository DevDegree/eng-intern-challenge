# frozen_string_literal: true

class Translator
  BRAILLE_CHAR_SIZE = 6

  BRAILLE_SYM_SPACE = '......'
  BRAILLE_SYM_CAPITAL = '.....O'
  BRAILLE_SYM_NUMBER = '.O.OOO'

  TRANSLATOR_MAP_CHARACTERS = Hash[
    'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..',
    'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..',
    'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.',
    'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.',
    'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO',
    'z' => 'O..OOO', ' ' => BRAILLE_SYM_SPACE
].freeze

  TRANSLATOR_MAP_NUMBERS = Hash[
    '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..', '5' => 'O..O..',
    '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..', '9' => '.OO...', '0' => '.OOO..'
].freeze

  class << self
    def translate(input)
      return translate_braille(input) if input.match(/\A[O.]*\z/)

      translate_english(input)
    end

    private

    # Translation from braille to english
    def translate_braille(braille_text)
      braille_map_characters = TRANSLATOR_MAP_CHARACTERS.invert.freeze
      braille_map_numbers = TRANSLATOR_MAP_NUMBERS.invert.freeze

      translation = String.new
      next_char_type = nil

      (0...braille_text.length).step(BRAILLE_CHAR_SIZE).each do |sequence_index|
        current_braille_sequence = braille_text[sequence_index...sequence_index + BRAILLE_CHAR_SIZE]

        case current_braille_sequence
        when BRAILLE_SYM_CAPITAL
          next_char_type = :capital
        when BRAILLE_SYM_NUMBER
          next_char_type = :number
        else
          next_char, next_char_type = translate_braille_character(
            current_braille_sequence,
            next_char_type,
            braille_map_numbers,
            braille_map_characters
          )

          translation << next_char unless next_char.nil?
        end
      end

      translation
    end

    def translate_braille_character(
      current_braille_sequence,
      next_char_type,
      braille_map_numbers,
      braille_map_characters
    )
      next_char = case next_char_type
      when :number
        if current_braille_sequence == BRAILLE_SYM_SPACE
          next_char_type = nil
          ' '
        else
          braille_map_numbers[current_braille_sequence]
        end
      when :capital
        next_char_type = nil
        braille_map_characters[current_braille_sequence]&.upcase
      else
        braille_map_characters[current_braille_sequence]
      end

      [next_char, next_char_type]
    end

    # Translate from english to braille
    def translate_english(english_text)
      translation = String.new
      reading_number = false

      english_text.each_char do |next_char|
        reading_number = false if next_char == ' '

        translated_chars = if reading_number
          TRANSLATOR_MAP_NUMBERS[next_char]
        elsif next_char >= 'A' && next_char <= 'Z'
          BRAILLE_SYM_CAPITAL + TRANSLATOR_MAP_CHARACTERS[next_char.downcase]
        elsif next_char >= '0' && next_char <= '9'
          reading_number = true
          BRAILLE_SYM_NUMBER + TRANSLATOR_MAP_NUMBERS[next_char]
        else
          TRANSLATOR_MAP_CHARACTERS[next_char.downcase]
        end

        translation << translated_chars unless translated_chars.nil?
      end

      translation
    end
  end
end

input = ARGV.join(' ')
puts Translator.translate(input)
