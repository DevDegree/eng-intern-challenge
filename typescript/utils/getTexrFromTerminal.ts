export default function getTextFromTerminal() {
  const text = process.argv.slice(2).join(' ');
  return text;
}
