$lang = "english"    # modular to supporte different languages

require_relative "helpers/visual_to_braille"
require_relative "helpers/braille_to_visual"

def main()
    input_string = ARGV[0]
    # first preference given to braille if valid
    if validate_braille(input_string)
        puts braille_to_visual(input_string, $lang)
    else
        puts visual_to_braille(input_string, $lang)
    end
end

# returns true if valid braille
def validate_braille(input_string)
    # check length is divisble by 6
    if input_string.length % 6 != 0
        return false
    end
    # check all characters are valid
    input_string.each_char do |char|
        if !(char == '.' or char == 'O')
            return false
        end
    end
    return true
end

main()
