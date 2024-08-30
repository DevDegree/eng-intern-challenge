RSpec.describe 'Braille Translator Script' do
  it 'outputs the correct string' do
    output = `ruby translator.rb Abc 123 xYz`
    expect(output.strip).to eq('.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO')
  end

  # ******************************
  # *  ENGLISH TO BRAILLE TESTS  *
  # ******************************

  # Number to braille tests
  it 'number to braille test1' do
    output = `ruby translator.rb 0`
    expect(output.strip).to eq('.O.OOO.OOO..')
  end
  it 'number to braille test2' do
    output = `ruby translator.rb 0123456789`
    expect(output.strip).to eq('.O.OOO.OOO..O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO...')
  end
  it 'number to braille test3' do
    output = `ruby translator.rb 987 654 321 0`
    expect(output.strip).to eq('.O.OOO.OO...O.OO..OOOO.........O.OOOOOO...O..O..OO.O.........O.OOOOO....O.O...O............O.OOO.OOO..')
  end
  it 'number to braille test4' do
    output = `ruby translator.rb 0 1 2 3 4 5 6 7 8 9`
    expect(output.strip).to eq('.O.OOO.OOO.........O.OOOO............O.OOOO.O..........O.OOOOO...........O.OOOOO.O.........O.OOOO..O.........O.OOOOOO..........O.OOOOOOO.........O.OOOO.OO.........O.OOO.OO...')
  end

  # Alphabet to braille tests (lowercase)
  it 'alphabet to braille test1' do
    output = `ruby translator.rb a`
    expect(output.strip).to eq('O.....')
  end
  it 'alphabet to braille test2' do
    output = `ruby translator.rb abcdefghijklmnopqrstuvwxyz`
    expect(output.strip).to eq('O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O.OOOOO.O.OOO..OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO')
  end
  it 'alphabet to braille test3' do
    output = `ruby translator.rb abcd efg hijk lmnop qrs tuv wxyz`
    expect(output.strip).to eq('O.....O.O...OO....OO.O........O..O..OOO...OOOO........O.OO...OO....OOO..O...O.......O.O.O.OO..O.OO.OO.O..OO.OOO.O.......OOOOO.O.OOO..OO.O........OOOO.O...OOO.O.OO.......OOO.OOO..OOOO.OOOO..OOO')
  end
  it 'alphabet to braille test4' do
    output = `ruby translator.rb a b c d e f g h i j k l m n o p q s r t u v w x y z`
    expect(output.strip).to eq('O...........O.O.........OO..........OO.O........O..O........OOO.........OOOO........O.OO.........OO..........OOO........O...O.......O.O.O.......OO..O.......OO.OO.......O..OO.......OOO.O.......OOOOO........OO.O.......O.OOO........OOOO.......O...OO......O.O.OO.......OOO.O......OO..OO......OO.OOO......O..OOO')
  end

  # Alphabet to braille tests (uppercase)
  it 'alphabet to braille test5' do
    output = `ruby translator.rb A`
    expect(output.strip).to eq('.....OO.....')
  end
  it 'alphabet to braille test6' do
    output = `ruby translator.rb ABCDEFGHIJKLMNOPQRSTUVWXYZ`
    expect(output.strip).to eq('.....OO..........OO.O........OOO.........OOO.O.......OO..O.......OOOO........OOOOO.......OO.OO.......O.OO........O.OOO.......OO...O......OO.O.O......OOO..O......OOO.OO......OO..OO......OOOO.O......OOOOOO......OO.OOO......O.OO.O......O.OOOO......OO...OO.....OO.O.OO.....O.OOO.O.....OOO..OO.....OOO.OOO.....OO..OOO')
  end
  it 'alphabet to braille test7' do
    output = `ruby translator.rb ABCD EFG HIJK LMNOP QRS TUV WXYZ`
    expect(output.strip).to eq('.....OO..........OO.O........OOO.........OOO.O.............OO..O.......OOOO........OOOOO.............OO.OO.......O.OO........O.OOO.......OO...O............OO.O.O......OOO..O......OOO.OO......OO..OO......OOOO.O............OOOOOO......OO.OOO......O.OO.O............O.OOOO......OO...OO.....OO.O.OO...........O.OOO.O.....OOO..OO.....OOO.OOO.....OO..OOO')
  end
  it 'alphabet to braille test8' do
    output = `ruby translator.rb A B C D E F G H I J K L M N O P Q S R T U V W X Y Z`
    expect(output.strip).to eq('.....OO................OO.O..............OOO...............OOO.O.............OO..O.............OOOO..............OOOOO.............OO.OO.............O.OO..............O.OOO.............OO...O............OO.O.O............OOO..O............OOO.OO............OO..OO............OOOO.O............OOOOOO............O.OO.O............OO.OOO............O.OOOO............OO...OO...........OO.O.OO...........O.OOO.O...........OOO..OO...........OOO.OOO...........OO..OOO')
  end

  # Mixed alphabet and number to braille tests
  it 'mixed alphabet and number to braille test1' do
    output = `ruby translator.rb abc 123 abc`
    expect(output.strip).to eq('O.....O.O...OO...........O.OOOO.....O.O...OO..........O.....O.O...OO....')
  end
  it 'mixed alphabet and number to braille test2' do
    output = `ruby translator.rb aBc 1 2 DeF 3 4`
    expect(output.strip).to eq('O..........OO.O...OO...........O.OOOO............O.OOOO.O..............OOO.O..O..O.......OOOO..........O.OOOOO...........O.OOOOO.O..')
  end

  # ******************************
  # *  BRAILLE TO ENGLISH TESTS  *
  # ******************************

  # Braille to number tests
  it 'braille to number test1' do
    output = `ruby translator.rb .O.OOO.OOO..`
    expect(output.strip).to eq('0')
  end
  it 'braille to number test2' do
    output = `ruby translator.rb .O.OOO.OOO..O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO...`
    expect(output.strip).to eq('0123456789')
  end
  it 'braille to number test3' do
    output = `ruby translator.rb .O.OOO.OO...O.OO..OOOO.........O.OOOOOO...O..O..OO.O.........O.OOOOO....O.O...O............O.OOO.OOO..`
    expect(output.strip).to eq('987 654 321 0')
  end
  it 'braille to number test4' do
    output = `ruby translator.rb .O.OOO.OOO.........O.OOOO............O.OOOO.O..........O.OOOOO...........O.OOOOO.O.........O.OOOO..O.........O.OOOOOO..........O.OOOOOOO.........O.OOOO.OO.........O.OOO.OO...`
    expect(output.strip).to eq('0 1 2 3 4 5 6 7 8 9')
  end

  # Braille to alphabet tests (lowercase)
  it 'braille to alphabet test1' do
    output = `ruby translator.rb O.....`
    expect(output.strip).to eq('a')
  end
  it 'braille to alphabet test2' do
    output = `ruby translator.rb O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O.OOOOO.O.OOO..OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO`
    expect(output.strip).to eq('abcdefghijklmnopqrstuvwxyz')
  end
  it 'braille to alphabet test3' do
    output = `ruby translator.rb O.....O.O...OO....OO.O........O..O..OOO...OOOO........O.OO...OO....OOO..O...O.......O.O.O.OO..O.OO.OO.O..OO.OOO.O.......OOOOO.O.OOO..OO.O........OOOO.O...OOO.O.OO.......OOO.OOO..OOOO.OOOO..OOO`
    expect(output.strip).to eq('abcd efg hijk lmnop qrs tuv wxyz')
  end
  it 'braille to alphabet test4' do
    output = `ruby translator.rb O...........O.O.........OO..........OO.O........O..O........OOO.........OOOO........O.OO.........OO..........OOO........O...O.......O.O.O.......OO..O.......OO.OO.......O..OO.......OOO.O.......OOOOO........OO.O.......O.OOO........OOOO.......O...OO......O.O.OO.......OOO.O......OO..OO......OO.OOO......O..OOO`
    expect(output.strip).to eq('a b c d e f g h i j k l m n o p q s r t u v w x y z')
  end

  # Braille to alphabet tests (uppercase)
  it 'braille to uppercase alphabet test1' do
    output = `ruby translator.rb .....OO.....`
    expect(output.strip).to eq('A')
  end
  it 'braille to uppercase alphabet test2' do
    output = `ruby translator.rb .....OO..........OO.O........OOO.........OOO.O.......OO..O.......OOOO........OOOOO.......OO.OO.......O.OO........O.OOO.......OO...O......OO.O.O......OOO..O......OOO.OO......OO..OO......OOOO.O......OOOOOO......OO.OOO......O.OO.O......O.OOOO......OO...OO.....OO.O.OO.....O.OOO.O.....OOO..OO.....OOO.OOO.....OO..OOO`
    expect(output.strip).to eq('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  end
  it 'braille to uppercase alphabet test3' do
    output = `ruby translator.rb .....OO..........OO.O........OOO.........OOO.O.............OO..O.......OOOO........OOOOO.............OO.OO.......O.OO........O.OOO.......OO...O............OO.O.O......OOO..O......OOO.OO......OO..OO......OOOO.O............OOOOOO......OO.OOO......O.OO.O............O.OOOO......OO...OO.....OO.O.OO...........O.OOO.O.....OOO..OO.....OOO.OOO.....OO..OOO`
    expect(output.strip).to eq('ABCD EFG HIJK LMNOP QRS TUV WXYZ')
  end
  it 'braille to uppercase alphabet test4' do
    output = `ruby translator.rb .....OO................OO.O..............OOO...............OOO.O.............OO..O.............OOOO..............OOOOO.............OO.OO.............O.OO..............O.OOO.............OO...O............OO.O.O............OOO..O............OOO.OO............OO..OO............OOOO.O............OOOOOO............O.OO.O............OO.OOO............O.OOOO............OO...OO...........OO.O.OO...........O.OOO.O...........OOO..OO...........OOO.OOO...........OO..OOO`
    expect(output.strip).to eq('A B C D E F G H I J K L M N O P Q S R T U V W X Y Z')
  end

  # Braille to mixed alphabet and number tests
  it 'braille to mixed alphabet and number test1' do
    output = `ruby translator.rb O.....O.O...OO...........O.OOOO.....O.O...OO..........O.....O.O...OO....`
    expect(output.strip).to eq('abc 123 abc')
  end
  it 'braille to mixed alphabet and number test2' do
    output = `ruby translator.rb O..........OO.O...OO...........O.OOOO............O.OOOO.O..............OOO.O..O..O.......OOOO..........O.OOOOO...........O.OOOOO.O..`
    expect(output.strip).to eq('aBc 1 2 DeF 3 4')
  end
end
