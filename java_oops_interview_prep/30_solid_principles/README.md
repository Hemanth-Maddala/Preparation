# SOLID Principles

## What is it?

Five principles for maintainable OOP code. One sentence each:

- **S**ingle Responsibility - a class has ONE reason to change.
- **O**pen/Closed - open for extension, closed for modification.
- **L**iskov Substitution - a subclass must be replaceable by its parent without breaking behavior.
- **I**nterface Segregation - many small interfaces beat one fat interface.
- **D**ependency Inversion - depend on abstractions, not concretions.

## Example

`Main.java` contains a tiny BAD then GOOD version of each. Run it; the output only exercises the O and D parts, but read all five side by side.

## Flow (per principle)

```
S: Report / ReportSaver / ReportPrinter   <- one job each
O: Shape(abstract) + Circle/Rectangle     <- add a shape, edit nothing
L: Square extends Rectangle = VIOLATION   <- don't fake IS-A
I: Worker + Eater instead of RobotWorker  <- robots don't eat
D: Notifier depends on MessageService     <- injected, swappable
```

## Important lines

```java
abstract double area();            // O: extension point
Notifier(MessageService s) {...}   // D: abstraction injected
implements Worker, Eater           // I: small interfaces
```

## Interview questions

1. Name all five SOLID principles.
2. What does the L stand for?
3. How does Dependency Inversion differ from Dependency Injection?

## Interview answer

S - one responsibility per class. O - extend behavior by adding code, not editing existing code. L - children must be usable wherever their parent is, without breaking logic. I - prefer several focused interfaces. D - high-level code should rely on abstractions (interfaces), not concrete classes; dependency injection is the common way to deliver that abstraction.

## Common mistake

Treating SOLID as a checklist of frameworks. It is about honoring the *why*: change becomes local, predictable, and safe.

## Remember

- One reason to change (S).
- Extend, don't modify (O).
- Substitutable children (L).
- Small interfaces (I).
- Depend on abstractions (D).
