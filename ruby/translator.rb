require_relative './braille_english_dictionary'

# Translator class to convert english to braille and vice versa
class Translator
  include BrailleEnglishDictionary

  # Translate string English->Braille or Braille->English depending on input
  def self.translate(str)
    if braille?(str)
      to_english(str)
    else
      to_braille(str)
    end
  end

  # Return true if string is braille, false otherwise
  def self.braille?(str)
    str.chars.all? { |c| ['.', 'O'].include?(c) } && (str.length % 6).zero?
  end

  # Convert braille string to english
  def self.to_english(str)
    english = ''
    is_alpha = true
    is_upcase = false

    # Iterate through string indices, moving 6 characters at a time
    0.step(str.length - 6, 6).each do |i|
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
    end

    english
  end

  def self.braille_char_to_eng(braille_char, is_alpha, is_upcase)
    if is_alpha
      char = BrailleEnglishDictionary::BRAILLE_TO_ALPHA[braille_char]
      char = char.upcase if is_upcase
    else
      char = BrailleEnglishDictionary::BRAILLE_TO_NUM[braille_char]
    end

    char
  end

  # Convert english string to braille
  def self.to_braille(str)
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
      when c.upcase
        braille << BrailleEnglishDictionary::BRAILLE_CAP_FOLLOWS
        braille << BrailleEnglishDictionary::ALPHA_TO_BRAILLE[c.downcase]
      else
        braille << BrailleEnglishDictionary::ALPHA_TO_BRAILLE[c]
      end
    end

    braille
  end
end

input_string = ARGV.join(' ')
print Translator.translate(input_string)
