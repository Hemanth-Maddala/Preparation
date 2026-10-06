// ============================================================
// 40 - OOP + EXCEPTIONS
// Checked vs unchecked, throw/throws, custom exception,
// and overriding rules for exceptions.
// ============================================================

// Custom CHECKED exception (extends Exception).
class InsufficientFundsException extends Exception {
    InsufficientFundsException(String message) {
        super(message);
    }
}

class BankAccount {
    private double balance;

    BankAccount(double balance) {
        this.balance = balance;
    }

    // 'throws' declares the checked exception the caller must handle.
    void withdraw(double amount) throws InsufficientFundsException {
        if (amount > balance) {
            throw new InsufficientFundsException("Not enough money");
        }
        balance -= amount;
    }
}

// Overriding + exceptions:
class Parent {
    void process() throws Exception {     // broad checked exception
        System.out.println("Parent process");
    }
}

class Child extends Parent {
    // Rule: override may throw SAME or NARROWER exceptions (or none).
    // It can NOT add new or broader checked exceptions.
    @Override
    void process() {                       // narrower: no throws at all
        System.out.println("Child process");
    }
}

public class Main {
    public static void main(String[] args) {
        // Checked exception forces handling.
        try {
            BankAccount acc = new BankAccount(50);
            acc.withdraw(100);
        } catch (InsufficientFundsException e) {
            System.out.println("Caught: " + e.getMessage());
        }

        // Unchecked (RuntimeException) - not forced to catch:
        try {
            String s = null;
            s.length();                    // NullPointerException
        } catch (NullPointerException e) {
            System.out.println("Caught unchecked NPE");
        }

        Parent p = new Child();
        try {
            p.process();
        } catch (Exception e) {            // ok: Parent declared it
            System.out.println(e.getMessage());
        }
    }
}
