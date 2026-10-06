// ============================================================
// 21 - COMPOSITION  (HAS-A, strong ownership)
// The whole CREATES and OWNS the part.
// The part has no life outside the whole.
// ============================================================

class Engine {
    void start() {
        System.out.println("Engine started");
    }
}

class Car {
    private Engine engine;    // Car HAS-A Engine

    // Composition: Car builds its own engine.
    // An engine has no reason to exist without the car that owns it.
    Car() {
        engine = new Engine();
    }

    void drive() {
        engine.start();
        System.out.println("Car is driving");
    }
}

public class Main {
    public static void main(String[] args) {
        Car c = new Car();      // engine is born with the car
        c.drive();

        // Nobody outside holds the engine reference - it belongs to car.
    }
}
