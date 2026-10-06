# Association

## What is it?

**Association** is a general "uses/knows" relationship between two independent classes. Objects exist and operate on their own; the link is formed when one uses the other (e.g. via a method parameter). It is the umbrella term: aggregation and composition are special kinds of association.

## Example

`Teacher` and `Student` are independent. `teaches(Student s)` creates the association only while the call happens - Teacher and Student have separate lifecycles.

## Flow

```
Teacher  <-------->  Student
   teaches(s)     each object independent
```

## Important lines

```java
void teaches(Student s) { }   // association via a parameter
Teacher t = new Teacher(...); // no need for Student to exist
```

## Interview questions

1. What is association in OOP?
2. How is association shown in code?
3. Association vs aggregation vs composition?

## Interview answer

Association is a relationship where one class uses another; both objects remain independent with their own lifecycles. In code it usually appears as a method parameter or field reference. Aggregation and composition are stronger forms of association that add ownership semantics.

## Common mistake

Saying association requires storing the other object as a field. It does not - a method parameter is a valid association.

## Remember

- Independent classes, independent lifecycles.
- Shown by parameters or fields.
- Parent of aggregation/composition.
- No ownership implied.
