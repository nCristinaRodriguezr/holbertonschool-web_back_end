export default function cleanSet(set, startString) {
  // Verifica si startString es una cadena no vacía
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }

  const result = [];
  set.forEach((value) => {
    if (value.startsWith(startString)) {
      result.push(value.slice(startString.length));
    }
  });

  return result.join('-');
}
