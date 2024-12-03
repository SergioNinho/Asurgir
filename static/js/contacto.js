window.onload=inicio;

function inicio(){
	document.getElementById("abrir_form").onclick = contacto;
	document.getElementById("contenedor_cerrar").onclick = ocultar;
	document.getElementById("").onclick = cargando;
}


function contacto(){
	let form=document.getElementById("contactanos");
	
	form.style.display = "block";
	form.style.position = "relative";	

}
function cargando(){
	let cargar=document.getElementById("cargando");
	
	cargar.style.display = "block";
	cargar.style.position = "relative";	

}
function ocultar(){
let ocultar=document.getElementById("contactanos");
ocultar.style.display = "none" ;

}