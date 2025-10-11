/*Saludo en la Consola:
   - Enunciado: Preséntate en la consola del navegador.
   - Requerimientos: Usa let o const para tu nombre y console.log() para saludar.*/


/*const miNombre = "josue delgado"; 
// Requerimiento 2: Usar console.log() para el saludo.
console.log("¡Hola! Mi nombre es " + miNombre + ".");

console.log(`Un placer. Estoy usando ${miNombre} como mi nombre de ejemplo.`);*/


/*Operadores Aritméticos:
   - Enunciado: ¡Matemáticas básicas!
   - Requerimientos: Suma, resta, multiplica y divide dos números, mostrando cada resultado en la consola.*/


/*const numeroA = 6;
const numeroB = 8;

const suma = numeroA + numeroB;
console.log(`Suma de ${numeroA} + ${numeroB}: ${suma}`);

const resta = numeroA - numeroB;
console.log(`Resta de ${numeroA} - ${numeroB}: ${resta}`);

const multiplicacion = numeroA * numeroB;
console.log(`Multiplicación de ${numeroA} * ${numeroB}: ${multiplicacion}`);

const division = numeroA / numeroB;
console.log(`División de ${numeroA} / ${numeroB}: ${division}`);*/



/*Array de Colores:
 Enunciado: Crea una paleta de colores.
Requerimiento 1: Crear un array (arreglo) de colores.

const paletaDeColores = [
    "Rojo",
    "Verde",
    "Azul",
    "Amarillo",
    "Violeta",
    "Naranja"
];

console.log("--- Paleta de Colores ---");
console.log(paletaDeColores);

const longitud = paletaDeColores.length;
console.log("\n--- Información del Array ---");
console.log(`La paleta de colores contiene ${longitud} elementos.`);

console.log(`El primer color es: ${paletaDeColores[0]}`);
console.log(`El último color es: ${paletaDeColores[longitud - 1]}`);*/




/*Objeto de Usuario:
   - Enunciado: Define un perfil de usuario.
   - Requerimientos: Crea un objeto con nombre, edad y email. Muestra el objeto y luego solo el email



const perfilUsuario = {
    nombre: "Ana Martínez",
    edad: 28,
    email: "ana.martinez@ejemplo.com",
    ciudad: "Madrid" // Propiedad adicional, opcional
};

console.log("--- Objeto de Perfil de Usuario Completo ---");
console.log(perfilUsuario);

console.log("\n--- Solo el Email ---");
console.log(`Email: ${perfilUsuario.email}`);*/





/*Comparación Lógica:
   - Enunciado: ¿Mayor o menor?
   - Requerimientos: Usa prompt() para pedir un número y alert() para mostrar si es mayor que 50 (true/false).*/

/*const inputUsuario = prompt("Por favor, introduce un número:");
const numeroIngresado = parseFloat(inputUsuario); 

let resultadoComparacion;

if (isNaN(numeroIngresado) || inputUsuario === null || inputUsuario.trim() === "") {
    
    resultadoComparacion = "Entrada inválida o cancelada.";
    console.log("El usuario no introdujo un número válido.");
} else {
    
    const esMayorQueCincuenta = numeroIngresado > 50;
    resultadoComparacion = `¿El número ${numeroIngresado} es mayor que 50? \nResultado: ${esMayorQueCincuenta}`;
    console.log(`Resultado de la comparación para ${numeroIngresado}: ${esMayorQueCincuenta}`);
}
alert(resultadoComparacion);   */




/*Función de Cálculo:
   - Enunciado: Calcula el IVA de un producto.
   - Requerimientos: Crea una función calcularIVA que reciba un precio y retorne el 21%.


function calcularIVA(precioBase) {
    // Definimos la tasa de IVA como constante (0.21 para el 21%)
    const tasaIVA = 0.21;

    // Calculamos el IVA: Precio base * Tasa
    const montoIVA = precioBase * tasaIVA;

    // Retornamos el monto del IVA
    return montoIVA;
}


const producto1 = 100;
const iva1 = calcularIVA(producto1);
const total1 = producto1 + iva1;

console.log(`--- Producto 1 (Precio Base: ${producto1}€) ---`);
console.log(`Monto de IVA (21%): ${iva1.toFixed(2)}€`); // toFixed(2) para formato de moneda
console.log(`Precio Total: ${total1.toFixed(2)}€`);

const producto2 = 45.99;
const iva2 = calcularIVA(producto2);
const total2 = producto2 + iva2;

console.log(`\n--- Producto 2 (Precio Base: ${producto2}€) ---`);
console.log(`Monto de IVA (21%): ${iva2.toFixed(2)}€`);
console.log(`Precio Total: ${total2.toFixed(2)}€`);

function calcularPrecioTotal(precioBase) {
    const tasaIVA = 1.21; // Multiplicar por 1.21 da el 100% + 21% de IVA
    return precioBase * tasaIVA;
}

const total3 = calcularPrecioTotal(100);
console.log(`\n--- Precio Total con la función alternativa (100€) ---`);
console.log(`Precio Total: ${total3.toFixed(2)}€`);*/




/*Contador con while:
    - Enunciado: Conteo personalizado.
    - Requerimientos: Usa while para contar hasta un número dado por el usuario, saltándote el número 5 con continue*/


/*function contadorPersonalizado() {
    const inputLimite = prompt("Introduce el número hasta el que deseas contar (ej. 10):");
    const limite = parseInt(inputLimite);

    if (isNaN(limite) || limite <= 0) {
        console.log("[ERROR] Por favor, introduce un número entero positivo válido.");
        return;
    }
    console.log(`\n--- INICIANDO CONTEO HASTA ${limite} (Saltando el 5) ---`);

    let contador = 1;

    while (contador <= limite) {
        
        if (contador === 5) {
            console.log(`[SALTO] Se ha omitido el número ${contador}.`);
            contador++; 
            continue; 
        }
        console.log(`Contando... ${contador}`);
        contador++;
    }
    console.log("--- CONTEO FINALIZADO ---");
}
contadorPersonalizado();*/





