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
      "f" => "OOO...", "g" => "OOOO..", "h" => "O.OO..", "i" => ".OO...", "j" => ".OOO..",
      "k" => "O...O.", "l" => "O.O.O.", "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.",
      "p" => "OOO.O.", "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.",
      "u" => "O...OO", "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO", "y" => "OO.OOO",
      "z" => "O..OOO",
      }
    @braille_number_map = {
      "1" => "O.....", "2" => "O.O...", "3" => "OO....", "4" => "OO.O..", "5" => "O..O..",
      "6" => "OOO...", "7" => "OOOO..", "8" => "O.OO..", "9" => ".O.O..", "0" => ".OOO..",
    }
    @applied_braille = {
      "upper" => ".....O",
      "number" =>  ".O.OOO",
	  " " => "......",
    }
    @english_letter_map = {
    "O....." => "a", "O.O..." => "b", "OO...." => "c", "OO.O.." => "d", "O..O.." => "e",
    "OOO..." => "f", "OOOO.." => "g", "O.OO.." => "h", ".OO..." => "i", ".OOO.." => "j",
    "O...O." => "k", "O.O.O." => "l", "OO..O." => "m", "OO.OO." => "n", "O..OO." => "o",
    "OOO.O." => "p", "OOOOO." => "q", "O.OOO." => "r", ".OO.O." => "s", ".OOOO." => "t",
    "O...OO" => "u", "O.O.OO" => "v", ".OOO.O" => "w", "OO..OO" => "x", "OO.OOO" => "y",
    "O..OOO" => "z"
  }

    @english_numbers_map = {
      "O....." => "1", "O.O..." => "2", "OO...." => "3", "OO.O.." => "4", "O..O.." => "5",
      "OOO..." => "6", "OOOO.." => "7", "O.OO.." => "8", ".O.O.." => "9", ".OOO.." => "0"
    }
    
    @applied_english = {
      ".....O" => "upper",
      ".O.OOO" => "number", 
	  "......" => " ",
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
        braille_to_english
        puts @english_translation
        return
      else
        return "Invalid Braille"
      end
    else
      english_to_braille
      puts @braille_translation
      return
    end
  end

  def braille_to_english()
    #clean input string into arrays 
    @input_string = @input_string.chars
    split_chars = @input_string.each_slice(6)
    cells = split_chars.map { |group| group.join("")}
    #iterate over cells 
    i = 0
    while i < cells.length() do 
      cell = cells[i]
      #check for applied symbols
      if @applied_english.has_key?(cell)
        if @applied_english[cell].to_s == "upper"
		      i += 1
          word = @english_letter_map[cells[i]].upcase
          @english_translation += word
        elsif @applied_english[cell].to_s == "number"
          i += 1
          while @applied_english[cell].to_s != " " do #iterate until there is space or end of string 
            if i == cells.length() #the sequence ends on a numerical value
              return
            end
            #add number 
            @english_translation += @english_numbers_map[cells[i]].to_s
            i += 1
          end
          #it must be a space now 
          @english_translation += @english_letter_map[cells[i]].to_s
          i += 1 
        end
      elsif @english_letter_map.has_key?(cell) #it is a letter
        @english_translation += @english_letter_map[cell].to_s
      end
      i += 1
    end
    return @english_translation
  end


  def english_to_braille() 
    #iterate over each char and get the braille value
    @input_string = @input_string.split("")
    for i in 0...@input_string.length
      char = @input_string[i]
      #alphanumeric 
      if char.match(/^[[:alnum:]]$/)
        #check if number or letter 
        if char.match(/[[:digit:]]/)
          #check if previous was number, otherwise add the number symbol 
          if i > 0 and @input_string[i-1].match?(/[[:digit:]]/)
            @braille_translation += @braille_number_map[char].to_s
          else #need to add the number symbol
            @braille_translation += @applied_braille["number"].to_s
            @braille_translation += @braille_number_map[char].to_s
          end
        else
          #its a letter
          if char == char.upcase  #check case 
            @braille_translation += @applied_braille["upper"].to_s 
          end 
          @braille_translation += @braille_letter_map[char.downcase].to_s
        end
      else #its non alphanumeric
        @braille_translation += @applied_braille[char].to_s
      end
    end
    return @braille_translation 
  end
end  

#input = "O.OO..O..O..O.O.O.O.O.O.O..OO..OOO.OO..OO.O.OOO.O.O.O.OO.O.." #hello world
#input = ".....OO.....O.O...OO....OOOOOO.O.OOOO.....O.O...OO...." #Abc 123
#input = ".OOOO.O..O...OO.O..OOOO..O.O..OO.OO.OOOO...O.OOOO......O.O..O....." #testing191

test = Translator.new
test.translate