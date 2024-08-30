def braille_to_visual(string, lang)

  if lang == "english"
    require_relative "../data/english"
  else 
    raise "Unknown language: #{lang}"
  end

  # tracks whether to read current segment as number or letter
  number_mode = false
  # tracks if next letter is capital (reset every segment)
  capital_left = 0

  num_segments = (string.length / 6) - 1

  output = ""

  # invert hashmaps to translate from braille to visual language
  special_inv = SPECIAL.invert
  letters_inv = LETTERS.invert
  nums_inv = NUMS.invert

  for i in 0..num_segments
      segment = "#{string[i*6, 6]}"                 # get segment as substring
      capital_left = [0, capital_left - 1].max

      
    if special_inv.has_key?(segment)
      if special_inv[segment] == ' '
          number_mode = false                       # reset to letter mode if space
          output.concat(' ')

      elsif special_inv[segment] == 'number'
          number_mode = true

      elsif special_inv[segment] == 'capital'
          capital_left = 2                          # set to 2 since it will auto decrement to 1 next iter
      end

      elsif number_mode
          if nums_inv.has_key?(segment)
              output.concat(nums_inv[segment])
              
          else
              raise "Expected number, got '#{segment}'. Translated so far: '#{output}'"
          end

      elsif capital_left == 1
          if letters_inv.has_key?(segment)
              output.concat(letters_inv[segment].upcase)

          else
              raise "Expected letter to capitalize, got '#{segment}'. Translated so far: '#{output}'"
          end
          
      elsif letters_inv.has_key?(segment)
          output.concat(letters_inv[segment])

      else
          raise "Translated so far '#{output}', but encountered unexpected segment '#{segment}'"
      end
  end

  return output
end
