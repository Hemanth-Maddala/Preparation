// ============================================================
// 19 - ASSOCIATION
// A "uses" relationship between independent classes.
// Teacher <--> Student: each can exist without the other.
// ============================================================

class Student {
    String name;

    Student(String name) {
        this.name = name;
    }
}

class Teacher {
    String name;

    Teacher(String name) {
        this.name = name;
    }

    // Teacher ASSOCIATED with Student: takes one as a parameter.
    void teaches(Student s) {
        System.out.println(name + " teaches " + s.name);
    }
}

public class Main {
    public static void main(String[] args) {
        Teacher t = new Teacher("Mr. Sharma");
        Student s = new Student("Ravi");

        // The relationship exists only when they interact.
        t.teaches(s);
    }
}
