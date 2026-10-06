// ============================================================
// 08 - METHOD OVERLOADING
// Same method name, DIFFERENT parameter list.
// Decided at COMPILE TIME = compile-time polymorphism.
// ============================================================

class Calculator {
    int add(int a, int b) {
        System.out.println("add(int, int)");
        return a + b;
    }

    int add(int a, int b, int c) {
        System.out.println("add(int, int, int)");
        return a + b + c;
    }

    double add(double a, double b) {
        System.out.println("add(double, double)");
        return a + b;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator calc = new Calculator();

        System.out.println(calc.add(2, 3));
        System.out.println(calc.add(2, 3, 4));
        System.out.println(calc.add(2.5, 3.5));
    }
}
