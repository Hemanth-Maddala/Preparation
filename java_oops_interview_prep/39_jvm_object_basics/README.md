# JVM Object Basics

## What is it?

When you write `Student s = new Student();`, two things exist:
- a **reference variable** `s` (holds the address) - lives on the **stack** (or inside another object);
- the **Student object** with its fields - lives on the **heap**.

## Example

`Student s = new Student("Ravi")`: `s` is a stack reference, the object is on the heap. `Student s2 = s;` makes two references to the SAME heap object - `s == s2` is true and changing `s2.name` changes what `s` sees. Setting both to null drops the references, and the object becomes eligible for **garbage collection**.

## Flow

```
Stack                     Heap
s ---> [address]  --->   Student{ name = "Priya" }
s2 ---> [address] -------^   (same object)
```

## Important lines

```java
Student s = new Student("Ravi");  // reference on stack, object on heap
Student s2 = s;                   // two references, ONE object
s == s2                           // true - same address
s = null;                         // reference dropped -> GC eligible
```

## Garbage collection concept

GC finds heap objects with no live references and reclaims them automatically. You never `free` in Java; you drop references and let GC work.

## Interview questions

1. Where does the object live vs the reference?
2. What does `Student s2 = s;` really copy?
3. When does an object become eligible for GC?

## Interview answer

The reference is a stack variable holding the object's address; the object and its fields live on the heap. Assigning `s2 = s` copies the reference, not the object - both point to the same heap object. An object is eligible for GC when no reachable references point to it.

## Common mistake

Thinking `s2 = s` duplicates the object. It duplicates only the reference.

## Remember

- Stack = references; heap = objects.
- Two references can share one object.
- Setting references to null frees objects for GC.
- GC is automatic; you cannot (and need not) free manually.
