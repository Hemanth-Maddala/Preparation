# Constructors

## What is it?

A **constructor** is a special method, named exactly like the class, with **no return type** (not even `void`). It runs automatically when `new` is called, to initialize the object. **Constructor overloading** means multiple constructors with different parameter lists.

## Example

`Student` has two constructors. `new Student()` uses the no-arg one; `new Student("Ravi", 7)` uses the parameterized one. The correct constructor is picked at compile time by the arguments.

## Flow

```
new Student()                -> name="Unknown", rollNo=0
new Student("Ravi", 7)       -> name="Ravi", rollNo=7
```

## Important lines

```java
Student() { ... }                    // constructor: same name, no return type
Student(String name, int rollNo) { } // parameterized constructor
new Student("Ravi", 7);              // 'new' calls the constructor
```

## Interview questions

1. What is the constructor naming rule?
2. Does a constructor have a return type?
3. What is a default constructor and when does it disappear?
4. Can constructors be overloaded?
5. When is a constructor called?

## Interview answer

A constructor is named exactly like its class and has no return type. It is invoked once, automatically, at `new` time to set up the object. If you write no constructor, Java adds a default no-arg one; if you write any constructor, the default disappears. Constructors can be overloaded by their parameter lists.

## Common mistake

Writing `void Student() { }` - that makes it a normal method, not a constructor, and the class gets no usable constructor.

## Remember

- Constructor name == class name.
- No return type, not even void.
- Runs once per object at `new`.
- Overloading = different parameter lists.
