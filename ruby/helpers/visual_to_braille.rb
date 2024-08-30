def visual_to_braille(string, lang)

  if lang == "english"
    require_relative "../data/english"
  else 
    raise "Unknown language: #{lang}"
  end

  output = ""
  number_mode = false

  string.each_char do |char|
      if LETTERS.has_key?(char)
          if number_mode
              raise "In number mode but attempting to translate letter"
          end
          output.concat(LETTERS[char])
          
      elsif LETTERS.has_key?(char.downcase)
          if number_mode
              raise "In number mode but attempting to translate letter"
          end
          output.concat(SPECIAL['capital'])
          output.concat(LETTERS[char.downcase])

      elsif NUMS.has_key?(char)
          if !number_mode
              number_mode = true
              output.concat(SPECIAL['number'])
          end

          output.concat(NUMS[char])
          
      elsif char == ' '
          number_mode = false
          output.concat(SPECIAL[char])
      else
          raise "Unexpected character received: '#{char}'"
     end
  end

  return output
end
