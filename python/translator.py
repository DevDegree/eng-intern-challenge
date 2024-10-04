import re
import sys
#create a translator class for translating between Braille words and English words
class Translator():
    def __init__(self):
        #upload the translating rules in dictionary(use the binary reprentation to represnt the Braille alphabet 0 means "." and 1 means "o")
        self.english_to_braille = {
            'a': 0b100000, 'b': 0b101000, 'c': 0b110000, 'd': 0b110100, 'e': 0b100100,
            'f': 0b111000, 'g': 0b111100, 'h': 0b101100, 'i': 0b011000, 'j': 0b011100,
            'k': 0b100010, 'l': 0b101010, 'm': 0b110010, 'n': 0b110110, 'o': 0b100110,
            'p': 0b111010, 'q': 0b111110, 'r': 0b101110, 's': 0b011010, 't': 0b011110,
            'u': 0b100011, 'v': 0b101011, 'w': 0b011101, 'x': 0b110011, 'y': 0b110111, 
            'z': 0b100111, 'capital': 0b000001, 'decimal': 0b010001, 'number': 0b010111,
            '.': 0b001101, ',':0b001000, '?': 0b001011, '!': 0b001110, ':': 0b001100,
            ';': 0b001010, '-': 0b000011, '/': 0b010010, '<': 0b011001, '>': 0b100110,
            '(': 0b101001, ')': 0b010110, ' ': 0b000000
        }
        
        self.braille_to_english = {value: key for key, value in self.english_to_braille.items()}
        
        #print(self.braille_to_english)
        
        self.capital = False
        self.number = False
        self.decimal = False
        #this variable is to use to solve the ambiguity of ">" and "o" since they have the same braille representation
        self.whitespace = False

    def is_capital(self, symbol):
        if self.braille_to_english[symbol] == 'capital':
            self.capital = True
            return True
        else:
            return False
        
    def is_number(self, symbol):
        if self.braille_to_english[symbol] == 'number':
            self.number = True
            return True
        else:
            return False
        
    def is_decimal(self, symbol):
        if self.braille_to_english[symbol] == 'decimal':
            self.decimal = True
            return True
        else:
            return False
        
    #helper function to switch between binary number and braille character
    def transfer_for_binary(self, string):
        ans = ''
        for i in string:
            if i == '0':
                ans += '.'
            elif i == '1':
                ans += 'O'
                
            elif i == 'O':
                ans += '1'
            elif i == '.':
                ans += '0'
        return ans 
    
    
    #helper function to take an english character and convert english letter to a braille character
    def letter_to_braille(self, letter):
        binary_braille = format(self.english_to_braille[letter], '06b')
        return self.transfer_for_binary(binary_braille)
    
    
    
    
    def translate_to_braille(self, word):
        braille = ''
        for c in word:
            if 'A' <= c <= 'Z':
                #print capital first
                braille += self.letter_to_braille('capital')
                braille += self.letter_to_braille(c.lower())
                self.number = False
            elif '0' <= c <= '9':
                if (not self.number):
                    braille += self.letter_to_braille('number')
                    self.number = True
                    
                #print(c)
                braille += self.letter_to_braille('j' if c == '0' else chr(ord(c) + 48))
                #print('j' if c == '0' else chr(ord(c) - 48))
            else:
                if (c == '.' and self.number):
                    braille += self.letter_to_braille('decimal')
                else:
                    braille += self.letter_to_braille(c)
                    self.number = False
        return braille
    
    #there is an ambiguity between ">" and "o" since they have the same braille representation, so I make a decision that if there is no whitespace before ">", then it should be "o" or "O"
    def translate_to_english(self, braille):
        binary_braille = int(self.transfer_for_binary(braille), 2)
        if self.is_capital(binary_braille):
            #print("debug1")
            self.whitespace = False
            return ''
        if self.is_number(binary_braille):
            self.whitespace = False
            return ''
        if self.is_decimal(binary_braille):
            self.whitespace = False
            return '.'
        
        c = self.braille_to_english[binary_braille]
        if self.capital:
            self.capital = False
            self.number = False
            if c == '>' :
                if not self.whitespace:
                    return 'O'
            self.whitespace = False
            return c.upper()
        
        if self.number:
            self.whitespace = False
            c = self.braille_to_english[binary_braille]
            self.decimal = False
            return '0' if c == 'j' else chr(ord(c) - 48)
        
        if c == ' ':
            self.whitespace = True
            return c
        if c == '>' :
            if not self.whitespace:
                return 'o'
        self.whitespace = False
        return c

        

    def translate(self, text, isbraille):
        translated_text = ''
        if isbraille:
            braille_list = [text[i:i+6] for i in range(0, len(text), 6)]
            #print(braille_list)
            for braille in braille_list:
                translated_text += self.translate_to_english(braille)
            
        else:
            word_list = re.findall(r'\S+|\s', text)
            #print(word_list)
            for word in word_list:
                translated_text += self.translate_to_braille(word)
        return translated_text
        
                
        
        
        
 
def main():
    if len(sys.argv) > 1:
        text = sys.argv[1]
        #print(text)
    else:
        print("Need argument usage: python translator.py <text>", file=sys.stderr)
        exit(1)
    
    isbraille = True
    text_length = 0
    for c in text:
        text_length += 1
        if (not c == '.' and not c == 'O'):
            isbraille = False
            break
        
    if isbraille:
        if text_length % 6 != 0:
            isbraille = False
    

    translator = Translator()
    
    translated_text = translator.translate(text, isbraille)
    print(translated_text)
    
    
    
        
if __name__ == "__main__":
    main()
     
        