# OOP Design Principles

## What is it?

Guidelines for readable, maintainable OOP:

- **DRY** - Don't Repeat Yourself. One copy of each piece of logic.
- **KISS** - Keep It Simple. The simplest design that works.
- **YAGNI** - You Aren't Gonna Need It. No speculative features.
- **High cohesion** - a class does one focused job well.
- **Low coupling** - classes depend on each other as little as possible.
- **Separation of concerns** - different problems live in different classes.
- **Program to an interface** - code against abstractions, not concretions.
- **Favor composition over inheritance** - delegate instead of inherit when possible.

## COHESION vs COUPLING (the classic question)

- **Cohesion**: how strongly the parts INSIDE a class belong together.
  High = all methods serve one clear purpose. Target: high.
- **Coupling**: how much one class depends on OTHERS.
  Low = changes in one class rarely force changes elsewhere. Target: low.

Good design = **high cohesion + low coupling**.

## Example

`Order` depends only on the `Payment` interface (low coupling, program to interface). `CardPayment` does one thing (high cohesion). `Tax.compute` is reused twice (DRY).

## Important lines

```java
class Order { Payment payment; Order(Payment p) {...} }  // low coupling
payment.pay(amount);        // depends on abstraction, not a concrete class
```

## Interview questions

1. Cohesion vs coupling - explain both and the target for each.
2. What does DRY mean? What is the downside of over-DRYing?
3. What does "program to an interface" mean?

## Interview answer

Cohesion is about a class's internal focus - high cohesion means each class owns one clear responsibility. Coupling is about inter-class dependence - low coupling means classes change independently. The ideal is high cohesion with low coupling. DRY avoids duplicated logic, but forcing reuse too hard can create tangled abstractions; KISS and YAGNI warn against complexity and speculative code.

## Common mistake

Mixing the two terms up. Remember: cohesion = inside a class, coupling = between classes.

## Remember

- High cohesion, low coupling = goal.
- DRY, KISS, YAGNI keep code simple.
- Program to interfaces.
- Favor composition over inheritance.
