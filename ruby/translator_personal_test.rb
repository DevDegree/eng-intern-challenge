RSpec.describe 'Braille Translator Script' do
  it 'outputs the correct string for mixed case and numbers' do
    output = `ruby translator.rb Abc 123 xYz`
    expect(output.strip).to eq('.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO')
  end

  it 'outputs the correct string for lowercase letters' do
    output = `ruby translator.rb abc`
    expect(output.strip).to eq('O.....O.O...OO....')
  end

  it 'outputs the correct string for uppercase letters' do
    output = `ruby translator.rb ABC`
    expect(output.strip).to eq('.....OO..........OO.O........OOO....')
  end

  it 'outputs the correct string for numbers' do
    output = `ruby translator.rb 123`
    expect(output.strip).to eq('.O.OOOO.....O.O...OO....')
  end

  it 'outputs the correct string for special characters' do
    output = `ruby translator.rb .,!`
    expect(output.strip).to eq('..OO.O..O.....OOO.')
  end

  it 'outputs the correct string for sentences with spaces' do
    output = `ruby translator.rb "a b"`
    expect(output.strip).to eq('O...........O.O...')
  end
end
