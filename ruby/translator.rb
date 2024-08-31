# frozen_string_literal: false

# Translator
class Translator
  ENGLISH = ("a".."z").to_a + ("0".."9").to_a + [" "]
  ENGLISH_NUMS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

  BRAILLE = [
    "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..",
    ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.",
    "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO",
    ".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", "......"]

  BRAILLE_NUMS = [".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...",
    "OOOO..", "O.OO..", ".OO..."]
  SPACE = "......"
  CAPITAL_FOLLOWS = ".....O"
  NUMBERS_FOLLOW = ".O.OOO"

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

  # input: arg array; output: array with items of length 6
  def self.arg_to_braille(array)
    result = []
    array&.each do |item|
      result.push(item.chars.each_slice(6).map(&:join))
    end
    result.flatten!
    result
  end

  def self.translate(arg)
    if braille?(arg)
      braille_to_english(arg)
    else
      english_to_braille(arg)
    end
  end
  # input arg array; output english string
  # ["O.....", "O.O..."]
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
        idx = BRAILLE.find_index(symbol)
        alphabet = ENGLISH[idx]
        if symbol == SPACE
          number = false
        end
        if capital
          result.push(alphabet.upcase)
          capital = false
        elsif number
          result.push(ENGLISH_NUMS[BRAILLE_NUMS.find_index(symbol)])
        else
          result.push(ENGLISH[idx])
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
        english_idx = ENGLISH.find_index(char.downcase)
        braille_symbol = BRAILLE[english_idx]
        braille << CAPITAL_FOLLOWS
        braille << braille_symbol
      elsif char == ' '
        braille << SPACE
        number = false
      elsif /[0-9]/.match(char)
        braille << NUMBERS_FOLLOW if number == false
        number = true
        english_idx = ENGLISH.find_index(char.downcase)
        braille_symbol = BRAILLE[english_idx]
        braille << braille_symbol
      elsif /[a-z]/.match(char)
        english_idx = ENGLISH.find_index(char)
        braille_symbol = BRAILLE[english_idx]
        braille << braille_symbol
      end
    end
    braille
  end
end

puts Translator.translate(ARGV)
