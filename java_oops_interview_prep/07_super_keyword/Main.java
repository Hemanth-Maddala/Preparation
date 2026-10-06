// ============================================================
// 07 - SUPER KEYWORD
// super.variable, super.method(), super(...) constructor call.
// ============================================================

class Animal {
    String name = "Animal";

    Animal(String name) {
        this.name = name;
        System.out.println("Animal constructor");
    }

    void speak() {
        System.out.println(name + " makes a sound");
    }
}

class Dog extends Animal {
    String name = "Dog field";   // shadows Animal.name

    Dog() {
        super("Bruno");          // super(...) calls parent constructor FIRST
        System.out.println("Dog constructor");
    }

    @Override
    void speak() {
        super.speak();           // super.method() runs the parent version
        System.out.println(name + " barks");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.speak();
    }
}
