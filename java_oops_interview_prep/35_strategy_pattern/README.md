# Strategy Pattern

## What is it?

**Strategy** extracts a behavior behind an interface, implements each variant as its own class, and gives a context a reference to whichever strategy it should use. The behavior is interchangeable at runtime.

## Problem it solves

Without strategy, payment looks like a huge if/else:

```java
if (type.equals("card")) { ... } else if (type.equals("upi")) { ... }
```

Every new type means editing that chain, and the method grows forever. Strategy turns each branch into a small class.

## Example

`PaymentStrategy` interface; `CardPayment` and `UPIPayment` implement it. `ShoppingCart` (the context) stores a strategy and delegates `checkout` to it. The same cart pays by card, then by UPI.

## Flow

```
            PaymentStrategy (pay)
               /           \
     CardPayment          UPIPayment
               \           /
              ShoppingCart (context)
                  checkout() -> strategy.pay(...)
```

## Important lines

```java
interface PaymentStrategy { void pay(int amount); }
class ShoppingCart { PaymentStrategy strategy; ... }
void checkout(int amount) { strategy.pay(amount); }   // delegation
cart.setPaymentStrategy(new UPIPayment());            // runtime swap
```

## Interview questions

1. What problem does Strategy solve?
2. Strategy vs if/else?
3. How is Strategy different from a simple interface implementation?

## Interview answer

Strategy encapsulates a family of algorithms behind an interface and lets a context delegate to any of them. It removes the if/else chains and makes each algorithm independently testable and swappable at runtime. The interface part alone is just abstraction; Strategy adds the context that holds and swaps the implementation.

## Common mistake

Hard-coding `new CardPayment()` inside the context - that is not strategy, it is a fixed dependency. The strategy must be injectable (constructor or setter).

## Remember

- Interface = the strategy contract.
- One class per variant.
- Context delegates and swaps strategies.
- Eliminates if/else branches.
