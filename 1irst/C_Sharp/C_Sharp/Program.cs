using System;

namespace C_Sharp
{
    public class BaseString 
    {
        protected string value;
    
        public BaseString(string v) {value = v;}
    
        public int len() {
            int result = 0;
            foreach(char c in this.value) {
                result++;
            }
            return result;
        }
    
        public string get() {
            return this.value;
        }
    }
    
    public class SymbolString : BaseString
    {
        public SymbolString(string v) :base(v) {}
        public string replace(char a, char b) {
            string result = this.value;
            for (int i = 0; i < this.len(); i++) {
                if (result[i] == a) {
                    string a1 = result.Substring(0, i);
                    string a2 = b.ToString();
                    string a3 = result.Substring(i+1);
                    result = a1 + a2 + a3;
                }
            }
            return result;
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            var baseS = new BaseString("Foo Bar");
            var symbolS = new SymbolString("Spam Eggs");
            Console.WriteLine($"Довжина базового рядка: {baseS.len()}");
            Console.WriteLine($"Довжина символьного рядка: {symbolS.len()}");
            Console.WriteLine("Замінемо 'g' на 'b' у символьному рядку");
            Console.WriteLine($"Результат: {symbolS.replace('g', 'b')}");
        }
    }
}