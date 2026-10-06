// ============================================================
// 09 - METHOD OVERRIDING
// Child redefines a parent method with the SAME signature.
// Decided at RUNTIME when called through a parent reference.
// ============================================================

class Animal {
    void speak() {
        System.out.println("Animal speaks");
    }
}

class Dog extends Animal {
    @Override
    void speak() {
        System.out.println("Dog barks");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal a = new Dog();   // parent reference, child object
        a.speak();              // Dog's version runs

        Animal plain = new Animal();
        plain.speak();          // Animal's version runs
    }
}
