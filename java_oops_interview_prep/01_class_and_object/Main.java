// ============================================================
// 01 - CLASS AND OBJECT
// Class = blueprint. Object = instance. new creates the object.
// ============================================================

class Student {
    String name;   // instance field: every object gets its own copy
    int rollNo;

    void introduce() {
        System.out.println("Hi, I am " + name + " (roll " + rollNo + ")");
    }
}

public class Main {
    public static void main(String[] args) {
        // 'new Student()' allocates an object in the heap.
        // 's1' is a REFERENCE variable pointing at that object.
        Student s1 = new Student();
        s1.name = "Ravi";
        s1.rollNo = 1;

        // 's2' is a SECOND, independent object.
        Student s2 = new Student();
        s2.name = "Priya";
        s2.rollNo = 2;

        s1.introduce();
        s2.introduce();
    }
}
