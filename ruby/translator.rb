=begin 
Tests cases 
Input: Hello world
Output: .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..

Input: 42
Output: .O.OOOOO.O..O.O...

Input: .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
Output: Abc 123

edge cases:
the braille string is not divisible by 6 
the braille string includes a character that is not a braille character

=end


class Translator
  def initialize
    @input_string = ""
    @braille_pattern = /^[O.]+$/
    @english_translation = ""
    @braille_translation = ""
    @braille_letter_map = {
      "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..", "e" => "O..O..",
      "f" => "OOO...", "g" => "OOOO..", "h" => "O.OO..", "i" => ".O.O..", "j" => ".OOO..",
      "k" => "O...O.", "l" => "O.O.O.", "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.",
      "p" => "OOO.O.", "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.",
      "u" => "O...OO", "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO", "y" => "OO.OOO",
      "z" => "O..OOO",
      }
    @braille_number_map = {
      "1" => "O.....", "2" => "O.O...", "3" => "OO....", "4" => "OO.O..", "5" => "O..O..",
      "6" => "OOO...", "7" => "OOOO..", "8" => "O.OO..", "9" => ".O.O..", "0" => ".OOO..",
    }
    @braille_non_alphanumeric_map = {
      "." => "OO..O.", "," => "OO.OOO", "?" => "OO.O..", "!" => "OO...O", ":" => "OO..OO",
      "-" => "OOOO..", "/" => "O.OO.O", "<" => "O..OO.", ">" => ".OO..O", "(" => ".O.OO.",
      ")" => "O.O..O", " " => "OOOOOO",
    }
    @applied_braille = {
      "upper" => ".....O",
      "decimal" => ".O...O",
      "number" =>  ".O.OOO",
    }
    @english_letter_map = {
    "O....." => "a", "O.O..." => "b", "OO...." => "c", "OO.O.." => "d", "O..O.." => "e",
    "OOO..." => "f", "OOOO.." => "g", "O.OO.." => "h", ".O.O.." => "i", ".OOO.." => "j",
    "O...O." => "k", "O.O.O." => "l", "OO..O." => "m", "OO.OO." => "n", "O..OO." => "o",
    "OOO.O." => "p", "OOOOO." => "q", "O.OOO." => "r", ".OO.O." => "s", ".OOOO." => "t",
    "O...OO" => "u", "O.O.OO" => "v", ".OOO.O" => "w", "OO..OO" => "x", "OO.OOO" => "y",
    "O..OOO" => "z"
  }

    @english_numbers_map = {
      "O....." => "1", "O.O..." => "2", "OO...." => "3", "OO.O.." => "4", "O..O.." => "5",
      "OOO..." => "6", "OOOO.." => "7", "O.OO.." => "8", ".O.O.." => "9", ".OOO.." => "0"
    }

    @english_non_alphanumeric = {
      "OO..O." => ".", "OO.OOO" => ",", "OO.O.." => "?", "OO...O" => "!", "OO..OO" => ":",
      "OOOO.." => "-", "O.OO.O" => "/", "O..OO." => "<", ".OO..O" => ">", ".O.OO." => "(",
      "O.O..O" => ")", "OOOOOO" => " "
    }
    
    @applied_english = {
      ".....O" => "upper",
      ".O...O" => ".",
      ".O.OOO" => "number", 
    }
  end

  def translate
    # Check if any arguments were passed
    if ARGV.empty?
      puts "No input string provided."
      exit
    end

    # Get the first argument
    @input_string = ARGV.join(" ")

    #validate input string and which function to call
    if @input_string.match?(@braille_pattern)
      if @input_string.length % 6 == 0
        puts "braille to engl"
        braille_to_english
        puts @english_translation
        return
      else
        return "Invalid Braille"
      end
    else
      puts "engl to braille"
      english_to_braille
      puts @braille_translation
      return
    end
  end

  def braille_to_english()
    #iterate for every 6 characters and check if its in alpha num or just applied braille 
    #clean input string into arrays 
    @input_string = @input_string.chars
    split_chars = @input_string.each_slice(6)
    cells = split_chars.map { |group| group.join("")}
    #iterate over cells 
    i = 0
    while i < cells.length() do 
      cell = cells[i]
      #puts cell
      if @applied_english.has_key?(cell)
        #puts "in applied braille"
        #puts applied_english[cell].to_s
        #if upper
        if @applied_english[cell].to_s == "upper"
          #puts "in upper case"
          word = @english_letter_map[cells[i+1]].upcase
          @english_translation += word
          i += 1
        elsif @applied_english[cell].to_s == "number"
          i += 1
          while i < cells.length() and cells[i] != "OOOOOO" do #iterate number until thre is a space then turn flag off
            #puts "in number case"
            @english_translation += @english_numbers_map[cells[i]].to_s
            i += 1
          end
          #it must be a space now 
          @english_translation += @english_letter_map[cells[i]].to_s
          i += 1 
        else #its a decimal 
          #puts "in deciamal"
          @english_translation += @applied_english[cell].to_s
        end
      elsif @english_letter_map.has_key?(cell)
        #puts "in letter"
        @english_translation += @english_letter_map[cell].to_s
      elsif @english_non_alphanumeric.has_key?(cell)
        @english_translation += @english_non_alphanumeric[cell].to_s
      end
      i += 1
    end
    puts @english_translation
  end


  def english_to_braille() 
    #iterate over each char and get the braille value
    @input_string = @input_string.split("")
    for i in 0...@input_string.length
      char = @input_string[i]
      #alphanumeric 
      if char.match(/^[[:alnum:]]$/)
        #check if number or letter 
        if char.is_a? Numeric 
          #need to put number following sign, then keep going and check if previous is 
          if @input_string[i-1].is_a? Numeric
            @braille_translation += @braille_number_map[char].to_s
          else #need to add the 
            @braille_translation += @applied_braille["number"].to_s
            @braille_translation += @braille_number_map[char].to_s
          end
        else
          #its a letter
          if char == char.upcase  #check case 
            @braille_translation += @applied_braille["upper"].to_s 
          end 
          @braille_translation += @braille_letter_map[char].to_s
        end
      else #its non alphanumeric
        @braille_translation += @applied_braille[char].to_s
      end
    end
    puts @braille_translation
    return @braille_translation 
  end
end  






#translate_to_braille("Hello World")




#input = "O.OO..O..O..O.O.O.O.O.O.O..OO..OOO.OO..OO.O.OOO.O.O.O.OO.O.." #hello world
#input = "O.OOO."
#input = ".....OO.....O.O...OO....OOOOOO.O.OOOO.....O.O...OO...." #Abc 123
#input = ".OOOO.O..O...OO.O..OOOO..O.O..OO.OO.OOOO...O.OOOO......O.O..O....." #testing191
#translate_to_english(input)
test = Translator.new
test.translate