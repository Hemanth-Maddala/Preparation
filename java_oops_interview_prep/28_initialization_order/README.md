# Initialization Order

## What is it?

The exact order Java follows when constructing an object. Knowing it lets you predict output of the classic "what prints?" interview questions.

## The order

1. **Static blocks** - once per class, at first class load, parent before child.
2. **Instance blocks** - every `new`, before the constructor, parent before child.
3. **Constructor body** - parent constructor runs before child constructor.

## Example output

```
Creating first Child:
1. Parent static block
2. Child static block
3. Parent instance block
4. Parent constructor
5. Child instance block
6. Child constructor
Creating second Child:
3. Parent instance block
4. Parent constructor
5. Child instance block
6. Child constructor
```

Static blocks do NOT repeat for the second object.

## Important lines

```java
static { }   // once per class, first
{ }          // every object, before constructor
Child() { }  // after parent constructor
```

## Interview questions

1. What is the initialization order in inheritance?
2. Do static blocks run twice?
3. Instance block vs constructor - which runs first?

## Interview answer

Statics run once at class load, parents first. For each object, parent instance blocks run, then the parent constructor, then the child's instance blocks, then the child's constructor. Static blocks never repeat for a second object of an already-loaded class.

## Common mistake

Forgetting instance blocks: they run on EVERY new, silently, before the constructor. They are rare in real code but common in interview questions.

## Remember

- Static once, instance every time.
- Parent always initializes first.
- Instance block < constructor body.
- Read order: static -> instance -> constructor.
