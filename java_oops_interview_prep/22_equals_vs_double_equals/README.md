# == vs equals()

## What is it?

`==` on objects compares **references** - are both variables pointing to the SAME object? On primitives it compares values. `equals()` compares **logical content**, but only if the class overrides it; by default `Object.equals()` is just `==`.

## Example

Two `Student(7)` objects are different objects (`==` false), but equal by content (`equals()` true). For Strings, literal pooling makes `s1 == s2` true, but `new String("hi")` creates a new object so `==` is false while `equals()` is true.

## Flow

```
a = [obj#1: 7]    b = [obj#2: 7]     c -> points to obj#1
a == b  -> false   (references differ)
a == c  -> true    (same reference)
a.equals(b) -> true (content: rollNo 7 == 7)
```

## Important lines

```java
a == b;                 // references
a.equals(b);            // content (needs @Override)
@Override public boolean equals(Object o) { ... }
```

## Interview questions

1. Difference between == and equals()?
2. When is == used for primitives?
3. Why does `new String("hi") == "hi"` give false?

## Interview answer

`==` compares primitive values or object references - whether two variables point to the same object. `equals()` compares content and must be overridden to define equality for your class. Without an override, equals() behaves exactly like ==.

## Common mistake

Using `==` to compare Strings for equality. Always `s1.equals(s2)` (mind the null).

## Remember

- == = reference (or primitive value).
- equals() = content, needs override.
- Object.equals() is reference equality by default.
- Always override equals() with hashCode().
