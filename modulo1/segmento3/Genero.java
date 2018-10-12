import java.util.Scanner;

public class Genero {
	public static void main (String args []) {
	
		Scanner teclado = new Scanner(System.in);
		
		System.out.print(" ingrese su genero (m/f): ");
		String Genero = teclado.nextLine();

		if (Genero.toUpperCase().equals("M")) {
			System.out.println(" es varon ");

		} else {
			System.out.println(" es mujer ");
		}
	}
}




		
