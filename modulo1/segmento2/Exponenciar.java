import java.util.Scanner;

public class Exponenciar {

	public static void main(String args []){
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("base: ");
		Integer base = Integer.parseInt(teclado.nextLine());

		System.out.print("exponente: ");
		Integer exponente = Integer.parseInt(teclado.nextLine());

		Integer resultado = potenciar(base,exponente);
		
		System.out.println(resultado);
	}

	public static Integer potenciar(Integer base , Integer exponente){
		Integer resultado = base;

		for(int i = 1; i < exponente; i++)
			resultado = resultado * base;

		return resultado;
	}
}
