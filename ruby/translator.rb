# frozen_string_literal: false

# Translator
class Translator
  ENGLISH_NUMS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  BRAILLE_NUMS = [".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...",
    "OOOO..", "O.OO..", ".OO..."]
  SPACE = "......"
  CAPITAL_FOLLOWS = ".....O"
  NUMBERS_FOLLOW = ".O.OOO"

  ENGLISH = ('a'..'z').to_a + [" "]
  BRAILLE = [
      "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..",
      ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.",
      "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO","......"]

  # ALPHABET HASHMAPS + SPACE
  ENGLISH_TO_BRAILLE_MAP = ENGLISH.zip(BRAILLE).to_h
  BRAILLE_TO_ENGLISH_MAP = ENGLISH_TO_BRAILLE_MAP.invert

  # NUM HASH MAPS
  ENG_BRAILLE_NUM = ENGLISH_NUMS.zip(BRAILLE_NUMS).to_h
  BRAILLE_ENG_NUM = BRAILLE_NUMS.zip(ENGLISH_NUMS).to_h

  BRAILLE_COLLECTION = BRAILLE.push(CAPITAL_FOLLOWS, NUMBERS_FOLLOW)

  # input: arg array; output: bool
  def self.braille?(arg)
    result = arg_to_braille(arg)
    result&.each do |item|
      return false unless BRAILLE_COLLECTION.include?(item)
    end
    return false if result.nil? || result == []

    true
  end

  # input: arg array; output: array with items of length 6 or nil
  def self.arg_to_braille(array)
    return if array.nil?

    return unless (array.join.length % 6).zero?

    array.join.scan(/.{6}/)
  end

  def self.translate(arg)
    if braille?(arg)
      braille_to_english(arg)
    else
      english_to_braille(arg)
    end
  end

  # input arg array; output english string
  def self.braille_to_english(data)
    result = []
    symbols = arg_to_braille(data)
    capital = false
    number = false

    symbols.each do |symbol|
      if symbol == CAPITAL_FOLLOWS
        capital = true
      elsif symbol == NUMBERS_FOLLOW
        number = true
      else
        if symbol == SPACE
          number = false
        end
        if capital
          result.push(BRAILLE_TO_ENGLISH_MAP[symbol].upcase)
          capital = false
        elsif number
          result.push(BRAILLE_ENG_NUM[symbol])
        else
          result.push(BRAILLE_TO_ENGLISH_MAP[symbol])
        end
      end
    end
    result.join
  end

  # input arg array; output braille string
  def self.english_to_braille(data)
    braille = ''
    string = data.join(' ')

    number = false
    string.each_char do |char|
      if /[A-Z]/.match(char)
        braille << CAPITAL_FOLLOWS
        braille << ENGLISH_TO_BRAILLE_MAP[char.downcase]
      elsif char == ' '
        braille << SPACE
        number = false
      elsif /[0-9]/.match(char)
        braille << NUMBERS_FOLLOW if number == false
        number = true
        braille << ENG_BRAILLE_NUM[char]
      elsif /[a-z]/.match(char)
        braille << ENGLISH_TO_BRAILLE_MAP[char]
      end
    end
    braille
  end
end

puts Translator.translate(ARGV)
