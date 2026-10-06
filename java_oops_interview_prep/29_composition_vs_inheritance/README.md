# Composition vs Inheritance

## What is it?

**Inheritance** (`Car extends Vehicle`) reuses behavior by IS-A. **Composition** (`Car has Engine`) reuses behavior by holding an object and delegating to it. The rule "favor composition over inheritance" means: when in doubt, choose composition - but inheritance is the right tool when a real IS-A relationship exists.

## Example

`Car extends Vehicle` - genuine IS-A, inherits `start()`. `Bike` uses composition: it owns an `Engine` and delegates `ignite()`. Bike exposes only what it wants.

## Flow

```
Inheritance:  Vehicle <-- Car      (IS-A, tight coupling to parent)
Composition:  Bike ---> Engine     (HAS-A, delegate, flexible)
```

## Important lines

```java
class Car extends Vehicle { }          // IS-A
private Engine engine = new Engine();  // HAS-A
engine.ignite();                       // delegation instead of inheritance
```

## When inheritance wins

- Genuine IS-A ("a Dog is an Animal").
- Child is really a specialized parent.
- Reusing a stable, non-changing parent API.

## When composition wins

- Code reuse without forcing a false IS-A.
- Parent API changes would break children.
- You want to expose only some behavior.

## Interview questions

1. Favor composition over inheritance - what does it mean?
2. When is inheritance the right choice?
3. Why does inheritance create coupling?

## Interview answer

Composition couples less: you hold a collaborator and delegate, choosing what to expose, and swaps are easy. Inheritance couples child to parent internals and any parent change can ripple through children. So prefer composition by default; use inheritance only for genuine IS-A relationships where the child truly is a specialized parent.

## Common mistake

Favoring composition "always". A Dog that is not an Animal is nonsense - inheritance is correct there. The rule is a default, not an absolute.

## Remember

- Inheritance = IS-A; composition = HAS-A.
- Composition = delegate to a field.
- Favor composition for flexibility.
- Use inheritance for real IS-A.
