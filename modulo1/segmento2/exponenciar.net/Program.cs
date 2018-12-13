using System;

namespace exponenciar.net
{
    class Program
    {
	static int potenciar (int basex, int exponenciar){
		int resultado = basex;

		for(int i = 1; i < exponenciar; i++)
			resultado = resultado * basex;
		
		return resultado;
	}


        static void Main(string[] args)
        {
            Console.Write("base: ");
	    int basex = int.Parse(Console.ReadLine());

	    Console.Write("exponente: ");
	    int exponente = int.Parse(Console.ReadLine());

	    int resultado = potenciar(basex, exponente);
	    
	    Console.WriteLine(resultado);
        }
    }
}
