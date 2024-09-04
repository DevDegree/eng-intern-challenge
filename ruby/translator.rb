class Translator
    def initialize
      @bra_trans = @eng_trans = @in = ""
      @pattern_bra = /^[O.]+$/
      @bra_num_mp = { "1" => "O.....", "2" => "O.O...", "3" => "OO....", "4" => "OO.O..", "5" => "O..O..",
                      "6" => "OOO...", "7" => "OOOO..", "8" => "O.OO..", "9" => ".O.O..", "0" => ".OOO.." }
      @bra_mp = { "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..", "e" => "O..O..",
                  "f" => "OOO...", "g" => "OOOO..", "h" => "O.OO..", "i" => ".OO...", "j" => ".OOO..",
                  "k" => "O...O.", "l" => "O.O.O.", "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.",
                  "p" => "OOO.O.", "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.",
                  "u" => "O...OO", "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO", "y" => "OO.OOO",
                  "z" => "O..OOO" }
      @eng_mp = @bra_mp.invert
      @bra_applied = { "upper" => ".....O", "number" => ".O.OOO", " " => "......" }
      @eng_num_mp = @bra_num_mp.invert
      @applied_eng = @bra_applied.invert
    end
  
    def translate
      if ARGV.empty?
        puts "No input string provided."
        exit
      end
  
      @in = ARGV.join(" ")
      return puts "Invalid Braille" if @in.match?(@pattern_bra) && @in.length % 6 != 0
  
      @in.match?(@pattern_bra) ? bra_to_eng : eng_to_bra
      puts @bra_trans.empty? ? @eng_trans : @bra_trans
    end
  
    def bra_to_eng
      cells = @in.chars.each_slice(6).map(&:join)
      i = 0
      while i < cells.length
        cell = cells[i]
        case @applied_eng[cell]
        when "upper"
          @eng_trans += @eng_mp[cells[i + 1]].upcase
          i += 1
        when "number"
          i += 1
          while @applied_eng[cells[i]] != " "
            break if i == cells.length
            @eng_trans += @eng_num_mp[cells[i]].to_s
            i += 1
          end
          @eng_trans += @eng_mp[cells[i]].to_s
          i += 1
        else
          @eng_trans += @eng_mp[cell].to_s if @eng_mp.key?(cell)
        end
        i += 1
      end
    end
  
    def eng_to_bra
      @in.each_char.with_index do |char, i|
        if char.match(/^[[:alnum:]]$/)
          if char.match(/[[:digit:]]/)
            @bra_trans += (i > 0 && @in[i - 1].match?(/[[:digit:]]/)) ? @bra_num_mp[char].to_s : @bra_applied["number"].to_s + @bra_num_mp[char].to_s
          else
            @bra_trans += (char == char.upcase ? @bra_applied["upper"].to_s : "") + (@bra_mp[char.downcase] || "")
          end
        else
          @bra_trans += @bra_applied[char].to_s
        end
      end
    end
  end
  
  
  test = Translator.new
  test.translate