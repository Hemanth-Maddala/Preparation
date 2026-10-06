// ============================================================
// 14 - MULTIPLE INTERFACES
// A class can implement SEVERAL interfaces at once.
// Java allows multiple inheritance of TYPE (through interfaces),
// but NOT multiple inheritance of IMPLEMENTATION (through classes).
// ============================================================

interface Swimmer {
    void swim();
}

interface Runner {
    void run();
}

// One class, two contracts.
class Athlete implements Swimmer, Runner {
    @Override
    public void swim() {
        System.out.println("Swimming laps");
    }

    @Override
    public void run() {
        System.out.println("Running 5k");
    }
}

public class Main {
    public static void main(String[] args) {
        Athlete a = new Athlete();

        // Use the object through either interface type.
        Swimmer s = a;
        Runner r = a;

        s.swim();
        r.run();
    }
}
