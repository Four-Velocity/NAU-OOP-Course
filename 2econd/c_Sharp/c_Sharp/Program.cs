using System;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

namespace c_Sharp
{
    public class Figure
    {
        public virtual double area() {return 0.0;}

        public virtual double perimeter() {return 0.0;}
    }

    public class Reactangle : Figure
    {
        public double ax, ay, bx, by, cx, cy, dx, dy, horizontal, vertical;
        public Reactangle(double ax, double ay, double cx, double cy)
        {
            this.ax = ax;
            this.ay = ay; 
            bx = ax;
            by = cy;
            this.cx = cx;
            this.cy = cy;
            dx = cx;
            dy = ay;
            horizontal = cx - ax;
            vertical = cy - ay;
        }

        public override double area()
        {
            return this.horizontal * this.vertical;
        }

        public override double perimeter()
        {
            return 2.0 * (this.horizontal + this.vertical);
        }
    }

    public class Circle : Figure
    {
        public double radius;

        public Circle(double radius)
        {
            this.radius = radius;
        }

        public override double area()
        {
            return Math.PI * Math.Pow(this.radius, 2.0);
        }

        public override double perimeter()
        {
            return 2.0 * Math.PI * this.radius;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Так розташовані вугли прямокутника\nB--------C\n|        |\n|        |\nA--------D\n");
            double ax = 0.0, ay = 0.0, cx = 40.0, cy = 15.0;
            var rectangle = new Reactangle(ax, ay, cx, cy);
            Console.Write($"A(x) = {ax}\nA(y) = {ay}\nC(x) = {cx}\nC(y) = {cy}\n");
            Console.WriteLine($"Площа прямокутника = {Math.Round(rectangle.area(), 4)}");
            Console.WriteLine($"Периметр прямокутника = {Math.Round(rectangle.perimeter(), 4)}\n");

            double radius = 18.00;
            var circle = new Circle(radius);
            Console.WriteLine($"Площа кругу = {Math.Round(circle.area(), 4)}");
            Console.WriteLine($"Периметр кругу = {Math.Round(circle.perimeter(), 4)}");
        }
    }
}