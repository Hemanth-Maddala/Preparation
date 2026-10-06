// ============================================================
// 13 - INTERFACE
// A CONTRACT: what a class can do, without saying how.
// A class IMPLEMENTS an interface.
// ============================================================

interface Animal {
    void makeSound();            // implicit public abstract

    default void sleep() {       // default method: has a body
        System.out.println("Sleeping...");
    }

    static void describe() {     // static method: called on interface
        System.out.println("I am an Animal");
    }
}

class Dog implements Animal {
    @Override
    public void makeSound() {    // must be public (weakening not allowed)
        System.out.println("Woof");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal d = new Dog();    // program to the interface type
        d.makeSound();           // implemented by Dog
        d.sleep();               // inherited default
        Animal.describe();       // static - call on the interface
    }
}
