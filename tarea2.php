<?php
//Ejercicio1: Saludo Personalizado
// Enunciado: Crea un script que guarde tu nombre y muestre un saludo como "Hola, Juan! Bienvenido a PHP."
// Requerimientos: Usa una variable, el operador de concatenación . e imprime con echo.

//$nombre = readline("ingrese su nombre: ");
//echo "hola, .$nombre .bienvenido a php";//







//Ejercicio: Calculadora Básica
//Enunciado: Declara dos números y calcula su suma, resta, multiplicación y división. Muestra cada resultado.
//Requerimientos: Usa variables para los números y los operadores +, -, *, /.


//$numero1 = (int) readline("ingrese un numero: ");
//$numero2 =(int)  readline("ingrese otro numero: ");

/*$suma = ($numero1 + $numero2 );
$resta = ( $numero1 - $numero2);
$multiplicación = ($numero1 * $numero2);
$division = ($numero1 / $numero2);

echo "Suma: " . ($numero1 + $numero2) . "\n";
echo "resta: " . ($numero1 - $numero2) . "\n";
echo "multiplicacion: " . ($numero1 * $numero2) . "\n";
echo "division: " . ($numero1 / $numero2) . "\n";*/








/*Ejercicio: Conversor de Moneda 💵➡️💶
* Enunciado: Convierte una cantidad en dólares a euros. Usa un tipo de cambio fijo (ej: 0.92).
* Requerimientos: Define una constante para el cambio y muestra el resultado final.*/


/*$dolares = (float)readline("ingrese la taza del dolar: ");
$euros = 0.92;

$covertidor_de_dolar_A_euro = $dolares/$euros;

echo "convertidor_de_dolar_a_euro: " . ($dolares / $euros) . "\n";*/



/*Ejercicio: ¿Mayor de Edad?
* Enunciado: Dada una edad, indica si la persona es mayor de edad (18+).
* Requerimientos: ¡Usa un if simple y el operador >=!*/


/*$edad = 18;

if ($edad >= 18) {
    echo "Eres mayor de edad.";
} else {
    echo "No eres mayor de edad.\n";
}    */









/*Ejercicio: ¿Par o Impar?
* Enunciado: Haz un script que diga si un número es par o impar.
* Requerimientos: La clave está en el operador módulo % y una estructura if-else.*/



/*$numero = (int) readline("ingrese un numero: ");

if ($numero == 0){
    echo "es cero";
} 
if else ($numero % 2 == 0){
    echo "es par"
}
else{
    echo "numero impar";
}*/










/*Ejercicio: Clasificación de Edades
* Enunciado: Según una edad, clasifica a la persona como niño, adolescente, adulto o adulto mayor.
* Requerimientos: ¡A usar if-elseif-else y operadores lógicos &&!*/


/*$edad = (int) readline("ingrese una edad: ");

if($edad <=1){
    echo "es un bebe"
}
elseif($edad >1 && $edad <=11){
     echo "is a child"
}
elseif($edad >11 && $edad<=17){
    echo "adolecente"
}
elseif($edad >17 && $edad <=50){
    echo "adulto"
}
else{
    "son viejos"
}*/








/*Ejercicio: Simulador de Login 
* Enunciado: Compara un usuario y contraseña ingresados con unos ya guardados. Muestra "Acceso concedido" o "Acceso denegado".
* Requerimientos: Necesitarás el operador de igualdad == y el lógico &&.*/


/*$nombre_usuario_correcto="admin";
$password_correcta = "21/09";

$usuario_ingresado = readline ("ingrese su admin: ");
$contrasena_ingresada =readline( "ingrese su password: ");

if (
    ($usuario_ingresado == $nombre_usuario_correcto &&
    $contrasena_ingresada == $password_correcta)
) {
    echo "acesso concedido";
}
else{
    echo "acceso denegado";
}*/








/*Ejercicio: Calculadora de Descuentos 🏷️
* Enunciado: Calcula el precio final de una compra aplicando descuentos según el monto (15% si > $100, 5% si está entre $50 y $100).
* Requerimientos: Usa if-elseif-else para calcular y mostrar el precio original, descuento y total.*/

/*$precioOriginal = 125.50; 

$porcentajeDescuento = 0;
$montoDescuento = 0;

if ($precioOriginal > 100) {
    $porcentajeDescuento = 0.15;
}
elseif ($precioOriginal >= 50 && $precioOriginal <= 100) {
    $porcentajeDescuento = 0.05;
}
else {
    $porcentajeDescuento = 0;
}
$montoDescuento = $precioOriginal * $porcentajeDescuento;
$precioFinal = $precioOriginal - $montoDescuento;

echo "--- Calculadora de Descuentos en PHP ---" . PHP_EOL;
echo " Precio Original:" . number_format($precioOriginal, 2) . PHP_EOL;

$porcentajeFormato = $porcentajeDescuento * 100;

if ($porcentajeDescuento > 0) {
    echo " Descuento Aplicado: " . $porcentajeFormato . "%" . PHP_EOL;
    echo " Monto del Descuento: -" . number_format($montoDescuento, 2) . PHP_EOL;
} else {
    echo " Descuento Aplicado: 0%" . PHP_EOL;
    echo " Monto del Descuento: -0.00" . PHP_EOL;
}
echo " Precio Final a Pagar: \" . number_format($precioFinal, 2) . PHP_EOL;
echo "----------------------------------------" . PHP_EOL;*/








/*Ejercicio: Días de la Semana
* Enunciado: Convierte un número del 1 al 7 al día de la semana correspondiente.
* Requerimientos: ¡Es el momento perfecto para usar la estructura switch-case con un default!*/

/*$dias_de_la_semana = readline("ingrese los dias de la semana: ");

switch($dias_de_la_semana){
    case "1":
    echo "es lunes";break;
    case "2":
    echo "es martes";break;

    case "3":
    echo "es miercoles";break;

    case "4":
    echo "es jueves";break;

    case "5":
    echo "es viernes";break;

    case "6": 
    echo "es sabado";break;

    case "7":
    echo "es domingo";break;

}*/







/*Ejercicio: Calificación Rápida
* Enunciado: Dada una nota (0-100), di si está "Aprobado" (>=60) o "Reprobado".
* Requerimientos: ¡Resuélvelo en una sola línea usando el operador ternario!*/

/*$nota = 75;
$resultado = ($nota >= 60) ? "Aprobado" : "Reprobado";
echo "la nota es: ". $resultado . PHP_EOL;*/










?>