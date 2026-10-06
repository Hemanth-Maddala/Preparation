// ============================================================
// 38 - DECORATOR PATTERN
// Wrap an object to ADD behavior dynamically, using composition.
// Coffee -> MilkDecorator -> SugarDecorator
// ============================================================

// Base interface.
interface Coffee {
    int cost();
}

// Concrete base implementation.
class PlainCoffee implements Coffee {
    @Override
    public int cost() {
        return 10;
    }
}

// DECORATOR: wraps a Coffee and adds behavior.
class MilkDecorator implements Coffee {
    private Coffee coffee;        // composition: wraps another Coffee

    MilkDecorator(Coffee coffee) {
        this.coffee = coffee;
    }

    @Override
    public int cost() {
        return coffee.cost() + 5;   // add milk
    }
}

class SugarDecorator implements Coffee {
    private Coffee coffee;

    SugarDecorator(Coffee coffee) {
        this.coffee = coffee;
    }

    @Override
    public int cost() {
        return coffee.cost() + 2;   // add sugar
    }
}

public class Main {
    public static void main(String[] args) {
        // Build layers at runtime: base + milk + sugar.
        Coffee coffee = new PlainCoffee();
        coffee = new MilkDecorator(coffee);
        coffee = new SugarDecorator(coffee);

        System.out.println("Total cost: " + coffee.cost());
    }
}
