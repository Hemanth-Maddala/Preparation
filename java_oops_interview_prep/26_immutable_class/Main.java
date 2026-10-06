// ============================================================
// 26 - IMMUTABLE CLASS
// final class + private final fields + constructor init
//             + no setters + defensive copies of mutable fields.
// ============================================================

import java.util.Arrays;

// final: cannot be extended (a subclass could break immutability).
final class Employee {

    private final String name;         // String is itself immutable
    private final int id;
    private final int[] scores;        // mutable field -> defensive copy

    Employee(String name, int id, int[] scores) {
        this.name = name;
        this.id = id;
        // Defensive copy: we keep OUR OWN array, not the caller's.
        this.scores = Arrays.copyOf(scores, scores.length);
    }

    // No setters - state can never change after construction.

    String getName() { return name; }
    int getId() { return id; }

    // Defensive copy on the way OUT too.
    int[] getScores() {
        return Arrays.copyOf(scores, scores.length);
    }
}

public class Main {
    public static void main(String[] args) {
        int[] original = { 90, 80, 70 };
        Employee e = new Employee("Ravi", 7, original);

        original[0] = 0;               // caller mutates their array...
        System.out.println("internal scores still intact: " + java.util.Arrays.toString(e.getScores()));

        int[] leaked = e.getScores();
        leaked[0] = 999;               // caller mutates the copy...
        System.out.println("original data still intact:   " + java.util.Arrays.toString(e.getScores()));
    }
}
