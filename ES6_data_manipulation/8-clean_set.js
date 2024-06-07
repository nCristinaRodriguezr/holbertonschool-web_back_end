export default function cleanSet(set, startString) {
  // Verifica si startString está definido y no está vacío
  if (!startString) {
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
