class BrailleTranslator
  
    def translate(input_sentence)
      return braille_to_english input_sentence if braille? input_sentence
  
      english_to_braille input_sentence
    end
  
    private
  
    def braille_to_english(braille_sentence)
    end
  
    def english_to_braille(english_sentence)
    end
  
    def braille?(str)
      str.count('^O.').zero?
    end
  end