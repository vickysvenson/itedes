import java.util.Scanner;

public class Ejercicio1 {
	public static void main(String args[]) { 
		Scanner teclado = new Scanner(System.in);

		String nombre;
		System.out.print("como te llamas: ");
		nombre = teclado.nextLine();
		
        Integer edad;
		System.out.print("cual es tu edad: ");
        edad = teclado.nextInt();
		
		System.out.println(nombre + " tiene " + edad.toString() + " años" );
	}  
}
