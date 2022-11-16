using System;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace vers
{
    class Program
    {
        static void Main(string[] args)
        {
            StreamWriter iro = new StreamWriter("vers.txt"); //megadja melyik fájlba írjon

            //kiiírja a fájlba a szöveget
            iro.WriteLine("Gil-galad was an Elven-king."); 
            iro.WriteLine("Of him the harpers sadly sing:");
            iro.WriteLine("the last whose realm was fair and free");
            iro.WriteLine("between the Mountains and the Sea.");
            iro.WriteLine();
            iro.WriteLine("His sword was long, his lance was keen,");
            iro.WriteLine("his shining helm afar was seen;");
            iro.WriteLine("the countless stars of heaven's field");
            iro.WriteLine("were mirrored in his silver shield.");
            iro.WriteLine();
            iro.WriteLine("But long ago he rode away,");
            iro.WriteLine("and where he dwelleth none can say;");
            iro.WriteLine("for into darkness fell his star");
            iro.WriteLine("in Mordor where the shadows are.");

            iro.Close();
            Console.ReadKey();
        }
    }
}
