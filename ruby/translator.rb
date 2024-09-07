
module TEXT_TYPE
  NOT_APPLICABLE = :N_A
  PLAINTEXT = :Plain
  BRAILLE = :Braille
end

Braille_To_Plaintext_Hash = {
  1 => 'a', 5 => 'b', 3 => 'c', 11 => 'd', 9 => 'e',
  7 => 'f', 15 => 'g', 13 => 'h', 6 => 'i', 14 => 'j',
  17 => 'k', 21 => 'l', 19 => 'm', 27 => 'n', 25 => 'o',
  23 => 'p', 31 => 'q', 29 => 'r', 22 => 's', 30 => 't',
  49 => 'u', 53 => 'v', 46 => 'w', 51 => 'x', 59 => 'y',
  57 => 'z'
}
Plaintext_To_Braille_Hash = Braille_To_Plaintext_Hash.invert


class StringBrailleConverter
  attr_accessor :lang
  def initialize(phrase = "")
    @phrase = phrase
    @lang = :N_A
  end

  def checkLang
    if @phrase.respond_to?("chars")
      @lang = :Plain
      @phrase.chars.each do |c|
        return if c != 'O' && c != '.'
      end
      # If it gets here, the phrase is thus fully Braille
      @lang = :Braille
    else
      puts "There is no string here."
      # @lang = TEXT_TYPE::NOT_APPLICABLE
    end
  end

  def toPlaintext
    return if @lang != :Braille
    
    #Mapping from https://stackoverflow.com/questions/25347435/how-to-split-the-string-by-certain-amount-of-characters-in-ruby 
    braille_chars = @phrase.chars.each_slice(6).map(&:join) 
    braille_val_arr = []
    plaintext_str = ""
    # return if braille_chars.last.length != 6

    b_cipher_value = 0
    braille_chars.each do |bchar|
      b_cipher_value = bchar.reverse
      b_cipher_value.gsub!('O', '1')
      b_cipher_value.gsub!('.', '0')
      braille_val_arr << b_cipher_value.to_i(2)
    end
    # Braille is now converted to binary-based ciphertext values.
    # Substitute original phrase with plaintext:
    
    is_capital = false
    is_num = false
    char_to_add = ""
    braille_val_arr.each do |value|
      case value
      when 0 # Space character
        is_num = false
        plaintext_str << ' '
      when 32 # Capital follows
        is_capital = true
      when 58 # Number follows
        is_num = true
      else
        char_to_add = Braille_To_Plaintext_Hash[value]
        if is_capital
          char_to_add = char_to_add.upcase
          is_capital = false
        elsif is_num
          char_to_add = ((char_to_add.ord - 46) % 10).to_s
          # char_to_add - ('a'-'1'); mod 10 for 'j' = '0'
        end
        plaintext_str.concat("#{char_to_add}")
      end
    end

    puts plaintext_str

  end # of toPlaintext method

  def toBraille
    return if @lang != :Plain
    braille_bin_arr = []
    brailletext_str = ""

    is_num = false
    @phrase.chars.each do |plainchar|
      if /[[:upper:]]/.match(plainchar)
        braille_bin_arr << 32 # Capital follows
        braille_bin_arr << Plaintext_To_Braille_Hash[plainchar.downcase!]
      elsif /[[:digit:]]/.match(plainchar)
        if !is_num
          braille_bin_arr << 58 # Number follows
          is_num = true
        end
        braille_bin_arr << Plaintext_To_Braille_Hash[
          (plainchar.ord + 48 + (plainchar == '0' ? 10 : 0)).chr
        ]
      elsif /[[:blank:]]/.match(plainchar) # Space
        braille_bin_arr << 0
        is_num = false
      else
        braille_bin_arr << Plaintext_To_Braille_Hash[plainchar]
      end
    end

    bin_str = ""
    braille_bin_arr.each do |bval|
      next if bval == nil # End of line
      # puts "Char: #{bval}"
      bin_str = bval.to_s(2).reverse
      # puts bin_str
      while bin_str.length < 6
        bin_str.concat('0')
      end
      bin_str.gsub!('1', 'O')
      bin_str.gsub!('0', '.')
      brailletext_str << bin_str
    end

    puts brailletext_str

  end # of toBraille method

end # of class

if __FILE__ == $0
  args = ARGV.join(" ")
  converter = StringBrailleConverter.new(args)
  converter.checkLang
  case converter.lang
  when :Braille
    converter.toPlaintext
    # puts "Braille"
  when :Plain
    converter.toBraille
    # puts "Plain"
  else 
    puts "Error"
  end
end