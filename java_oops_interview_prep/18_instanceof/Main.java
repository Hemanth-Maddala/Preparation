// ============================================================
// 18 - INSTANCEOF
// Type check at runtime. Useful before a downcast.
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

public class Main {
    public static void main(String[] args) {
        Animal a = new Dog();

        System.out.println("a instanceof Dog    : " + (a instanceof Dog));
        System.out.println("a instanceof Animal : " + (a instanceof Animal));
        Object o = a;                       // via Object so the type check compiles
        System.out.println("a instanceof String : " + (o instanceof String));
        System.out.println("null instanceof X   : " + (null instanceof String));

        // Practical use: safe downcast.
        if (a instanceof Dog) {
            Dog d = (Dog) a;
            d.fetch();
        }
    }
}
