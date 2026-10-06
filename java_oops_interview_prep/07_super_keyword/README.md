# The `super` Keyword

## What is it?

`super` refers to the **parent class**. Three uses: `super.variable` reads a hidden parent field, `super.method()` calls the parent version of an overridden method, and `super(...)` invokes a parent constructor.

## Example

`Dog`'s constructor calls `super("Bruno")` first. In `speak()`, `super.speak()` runs Animal's version, then Dog adds its own line. `super.name` would reach Animal's field.

## Flow

```
Dog() -> super("Bruno") [Animal constructor runs first]
      -> Dog constructor body
speak() -> super.speak() [Animal.speak() prints]
        -> then Dog's own print
```

## Important lines

```java
super("Bruno");    // parent constructor call - MUST be first statement
super.speak();     // parent method call
super.name;        // parent field access
```

## Interview questions

1. What are the three uses of `super`?
2. Why must `super(...)` be the first statement in a constructor?
3. What happens if you don't call `super(...)` explicitly?

## Interview answer

`super` gives access to the parent: its fields, its methods, and its constructors. `super(...)` must be the first statement in a constructor because the parent part of the object must be built before the child adds anything. If you do not write it, the compiler inserts `super()` (the no-arg parent constructor).

## Common mistake

Thinking `super` and `this` are the same. `this` = current object, `super` = the parent part of the current object.

## Remember

- `super()` first line - parent constructor always runs first.
- `super.method()` calls the overridden parent method.
- `super.field` reaches a shadowed parent field.
- Compiler adds `super()` automatically if missing.
