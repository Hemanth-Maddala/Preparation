// ============================================================
// 24 - TOSTRING
// Object's default: ClassName@hexHash. Override for readability.
// println(obj) calls obj.toString() automatically.
// ============================================================

class Student {
    String name;
    int rollNo;

    Student(String name, int rollNo) {
        this.name = name;
        this.rollNo = rollNo;
    }

    // Without this, output would be Student@1b6d3586 style.
    @Override
    public String toString() {
        return "Student{name='" + name + "', rollNo=" + rollNo + "}";
    }
}

public class Main {
    public static void main(String[] args) {
        Student s = new Student("Ravi", 7);

        // Both lines print the SAME thing: println calls toString().
        System.out.println(s);
        System.out.println(s.toString());

        // String concatenation also uses toString().
        String message = "Details: " + s;
        System.out.println(message);
    }
}
