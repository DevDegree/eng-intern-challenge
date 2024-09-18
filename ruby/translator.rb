class Translator 
    ENGLISH_TO_BRAILLE = {
        'a' => 'O.....',
        'b' => 'O.O...',
        'c' => 'OO....',
        'd' => 'OO.O..',
        'e' => 'O..O..',
        'f' => 'OOO...',
        'g' => 'OOOO..',
        'h' => 'O.OO..',
        'i' => '.OO...',
        'j' => '.OOO..',
        'k' => 'O...O.',
        'l' => 'O.O.O.',
        'm' => 'OO..O.',
        'n' => 'OO.OO.',
        'o' => 'O..OO.',
        'p' => 'OOO.O.',
        'q' => 'OOOOO.',
        'r' => 'O.OOO.',
        's' => '.OO.O.',
        't' => '.OOOO.',
        'u' => 'O...OO',
        'v' => 'O.O.OO',
        'w' => '.OOO.O',
        'x' => 'OO..OO',
        'y' => 'OO.OOO',
        'z' => 'O..OOO',
        ' ' => '......',
        'CAPITAL' => '.....O',
        'NUMBER' => '.O.OOO'
    }

    BRAILLE_TO_ENGLISH = ENGLISH_TO_BRAILLE.invert

    def handle_smart_translation(input) 
        if !input.match?(/[^O\.]/)
            puts braille_to_english(input)
        else
            puts english_to_braille(input)
        end
    end

    private

    def english_to_braille(english) 
        result = ""
        in_number_mode = false

        english.each_char do |char| 
            if char.match?(/[A-Z]/)
                result += ENGLISH_TO_BRAILLE['CAPITAL']
                char = char.downcase
            end

            if char.match?(/[1-9]/)
                result += ENGLISH_TO_BRAILLE['NUMBER'] unless in_number_mode
                in_number_mode = true
                char = ('a'.ord + char.to_i - 1).chr
            else
                in_number_mode = false
            end

            result += ENGLISH_TO_BRAILLE[char] || ''
        end

        result
    end

    def braille_to_english(braille) 
        result = ""
        split_string = braille.chars.each_slice(6).map(&:join)
        isNumberMode = false
        skipChar = false

        if braille.length % 6 != 0
            puts("Invalid braille string.")
            return
        end

        split_string.each_with_index do |braille_char, index|
            if skipChar
                skipChar = false
                next
            end

            if braille_char == "......"
                isNumberMode = false
            end

            if isNumberMode
                result += (BRAILLE_TO_ENGLISH[braille_char].ord - 'a'.ord + 1).to_s
                next
            end

            if braille_char == ".....O"
                next_char = BRAILLE_TO_ENGLISH[split_string[index + 1]]
                result += next_char.to_s.upcase
                skipChar = true
            elsif braille_char == ".O.OOO"
                isNumberMode = true
                next
            else
                result += BRAILLE_TO_ENGLISH[braille_char]
            end
        end

        result
    end
end

if __FILE__ == $0
    input_text = ARGV.join(" ")

    if input_text.empty?
        puts "Please provide text to translate."
    else  
        Translator.new.handle_smart_translation(input_text)
    end
end