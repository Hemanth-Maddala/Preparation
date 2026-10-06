# final

## What is it?

`final` is a lock:
- **final variable** - cannot be reassigned.
- **final method** - cannot be overridden.
- **final class** - cannot be extended.

It says nothing about the object itself being unchangeable.

## Example

`Point` is a final class with a final field. `lock()` is a final method - `Child` cannot override it. `MAX` cannot be reassigned. The `StringBuilder` is a `final` reference but its content still changes - proving final != immutable.

## Flow

```
final variable -> cannot reassign       final int MAX = 100; MAX = 200;  ERROR
final method   -> cannot override       final void lock() { }
final class    -> cannot extend         final class Point { }
final ref      -> object STILL mutable  sb.append(...) works
```

## Important lines

```java
final int MAX = 100;              // constant-like
final void lock() { }             // locked behavior
final class Point { }             // sealed from subclassing
final StringBuilder sb = ...;     // ref fixed, object mutable
```

## Interview questions

1. What can final apply to and what does each mean?
2. Does final make an object immutable?
3. Can a final field be set after the constructor starts?

## Interview answer

final on a variable prevents reassignment; on a method prevents overriding; on a class prevents extending. It does not freeze the object - a final reference to a mutable object still allows that object's contents to change. A final field must be assigned exactly once (at declaration, in an initializer, or in the constructor).

## Common mistake

Assuming `final List` is immutable. It is not - you just cannot point the reference elsewhere. Immutability is a separate design decision.

## Remember

- final variable = no reassign.
- final method = no override.
- final class = no subclass.
- final reference != immutable object.
