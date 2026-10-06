# Inheritance

## What is it?

Inheritance lets a **child** class (`Dog`) reuse and extend a **parent** class (`Animal`) using `extends`. It models an IS-A relationship: a Dog IS-A Animal. The child inherits the parent's accessible fields and methods and can add its own.

## Example

`Dog extends Animal`. `Dog` gets `name` and `eat()` for free, then adds `bark()`. This removes duplication - one definition of `eat()` serves all animals.

## Flow

```
Animal (name, eat())
   ^
   |
 Dog (bark())   <- IS-A Animal, inherits name + eat()
```

## Important lines

```java
class Dog extends Animal { }   // the IS-A link
d.name = "Bruno";              // using an inherited field
d.eat();                       // calling an inherited method
```

## Interview questions

1. What does the child inherit from the parent?
2. What does `extends` mean?
3. Is inheritance IS-A or HAS-A?
4. Can a child access private parent members?

## Interview answer

The child inherits all non-private fields and methods, plus the IS-A relationship and the parent type. Private members exist in the object but are not directly accessible - use protected/public or accessor methods. One parent class per child; multiple inheritance is not supported for classes.

## Common mistake

Using inheritance for a "uses" relationship (Car extends Wheel). Inheritance must express IS-A, otherwise composition is better.

## Remember

- `extends` = IS-A relationship.
- Child reuses non-private parent members.
- Child can add fields/methods.
- Private parent members are not directly accessible.
- One parent class per class in Java.
