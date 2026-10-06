# Decorator Pattern

## What is it?

**Decorator** adds behavior to an object **dynamically** by wrapping it in another object that implements the same interface and delegates, adding its own behavior on top.

## Example

`Coffee` is the interface. `PlainCoffee` is the base. `MilkDecorator` and `SugarDecorator` each wrap a `Coffee` and add cost. Layers are composed at runtime: `PlainCoffee + Milk + Sugar`.

## Flow

```
PlainCoffee(10)
   + MilkDecorator -> 10 + 5
      + SugarDecorator -> 15 + 2 = 17
```

## Decorator vs inheritance

Inheritance would require a class per combination (MilkSugarCoffee, SugarMilkCoffee...). Decorator composes the same wrappers in any order with far fewer classes.

## Important lines

```java
class MilkDecorator implements Coffee {
    private Coffee coffee;              // wrap the same interface
    public int cost() { return coffee.cost() + 5; }  // add behavior
}
coffee = new MilkDecorator(coffee);     // runtime layering
```

## Interview questions

1. What problem does Decorator solve?
2. Decorator vs inheritance?
3. How is Decorator different from Adapter?

## Interview answer

Decorator wraps an object to add behavior dynamically, without changing its interface, by composing wrappers at runtime. This avoids the combinatorial explosion of subclasses. Unlike the Adapter (which changes the interface), the Decorator keeps the same interface and just extends behavior.

## Common mistake

Confusing Decorator with Adapter. Adapter translates interfaces; Decorator keeps the interface and layers behavior.

## Remember

- Same interface, wrapped.
- Adds behavior at runtime.
- Avoids subclass explosion.
- Composition over inheritance.
