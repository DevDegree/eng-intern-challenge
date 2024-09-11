import readline from 'readline';
import { Choice } from '../types';

class PromptService {
  constructor() {
  }

  async select(message: string, choices: Choice[]): Promise<string> {
    return new Promise((resolve) => {
      let selectedIndex = 0;
      let firstRender = true;

      const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
      });

      readline.emitKeypressEvents(process.stdin);
      if (process.stdin.isTTY) {
        process.stdin.setRawMode(true);
      }

      const render = () => {
        if (!firstRender) {
          // Move cursor up by the number of choices plus the message line
          process.stdout.write(`\x1b[${choices.length + 1}A`);
        }
        
        // Clear the lines
        process.stdout.write('\x1b[0J');
        
        console.log(message);
        choices.forEach((choice, index) => {
          if (index === selectedIndex) {
            console.log(`> ${choice.name}`);
          } else {
            console.log(`  ${choice.name}`);
          }
        });

        // Hide the cursor
        process.stdout.write('\x1b[?25l');

        firstRender = false;
      };

      render();

      process.stdin.on('keypress', (_, key) => {
        if (key.name === 'up') {
          selectedIndex = (selectedIndex - 1 + choices.length) % choices.length;
        } else if (key.name === 'down') {
          selectedIndex = (selectedIndex + 1) % choices.length;
        } else if (key.name === 'return') {
          // Clear the menu
          process.stdout.write(`\x1b[${choices.length + 2}A`);
          for (let i = 0; i < choices.length + 1; i++) {
            process.stdout.write('\x1b[K\n');
          }
          process.stdout.write(`\x1b[${choices.length + 1}A`);

          // Display the selected option
          console.log(`${message}: ${choices[selectedIndex].name}`);

          // Show the cursor again before resolving
          process.stdout.write('\x1b[?25h');

          rl.close();
          process.stdin.removeAllListeners('keypress');
          if (process.stdin.isTTY) {
            process.stdin.setRawMode(false);
          }
          resolve(choices[selectedIndex].value);
          return;
        }
        render();
      });

      // Ensure the cursor is shown if the process is interrupted
      process.on('SIGINT', () => {
        process.stdout.write('\x1b[?25h');
        process.exit();
      });
    });
  }

  async input(message: string, validate?: (input: string) => boolean | string): Promise<string> {
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    const promptUser = (): Promise<string> => {
      return new Promise((resolve) => {
        rl.question(message + ' ', (answer) => {
          if (validate) {
            const validationResult = validate(answer);
            if (typeof validationResult === 'string') {
              console.log(validationResult);
              resolve(promptUser());
            } else if (!validationResult) {
              console.log('Invalid input. Please try again.');
              resolve(promptUser());
            } else {
              rl.close();
              resolve(answer);
            }
          } else {
            rl.close();
            resolve(answer);
          }
        });
      });
    };

    return promptUser();
  }

  async confirm(message: string, defaultValue: boolean): Promise<boolean> {
    const answer = await this.input(`${message} (y/n) [${defaultValue ? 'Y/n' : 'y/N'}]: `);
    if (answer.toLowerCase() === 'y') return true;
    if (answer.toLowerCase() === 'n') return false;
    return defaultValue;
  }
}

export default PromptService;