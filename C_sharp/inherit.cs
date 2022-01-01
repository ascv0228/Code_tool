using System;
class ShapeApplications{
    abstract class Shape
    {
        public abstract double area {get;}
    }
    class Rectangle : Shape{
        private int _width;
        private int _height;
        public Rectangle (int h, int w){
            _height = h;
            _width  = w;
        }
        public override double area => _height*_width;
        public string info => $"Height : {_height}, Width : {_width}, Area : {area}"; 
    }
    class Circle : Shape{
        private int _radius;
        public Circle (int r){
            _radius = r;
        }
        public override double area => _radius*_radius*Math.PI;
    }
    
    class Program{
        static void Main() {
            Rectangle r = new Rectangle(3 ,5);
            Console.WriteLine($"Rectangle Area = {r.area}");
            Console.WriteLine(r.info);
            Circle c = new Circle(10);
            Console.WriteLine($"Circle Area = {c.area}");
        }
    }
}
