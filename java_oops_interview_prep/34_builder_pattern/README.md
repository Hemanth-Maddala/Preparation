# Builder Pattern

## What is it?

**Builder** constructs an object step by step with fluent method calls. It shines when a class has several optional parameters - constructors get unwieldy and easy to misuse.

## Problem it solves

With many fields, constructors become a mess: `Pizza("large", "mushroom", true)` - which parameter is which? With optional fields you would need many constructor overloads. The builder names every value: `.topping(...)` is obviously the topping.

## Example

`Pizza.Builder("large").topping("mushroom").extraCheese(true).build()`. The size is required (Builder's constructor), the rest are optional. Each setter returns `this` for chaining.

## Flow

```
new Builder("large")     required value
  .topping("mushroom")   optional 1
  .extraCheese(true)     optional 2
  .build()               -> immutable Pizza
```

## Important lines

```java
static class Builder { ... }
Builder topping(String t) { topping = t; return this; }   // chainable
Pizza build() { return new Pizza(this); }                 // produces object
private Pizza(Builder b) { ... }                          // only builder builds
```

## Interview questions

1. When should you use the Builder pattern?
2. How do you make setters chainable?
3. Builder vs many constructors?

## Interview answer

Builder is for classes with many optional parameters where constructors become confusing. The builder names each value, chains with `return this`, and `build()` creates an immutable object. It beats long constructors and constructor-overload explosions. In modern Java, record components with a constructor or small focused classes often suffice - use builder when the field count is genuinely high.

## Common mistake

Using a builder for 2-3 required fields. A plain constructor is simpler - KISS wins.

## Remember

- Many optional fields -> builder.
- Setters return `this` to chain.
- `build()` constructs the final object.
- Often pairs with immutability.
