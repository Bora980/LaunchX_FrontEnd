// Encontrar elementos de HTML

const titulo = document.getElementById("titulo");
const parrafo = document.getElementsByTagName("p");
const links = document.getElementsByClassName("links");

// Cambiar valores de HTML
titulo.innerHTML = "Título cambiado";
parrafo[0].innerHTML = "Párrafo cambiado";

document.getElementById("demo").innerHTML=
    "El texto en el parrafo (index 0) es : " + parrafo[0].innerHTML;

links[0].href = "https://www.google.com";
links[0].target = "_blank";

// Cambiar estilos

titulo.style.color = "red";

// Eventos

function cambiarTexto(obj){
    obj.innerHTML = "Texto clickeado";
}

function m0ver(obj){
    obj.innerHTML = "Mouse encima";
}

function m0ut(obj){
    obj.innerHTML = "Mouse fuera";
}

function mDown(obj){
    obj.style.backgroundColor = "#1ec5e5";
    obj.innerHTML = "sueltame";
} 

function mUp(obj){
    obj.style.backgroundColor = "#D94A38";
    obj.innerHTML = "gracias";
}

// addEvenListener

const boton = document.getElementById("boton");
boton.addEventListener("click", alerta);
//boton.addEventListener("click", () => alert("Hola Holaaaa")); // Aquí se hace con función flecha

function alerta(){
    alert("Hola Explorers");
}