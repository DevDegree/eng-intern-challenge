BRAILLE_TO_LATIN = {
  "O....." => 'a', "O.O..." => 'b', "OO...." => 'c', "OO.O.." => 'd', "O..O.." => 'e',
  "OOO..." => 'f', "OOOO.." => 'g', "O.OO.." => 'h', ".OO..." => 'i', ".OOO.." => 'j',
  "O...O." => 'k', "O.O.O." => 'l', "OO..O." => 'm', "OO.OO." => 'n', "O..OO." => 'o',
  "OOO.O." => 'p', "OOOOO." => 'q', "O.OOO." => 'r', ".OO.O." => 's', ".OOOO." => 't',
  "O...OO" => 'u', "O.O.OO" => 'v', ".OOO.O" => 'w', "OO..OO" => 'x', "OO.OOO" => 'y',
  "O..OOO" => 'z'
}

LATIN_TO_BRAILLE = BRAILLE_TO_LATIN.invert

# Special characters
CAPITAL = ".....O"
NUMBER = ".O.OOO"
SPACE = "......"

def translate_braille(braille_text)
  is_capital = false
  is_number = false
  latin_text = ""

  braille_text.scan(/.{6}/).each do |braille_char|

    # Handle special indicators
    if (braille_char == CAPITAL)
      is_capital = true
      next
    elsif braille_char == NUMBER
      is_number = true
      next
    end
    
    # Handle case where numbers are followed by space
    if is_number && braille_char == SPACE
      is_number=false
      latin_text += " "; 
    # Handle number
    elsif is_number
      latin_text += ((BRAILLE_TO_LATIN[braille_char].ord-'a'.ord + 1)%10).to_s  
    # Handle space
    elsif braille_char == SPACE
      latin_text += " "
    # Handle capital
    elsif is_capital
      latin_text += BRAILLE_TO_LATIN[braille_char].upcase
      is_capital= false
    # Handle normal character
    else
      latin_text += BRAILLE_TO_LATIN[braille_char]
    end  
  end
  latin_text
end

def translate_english(text)
  braille_text = ""
  number_seen = false

  text.each_char do |char|

    # Handle letters
    if char =~ /[A-Z]/  
      braille_text += CAPITAL  
      braille_text += LATIN_TO_BRAILLE[char.downcase] 
    elsif char =~ /[a-z]/
      braille_text += LATIN_TO_BRAILLE[char]
    end

    # Handle numbers
    if char =~ /[0-9]/
      # Start of number sequence
      if !number_seen
        braille_text += NUMBER
        number_seen = true
      end
      braille_text += LATIN_TO_BRAILLE[(((char.ord-'1'.ord)%10)+'a'.ord).chr]  
      next
    else
      number_seen = false
    end

    # Handle space
    if char == " "
      braille_text += SPACE
    end
  end

  braille_text
end

def braille(text)
  /^((O|\.){6})+$/.match?(text)
end

string_input = ARGV.join(' ')
puts (braille(string_input) ? translate_braille(string_input) : translate_english(string_input))