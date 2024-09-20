export default function isBraille(textToTranslate:string) {
  const regex = /^[.O]*$/;
  return regex.test(textToTranslate);
}
