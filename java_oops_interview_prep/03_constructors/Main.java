// ============================================================
// 03 - CONSTRUCTORS
// Constructors initialize an object at creation time.
// ============================================================

class Student {
    String name;
    int rollNo;

    // No-arg constructor.
    Student() {
        name = "Unknown";
        rollNo = 0;
    }

    // Parameterized constructor (overloading).
    Student(String name, int rollNo) {
        this.name = name;      // 'this' = the object being created
        this.rollNo = rollNo;
    }

    void display() {
        System.out.println(name + " (roll " + rollNo + ")");
    }
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student();                 // no-arg
        Student s2 = new Student("Ravi", 7);        // parameterized

        s1.display();
        s2.display();
    }
}
