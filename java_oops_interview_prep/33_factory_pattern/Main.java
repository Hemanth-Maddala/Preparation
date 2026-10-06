// ============================================================
// 33 - FACTORY PATTERN
// Move object creation into a factory so callers depend on an
// interface, not on which concrete class gets created.
// ============================================================

interface Shape {
    void draw();
}

class Circle implements Shape {
    public void draw() {
        System.out.println("Drawing a circle");
    }
}

class Rectangle implements Shape {
    public void draw() {
        System.out.println("Drawing a rectangle");
    }
}

// The factory decides WHICH concrete Shape to create.
class ShapeFactory {
    static Shape create(String type) {
        if (type.equalsIgnoreCase("circle")) {
            return new Circle();
        } else if (type.equalsIgnoreCase("rectangle")) {
            return new Rectangle();
        }
        throw new IllegalArgumentException("Unknown shape: " + type);
    }
}

public class Main {
    public static void main(String[] args) {
        // Caller never uses 'new Circle()' - it just asks the factory.
        Shape s1 = ShapeFactory.create("circle");
        Shape s2 = ShapeFactory.create("rectangle");

        s1.draw();
        s2.draw();
    }
}
