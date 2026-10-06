# The `this` Keyword

## What is it?

`this` is a reference to the **current object** - the object whose method/constructor is running. It is used to (1) resolve variable shadowing and (2) call another constructor of the same class with `this(...)`.

## Example

The constructor `Student(String name)` has a parameter that shadows the field `name`. `this.name = name` assigns the parameter to the field. The no-arg constructor calls `this("No name")` to delegate.

## Flow

```
new Student()        -> this("No name") -> this.name = "No name"
new Student("Ravi")  -> this.name = "Ravi"
```

## Important lines

```java
this.name = name;         // field = parameter (kills shadowing)
this("No name");          // constructor chaining (must be first line)
```

## Interview questions

1. What does `this` refer to?
2. How do you solve the shadowing problem in a constructor?
3. What is `this(...)` used for and what is its rule?
4. Can you use `this` inside a static method?

## Interview answer

`this` is the reference to the object on which the current code runs. In `this.name = name`, the left `name` is the field, the right is the parameter. `this(...)` calls a sibling constructor and must be the very first statement. You cannot use `this` in static methods because there is no current object.

## Common mistake

Writing `name = name;` in a constructor - this assigns the parameter to itself and the field stays null/default. `this.name = name` is required.

## Remember

- `this` = current object.
- Fixes shadowing between fields and parameters.
- `this(...)` chains constructors; must be first statement.
- No `this` inside static code.
