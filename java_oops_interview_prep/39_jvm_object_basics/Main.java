// ============================================================
// 39 - JVM OBJECT BASICS (not a deep dive)
// Student s = new Student();
//  - 's' is a REFERENCE on the STACK (or inside an object).
//  - the Student OBJECT lives on the HEAP.
//  - GC reclaims heap objects no longer referenced.
// ============================================================

class Student {
    String name;

    Student(String name) {
        this.name = name;
    }
}

public class Main {
    public static void main(String[] args) {
        // Stack: variable 's'      -> holds the address/reference
        // Heap : the Student object -> holds its fields
        Student s = new Student("Ravi");

        // s1 and s2 refer to the SAME object: two references,
        // one object. Changing via one is visible via the other.
        Student s2 = s;
        s2.name = "Priya";

        System.out.println("s.name   = " + s.name);     // Priya
        System.out.println("same obj = " + (s == s2));  // true

        // Dropping the reference makes the object eligible for GC.
        s = null;
        s2 = null;
        System.out.println("references dropped - object can be collected");
    }
}
