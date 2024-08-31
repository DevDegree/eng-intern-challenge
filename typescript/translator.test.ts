import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

describe('translator.ts output', () => {
  it('should print the correct output to the console', async () => {
    const { stdout } = await execAsync('ts-node translator.ts Abc 123 xYz');

    const expected = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO';
    expect(stdout.trim()).toBe(expected);
  });
  it('additional test 1', async () => {
    const { stdout } = await execAsync('ts-node translator.ts Hello world');
    const expected = '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..';
    expect(stdout.trim()).toBe(expected);
  })
  it('additional test 2', async () => {
    const { stdout } = await execAsync('ts-node translator.ts 42');
    const expected = '.O.OOOOO.O..O.O...';
    expect(stdout.trim()).toBe(expected);
  })
  it('additional test 3', async () => {
    const { stdout } = await execAsync('ts-node translator.ts .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..');
    const expected = 'Hello world';
    expect(stdout.trim()).toBe(expected);
  })
  it('additional test 4', async () => {
    const { stdout } = await execAsync('ts-node translator.ts .O.OOOOO.O..O.O...');
    const expected = '42';
    expect(stdout.trim()).toBe(expected);
  })
  it ('additional test 5', async () => {
    const { stdout } = await execAsync('ts-node translator.ts 456 7890');
    const expected = '.O.OOOOO.O..O..O..OOO..........O.OOOOOOO..O.OO...OO....OOO..';
    expect(stdout.trim()).toBe(expected);
  })
});
