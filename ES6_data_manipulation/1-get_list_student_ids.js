function getListStudentIds(students) {
  // Verifica si el argumento es un array
  if (!Array.isArray(students)) {
    return [];
  }

  // Usa el método map para extraer los IDs
  return students.map((student) => student.id);
}

export default getListStudentIds;
