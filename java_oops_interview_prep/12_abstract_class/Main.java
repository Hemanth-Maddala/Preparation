// ============================================================
// 12 - ABSTRACT CLASS
// Cannot be instantiated. Can mix abstract + concrete members.
// ============================================================

abstract class Shape {
    String color;

    Shape(String color) {          // abstract classes CAN have constructors
        this.color = color;
    }

    abstract double area();        // abstract: no body, must be overridden

    void describe() {              // concrete: inherited as-is
        System.out.println(color + " shape");
    }
}

class Circle extends Shape {
    double r;

    Circle(String color, double r) {
        super(color);              // parent constructor runs
        this.r = r;
    }

    @Override
    double area() {
        return 3.14 * r * r;
    }
}

public class Main {
    public static void main(String[] args) {
        // Shape s = new Shape("red");  // COMPILE ERROR: abstract

        Shape s = new Circle("red", 2);   // concrete subclass
        s.describe();
        System.out.println("Area: " + s.area());
    }
}
