class BrailleTranslator
    BRAILLE_ALPHABET = {
      'a' => 'O.....', 'b' => 'O.O...', 'c' => 'OO....', 'd' => 'OO.O..', 'e' => 'O..O..',
      'f' => 'OOO...', 'g' => 'OOOO..', 'h' => 'O.OO..', 'i' => '.OO...', 'j' => '.OOO..',
      'k' => 'O...O.', 'l' => 'O.O.O.', 'm' => 'OO..O.', 'n' => 'OO.OO.', 'o' => 'O..OO.',
      'p' => 'OOO.O.', 'q' => 'OOOOO.', 'r' => 'O.OOO.', 's' => '.OO.O.', 't' => '.OOOO.',
      'u' => 'O...OO', 'v' => 'O.O.OO', 'w' => '.OOO.O', 'x' => 'OO..OO', 'y' => 'OO.OOO',
      'z' => 'O..OOO', ' ' => '......'
    }
  
    BRAILLE_NUMBERS = {
      '1' => 'O.....', '2' => 'O.O...', '3' => 'OO....', '4' => 'OO.O..', '5' => 'O..O..',
      '6' => 'OOO...', '7' => 'OOOO..', '8' => 'O.OO..', '9' => '.OO...', '0' => '.OOO..'
    }
  
    BRAILLE_SPECIAL = {
      'capital' => '.....O',  
      'number'  => '.O.OOO'  
    }
  
    # braille to english
    ENGLISH_ALPHABET = BRAILLE_ALPHABET.invert
    ENGLISH_NUMBERS = BRAILLE_NUMBERS.invert
    SPECIAL_BRAILLE = BRAILLE_SPECIAL.invert
  
    # new BrailleTranslator instance
    def initialize(input_string)
      @input_string = input_string
      @number_mode = false
      @capital_mode = false
    end
  
    #determine translation direction
    def translate
      if is_braille?
        braille_to_english
      else
        english_to_braille
      end
    end
  
    private
  
    # Detect if the input is braille
    def is_braille?
      @input_string.chars.all? { |c| c == 'O' || c == '.' }
    end
  
    #English to Braille
    def english_to_braille
      result = []
      @number_mode = false
  
      @input_string.each_char do |char|
        result << handle_capital(char) if char =~ /[A-Z]/
        result << handle_number(char) if char =~ /\d/
  
        if BRAILLE_ALPHABET[char.downcase]
          result << BRAILLE_ALPHABET[char.downcase]
        elsif BRAILLE_NUMBERS[char]
          result << BRAILLE_NUMBERS[char]
        end
  
        result << reset_number_mode(char)
      end
  
      result.compact.join
    end
  

    # Handles capital letters
    def handle_capital(char)
      return unless char =~ /[A-Z]/
      BRAILLE_SPECIAL['capital']
    end
  
    # Handles numbers 
    def handle_number(char)
      if !@number_mode
        @number_mode = true
        BRAILLE_SPECIAL['number']
      end
    end
  
    # Reset number mode after spaces
    def reset_number_mode(char)
      @number_mode = false if char == ' '
      nil
    end
  
    #Braille to English
    def braille_to_english
      result = []
      @number_mode = false
      @capital_mode = false
  
      # Split into 6-character chunks
      chars = @input_string.scan(/.{6}/)
  
      # Process each chunk
      chars.each do |braille_char|
        if braille_char == '......'  # Handle spaces
          result << ' '
        else
          # Handle special characters (capital, number)
          special_char = handle_braille_special(braille_char)
          if special_char.nil?  # If special mode , skip this chunk
            next
          else
            result << special_char 
          end
        end
      end
  
      result.join
    end
  
    # Handles special characters
    def handle_braille_special(braille_char)
      if braille_char == BRAILLE_SPECIAL['capital']
        @capital_mode = true
        return nil
      elsif braille_char == BRAILLE_SPECIAL['number']
        @number_mode = true
        return nil
      end
  
      # Translate based on the current mode (number/capital/regular)
      if @number_mode
        char = ENGLISH_NUMBERS[braille_char]
        @number_mode = false if braille_char == '......'  # Space resets number mode
      else
        char = ENGLISH_ALPHABET[braille_char]
        if @capital_mode
          char = char.upcase  
          @capital_mode = false 
        end
      end
  
      char  #
    end
  end
  
  # Command-line interface
  def main
    input_string = ARGV[0]
    translator = BrailleTranslator.new(input_string)
    puts translator.translate
  end
  
  if __FILE__ == $0
    main
  end