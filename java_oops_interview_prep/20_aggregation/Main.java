// ============================================================
// 20 - AGGREGATION  (HAS-A, weak ownership)
// The "whole" holds a reference to the "part",
// but the PART can exist independently of the whole.
// ============================================================

class Employee {
    String name;

    Employee(String name) {
        this.name = name;
    }

    void work() {
        System.out.println(name + " is working");
    }
}

class Department {
    String name;
    Employee[] employees;     // Department HAS-A Employees

    // Employees are passed IN from outside -> they exist without us.
    Department(String name, Employee[] employees) {
        this.name = name;
        this.employees = employees;
    }
}

public class Main {
    public static void main(String[] args) {
        // Employees created and owned by the caller, not the Department.
        Employee e1 = new Employee("Ravi");
        Employee e2 = new Employee("Priya");

        Department dept = new Department("IT", new Employee[] { e1, e2 });

        // Even if 'dept' disappears, e1/e2 keep living.
        e1.work();
        e2.work();
        System.out.println(dept.name + " department has " + dept.employees.length + " employees");
    }
}
