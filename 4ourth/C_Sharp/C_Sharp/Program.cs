using System;
using System.IO;
using System.Security.Permissions;

namespace C_Sharp
{
    class Handler
    {
        private double result;
        public double a, b, c, d;
        public Handler(double a, double b, double c, double d)
        {
            this.a = a;
            this.b = b;
            this.c = c;
            this.d = d;
            this.result = Double.NaN;
        }

        public double getResult()
        {
            if (Double.IsNaN(result)) throw new NotImplementedException("Значення ще не обчислене");
            else return this.result;
                
        }

        public double[] calculate(bool debug=false)
        {
            double first, second, third, fourth, fifth, sixth, seventh;
            double[] ret = new double[7];
            if (debug) Console.WriteLine("\nПочаток обчислення");
            if (debug) Console.Write($"[lg(4*{b}-{c})*{a}]/[{b}+{c}/{d}-1] = ");
            first = 4 * b;
            ret[0] = first;
            if (debug) Console.Write($"[lg({first}-{c})*{a}]/[{b}+{c}/{d}-1] = ");
            second = first - c;
            ret[1] = second;
            if (debug) Console.Write($"[lg({second})*{a}]/[{b}+{c}/{d}-1] = ");
            if (second <= 0) throw new InvalidDataException($"Базою логарифму не може бути {second}");
            third = Math.Log10(second);
            ret[2] = third;
            if (debug) Console.Write($"[{third}*{a}]/[{b}+{c}/{d}-1] = ");
            fourth = third * a;
            ret[3] = fourth;
            if (debug) Console.Write($"[{fourth}]/[{b}+{c}/{d}-1] = ");
            if (d == 0) throw new DivideByZeroException("d не може дорівнювати 0");
            fifth = c / d;
            ret[4] = fifth;
            if (debug) Console.Write($"[{fourth}]/[{b}+{fifth}-1] = ");
            sixth = b + fifth;
            ret[5] = sixth;
            if (debug) Console.Write($"[{fourth}]/[{sixth}-1] = ");
            seventh = sixth - 1;
            ret[6] = seventh;
            if (debug) Console.Write($"[{fourth}]/[{seventh}] = ");
            if (seventh == 0) throw new DivideByZeroException("b+c/d-1 не може дорівнювати 0");
            result = fourth / seventh;
            if (debug) Console.WriteLine($"{result}");
            return ret;
        }

        public void logger()
        {
            using (StreamWriter log = new StreamWriter("logs/c#.log.csv", true, System.Text.Encoding.Default))
            {
                double[] calc = new double[7];
                string literal = ", ";
                try
                {
                    calc = calculate();
                }
                catch (DivideByZeroException)
                {
                    log.Write("e0");
                }
                catch (InvalidDataException)
                {
                    log.Write("eL");
                }
                catch
                {
                    log.Write("e?");
                }

                try
                {
                    log.Write($"{getResult()}, {string.Join(literal, calc)}\r\n");
                }
                catch (NotImplementedException)
                {
                    log.Write($"eI\r\n");
                }
                
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            using (StreamReader values = new StreamReader("start_values.tsv", System.Text.Encoding.Default))
            {
                string line;
                using (StreamWriter log = new StreamWriter("logs/c#.log.csv", false, System.Text.Encoding.Default)){
                    log.Write("Result,First,Second,Third,Fourth,Fifth,Sixth,Seventh\r\n");
                }
                while ((line = values.ReadLine()) != null)
                {
                    String[] v = line.Split('\t');
                    var handler = new Handler(Convert.ToDouble(v[0]),Convert.ToDouble(v[1]),Convert.ToDouble(v[2]),Convert.ToDouble(v[3]));
                    handler.logger();
                }
            }
        }
    }
}