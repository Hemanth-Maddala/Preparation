// ============================================================
// 27 - CONSTRUCTOR CHAINING
// this(...) chains within the same class.
// super(...) chains to the parent class.
// Execution order: PARENT constructor completes FIRST.
// ============================================================

class Animal {
    Animal() {
        System.out.println("1. Animal constructor");
    }

    Animal(String name) {
        System.out.println("1. Animal(String) -> " + name);
    }
}

class Dog extends Animal {
    Dog() {
        this("Bruno");             // step 2: chain to sibling constructor
        System.out.println("4. Dog() constructor");
    }

    Dog(String name) {
        super(name);               // step 3: chain to parent
        System.out.println("3. Dog(String) constructor");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Creating new Dog():");
        new Dog();
    }
}
