# Factory Pattern

## What is it?

**Factory** centralizes object creation in one method/class. Callers ask the factory for an object and receive it through an interface, so they never depend on which concrete class was built.

## Problem it solves

Without a factory, every caller writes `new Circle()`, `new Rectangle()`, and editing the choice logic means touching every caller. The factory puts that choice in one place.

## Example

`ShapeFactory.create("circle")` returns a `Shape`. The caller only knows `Shape`. Adding a `Triangle` means editing the factory, not the callers.

## Flow

```
Caller --"circle"--> ShapeFactory --> new Circle()
Caller --"rectangle"--> ShapeFactory --> new Rectangle()
        result type: Shape (interface)
```

## Important lines

```java
static Shape create(String type) {   // the single decision point
    if (...) return new Circle();
    return new Rectangle();
}
Shape s = ShapeFactory.create("circle");  // caller stays decoupled
```

## When useful

- Creation logic is non-trivial (choice, config, caching).
- Callers should not care which concrete type they get.
- You want to test with different implementations.

## Interview questions

1. What problem does the Factory pattern solve?
2. Factory vs constructor?
3. When is a factory overkill?

## Interview answer

Factory separates creation from use: one method decides which concrete class to instantiate, and callers depend on the interface. This keeps changes local and supports testing and swapping implementations. For trivial `new` with no decision logic, a factory is overkill.

## Common mistake

Adding factories everywhere. If there is no decision or complexity in creation, a plain constructor is simpler.

## Remember

- Centralizes creation.
- Caller depends on the interface.
- Easy to add new types.
- Don't overuse.
