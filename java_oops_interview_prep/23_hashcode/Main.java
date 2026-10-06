// ============================================================
// 23 - HASHCODE  (and the equals()/hashCode() contract)
// CONTRACT: if a.equals(b) is true,
//           then a.hashCode() MUST equal b.hashCode().
// ============================================================

class Student {
    String name;
    int rollNo;

    Student(String name, int rollNo) {
        this.name = name;
        this.rollNo = rollNo;
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof Student)) {
            return false;
        }
        Student other = (Student) o;
        return name.equals(other.name) && rollNo == other.rollNo;
    }

    // Equal objects MUST produce equal hashCodes.
    @Override
    public int hashCode() {
        return 31 * rollNo + name.hashCode();
    }
}

public class Main {
    public static void main(String[] args) {
        Student a = new Student("Ravi", 7);
        Student b = new Student("Ravi", 7);

        System.out.println("a.equals(b)      : " + a.equals(b));
        System.out.println("a.hashCode()     : " + a.hashCode());
        System.out.println("b.hashCode()     : " + b.hashCode());

        // Consistent hashCode + equals -> HashSet deduplicates correctly.
        java.util.Set<Student> set = new java.util.HashSet<>();
        set.add(a);
        set.add(b);
        System.out.println("set size (want 1): " + set.size());
    }
}
