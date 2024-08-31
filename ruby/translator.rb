require_relative 'constants'
require_relative 'get_input_type'
require_relative 'translate_braille_to_english'
require_relative 'translate_english_to_braille'


def main()
  input_type = get_input_type()

  if input_type == BRAILLE_TYPE
    puts translate_braille_to_english(ARGV[0])
    return
  elsif input_type == ENGLISH_TYPE
    puts translate_english_to_braille(ARGV)
    return
  else
    puts "Invalid input type"
    return
  end
end

main()
