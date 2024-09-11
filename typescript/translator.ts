import Translator from './src/index';

try {
    const translator = new Translator();
    const args = process.argv.slice(2);

    if (args.length > 0) {
        translator.run(args);
    } else {
        translator.run([]);
    }
} catch (error) {
    console.error(error);
}
