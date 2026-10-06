# Method Overloading

## What is it?

Overloading = several methods with the **same name** but **different parameter lists** (count or types). The compiler picks the right one at **compile time**, so it is called compile-time polymorphism.

## Example

`Calculator.add` has three versions: `(int,int)`, `(int,int,int)`, `(double,double)`. Each call is resolved by the arguments you pass.

## Flow

```
calc.add(2,3)        -> add(int, int)
calc.add(2,3,4)      -> add(int, int, int)
calc.add(2.5,3.5)    -> add(double, double)
```

## Important lines

```java
int add(int a, int b) { }
int add(int a, int b, int c) { }   // same name, different params
double add(double a, double b) { }
```

## Interview questions

1. What is method overloading?
2. Can you overload only by changing the return type?
3. Is overloading compile-time or runtime polymorphism?
4. Can constructors be overloaded?

## Interview answer

Overloading means same method name with different parameter lists. The compiler selects the version at compile time based on the arguments. Return type alone cannot differentiate overloads - the parameter list is what matters. Constructors can be overloaded too.

## Common mistake

Trying to overload by return type only:

```java
int foo() { }
double foo() { }   // COMPILE ERROR - not allowed
```

## Remember

- Same name, different parameter list.
- Compile-time selection.
- Return type does NOT count.
- Constructors can be overloaded.
