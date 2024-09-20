export default function splitByNumberOfChar(textToSplit : string, numberOfChar: number) {
  const characters = [];
  for (let i = 0; i < textToSplit.length; i += numberOfChar) {
    characters.push(textToSplit.substring(i, i + numberOfChar));
  }
  return characters;
}
