// ============================================================
// 25 - OBJECT CLASS
// EVERY class in Java extends java.lang.Object implicitly.
// Object gives us: toString, equals, hashCode, getClass, clone, ...
// ============================================================

class Student extends Object {    // 'extends Object' is implicit anyway
    String name;

    Student(String name) {
        this.name = name;
    }

    // We OVERRIDE Object's methods to give them meaning:
    @Override
    public String toString() {
        return "Student(" + name + ")";
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof Student)) {
            return false;
        }
        return name.equals(((Student) o).name);
    }
}

public class Main {
    public static void main(String[] args) {
        Student s = new Student("Ravi");

        System.out.println(s);                    // our toString
        System.out.println("class: " + s.getClass().getSimpleName());  // getClass()

        // equals() and hashCode() exist because of Object.
        System.out.println("equals itself: " + s.equals(s));
        System.out.println("hashCode: " + s.hashCode());
    }
}
