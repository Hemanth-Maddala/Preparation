# Instance Variables and Methods

## What is it?

**Instance variables** are fields declared inside a class; each object gets its own copy. **Instance methods** are non-static methods that run against one object and can read/write that object's variables.

## Example

Two `Counter` objects. `a.increment()` runs twice, `b.increment()` once. `a` and `b` hold independent state, which proves instance variables are per-object, not shared.

## Flow

```
Counter a --------------> count = 2     Counter b ----------------> count = 1
      (a.increment() twice)                  (b.increment() once)
```

## Important lines

```java
int count;              // instance variable (per object)
void increment() { count++; }   // instance method changes this object
a.display();   // uses a's state
b.display();   // uses b's state
```

## Interview questions

1. Where do instance variables live - class or object?
2. Can two objects of the same class have different field values?
3. What is the difference between an instance variable and a static variable?

## Interview answer

Instance variables are stored inside each object, so every object has its own independent copy. Instance methods operate on that specific object's data. Two objects of the same class can have completely different values in the same fields.

## Common mistake

Thinking fields are shared between objects. They are NOT - each `new` creates fresh copies. Only `static` fields are shared.

## Remember

- `new` object = fresh copy of all instance variables.
- Instance methods always run against one object (`this`).
- Two objects never interfere through instance variables.
- This is the foundation of "objects hold their own state".
