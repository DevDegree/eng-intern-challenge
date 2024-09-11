require_relative 'constants'

class EnglishToBraille
  def translate(text)
    braille = ''

    mode = :alphabet
    text.chars do |char|
      braille += if char.match?(/[A-Z]/)
                   mode = :alphabet
                   CAPITAL_FOLLOWS + ALPHABET_BRAILLE_MAP[char.downcase.to_sym]
                 elsif char.match?(/\d/)
                   if mode == :alphabet
                     mode = :number
                     NUMBERS_FOLLOW + NUMBERS_BRAILLE_MAP[char.to_sym]
                   else
                     NUMBERS_BRAILLE_MAP[char.to_sym]
                   end
                 else
                   mode = :alphabet
                   ALPHABET_BRAILLE_MAP[char.to_sym]
                 end
    end
    braille
  end
end
