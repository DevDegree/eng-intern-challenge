import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

describe('translator.ts output', () => {
  it('should print the correct output to the console', async () => {
    const { stdout } = await execAsync('ts-node translator.ts Abc 123 xYz');

    const expected = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO';
    expect(stdout.trim()).toBe(expected);
  });
});
