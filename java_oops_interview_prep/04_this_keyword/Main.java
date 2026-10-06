// ============================================================
// 04 - THIS KEYWORD
// 'this' = the current object. Resolves shadowing and chains.
// ============================================================

class Student {
    String name;

    // Parameter 'name' SHADOWS the field 'name'.
    // 'this.name' means the FIELD; 'name' alone means the parameter.
    Student(String name) {
        this.name = name;
    }

    // Constructor chaining: no-arg constructor delegates to (String).
    Student() {
        this("No name");      // this(...) MUST be the first statement
    }

    void display() {
        System.out.println("name = " + name);
    }
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student("Ravi");
        Student s2 = new Student();     // chains to this("No name")

        s1.display();
        s2.display();
    }
}
