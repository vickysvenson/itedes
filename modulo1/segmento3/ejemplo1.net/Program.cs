using System;

namespace ejemplo1.net
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("ingrese su edad ");
			int edad = Int32.Parse(Console.ReadLine());
			
			if (edad >= 18)
			{
					Console.WriteLine(" es mayor ");
			}
			else
			{
					Console.WriteLine(" es menor ");
					
        	}
		}
	}
}
