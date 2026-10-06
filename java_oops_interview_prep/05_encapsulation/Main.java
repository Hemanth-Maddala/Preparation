// ============================================================
// 05 - ENCAPSULATION
// Private data + public methods = controlled, validated access.
// ============================================================

class BankAccount {
    // Data hiding: no one outside this class can touch 'balance'.
    private double balance;

    BankAccount(double initial) {
        if (initial < 0) {
            throw new IllegalArgumentException("No negative balance");
        }
        balance = initial;
    }

    // Controlled access with validation.
    void deposit(double amount) {
        if (amount <= 0) {
            System.out.println("Rejected: amount must be positive");
            return;
        }
        balance += amount;
    }

    void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Rejected: amount must be positive");
            return;
        }
        if (amount > balance) {
            System.out.println("Rejected: insufficient funds");
            return;
        }
        balance -= amount;
    }

    // Read-only access: no setter exposed.
    double getBalance() {
        return balance;
    }
}

public class Main {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount(100);
        acc.deposit(50);
        acc.withdraw(200);          // rejected
        acc.withdraw(30);           // ok
        System.out.println("Balance: " + acc.getBalance());
    }
}
