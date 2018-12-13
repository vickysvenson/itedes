function exponenciar() {
	let resultado = base;

	for(let i = 1; i < exponente; i++)
		resultado *= base;

	return resultado;
}


function potenciar() {
	base = parseInt(prompt('base: '));
	exponente = parseInt(prompt('exponente: '));
	const resultado = exponenciar(base, exponente);

	alert(resultado);
}	
