export default function guardrail(mathFunction) {
  const queue = [];

  try {
    // Ejecutar la función y añadir el resultado al array
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    // Añadir el mensaje de error formateado al array si ocurre una excepción
    queue.push(`Error: ${error.message}`);
  }

  // Añadir el mensaje final al array
  queue.push('Guardrail was processed');

  return queue;
}
