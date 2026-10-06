// ============================================================
// 10 - RUNTIME POLYMORPHISM  (VERY IMPORTANT)
//
// Two things matter for every variable:
//   REFERENCE TYPE : what the compiler lets you call
//   OBJECT TYPE    : which code actually runs
//
// Animal a = new Dog();
// REFERENCE TYPE = Animal  -> a.speak() must exist in Animal
// OBJECT TYPE    = Dog     -> Dog's speak() is what RUNS
//
// This is dynamic method dispatch.
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

class Cat extends Animal {
    @Override
    void speak() {
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        // The SAME parent reference points to DIFFERENT objects.
        Animal a = new Dog();
        a.speak();          // object type Dog  -> Dog.speak()

        a = new Cat();
        a.speak();          // object type Cat  -> Cat.speak()

        // Works in collections too - this is why polymorphism is useful.
        Animal[] zoo = { new Dog(), new Cat(), new Animal() };
        for (Animal animal : zoo) {
            animal.speak();   // each runs its OWN version
        }
    }
}
