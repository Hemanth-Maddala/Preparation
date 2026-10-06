# Runtime Polymorphism

## What is it?

**Runtime polymorphism (dynamic method dispatch)** happens when a parent reference points to a child object: `Animal a = new Dog();`. The method that runs is chosen at **runtime by the OBJECT type**, not the reference type. This lets one variable behave differently for different objects.

## Example

`a` is declared as `Animal` (reference type) but points to `Dog` and then `Cat` objects. Calling `a.speak()` runs `Dog.speak()` then `Cat.speak()`. The exact same line `a.speak()` produces different behavior.

## Flow

```
       reference type: Animal
       a.speak()  ->  who runs?
                |
        +-------+--------+
        v                 v
   object: Dog        object: Cat
   Dog.speak()        Cat.speak()
        |
  RUNTIME checks the OBJECT, not the reference
```

## Important lines

```java
Animal a = new Dog();    // REFERENCE TYPE = Animal
                         // OBJECT TYPE    = Dog
a.speak();               // Dog.speak() runs - dynamic dispatch

Animal[] zoo = { new Dog(), new Cat() };
for (Animal x : zoo) x.speak();   // each object's own version
```

## Interview questions

1. What is runtime polymorphism?
2. `Animal a = new Dog(); a.sound();` - what runs and why?
3. What is dynamic method dispatch?
4. Why is polymorphism useful in real code?

## Interview answer

At runtime, Java looks at the actual object a reference points to and calls that object's method. In `Animal a = new Dog(); a.speak();`, the object is a Dog, so Dog.speak() runs. This is called dynamic method dispatch, and it lets us write code against a parent type that works for many child types.

## Common mistake

Assuming the reference type decides which method runs. It decides what you CAN call (the method must exist in Animal), but the object type decides HOW it runs. One more trap: fields are NOT polymorphic - only methods are.

## Remember

- Reference type = what compiles.
- Object type = what runs.
- Same line, different objects, different behavior.
- Only non-static methods are polymorphic.
