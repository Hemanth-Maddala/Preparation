# Interface

## What is it?

An **interface** is a contract - a list of methods a class promises to implement, using `implements`. Modern interfaces also support `default` methods (with a body, can be overridden) and `static` methods. Interfaces give "multiple inheritance of type".

## Example

`Animal` declares `makeSound()`. `Dog implements Animal` must provide it. `sleep()` is a default method Dog inherits for free; `describe()` is static and called on the interface itself.

## Flow

```
interface Animal (makeSound abstract, sleep default, describe static)
        ^ implements
        |
      Dog (provides makeSound)
```

## Important lines

```java
interface Animal { void makeSound(); }   // abstract contract
class Dog implements Animal { public void makeSound() { } }
d.sleep();         // default method inherited
Animal.describe(); // static method on interface
```

## Interview questions

1. What is an interface?
2. Abstract class vs interface?
3. What are default and static methods?
4. Why are interface methods public?

## Interview answer

An interface is a contract defining behavior that implementing classes must provide. Interfaces support multiple inheritance of type - a class can implement several. Default methods add shared behavior to an interface without breaking implementors; static methods are utility methods on the interface. Implemented methods must be public because an interface method is implicitly public and overriding cannot reduce visibility.

## Common mistake

Forgetting the class must make interface methods `public` - reducing visibility to package/private is not allowed and won't compile.

## Remember

- `implements` = promise to provide the behavior.
- A class can implement many interfaces.
- default methods have bodies; static methods call on the interface.
- Implementations must be public.
