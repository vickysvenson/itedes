import java.util.Scanner;

public class Ejercicio1 {
	public static void main(String args[]) {
		Scanner teclado = new Scanner(System.in);
		   
		System.out.print("ingrese barrio: ");
		String barrio = teclado.nextLine();
		   
		System.out.print("ingrese direccion de la comisaria mas cercana : ");
		String direccion = teclado.nextLine();

		System.out.print("ingrese entrecalle1: ");
		String entrecalle1 = teclado.nextLine();

		System.out.print("ingrese entrecalle2: ");
		String entrecalle2 = teclado.nextLine();

		System.out.println(" la comisaria " + barrio + " queda en " + direccion + " entre " + entrecalle1 + " y " + entrecalle2);
	}
}
