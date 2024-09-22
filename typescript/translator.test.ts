import { exec } from "child_process";
import { promisify } from "util";

const execAsync = promisify(exec);

describe("translator.ts output", () => {
    describe("english to braille translation", () => {
        it("Abc 123 xYz", async () => {
            const { stdout } = await execAsync(
                "ts-node translator.ts Abc 123 xYz"
            );

            const expected =
                ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO";
            expect(stdout.trim()).toBe(expected);
        });

        it("Hello world", async () => {
            const { stdout } = await execAsync(
                "ts-node translator.ts Hello world"
            );

            const expected =
                ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..";
            expect(stdout.trim()).toBe(expected);
        });
    });

    describe("braille to english translation", () => {
        it("Abc 123 xYz", async () => {
            const { stdout } = await execAsync(
                "ts-node translator.ts .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
            );

            const expected = "Abc 123 xYz";
            expect(stdout.trim()).toBe(expected);
        });

        it("Hello world", async () => {
            const { stdout } = await execAsync(
                "ts-node translator.ts .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
            );

            const expected = "Hello world";
            expect(stdout.trim()).toBe(expected);
        });
    });
});
