# Multiple Interfaces

## What is it?

A class uses `implements Swimmer, Runner` to satisfy **several contracts** at once. This is "multiple inheritance of type": the class IS-A Swimmer AND IS-A Runner, while still extending exactly one class.

## Example

`Athlete implements Swimmer, Runner` provides both `swim()` and `run()`. The same object can be used as a `Swimmer` or a `Runner`.

## Flow

```
Swimmer (swim)   Runner (run)
      \          /
       \        /
      Athlete (provides both)
```

## Important lines

```java
class Athlete implements Swimmer, Runner { }  // multiple contracts
Swimmer s = a;   // treated as a Swimmer
Runner  r = a;   // treated as a Runner
```

## The diamond problem (basic level)

If two interfaces both declare the same default method, the class MUST override it or the code will not compile:

```java
interface A { default void m() { } }
interface B { default void m() { } }
class C implements A, B { public void m() { } }  // required
```

## Interview questions

1. Why does Java allow multiple interfaces but not multiple classes?
2. What is the diamond problem?
3. How is the diamond problem resolved with default methods?

## Interview answer

Classes share implementation, which creates ambiguity in the diamond problem, so Java allows only one parent class. Interfaces only declare contracts (plus default methods), so multiple inheritance of type is safe. If two interfaces contribute the same default method, the class must override it, removing the ambiguity.

## Common mistake

Assuming you can `extends` two classes. That is a compile error - only one class parent is allowed; use interfaces for the rest.

## Remember

- `implements A, B` = multiple inheritance of type.
- One class parent maximum.
- Conflicting default methods must be overridden.
