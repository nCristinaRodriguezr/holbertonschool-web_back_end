function createInt8TypedArray(length, position, value) {
  // Crear un nuevo ArrayBuffer con la longitud especificada
  const buffer = new ArrayBuffer(length);

  // Crear una vista DataView sobre el buffer
  const dataView = new DataView(buffer);

  // Verificar si la posición está dentro del rango
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Asignar el valor a la posición especificada
  dataView.setInt8(position, value);

  // Devolver el DataView
  return dataView;
}

export default createInt8TypedArray;
