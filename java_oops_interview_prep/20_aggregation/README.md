# Aggregation

## What is it?

**Aggregation** is a **HAS-A** relationship with *weak ownership*: the whole (Department) holds references to parts (Employees), but the parts are created outside and live on independently.

## Example

Employees are created in `main` and passed into `Department`. Deleting the department does not delete the employees. This is the key difference from composition.

## Flow

```
Department  <>--------  Employee
   HAS-A (weak)        each employee survives without dept
```

## Important lines

```java
Employee[] employees;                       // the HAS-A field
Department(String name, Employee[] es) { }  // parts injected from outside
Employee e1 = new Employee("Ravi");         // exists independently
```

## Interview questions

1. What is aggregation?
2. How is aggregation different from composition?
3. What does "weak ownership" mean?

## Interview answer

Aggregation is a HAS-A relationship where the part can exist without the whole. The whole receives references from outside (constructor or setter), so the lifecycle of the parts is not controlled by the whole. Composition is the strong-ownership version: the whole creates and destroys its parts.

## Common mistake

Confusing aggregation with composition. Ask: "if I delete the whole, does the part still make sense alone?" If yes -> aggregation; if no -> composition.

## Remember

- HAS-A, weak ownership.
- Parts passed in from outside.
- Part outlives the whole.
- Same lifecycle: not required.
