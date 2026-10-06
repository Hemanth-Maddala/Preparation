// ============================================================
// 16 - STATIC
// Class-level, not object-level. One copy shared by all objects.
// ============================================================

class Counter {
    static int total = 0;     // ONE copy for the whole class
    int instanceCount = 0;    // per-object copy

    Counter() {
        total++;
        instanceCount++;
    }

    static void showTotal() {         // static method
        System.out.println("total objects = " + total);
        // System.out.println(instanceCount); // ERROR: no 'this' here
    }
}

public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        Counter c3 = new Counter();

        // Static accessed via the CLASS NAME (works via objects too).
        Counter.showTotal();

        // Instance variable differs per object.
        System.out.println("c3.instanceCount = " + c3.instanceCount);
        System.out.println("Counter.total    = " + Counter.total);
    }
}
