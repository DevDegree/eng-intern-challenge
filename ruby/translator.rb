require_relative 'constants'
require_relative 'get_input_type'
require_relative 'translate_braille_to_english'

def translate_english_to_braille(english_string)
  result = ""

  # check if capital
  # check if number
end


def main()
  input_type = get_input_type()

  if input_type == BRAILLE_TYPE
    puts translate_braille_to_english(ARGV[0])
    return
  else
    puts "English"
  end

end

main()
