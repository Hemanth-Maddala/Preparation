# Constructor Chaining

## What is it?

Constructors call other constructors:
- `this(...)` - another constructor of the SAME class.
- `super(...)` - a constructor of the PARENT class.

Both must be the FIRST statement. A constructor can call `this(...)` or `super(...)`, never both.

## Example

`new Dog()` -> `this("Bruno")` -> `super(name)` -> Animal(String) runs -> back to Dog(String) -> back to Dog(). The parent body always finishes before any child body.

## Flow

```
new Dog()
  -> Dog()            step 2 (delegates)
  -> Dog(String)      step 3 (delegates)
  -> Animal(String)   step 1 RUNS FIRST
  back in Dog(String) prints
  back in Dog()       prints last
```

## Important lines

```java
Dog() { this("Bruno"); ... }       // same-class chaining
Dog(String n) { super(n); ... }    // parent chaining
// this(...) or super(...) must be the first statement
```

## Interview questions

1. What is constructor chaining?
2. Why must super() be the first statement?
3. Can a constructor call both this() and super()?

## Interview answer

Chaining means one constructor delegates to another via this() or super(). Parent code must run before child code because the parent part of the object must exist first, so the call is forced to be the first statement. A constructor uses this() OR super(), not both.

## Common mistake

Thinking the child constructor body runs before the parent's. It does not - the parent (or the chained constructor) finishes first.

## Remember

- this() -> same class; super() -> parent.
- First statement rule.
- Parent runs before child.
- this() and super() are mutually exclusive.
