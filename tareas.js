/*Saludo Personalizado 
Enunciado: Saluda al usuario por su nombre.
Requerimientos: Usar prompt() y console.log().

const nombre = prompt("¿Cual es tu nombre?");
console.log("Hola " + nombre);*/




/*Conversor de Moneda 
Enunciado: Convierte dólares a euros.
Requerimientos: Usar una constante para la tasa de cambio y parseFloat().

const tasaDeCambio = 0.85;
const dolares = parseFloat(prompt("Ingresa la cantidad en dólares:"));
const euros = dolares * tasaDeCambio;
console.log(dolares + " dólares son " + euros.toFixed(2) + " euros.");*/





/*Comparador de Números >
Enunciado: Pide dos números y di cuál es el mayor.
Requerimientos: Usar prompt() y una estructura if-elif-else.

const numero1 = parseFloat(prompt("Ingresa el primer número:"));
const numero2 = parseFloat(prompt("Ingresa el segundo número:"));

if (numero1 > numero2) {
    console.log(numero1 + " es mayor que " + numero2);
} else if (numero2 > numero1) {
    console.log(numero2 + " es mayor que " + numero1);
} else {
    console.log("Ambos números son iguales.");
}*/







/*Acceso a Club Nocturno 
Enunciado: Verifica si alguien puede entrar (mayor de edad Y con dinero).
Requerimientos: Usar el operador && (AND) en un if.

const edad = Number(prompt("¿Cual es tu edad?"));
const dinero = parseFloat(prompt("¿Cuanto dinero tienes?"));
const edadMinima = 18;
const dineroMinimo = 20.0;
if (edad >= edadMinima && dinero >= dineroMinimo) {
    console.log("Puedes entrar al club nocturno.");
} else {
    console.log("No puedes entrar al club nocturno.");
}*/




/*Día Laboral o Fin de Semana 
Enunciado: Dime qué tipo de día es según el nombre.
Requerimientos: Usar una estructura switch.

const dia = prompt("Ingresa el día de la semana:").toLowerCase();
switch (dia) {
    case "lunes":
    case "martes":
    case "miércoles":
    case "jueves":
    case "viernes":
        console.log(dia + " es un día laboral.");
        break;
    case "sábado":
    case "domingo":
        console.log(dia + " es fin de semana.");   
        break;
    default:
        console.log("Entrada no válida. Por favor, ingresa un día de la semana.");
        break;
}*/






/*Tabla de Multiplicar 
Enunciado: Muestra la tabla de multiplicar de un número.
Requerimientos: Pedir un número y usar un bucle for del 1 al 10.

const numero = parseInt(prompt("Ingresa un número para ver su tabla de multiplicar:"));
for (let i = 1; i <= 10; i++) {
    console.log(numero + " x " + i + " = " + (numero * i));
}*/ 







/*Cuenta Regresiva ⏲
Enunciado: Haz una cuenta regresiva desde un número hasta 0.
Requerimientos: Usar un bucle while.

let numero = parseInt(prompt("Ingresa un número para iniciar la cuenta regresiva:"));
while (numero >= 0) {
    console.log(numero);
    numero--;
}*/ 





/*Validador de Contraseña 
Enunciado: No dejes pasar al usuario hasta que escriba la contraseña correcta.
Requerimientos: Usar un bucle do-while.

const contraseñaCorrecta = josue0431*;
let contraseñaIngresada;
do {
    contraseñaIngresada = prompt("Ingresa la contraseña:");
} while (contraseñaIngresada !== contraseñaCorrecta);

console.log("Contraseña correcta. Acceso concedido.");*/







/*Sumador Acumulativo 
Enunciado: Pide números y súmalos hasta que el usuario ingrese un 0.
Requerimientos: Usar un bucle infinito (while(true)) y salir con break.

const tasaDeCambio = 0.85;
const dolares = parseFloat(prompt("Ingresa la cantidad en dólares:"));
const euros = dolares * tasaDeCambio;
console.log(dolares + " dólares son " + euros.toFixed(2) + " euros.");

let suma = 0;
while (true) {
    const numero = parseFloat(prompt("Ingresa un número para sumar (0 para terminar):"));
    if (numero === 0) {
        break;
    }
    suma += numero;
}
console.log("La suma total es: " + suma);*/






/*FizzBuzz Clásico 
Enunciado: Imprime números del 1 al 100, cambiando los múltiplos de 3 por "Fizz", los de 5 por "Buzz" y los de ambos por "FizzBuzz".
Requerimientos: Usar un bucle for y el operador módulo (%).

for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FizzBuzz");    
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }                                   
}*/









