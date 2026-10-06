# instanceof

## What is it?

`x instanceof Type` asks at runtime: "is the object x points to a Type (or a subclass of it)?" Returns `true`/`false`, and returns `false` for `null`.

## Example

A `Dog` object is `instanceof Dog`, `instanceof Animal`, but not `instanceof String`. The typical use: guard a downcast so it can never throw ClassCastException.

## Flow

```
a = new Dog()
a instanceof Dog    -> true   (is a Dog)
a instanceof Animal -> true   (Dog IS-A Animal)
a instanceof String -> false
```

## Important lines

```java
if (a instanceof Dog) {      // check BEFORE casting
    Dog d = (Dog) a;
}
(null instanceof String)     // false - no NPE
```

## Interview questions

1. What does instanceof do?
2. What happens with instanceof on null?
3. When is instanceof a code smell?

## Interview answer

instanceof tests whether an object is an instance of a given type (including subclasses) and is the safe way to guard a downcast. On null it returns false without error. Excessive instanceof chains in a loop can indicate a poor design - polymorphism (an overridden method) is usually the cleaner answer.

## Common mistake

Thinking instanceof checks the reference type. It checks the actual OBJECT type at runtime.

## Remember

- Checks the object, not the reference.
- Returns false for null.
- Best friend of downcasting.
- Many instanceof checks = reconsider design.
