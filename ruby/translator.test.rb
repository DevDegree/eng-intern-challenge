RSpec.describe 'Braille Translator Script' do
  it 'outputs the correct string' do
    output = `ruby translator.rb Abc 123 xYz`
    expect(output.strip).to eq('.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO')
  end
end
