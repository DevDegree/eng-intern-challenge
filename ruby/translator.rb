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
      'number' => '.O.OOO'
    }
  
    ENGLISH_ALPHABET = BRAILLE_ALPHABET.invert
    ENGLISH_NUMBERS = BRAILLE_NUMBERS.invert
    SPECIAL_BRAILLE = BRAILLE_SPECIAL.invert
  
    def initialize(input_string)
      @input_string = input_string
      @number_mode = false
      @capital_mode = false
    end
  
    def translate
      if is_braille?
        braille_to_english
      else
        english_to_braille
      end
    end
  
    private
  
    def is_braille?
      @input_string.chars.all? { |c| c == 'O' || c == '.' }
    end
  
    def english_to_braille
      result = []
      @number_mode = false
  
      @input_string.each_char do |char|
        # Handle spaces
        if char == ' '
          result << BRAILLE_ALPHABET[char]
          next
        end
  
        # Handle capital letters
        if char =~ /[A-Z]/
          result << BRAILLE_SPECIAL['capital']  # Add Braille capital prefix
          char = char.downcase  # Continue with lowercase equivalent
        end
  
        # Handle numbers
        if char =~ /\d/
          unless @number_mode
            result << BRAILLE_SPECIAL['number']  # Add Braille number prefix
            @number_mode = true
          end
          result << BRAILLE_NUMBERS[char]
          next
        end
  
        # Reset number mode after a non-number character
        @number_mode = false if char !~ /\d/
  
        # Translate letters
        result << BRAILLE_ALPHABET[char] if BRAILLE_ALPHABET[char]
      end
  
      result.join  # Join without spaces to avoid adding extra spaces between Braille characters
    end
  
    def braille_to_english
      result = []
      @number_mode = false
      @capital_mode = false
      chars = @input_string.scan(/.{6}/)  # Braille characters are 6-dots long
  
      chars.each do |braille_char|
        if braille_char == '......'  # Handle spaces
          result << ' '
          next
        end
  
        # Handle special characters (capital and number)
        if braille_char == BRAILLE_SPECIAL['capital']
          @capital_mode = true
          next
        elsif braille_char == BRAILLE_SPECIAL['number']
          @number_mode = true
          next
        end
  
        if @number_mode
          result << ENGLISH_NUMBERS[braille_char]
          @number_mode = false
        else
          letter = ENGLISH_ALPHABET[braille_char]
          if @capital_mode
            letter = letter.upcase
            @capital_mode = false
          end
          result << letter
        end
      end
  
      result.join
    end
  end
  
  # Command-line interface
  def main

    input_string = ARGV.join(" ")
    translator = BrailleTranslator.new(input_string)
    puts translator.translate
  end
  
  if __FILE__ == $0
    main
  end