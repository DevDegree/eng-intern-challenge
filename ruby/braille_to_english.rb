require_relative 'constants'

class BrailleToEnglish
  def translate(braille)
    english = ''
    i = 0
    capitalize_next = false
    number_mode = false

    while i < braille.length
      char = braille[i, 6]
      if char == CAPITAL_FOLLOWS
        capitalize_next = true
      elsif char == NUMBERS_FOLLOW
        number_mode = true
      elsif char == '......'
        english += ' '
        number_mode = false
      else
        if number_mode
          english += BRAILLE_NUMBERS_MAP[char].to_s
        else
          letter = BRAILLE_ALPHABET_MAP[char].to_s
          letter.upcase! if capitalize_next
          english += letter
        end
        capitalize_next = false
      end
      i += 6
    end
    english
  end
end
