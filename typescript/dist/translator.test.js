"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const child_process_1 = require("child_process");
const util_1 = require("util");
const execAsync = (0, util_1.promisify)(child_process_1.exec);
describe("translator.ts output", () => {
    it("should print the correct output to the console", () => __awaiter(void 0, void 0, void 0, function* () {
        const { stdout } = yield execAsync("ts-node translator.ts Abc 123 xYz");
        const expected = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO";
        expect(stdout.trim()).toBe(expected);
    }));
    it("braille -> alphabet + random capitals", () => __awaiter(void 0, void 0, void 0, function* () {
        const { stdout } = yield execAsync("ts-node translator.ts O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O......OOOOOO......OO.OOO......O.OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO");
        const expected = "abcdefghijklmnopQRStuvwxyz";
        expect(stdout.trim()).toBe(expected);
    }));
    it("should print the correct output to the console", () => __awaiter(void 0, void 0, void 0, function* () {
        const { stdout } = yield execAsync("ts-node translator.ts .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..");
        const expected = "Hello world";
        expect(stdout.trim()).toBe(expected);
    }));
    it("braille -> 42", () => __awaiter(void 0, void 0, void 0, function* () {
        const { stdout } = yield execAsync("ts-node translator.ts .O.OOOOO.O..O.O...");
        const expected = "42";
        expect(stdout.trim()).toBe(expected);
    }));
    it("braille -> Abc 123", () => __awaiter(void 0, void 0, void 0, function* () {
        const { stdout } = yield execAsync("ts-node translator.ts .....OO.....O.O...OO...........O.OOOO.....O.O...OO....");
        const expected = "Abc 123";
        expect(stdout.trim()).toBe(expected);
    }));
});
