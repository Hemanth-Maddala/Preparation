# Class and Object

## What is it?

A **class** is a blueprint that describes what data (fields) and behavior (methods) an object has. An **object** is a concrete instance of that blueprint, created with `new`. The variable that points to the object is called a **reference variable**.

## Example

`Student` is the class (blueprint). `s1` and `s2` are two separate objects made from that blueprint. Each object carries its own `name` and `rollNo`, so changing one does not affect the other.

## Flow

```
Student (blueprint: name, rollNo, introduce())
        |
        |  new
        v
  +------------+      +------------+
  | s1 (Ravi)  |      | s2 (Priya) |
  | rollNo = 1 |      | rollNo = 2 |
  +------------+      +------------+
```

## Important lines

```java
Student s1 = new Student();   // 'new' creates the object
s1.name = "Ravi";             // reference variable accesses object
Student s2 = new Student();   // a second independent object
```

## Interview questions

1. What is the difference between a class and an object?
2. What does the `new` keyword do?
3. What is a reference variable?
4. How many objects does `Student s = new Student();` create?

## Interview answer

A class is a blueprint describing state and behavior. An object is one concrete instance of that blueprint, created with `new`, holding its own copy of the state. The reference variable just points to the object in memory.

## Common mistake

Thinking `Student s1 = new Student();` creates two things named Student. It creates ONE object; `s1` is just a reference (like a remote control) pointing to it.

## Remember

- Class = blueprint, object = instance.
- `new` allocates the object.
- Reference variable points to the object; it is not the object.
- Multiple objects from one class are fully independent.
