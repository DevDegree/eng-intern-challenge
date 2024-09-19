$braille_sym = ["......", "..OOO.", "", "", "","", "", "", "O.O..O", ".O.OO.", "", "", "..O...", "....OO", "..OO.O", ".O..O.", ".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...","..OO..", "..O.O.", ".OO..O", "", "O..OO.", "..O.OO", ""]
$braille_letters = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"]
$braille_wildcards = [".....O", ".O...O", ".O.OOO"]

$braille_sym_r = {"......": " ", "..OOO.": "!", "":"", "":"", "":"","":"", "":"", "":"", "O.O..O", ".O.OO.", "", "", "..O...", "....OO", "..OO.O", ".O..O.", ".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...","..OO..", "..O.O.", ".OO..O", "", "O..OO.", "..O.OO", ""}
$braille_letters_r = {"O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"}
$braille_wildcards_r = {".....O", ".O...O", ".O.OOO"}
# < = > ? @

def braille(str)
    return "eng"
end

def eng_to_braille(str)
    outr = ""
    base_ch = 32
    end_ch = 64

    numericS = false

    str.each_byte do |i|
        capital = (i <= 90 && i >= 65)
        lowercase = (i <= 122 && i>=97)
        numeric = (i <= 57 && i >= 48)
        dec_fols = (i == 46 && numericS)
        
        if (i >= base_ch && i <= end_ch && !numeric && !dec_fols)
            outr += $braille_sym[i-base_ch]

            if (i == 32)
                numericS = false
            end
        else
            if (capital)
                outr += $braille_wildcards[0] + $braille_letters[i-(end_ch+1)]
            elsif (numeric)
                if (!numericS)
                    outr += $braille_wildcards[2] + $braille_sym[i-base_ch]
                else
                    outr += $braille_sym[i-base_ch]
                end
            elsif (dec_fols)
                outr += $braille_wildcards[1]
            elsif (lowercase)
                outr += $braille_letters[i-97]
            end

            numericS = numeric
        end
    
    end


    return outr
end

user_argvs = ARGV
if (user_argvs.length == 1)
  user_valid = user_argvs[0].to_s

  if ((user_valid[0] == "O" || user_valid[0] == ".") && user_valid.length >= 6)
    # detected braille, switch to braille mode
     puts braille(user_valid)
  else
     puts user_valid[0].bytes
     puts eng_to_braille(user_valid)
    end
  
else
  end