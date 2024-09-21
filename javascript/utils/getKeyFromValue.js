export default function getKeyFromValue(object, value) {
  return Object.entries(object).find(([, val]) => val === value)?.[0];
}
