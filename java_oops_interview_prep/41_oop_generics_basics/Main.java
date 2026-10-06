// ============================================================
// 41 - OOP + GENERICS BASICS
// class Box<T>: write one class, use it with many types,
// with compile-time type safety and no casting.
// ============================================================

import java.util.ArrayList;
import java.util.List;

// Generic class: T is a placeholder for the real type.
class Box<T> {
    private T item;

    void set(T item) {
        this.item = item;
    }

    T get() {
        return item;
    }
}

// Generic method: <T> before the return type.
class Helper {
    static <T> void printAll(List<T> list) {
        for (T x : list) {
            System.out.print(x + " ");
        }
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {
        // One generic class, two concrete uses.
        Box<String> stringBox = new Box<>();
        stringBox.set("hello");
        String s = stringBox.get();      // no cast needed

        Box<Integer> intBox = new Box<>();
        intBox.set(42);
        Integer n = intBox.get();

        System.out.println("stringBox: " + s + ", intBox: " + n);

        // Without generics we would get raw Object and cast everywhere:
        // String s = (String) stringBox.get();   // risky cast

        // Generic method in action.
        Helper.printAll(List.of("a", "b", "c"));
        Helper.printAll(List.of(1, 2, 3));
    }
}
