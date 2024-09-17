char_to_braille = {
  "a" => "O.....",
  "b" => "O.O...",
  "c" => "OO....",
  "d" => "OO.O..",
  "e" => "O..O..",
  "f" => "OOO...",
  "g" => "OOOO..",
  "h" => "O.OO..",
  "i" => ".OO...",
  "j" => ".OOO..",
  "k" => "O...O.",
  "l" => "O.O.O.",
  "m" => "OO..O.",
  "n" => "OO.OO.",
  "o" => "O..OO.",
  "p" => "OOO.O.",
  "q" => "OOOOO.",
  "r" => "O.OOO.",
  "s" => ".OO.O.",
  "t" => ".OOOO.",
  "u" => "O...OO",
  "v" => "O.O.OO",
  "w" => ".OOO.O",
  "x" => "OO..OO",
  "y" => "OO.OOO",
  "z" => "O..OOO"
}

braille_to_char = char_to_braille.invert

special_char_to_braille = braille_map = {
  "1" => "O.....",
  "2" => "O.O...",
  "3" => "OO....",
  "4" => "OO.O..",
  "5" => "O..O..",
  "6" => "OOO...",
  "7" => "OOOO..",
  "8" => "O.OO..",
  "9" => ".OO...",
  "0" => ".OOO..",
  "." => "..OO.O",
  "," => "..O...",
  "?" => "..OO.O",
  "!" => "..O.OO",
  ":" => "..OO..",
  ";" => "..O.O.",
  "-" => "....OO",
  "/" => ".O..O.",
  "<" => ".OO..O",
  ">" => "O..OO.",
  "(" => "O.O..O",
  ")" => ".O.OO.",
  " " => "......",
}

braille_to_special_char = special_char_to_braille.invert

meta_chars = {
  "capital follows" => ".....O",
  "number follows" => ".O.OOO",
  "decimal follows" => ".O...O",
}

braille_to_meta_char = meta_chars.invert

user_args = ARGV

# If the inputted string has no spaces and only contains O's and .'s, it will be treated as Braille and translated to English
if (user_args.length == 1 and !!user_args[0].match(/\A[\.O]*\z/) and user_args[0].length % 6 == 0)  
  braille_str = user_args[0]
  str_len = braille_str.length
  cap_follows = false
  num_follows = false

  (0..str_len-1).step(6) do |i|
    if braille_to_char.has_key?(braille_str[i, 6]) and not num_follows
      c = braille_to_char[braille_str[i, 6]]
      if cap_follows
        c = c.upcase
        cap_follows = false
      end
      print c
    elsif braille_to_special_char.has_key?(braille_str[i, 6])
      print braille_to_special_char[braille_str[i, 6]]

      if braille_str[i, 6] == special_char_to_braille[" "]
        num_follows = false
      end
    elsif braille_to_meta_char.has_key?(braille_str[i, 6])
      if braille_str[i, 6] == meta_chars["capital follows"]
        cap_follows = true
      elsif braille_str[i, 6] == meta_chars["number follows"]
        num_follows = true
      elsif braille_str[i, 6] == meta_chars["decimal follows"]
        print "."
      end 
    else
      # Silently fail on invalid Braille
      print "?"
    end
  end

# Otherwise, it will be treated from English and translated to Braille
else
  counter = 1
  num_follows = false
  user_args.each do |word|
    word.length.times do |i|
      if char_to_braille.has_key?(word[i].downcase) and not num_follows
        if /[[:upper:]]/.match(word[i])
          print meta_chars["capital follows"]
          print char_to_braille[word[i].downcase]
        else
          print char_to_braille[word[i]]
        end
      else
        if word[i] == "." and num_follows
          print meta_chars["decimal follows"]
        elsif special_char_to_braille.has_key?(word[i])
          if word[i] == "#{word[i].to_i}" and not num_follows
            print meta_chars["number follows"]
            num_follows = true
          end
          print special_char_to_braille[word[i]]
        else
          print "?"
        end
      end
    end

    # Don't print the space after the last word
    if counter != user_args.length
      print special_char_to_braille[" "]
    end
    counter += 1
    num_follows = false
  end 
end

# Add a new line to the output
puts ""

