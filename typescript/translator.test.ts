import { exec } from 'child_process';
import { promisify } from 'util';
import { translate } from './translator';

const execAsync = promisify(exec);

describe('translator.ts output', () => {
  it('should print the correct output to the console', async () => {
    const { stdout } = await execAsync('ts-node translator.ts Abc 123 xYz');

    const expected = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO';
    expect(stdout.trim()).toBe(expected);
  });
});

describe('translate()', () => {
  test('readme example 1', () => {
    const input = "Hello world";
    const expected = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..";
    const actual = translate(input);
    expect(actual).toBe(expected);
  });

  test('readme example 2', () => {
    const input = "42";
    const expected = ".O.OOOOO.O..O.O...";
    const actual = translate(input);
    expect(actual).toBe(expected);
  });

  test('readme example 3', () => {
    const input = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....";
    const expected = "Abc 123";
    const actual = translate(input);
    expect(actual).toBe(expected);
  });
})
