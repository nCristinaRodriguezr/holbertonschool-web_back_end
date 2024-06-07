export default function hasValuesFromArray(set, array) {
  // Utiliza el método every para verificar si todos los elementos del array
  // están presentes en el set
  return array.every((element) => set.has(element));
}
