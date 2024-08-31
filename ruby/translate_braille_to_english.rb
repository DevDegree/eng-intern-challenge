require_relative "constants"

def translate_braille_to_english(braille_string)
  if braille_string.length % 6 != 0
    puts "Braille input length must be divisible by 6"
    return
  end

  result = ""
  is_number = false
  index = 0

  while index < braille_string.length
    braille_symbol = braille_string[index, 6]

    if !BRAILLE_TO_ENGLISH_DICT.key?(braille_symbol) &&
      braille_symbol != BRAILLE_CAPITAL_FOLLOWS &&
      braille_symbol != BRAILLE_NUMBER_FOLLOWS
      puts "#{braille_symbol} is not valid braille"
      return
    end

    case braille_symbol
    when BRAILLE_CAPITAL_FOLLOWS
      index += 6
      braille_symbol = braille_string[index, 6]
      result += BRAILLE_TO_ENGLISH_DICT[braille_symbol].upcase
    when BRAILLE_NUMBER_FOLLOWS
      is_number = true
    when "......"
      is_number = false
      result += BRAILLE_TO_ENGLISH_DICT[braille_symbol]
    else
      result += is_number ? BRAILLE_TO_NUMBERS_DICT[braille_symbol] : BRAILLE_TO_ENGLISH_DICT[braille_symbol]
    end

    index += 6
  end

  return result
end
