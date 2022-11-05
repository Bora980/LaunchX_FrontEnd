console.log("\n**********Variables**********\n");
var numero1 = 4;
let numero2 = 6;
const numero3 = 0;
let numero4 = "4";
console.log("Número 1: "+ numero1 +" Nùmero 2"+ numero2+" Nùmero 3"+ numero3);

console.log("\n**********Cadenas**********\n");
var frase1 = "Ejemplo comillas dobles";
var frase2 = 'Ejemplo comillas simples';
var frase3 = `Ejemplo comillas ${numero1} invertidas`;
console.log(frase1 + "\n" + frase2 + "\n" + frase3);

/* Las condicionales se pueden usar valores como > < == === != y cada una tiene una
funcionalidad de comparación entre elementos*/

console.log("\n**********Condicionales*********\n");

console.log(numero1 === numero1);
console.log(numero1 < numero2);
console.log(numero3 != numero3);

console.log("Condición == ", numero1 == numero4 );
console.log("Condición === ", numero1 === numero4);

console.log("\n**********Operador lógico AND*********\n");
console.log((true && false && true)|| false);
console.log(numero1 === numero1 && numero1 < numero2);

console.log("\n**********Operador lógico OR*********\n");
console.log(false || true || (false && true));
console.log(numero2 > numero1 || numero3 != numero3);

console.log("\n**********Arreglos*********\n");
let listaDeNumeros = [2,3,5,7,11,234];

console.log(listaDeNumeros[5]);

// El Push pone los valores al arreglo 
listaDeNumeros.push(16);
listaDeNumeros.push(939);

// El Pop quita el último valor del arreglo
listaDeNumeros.pop();

console.log(listaDeNumeros);
console.log(listaDeNumeros.length);

let listaDePalabras = ["Explorer","MisionComander","LaunchX","Innovaccion","JavaScript"];
console.log(listaDePalabras);
console.log(listaDePalabras.length);

// Las cadenas (strings pueden ser tratadas como arreglos)

let palabra = "Explorer";
console.log(palabra[2]);
console.log(palabra.length);

console.log("\n**********Objetos*********\n");

let explorer = {
    nombre: "Nombre del Explorer",
    email: "email@innovaccion.mx",
    numReg: 12345,
    mision: "FronEnd",
    proyectos: ["Abogabot", "Taqueria", "Pastelería", "Vacunanión"],
    proPer:{
        escolar: "Tareas",
        profesional:"Trabajo",
        personal: "Negocio",
        cuantos: 3
    },
};

//console.log(explorer);

console.log(explorer.proPer.escolar);
console.log(
    "Proyectos: " + explorer.proPer.cuantos + " " + explorer.proPer.escolar);


// Fluno condicional

let number1 = 2;
let number2 = 6;

console.log("************* if / else ****************");
if(number1 > number2 && number2 > 5){
    var variable1= 3;
    console.log("El número 1 es mayor que número 2");
}

else if(number1 == number2 || number1 < 3){
    var variable1= 2;
    console.log("Los números son iguales");
}
else {
    var variable1= 1;
    console.log("El número 2 es mayor que número 1");
}

console.log(variable1);

// ciclo condicional

console.log("\n************** While **************\n");
let numberWhile = 5;

while (numberWhile <= 12){
    console.log(numberWhile);
    numberWhile = numberWhile + 2;
}
console.log("Aquí ya salió del while " + numberWhile);

//ciclo condicional de una iteración mínimo
console.log("\n************** Do While **************\n");
let numeroDoWhile = 12;
do {
    numeroDoWhile = numeroDoWhile + 2;
    console.log(numeroDoWhile);
} while (numeroDoWhile < 20);
console.log("Aquí sale del Do While " + numeroDoWhile);

// Ciclo for con iteración controlada
console.log("\n************** For **************\n");
let numeroFor = 0;
for (numeroFor; numeroFor <= 12; numeroFor = numeroFor + 1){
    console.log(numeroFor)
}
console.log("Aquí salimos del For " + numeroFor);

// Opciones para evitar anidar condicionales
console.log("\n************** Switch **************\n");
switch(prompt("¿Cómo está el clima?")){
    case "lluvioso":
        console.log("No te vayas a mojar");
        break;
    case "soleado":
        console.log("Ponte bloqueador");
        break;
    case "nublado":
        console.log("Tápate bien");
        break;
    default:
        console.log("No se como está el clima");
        break;
}
console.log("Aquí salimos del Switch");
