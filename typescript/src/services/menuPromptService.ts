import { Strings } from '../constants/strings';
import PromptService from './promptService';

class MenuPromptService {
  private promptService: PromptService;

  constructor() {
    this.promptService = new PromptService();
  }

  async promptMainMenu(): Promise<string> {
    const action = await this.promptService.select(
      'Translator CLI',
      [
        { name: '🌐 Translate', value: Strings.ACTIONS.TRANSLATE },
        { name: '🚪 Exit', value: Strings.ACTIONS.EXIT }
      ]
    );
    return action;
  }

  async promptForText(): Promise<string> {
    const text = await this.promptService.input('Enter the text to translate:', (input: string) => input.trim() !== '' || 'Text cannot be empty');
    return text;
  }
}

export default MenuPromptService;