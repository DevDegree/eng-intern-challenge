# Ruby Instructions

### Command Line
You can use the script from the command line. It automatically detects whether the input is English or Braille and translates it accordingly.

#### Translating English to Braille
```bash
ruby translator.rb "Hello World 123"
```
This command will output the Braille representation of the provided English text.

#### Translating Braille to English
```bash
ruby translator.rb "O.....O.O...OO......O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
```
This command will output the English text corresponding to the provided Braille.

### Functions
The script provides the following key functions:

- **`translate_to_braille(text)`**: Translates English text into Braille.
- **`translate_to_english(input)`**: Translates Braille back into English. Includes a check to ensure that the input is a valid Braille string (i.e., its length is a multiple of six).
- **`determine_input_type(input)`**: Determines whether the input is English or Braille based on its content.

## Example
### Translating English to Braille
```ruby
text = "Hello 123"
braille = translate_to_braille(text)
puts braille
```
Output:
```
.....O.O...O..O..O.O...OO....O......O.OOOO.....O.O...OO...
```

### Translating Braille to English
```ruby
braille = "O.....O.O...OO......O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
english = translate_to_english(braille)
puts english
```
Output:
```
Hello 123
```

## Error Handling
When translating Braille to English, the script will raise an error if the Braille input length is not a multiple of six. This ensures that the input is correctly formatted for translation.

Example:
```ruby
invalid_braille = "O.....O.O...O"
begin
  english = translate_to_english(invalid_braille)
rescue => e
  puts e.message
end
```
Output:
```
Invalid Braille input: Length must be a multiple of 6.
```

## Testing
An RSpec test is included to verify the correctness of the translation functions. To run the tests:

```bash
rspec translator.test.rb
```
The tests were:
```ruby
RSpec.describe 'Braille Translator Script' do
  it 'outputs the correct string' do
    output = `ruby translator.rb Abc 123 xYz`
    expect(output.strip).to eq('.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO')
  end
end

RSpec.describe 'English Translator Script' do
  it 'outputs the correct string' do
    output = `ruby translator.rb .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO`
    expect(output.strip).to eq('Abc 123 xYz')
  end
end
```
### Results
![TestDone](https://github.com/user-attachments/assets/35e5bd00-f0c9-44de-9324-fc8e34a63f81)
