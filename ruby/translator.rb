$braille_sym = ["......", "..OOO.", "", "", "","", "", "", "O.O..O", ".O.OO.", "", "", "..O...", "....OO", "..OO.O", ".O..O.", ".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...","..OO..", "..O.O.", ".OO..O", "", "O..OO.", "..O.OO", ""]
$braille_letters = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"]
$braille_wildcards = [".....O", ".O...O", ".O.OOO"]

$braille_table_num = {}
$braille_table_splet = {}
# < = > ? @

def populate_table()
    base_ch = 32
    end_ch = 64
    i = 0

    $braille_sym.each do |v|
        if (base_ch + i < 48 || base_ch + i > 57)
            $braille_table_splet[v] = base_ch + i
        else
            $braille_table_num[v] = base_ch + i  
        end
        i += 1
    end
    i = 0
    $braille_letters.each do |v|
        $braille_table_splet[v] = 97 + i
        i += 1
    end
    i = 0
    $braille_wildcards.each do |v|
        $braille_table_splet[v] = i
        i += 1
    end
end

def braille(str)
    outstr = ""
    capital = false
    numericS = false

    checkstr = ""
    ind = 0

    # Extract each character per 6 byte block of braille ascii
    str.each_byte do |i|
        if (i != 46 && i != 79)
            return outstr
        else
            end
        #puts i.chr
        if (ind <= 5)
            checkstr += i.chr
            ind += 1
        else

            val = $braille_table_splet[checkstr]
            #puts val
            if (val == 0)
                capital = true
            elsif (val == 1)
                outstr += "."
            elsif (val == 2)
                numericS = true
            end

            if (val > 32)
                 if (!numericS)
                    if (capital && val >= 97)
                        outstr += (val - 32).chr
                        capital = false
                    else
                        outstr += val.chr
                    end
                else
                    val2 = $braille_table_num[checkstr]
                    outstr += val2.chr
                end
            else
                if (!numericS)
                    outstr += val.chr
                else
                end
                numericS = (numericS && val != 32)
            end
            checkstr = i.chr
            ind = 1
        end
    end

    # Extract the last block

    val = $braille_table_splet[checkstr]
    #puts val
    if (val == 0)
        capital = true
    elsif (val == 1)
        outstr += "."
    elsif (val == 2)
        numericS = true
    end

    if (val > 32)
        if (!numericS)
            if (capital && val >= 97)
                outstr += (val - 32).chr
                capital = false
            else
                outstr += val.chr
                
            end
        else
            val2 = $braille_table_num[checkstr]
            outstr += val2.chr
        end
    else
        if (!numericS) 
            outstr += val.chr
        else
        end
        numericS = (numericS && val != 32)
    end

    return outstr
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

            if (i == 32 && numericS)
                outr += $braille_sym[0]
                numericS = false
            end
        else
            if (capital)
                if (numericS)
                    outr += $braille_sym[0]
                    numericS = false
                else
                end
                outr += $braille_wildcards[0] + $braille_letters[i-(end_ch+1)]
            elsif (numeric)
                if (!numericS)
                    outr += $braille_wildcards[2] + $braille_sym[i-base_ch]
                else
                    outr += $braille_sym[i-base_ch]
                end
            elsif (dec_fols)
                outr += $braille_wildcards[1]
                numeric = true
            elsif (lowercase)
                if (numericS)
                    outr += $braille_sym[0]
                    numericS = false
                else
                end
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
     populate_table()
     puts braille(user_valid)
  else
     puts eng_to_braille(user_valid)
    end
  
else
  end