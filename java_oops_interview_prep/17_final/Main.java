// ============================================================
// 17 - FINAL
// final variable : cannot be reassigned
// final method   : cannot be overridden
// final class    : cannot be extended
// IMPORTANT: final reference != immutable object.
// ============================================================

final class Point {                 // final class: no one extends Point
    private final int x;            // final field: assigned once

    Point(int x) { this.x = x; }

    int getX() { return x; }
}

class Base {
    final void lock() {             // final method: cannot be overridden
        System.out.println("locked behavior");
    }
}

class Child extends Base {
    // void lock() { }              // COMPILE ERROR: final method
}

public class Main {
    public static void main(String[] args) {
        final int MAX = 100;        // final variable
        // MAX = 200;               // COMPILE ERROR: cannot reassign

        final Point p = new Point(5);
        System.out.println(p.getX());

        // final REFERENCE, MUTABLE OBJECT:
        final StringBuilder sb = new StringBuilder("Java");
        sb.append(" OOP");          // the OBJECT changed
        System.out.println(sb);
        // sb = new StringBuilder(); // COMPILE ERROR: reference can't change
    }
}
