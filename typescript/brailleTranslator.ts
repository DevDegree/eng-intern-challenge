import { brailleLetters, brailleNumbers, utilityMap } from "./objects";
import { Action, Braille } from "./types";

// Credit: https://stackoverflow.com/questions/6259515/how-can-i-split-a-string-into-segments-of-n-characters
function chunk(str: string) {
  return str.match(/.{1,6}/g) as Braille[];
}

function translateBraille(
  chunk: Braille,
  action: Action
): { action: Action; value?: string } {
  if (chunk === utilityMap["capitalize"]) {
    return { action: "capitalize" };
  }
  if (chunk === utilityMap["number"]) {
    return { action: "number" };
  }

  if (chunk === utilityMap["space"]) {
    return { action: "none", value: " " };
  }

  if (action == "number") {
    return { action: "number", value: brailleNumbers[chunk] };
  }

  if (action == "capitalize") {
    return { action: "none", value: brailleLetters[chunk].toUpperCase() };
  }

  return { action: "none", value: brailleLetters[chunk] };
}

export default function brailleTranslator(str: string) {
  let chunks: Braille[] = chunk(str);
  let action: Action = "none";
  let output = "";

  for (let brailleChunk of chunks) {
    let result = translateBraille(brailleChunk, action);
    if (result.value) {
      output += result.value;
    }

    action = result.action;
  }

  return output;
}
