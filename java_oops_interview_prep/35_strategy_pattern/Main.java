// ============================================================
// 35 - STRATEGY PATTERN
// Define an interface for a behavior, put each variant in its own
// class, and let a CONTEXT hold any strategy.
// Kills big if/else chains; behavior can change at runtime.
// ============================================================

interface PaymentStrategy {
    void pay(int amount);
}

class CardPayment implements PaymentStrategy {
    @Override
    public void pay(int amount) {
        System.out.println("Paid " + amount + " using Card");
    }
}

class UPIPayment implements PaymentStrategy {
    @Override
    public void pay(int amount) {
        System.out.println("Paid " + amount + " using UPI");
    }
}

// CONTEXT: holds a strategy and delegates to it.
class ShoppingCart {
    private PaymentStrategy strategy;

    void setPaymentStrategy(PaymentStrategy strategy) {
        this.strategy = strategy;
    }

    void checkout(int amount) {
        strategy.pay(amount);        // delegate - no if/else here
    }
}

public class Main {
    public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();

        // Same cart, different payment behavior - swapped at runtime.
        cart.setPaymentStrategy(new CardPayment());
        cart.checkout(100);

        cart.setPaymentStrategy(new UPIPayment());
        cart.checkout(50);
    }
}
