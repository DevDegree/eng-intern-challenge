RSpec.describe 'Braille Translator Script' do
  it 'correctly translates English to Braille' do
    output = `ruby translator.rb Abc 123 xYz`
    expect(output.strip).to eq('.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO')
  end

  it 'correctly translates Braille to English' do
    braille_input = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO'
    output = `ruby translator.rb #{braille_input}`
    expect(output.strip).to eq('Abc 123 xYz')
  end
end
