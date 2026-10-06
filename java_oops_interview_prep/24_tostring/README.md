# toString()

## What is it?

`toString()` returns a text representation of an object. `Object`'s default is `ClassName@hexHash`. Overriding it gives readable output for logging and debugging.

## Example

`Student` overrides `toString()` to print its fields. `System.out.println(s)` and `"Details: " + s` both trigger `s.toString()` automatically.

## Flow

```
println(s)  -->  s.toString()  -->  "Student{name='Ravi', rollNo=7}"
```

## Important lines

```java
@Override
public String toString() {
    return "Student{name='" + name + "', rollNo=" + rollNo + "}";
}
System.out.println(s);   // println calls toString() for you
```

## Interview questions

1. What does Object.toString() return by default?
2. Why override toString()?
3. How does println use toString()?

## Interview answer

The default toString() returns ClassName@hash. Overriding it makes objects print as readable text, which helps debugging. print/println and string concatenation call toString() automatically when they receive an object.

## Common mistake

Forgetting that printing a list of objects uses each element's toString(). `System.out.println(list)` prints the list's toString, not each element's.

## Remember

- Default: ClassName@hexHash.
- println/concatenation auto-call toString().
- Override for readable debugging output.
- Return a consistent, informative format.
