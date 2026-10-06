# Abstract Class

## What is it?

An **abstract class** is a partially implemented parent. It **cannot be instantiated** (`new Shape()` is a compile error). It may have abstract methods (no body) that subclasses must implement, plus fields, constructors, and concrete methods.

## Example

`Shape` is abstract: `area()` is abstract (each shape computes it differently), `describe()` is concrete (shared by all shapes). `Circle` implements `area()`. The constructor runs through `super(...)` when a Circle is built.

## Flow

```
abstract Shape (color field, constructor, abstract area(), concrete describe())
      ^  must implement area()
      |
   Circle (overrides area())
```

## Important lines

```java
abstract class Shape { }
abstract double area();          // no body
void describe() { }              // concrete - inherited as-is
Shape s = new Circle("red", 2);  // instantiate the SUBCLASS
```

## Interview questions

1. Can you instantiate an abstract class?
2. Can an abstract class have a constructor?
3. Abstract class vs interface?
4. Can an abstract class have no abstract methods?

## Interview answer

An abstract class cannot be instantiated; it is designed to be extended. It can have a constructor (it runs via super when a subclass is created), fields, concrete methods, and abstract methods that force subclasses to implement behavior. A class with zero abstract methods can still be declared abstract to prevent instantiation.

## Common mistake

Trying to do `new Shape()`. It will not compile - you must create an instance of a concrete subclass.

## Remember

- Cannot be instantiated directly.
- Can have constructor, fields, concrete + abstract methods.
- Abstract methods must be implemented by the first concrete subclass.
- Partial implementation for sharing among subclasses.
