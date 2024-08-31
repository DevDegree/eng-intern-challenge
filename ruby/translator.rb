# frozen_string_literal: false

# Translator:
class Translator
  @english = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                     "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
  @english_nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  @braille = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..",
  ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.",
  "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO",
  ".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", "......"]

  @braille_nums = [".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO..."]
  @capital_follows = ".....O"
  @space = "......"
  @number_follows = ".O.OOO"

  @braille_collection = @braille.push(@capital_follows, @number_follows)
  # attr_reader :@english, :@braille, :@capital_follows, :@number_follows

  # input: arg array; output: bool
  def self.braille?(arg)
    result = arg_to_braille(arg)
    result&.each do |item|
      return false unless @braille_collection.include?(item)
    end
    return false if result.nil? || result == []

    true
  end

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
    capital = false
    number = false

    symbols = arg_to_braille(data)
    symbols.each do |symbol|
      if symbol == @capital_follows
        capital = true
      elsif symbol == @number_follows
        number = true
      else
        idx = @braille.find_index(symbol)
        alphabet = @english[idx]
        if symbol == @space
          number = false
        end
        if capital
          result.push(alphabet.upcase)
          capital = false
        elsif number
          result.push(@english_nums[@braille_nums.find_index(symbol)])
        else
          result.push(@english[idx])
        end

      end
    end
    result.join('')
  end

  # input arg array; output braille string
  def self.english_to_braille(data)
    braille = ''
    string = data.join(' ')

    number = false
    string.each_char do |char|
      if /[A-Z]/.match(char)
        english_idx = @english.find_index(char.downcase)
        braille_symbol = @braille[english_idx]
        braille << @capital_follows
        braille << braille_symbol
      elsif char == ' '
        braille << @space
        number = false
      elsif /[0-9]/.match(char)
        braille << @number_follows if number == false
        number = true
        english_idx = @english.find_index(char.downcase)
        braille_symbol = @braille[english_idx]
        braille << braille_symbol
      elsif /[a-z]/.match(char)
        english_idx = @english.find_index(char)
        braille_symbol = @braille[english_idx]
        braille << braille_symbol
      end
    end
    braille
  end
end

puts Translator.translate(ARGV)
