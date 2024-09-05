import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

describe('translator.ts output', () => {
  it('should translate Braille to English (Abc 123 xYz)', async () => {
    const { stdout } = await execAsync('ts-node translator.ts .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO');
    const expected = 'Abc 123 xYz';
    expect(stdout.trim()).toBe(expected);
  });

  it('should translate English to Braille (Hello world)', async () => {
    const { stdout } = await execAsync('ts-node translator.ts Hello world');
    const expected = '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..';
    expect(stdout.trim()).toBe(expected);
  });

  it('should translate numbers correctly (42)', async () => {
    const { stdout } = await execAsync('ts-node translator.ts 42');
    const expected = '.O.OOOOO.O..O.O...';
    expect(stdout.trim()).toBe(expected);
  });
});
