require_relative './braille_english_dictionary'

# Translator class to convert english to braille and vice versa
class Translator
  include BrailleEnglishDictionary

  class << self
    # Translate string English->Braille or Braille->English depending on input
    def translate(str)
      if braille?(str)
        to_english(str)
      else
        to_braille(str)
      end
    end

    private

    # Return true if string is braille, false otherwise
    def braille?(str)
      str.chars.all? { |c| ['.', 'O'].include?(c) }
    end

    # Convert braille string to english
    def to_english(str)
      english = ''
      is_alpha = true
      is_upcase = false

      # Iterate through string indices, moving 6 characters at a time
      i = 0
      while i < str.length
        braille_char = str[i...i + 6]

        case braille_char
        when BrailleEnglishDictionary::BRAILLE_CAP_FOLLOWS
          is_upcase = true
        when BrailleEnglishDictionary::BRAILLE_NUM_FOLLOWS
          is_alpha = false
        when BrailleEnglishDictionary::BRAILLE_SPACE
          english << ' '
          is_alpha = true
        else
          english << braille_char_to_eng(braille_char, is_alpha, is_upcase)
          is_upcase = false
        end

        i += 6
      end

      english
    end

    def braille_char_to_eng(braille_char, is_alpha, is_upcase)
      char = if is_alpha
               BrailleEnglishDictionary::BRAILLE_TO_ALPHA[braille_char]
             else
               BrailleEnglishDictionary::BRAILLE_TO_NUM[braille_char]
             end

      raise ArgumentError, "Invalid braille character '#{braille_char}'" if char.nil?

      char = char.upcase if is_upcase
      char
    end

    # Convert english string to braille
    def to_braille(str)
      braille = ''
      is_alpha = true

      str.each_char do |c|
        case c
        when /[0-9]/
          braille << BrailleEnglishDictionary::BRAILLE_NUM_FOLLOWS if is_alpha
          braille << BrailleEnglishDictionary::NUM_TO_BRAILLE[c]
          is_alpha = false
        when ' '
          braille << BrailleEnglishDictionary::BRAILLE_SPACE
          is_alpha = true
        else
          braille << BrailleEnglishDictionary::BRAILLE_CAP_FOLLOWS if c == c.upcase
          char = BrailleEnglishDictionary::ALPHA_TO_BRAILLE[c.downcase]

          raise ArgumentError, "Invalid character '#{c}'" if char.nil?

          braille << char
        end
      end

      braille
    end
  end
end

input_string = ARGV.join(' ')
print Translator.translate(input_string)
