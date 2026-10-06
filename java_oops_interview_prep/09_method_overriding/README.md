# Method Overriding

## What is it?

Overriding = a child defines a method with the **same signature** (name + parameters) as the parent, replacing the parent's behavior. `@Override` is a safety annotation. The decision of which version runs happens at **runtime**, based on the object type.

## Example

`Dog` overrides `speak()`. Calling `a.speak()` where `a` is an `Animal` reference to a `Dog` object runs Dog's version. This is the seed of runtime polymorphism.

## Flow

```
Animal.speak()  --overridden by-->  Dog.speak()
   a.speak() where a points to Dog -> "Dog barks"
```

## Important lines

```java
@Override
void speak() { System.out.println("Dog barks"); }   // same signature
Animal a = new Dog();
a.speak();          // runtime decides: Dog's version
```

## Interview questions

1. What is method overriding?
2. What rules must an override follow?
3. What does @Override do?
4. Can a private method be overridden?

## Interview answer

Overriding is when a subclass provides its own implementation of a parent method with the same signature. The version that runs is chosen at runtime by the actual object. `@Override` makes the compiler verify you really are overriding. Private methods cannot be overridden - they are not visible to the child.

## Common mistake

Overriding but changing the parameter list - that is overloading, not overriding, and `@Override` will fail to compile.

## Remember

- Same signature as parent method.
- `@Override` verifies at compile time.
- Runtime decides which version runs.
- Cannot override static, final, or private methods.
