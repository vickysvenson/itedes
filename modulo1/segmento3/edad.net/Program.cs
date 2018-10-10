using System;

namespace edad.net
{
    class Program
    {
        static void Main(string[] args)
        {
           Console.WriteLine(" ingrese su edad :");
		   int edad =Int32.Parse(Console.ReadLine());
		   if(edad >= 18)
		   {
				   Console.WriteLine("ud.es mayor " ) ;
		   }
        }
    }
}
