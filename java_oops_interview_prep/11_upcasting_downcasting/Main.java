// ============================================================
// 11 - UPCASTING AND DOWNCASTING
// Upcast   = child -> parent   (safe, implicit)
// Downcast = parent -> child   (risky, needs explicit cast)
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

    void fetch() {
        System.out.println("Dog fetches");
    }
}

class Cat extends Animal {
    @Override
    void speak() {
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        // UPCASTING: Dog -> Animal. Safe because Dog IS-A Animal.
        Animal a = new Dog();
        a.speak();               // Dog's speak runs (polymorphism)
        // a.fetch();            // COMPILE ERROR: Animal has no fetch()

        // DOWNCASTING: back to Dog. Must check with instanceof first.
        if (a instanceof Dog) {
            Dog d = (Dog) a;     // explicit cast
            d.fetch();           // now we can call Dog-only methods
        }

        // DANGEROUS downcast: a is a Cat, NOT a Dog.
        Animal cat = new Cat();
        // Dog bad = (Dog) cat;  // ClassCastException at runtime!

        if (cat instanceof Dog) {
            System.out.println("won't reach here");
        } else {
            System.out.println("cat is not a Dog - cast safely skipped");
        }
    }
}
