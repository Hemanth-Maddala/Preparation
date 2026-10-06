// ============================================================
// 02 - INSTANCE VARIABLES AND METHODS
// Instance state belongs to each object. Methods act on it.
// ============================================================

class Counter {
    // Instance variables: every Counter object has its OWN copy.
    int count;

    // Instance method: reads and changes THIS object's state.
    void increment() {
        count++;               // 'count' here means this.count
    }

    void display() {
        System.out.println("count = " + count);
    }
}

public class Main {
    public static void main(String[] args) {
        Counter a = new Counter();
        Counter b = new Counter();

        a.increment();
        a.increment();
        b.increment();

        // Same methods, different objects -> different state.
        a.display();   // count = 2
        b.display();   // count = 1
    }
}
