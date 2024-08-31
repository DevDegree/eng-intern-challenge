require_relative "constants"

def translate_english_to_braille(english_string_array)
  result = ""
  number_follows_added = false

  english_string_array.each_with_index do |word, word_index|
    word.each_char do |char|
      case char
      when 'a'..'z'
        result += ENGLISH_TO_BRAILLE_DICT[char]
      when 'A'..'Z'
        result += BRAILLE_CAPITAL_FOLLOWS
        result += ENGLISH_TO_BRAILLE_DICT[char.downcase]
      when '0'..'9'
        if !number_follows_added
          result += BRAILLE_NUMBER_FOLLOWS
          number_follows_added = true
        end

        result += NUMBERS_TO_BRAILLE_DICT[char]
      else
        puts "Input must only include English letters a-z, numbers 0-9, or spaces"
        return
      end
    end

    if word_index < english_string_array.length - 1
      result += ENGLISH_TO_BRAILLE_DICT[" "]
      number_follows_added = false
    end
  end

  result
end
