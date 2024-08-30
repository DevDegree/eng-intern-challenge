RSpec.describe 'Braille Translator Script' do
  it 'outputs the correct string for "Hello world"' do
    output = `ruby translator.rb Hello world`
    expect(output.strip).to eq('.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..')
  end

  it 'outputs the correct string for "42"' do
    output = `ruby translator.rb 42`
    expect(output.strip).to eq('.O.OOOOO.O..O.O...')
  end

  it 'outputs the correct string for Braille to text translation with a sentence' do
    output = `ruby translator.rb .....OO.....O.O...OO...........O.OOOO.....O.O...OO....`
    expect(output.strip).to eq('Abc 123')
  end

  it 'outputs the correct string for Braille to text translation with "Abc"' do
    output = `ruby translator.rb .....OO.....O.O...OO....`
    expect(output.strip).to eq('Abc')
  end

  it 'outputs the correct string for Braille to text translation with "123"' do
    output = `ruby translator.rb .O.OOOO.....O.O...OO....`
    expect(output.strip).to eq('123')
  end

  it 'outputs the correct string for text to Braille translation with anmol' do
    output = `ruby translator.rb anmol`
    expect(output.strip).to eq('O.....OO.OO.OO..O.O..OO.O.O.O.')
  end

  it 'outputs the correct string for text to Braille translation with "2025 W"' do
    output = `ruby translator.rb 2025 W`
    expect(output.strip).to eq('.O.OOOO.O....OOO..O.O...O..O.............O.OOO.O')
  end
end
