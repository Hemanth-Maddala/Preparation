# The Object Class

## What is it?

`java.lang.Object` is the **root of every class**. If you do not write `extends`, your class implicitly extends Object. That is why every object has `toString()`, `equals()`, `hashCode()`, `getClass()`, and more.

## Example

`Student extends Object` (implicit). It overrides `toString()` and `equals()`; `getClass()` and `hashCode()` still come from Object.

## Important Object methods

- `toString()` - text representation; default ClassName@hash.
- `equals(Object)` - reference equality by default.
- `hashCode()` - int hash; must match equals().
- `getClass()` - final; returns the RUNTIME class (object type).
- `clone()` - shallow copy; rarely used, requires Cloneable.
- `finalize()` - legacy; deprecated. Do NOT manage lifecycle with it. Use try-with-resources / AutoCloseable / constructors instead.

## Important lines

```java
s.getClass().getSimpleName();   // runtime class: "Student"
s.toString();                   // inherited unless overridden
```

## Interview questions

1. What methods does every Java class inherit?
2. What does getClass() return?
3. Should finalize() be used for cleanup?

## Interview answer

Every class inherits from Object, so every object has toString, equals, hashCode, getClass, clone, and finalize. getClass() returns the actual runtime class of the object. finalize() is legacy and unreliable - modern Java uses try-with-resources and AutoCloseable instead.

## Common mistake

Thinking finalize() is a normal cleanup mechanism. It is deprecated and unpredictable; never rely on it.

## Remember

- Object is the root of all classes.
- Inherited methods: toString, equals, hashCode, getClass.
- getClass() reveals the object type at runtime.
- finalize() is legacy, not modern lifecycle management.
