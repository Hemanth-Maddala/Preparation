// ============================================================
// 34 - BUILDER PATTERN
// Many parameters -> fluent, readable construction.
// new Pizza.Builder("large").topping(...).extraCheese(true).build()
// ============================================================

class Pizza {
    private final String size;      // required
    private final String topping;   // optional
    private final boolean extraCheese; // optional

    // Private constructor: only the Builder can build a Pizza.
    private Pizza(Builder b) {
        this.size = b.size;
        this.topping = b.topping;
        this.extraCheese = b.extraCheese;
    }

    // Nested builder that mirrors the fields.
    static class Builder {
        private final String size;             // required via Builder ctor
        private String topping = "none";
        private boolean extraCheese = false;

        Builder(String size) {
            this.size = size;
        }

        Builder topping(String topping) {
            this.topping = topping;
            return this;                       // enables chaining
        }

        Builder extraCheese(boolean extraCheese) {
            this.extraCheese = extraCheese;
            return this;
        }

        Pizza build() {
            return new Pizza(this);
        }
    }

    @Override
    public String toString() {
        return "Pizza(" + size + ", " + topping + ", cheese=" + extraCheese + ")";
    }
}

public class Main {
    public static void main(String[] args) {
        // Readable, self-documenting construction.
        Pizza pizza = new Pizza.Builder("large")
                .topping("mushroom")
                .extraCheese(true)
                .build();

        // Optional fields can be skipped.
        Pizza plain = new Pizza.Builder("medium").build();

        System.out.println(pizza);
        System.out.println(plain);
    }
}
