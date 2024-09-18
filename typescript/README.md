# TypeScript Instructions

1. Set up: install dependencies

   ```
   cd typescript/
   ```

   ```
   npm i
   ```

2. Run with dev (no build):

   ```
   npm run dev <input>
   ```

   Replace `<input>` with the text or Braille you want to translate.

3. To build the project, run:

   ```
   npm run build
   ```

4. Run with compiled javascript (requires build):

   ```
   npm start <input>
   ```

5. To run the tests, execute:
   ```
   npm test
   ```

## Project Structure

- `translator.ts`: Contains the main translation logic.
- `translatorUtils.ts`: Includes utility functions and data structures for the translator.
- `translator.test.ts`: Contains the test cases for the translator.
- `tsconfig.json`: TypeScript configuration file.
- `package.json`: Defines project dependencies and scripts.

## Notes

1. **Data Structures**: The solution uses `Map` objects to store the Braille-to-English and English-to-Braille mappings. Enables O(1) lookup times.

2. **Input Detection**: The code determines whether the input is Braille or text using regex, taking advantage of limited language defined for the question.
