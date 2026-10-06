// ============================================================
// 15 - ACCESS MODIFIERS
// private, (package-private/default), protected, public.
// Same-package demo. (Protected shines across packages.)
// ============================================================

class Employee {
    private String id;              // only inside this class
    String dept;                    // (default) same package only
    protected double salary;        // same package OR subclass (any pkg)
    public String name;             // everyone

    Employee(String id, String name, String dept, double salary) {
        this.id = id;
        this.name = name;
        this.dept = dept;
        this.salary = salary;
    }

    void showId() {                 // private is reachable INSIDE the class
        System.out.println("private id: " + id);
    }
}

public class Main {
    public static void main(String[] args) {
        Employee e = new Employee("E1", "Ravi", "IT", 50000);

        System.out.println("public name:  " + e.name);   // ok
        System.out.println("default dept: " + e.dept);   // ok (same package)
        System.out.println("protected:    " + e.salary); // ok (same package)
        // System.out.println(e.id);                      // ERROR: private

        e.showId();                 // class internals print their own id
    }
}
