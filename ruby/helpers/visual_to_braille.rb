def visual_to_braille(string, lang)

  if lang == "english"
    require_relative "../data/english"
  else 
    raise "Unknown language: #{lang}"
  end

  output = ""
  number_mode = false

  string.each_char do |char|                        # iterate through each character
      if LETTERS.has_key?(char)
          if number_mode
              raise "In number mode but attempting to translate letter"
          end
          output.concat(LETTERS[char])
          
      elsif LETTERS.has_key?(char.downcase)         # if input character is upper case
          if number_mode
              raise "In number mode but attempting to translate letter"
          end
          output.concat(SPECIAL['capital'])
          output.concat(LETTERS[char.downcase])

      elsif NUMS.has_key?(char)
          if !number_mode                           # if not in number mode, need to append special char
              number_mode = true
              output.concat(SPECIAL['number'])
          end

          output.concat(NUMS[char])
          
      elsif char == ' '
          number_mode = false                       # reset to letter mode
          output.concat(SPECIAL[char])
      else
          raise "Unexpected character received: '#{char}'"
     end
  end

  return output
end
