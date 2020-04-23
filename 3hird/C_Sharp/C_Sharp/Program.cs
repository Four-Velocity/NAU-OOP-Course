using System;
using System.Collections.Generic;

namespace C_Sharp
{
    class String
    {
        protected string value;
        public String(string value)
        {
            this.value = value;
        }
        public int len()
        {
            return this.value.Length;
        }

        public void all_upper()
        {
            this.value = this.value.ToUpper();
        }

        public int compare(string str)
        {
            if (this.value == str) return 1;
            else return 0;
        }

        public string get()
        {
            return this.value;
        }
    }

    class Text
    {
        private List<String> Strings;

        public Text() {this.Strings = new List<String>();}
        
        private int length()
        {
            return this.Strings.Count;
        }
        
        public void show()
        {
            if (length() == 0)
            {
                Console.WriteLine("EMPTY!");
            }
            else
            {
                foreach (String str in Strings)
                {
                    Console.WriteLine(str.get());
                } 
            }
            
        }

        public void add(String str)
        {
            this.Strings.Add(str);
        }

        public void delete_one(int index = -1)
        {
            if (length() > 0)
            {
                if (index < 0)
                {
                    this.Strings.RemoveAt(this.Strings.Count + index);
                }
                else
                {
                    this.Strings.RemoveAt(index);
                }
            }
        }

        public void delete_all()
        {
            this.Strings.Clear();
        }

        public void delete_len(int del_len)
        {
            List<int> result;
            result = new List<int>();
            for (int i = 0; i < length(); i++)
            {
                if (this.Strings[i].len() == del_len) result.Add(i);
            }
            for (int i = 0; i < result.Count; i++) this.Strings.RemoveAt(result[i] - i);
        }

        public void upper()
        {
            foreach (String str in Strings)
            {
                str.all_upper();
            }
        }

        public void search(string search_str)
        {
            int result = 0;
            foreach (String str in Strings)
            {
                result += str.compare(search_str);
            }

            Console.WriteLine($"{result} '{search_str}' в тексті");
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            var s1 = new String("Foo Bar");
            var s2 = new String("Spam Eggs");
            var s3 = new String("Pupa Lupa");
            var s4 = new String("C++ is harder");

            var t1 = new Text();
            var t2 = new Text();
            var t3 = new Text();
            var t4 = new Text();

            List<Text> T;
            List<String> S;
            S = new List<String>();
            T = new List<Text>();
            
            T.Add(t1);
            T.Add(t2);
            T.Add(t3);
            T.Add(t4);
            
            S.Add(s1);
            S.Add(s2);
            S.Add(s3);
            S.Add(s4);
                
            foreach (Text t in T)
            {
                foreach (String s in S)
                {
                    t.add(s);                  
                }   
            }
            
            Console.WriteLine("Повне очищення");
            t1.delete_all();
            t1.show();
            Console.WriteLine("Видалення одного елемента");
            t2.delete_one();
            t2.delete_one(1);
            t2.show();
            Console.WriteLine("Видалення за довжиною");
            t3.delete_len(9);
            t3.show();
            Console.WriteLine("Інше");
            t4.add(s3);
            t4.search("Spam Eggs");
            t4.search("Pupa Lupa");
            t4.upper();
            t4.show();
        }
    }
}