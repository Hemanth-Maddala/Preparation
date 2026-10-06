// ============================================================
// 29 - COMPOSITION VS INHERITANCE
// Inheritance: Car extends Vehicle  (IS-A, reuse by inheritance)
// Composition: Car has Engine       (HAS-A, reuse by delegation)
// "Favor composition over inheritance" - but inheritance is fine
// when a genuine IS-A relationship exists.
// ============================================================

class Vehicle {
    void start() {
        System.out.println("Vehicle starts");
    }
}

// INHERITANCE: Car IS-A Vehicle.
class Car extends Vehicle {
    void openDoors() {
        System.out.println("Doors opened");
    }
}

class Engine {
    void ignite() {
        System.out.println("Engine ignited");
    }
}

class Bike {
    // COMPOSITION: Bike HAS-A Engine (delegates behavior).
    private Engine engine = new Engine();

    void ride() {
        engine.ignite();          // delegate, do not inherit
        System.out.println("Bike moving");
    }
}

public class Main {
    public static void main(String[] args) {
        Car car = new Car();
        car.start();              // inherited behavior
        car.openDoors();

        Bike bike = new Bike();
        bike.ride();              // composed behavior
    }
}
