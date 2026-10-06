# OOP + Generics Basics

## What is it?

Generics let you write one class/method and use it with many types: `Box<String>`, `Box<Integer>`. The real type is checked at **compile time**, giving type safety without casting.

## Example

`Box<T>` stores and returns a `T`. `Box<String>` gives back a `String` with no cast; `Box<Integer>` an `Integer`. Without generics you would store `Object` and cast on the way out - with a possible `ClassCastException`.

## Benefits

- **Type safety** - wrong types fail at compile time, not runtime.
- **Reusability** - one generic class serves all types.
- **No casting** - the compiler knows the type.

## Wildcards (basic level)

- `? extends Number` - read: "some subtype of Number" (upper bound).
- `? super Integer` - write: "some supertype of Integer" (lower bound).

Remember the rule of thumb: **extends = read/produce, super = write/consume**. For interviews, knowing they exist and when each is used is enough.

## Important lines

```java
class Box<T> { T get() { ... } }      // generic class
static <T> void printAll(List<T> list)  // generic method
Box<String> box = new Box<>();        // diamond: infer the type
```

## Interview questions

1. What problem do generics solve?
2. What does the diamond `<>` mean?
3. When would you use ? extends vs ? super?

## Interview answer

Generics provide compile-time type safety and let one class work with many types, removing manual casting. The diamond `<>` lets the compiler infer the type from the declaration. `? extends T` is for reading values (upper bound), `? super T` for writing (lower bound).

## Common mistake

Using raw types (`Box box = new Box()`) - that bypasses all generics checks and brings back unsafe casting. Always use the type parameter or diamond.

## Remember

- `<T>` = one generic, many types.
- Compile-time type safety.
- No casts needed.
- extends = produce, super = consume.
