import java.util.Scanner;

public class Ejercicio2 {
	public static void main(String args []) {
	
		Scanner teclado = new Scanner(System.in);
		System.out.print("ingrese un numero: ");
		
		Integer nro = Integer.parseInt(teclado.nextLine());
		Integer resto = nro % 2;

		if (resto == 0) {
				System.out.println(nro.toString() + " es par ");
		} else {
				System.out.println(nro.toString() + " no es par ");
		}
	}
}
