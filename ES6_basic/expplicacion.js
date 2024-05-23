





/*
// con variables
console.log(x); // undefined
let x = 5;
console.log(x); // 5

/*
var x;          // Declaración elevada
console.log(x); // undefined (x está declarado pero no inicializado)
x = 5;          // Inicialización
console.log(x); // 5

// con funciones
sayHello(); // "Hello, world!"

function sayHello() {
  console.log("Hello, world!");
}
*/



//For in

const persona = {
  nombre: "Juan",
  edad: 30,
  ocupacion: "Desarrollador"
};

for (const propiedad in persona) {
  console.log(persona[propiedad]);
}
// For OF

const numeros = [1, 2, 3, 4, 5];

for (const numero in numeros) {
  console.log(numero);
}
