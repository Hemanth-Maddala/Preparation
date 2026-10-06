// ============================================================
// 31 - OOP DESIGN PRINCIPLES
// DRY, KISS, YAGNI, high cohesion, low coupling,
// separation of concerns, program to an interface,
// favor composition over inheritance.
// Focus: COHESION vs COUPLING.
// ============================================================

// DRY: Don't Repeat Yourself. Reused logic lives in ONE method.
class Tax {
    double compute(double amount, double rate) {
        return amount * rate / 100;
    }
}

// HIGH COHESION + LOW COUPLING example.
// Each class below does ONE job (cohesion) and knows only about
// small abstractions, not each other's internals (coupling).

interface Payment {
    void pay(double amount);
}

class CardPayment implements Payment {
    public void pay(double amount) {
        System.out.println("Card: " + amount);
    }
}

class Order {
    // Order depends on the Payment ABSTRACTION, not a concrete class.
    private Payment payment;

    Order(Payment payment) {
        this.payment = payment;
    }

    void checkout(double amount) {
        payment.pay(amount);          // low coupling: only talks to Payment
    }
}

public class Main {
    public static void main(String[] args) {
        // DRY in action: one method, two callers.
        Tax tax = new Tax();
        System.out.println("Tax A: " + tax.compute(1000, 18));
        System.out.println("Tax B: " + tax.compute(500, 5));

        // Low coupling + program to an interface.
        Order order = new Order(new CardPayment());
        order.checkout(999.0);
    }
}
