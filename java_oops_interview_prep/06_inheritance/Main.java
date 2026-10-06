// ============================================================
// 06 - INHERITANCE
// Child extends Parent: IS-A relationship. Child inherits
// accessible members and can add its own.
// ============================================================

class Animal {
    String name;

    void eat() {
        System.out.println(name + " is eating");
    }
}

// 'extends' creates the IS-A relationship: a Dog IS-A Animal.
class Dog extends Animal {
    // Inherits name and eat() from Animal.
    void bark() {
        System.out.println(name + " says Woof");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.name = "Bruno";       // inherited field
        d.eat();                // inherited method
        d.bark();               // Dog's own method
    }
}
