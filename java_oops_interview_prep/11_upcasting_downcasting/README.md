# Upcasting and Downcasting

## What is it?

**Upcasting** moves a reference up the hierarchy: child -> parent (`Animal a = new Dog();`). It is always safe because a Dog IS-A Animal. **Downcasting** moves down: parent -> child (`Dog d = (Dog) a;`). It is dangerous because the object might not actually be that subtype, causing `ClassCastException`.

## Example

`a = new Dog()` upcasts. `instanceof` guards the downcast before calling the Dog-only `fetch()`. Casting a `Cat` object to `Dog` would crash.

## Flow

```
Animal (speak)
   ^
   | upcast (safe, implicit)      Animal a = new Dog();
   |
 Dog (speak, fetch)
   ^
   | downcast (explicit cast)     Dog d = (Dog) a;
```

## Important lines

```java
Animal a = new Dog();       // upcasting: safe, implicit
Dog d = (Dog) a;            // downcasting: explicit, risky
if (a instanceof Dog) { }   // always guard a downcast
```

## Interview questions

1. Why is upcasting safe?
2. When is downcasting dangerous?
3. What is ClassCastException?
4. Why use instanceof before downcasting?

## Interview answer

Upcasting is safe because a child always IS-A parent. Downcasting claims the object is a specific subtype; if it is not, the JVM throws ClassCastException at runtime. So we check with `instanceof` first, then cast - the check makes the cast safe.

## Common mistake

Downcasting a reference that actually points to a different sibling (like Cat to Dog) - compiles fine but crashes at runtime. Always `instanceof` first.

## Remember

- Upcast = implicit, safe.
- Downcast = explicit `(Type)`, risky.
- ClassCastException if the object is the wrong type.
- `instanceof` before downcast.
