// ============================================================
// 22 - == VS equals()
// ==      : compares REFERENCES (or primitive VALUES)
// equals(): compares logical CONTENT (must be overridden)
// ============================================================

class Student {
    int rollNo;

    Student(int rollNo) {
        this.rollNo = rollNo;
    }

    // Define what "equal" means: same roll number.
    @Override
    public boolean equals(Object o) {
        if (!(o instanceof Student)) {
            return false;
        }
        Student other = (Student) o;
        return rollNo == other.rollNo;
    }
}

public class Main {
    public static void main(String[] args) {
        Student a = new Student(7);
        Student b = new Student(7);
        Student c = a;

        System.out.println("a == b        : " + (a == b));       // false: diff objects
        System.out.println("a == c        : " + (a == c));       // true:  same object
        System.out.println("a.equals(b)   : " + a.equals(b));    // true:  same content

        // Strings: == compares references, equals() compares text.
        String s1 = "hi";
        String s2 = "hi";                       // same pool literal
        String s3 = new String("hi");           // brand new object
        System.out.println("s1 == s2      : " + (s1 == s2));     // true
        System.out.println("s1 == s3      : " + (s1 == s3));     // false
        System.out.println("s1.equals(s3) : " + s1.equals(s3));  // true
    }
}
