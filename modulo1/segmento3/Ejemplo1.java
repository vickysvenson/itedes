import java.util.Scanner;
public class Ejemplo1 {
	public static void main (String args []){
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print(" ingrese su edad ");
		Integer edad= Integer.parseInt(teclado.nextLine());

		if (edad >=18){
				System.out.println(" es mayor de edad ");
		} else { 
				System.out.println(" es menor de edad ");
		
		}
	}
}

