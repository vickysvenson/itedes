using System;

namespace calculadora
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("ingrese una opcion (1 , 2 o 3): ");
			int opcion = Int32.Parse(Console.ReadLine());
			
			if (opcion == 1)
			{
				Console.WriteLine(" eligio 1 ");
			} else if (opcion == 2)
			{
				Console.WriteLine(" eligio 2 ");
			} else if (opcion == 3)
			{
				Console.WriteLine(" eligio 3 ");
			} else 
			{
				Console.WriteLine(" opcion invalida ");
			}
	


        }
    }
}
