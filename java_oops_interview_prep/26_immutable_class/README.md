# Immutable Class

## What is it?

An **immutable** object never changes after creation. To build one: `final` class, `private final` fields, assign everything in the constructor, **no setters**, and make **defensive copies** of any mutable fields.

## Example

`Employee` stores `name` (String, already immutable) and `int[] scores` (mutable). Both constructor and getter use `Arrays.copyOf` so nobody outside can touch the internal array.

## Flow

```
caller passes int[]  ->  constructor COPIES it
caller mutates theirs -> our copy is safe
getScores() returns a COPY -> caller mutating it cannot hurt us
```

## Important lines

```java
final class Employee { }                     // no subclassing
private final int[] scores;                  // final field
this.scores = Arrays.copyOf(scores, ...);    // defensive copy in
Arrays.copyOf(scores, ...);                  // defensive copy out
```

## String is immutable

`String` follows this pattern: its char data never changes after creation. `s = s + "x"` creates a NEW String; the old one is untouched. That is why Strings are safe to share, cache, and use as map keys.

## final != immutable

`final` only locks the reference. The object can still change (`final StringBuilder sb` can still `.append()`). Immutability is an object-level guarantee; final is one tool used to build it.

## Interview questions

1. How do you make a class immutable?
2. Why use defensive copies?
3. Why is String immutable and what does it enable?

## Interview answer

Make the class final, fields private final, initialize all fields in the constructor, provide no setters, and copy mutable fields on the way in and out. This guarantees state never changes, which makes objects safe to share and use as keys. final alone is not enough - it only fixes the reference, not the object.

## Common mistake

Returning the internal array reference directly from a getter - the caller can now mutate private state. Always return a copy.

## Remember

- final class, private final fields, no setters.
- Defensive copy on input AND output.
- String is the classic example.
- final reference != immutable object.
