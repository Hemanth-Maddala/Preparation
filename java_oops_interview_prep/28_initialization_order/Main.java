// ============================================================
// 28 - INITIALIZATION ORDER
// Order when an object is created:
//   1. static blocks (class load, parent first) - once per class
//   2. instance blocks - every new object, parent first
//   3. constructors - parent first, then child
// ============================================================

class Parent {
    static {
        System.out.println("1. Parent static block");
    }

    {
        System.out.println("3. Parent instance block");
    }

    Parent() {
        System.out.println("4. Parent constructor");
    }
}

class Child extends Parent {
    static {
        System.out.println("2. Child static block");
    }

    {
        System.out.println("5. Child instance block");
    }

    Child() {
        System.out.println("6. Child constructor");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Creating first Child:");
        new Child();

        System.out.println("Creating second Child:");
        new Child();
    }
}
