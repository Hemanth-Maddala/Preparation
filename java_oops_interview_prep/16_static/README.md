# static

## What is it?

`static` means **class-level**: one copy shared by every object (static variable), callable without an object (static method), run once at class load (static block). Non-static members are per-object.

## Example

`total` counts all objects ever created because it is shared. `instanceCount` is per-object. `showTotal()` is static and can only touch static members - no `this`.

## Flow

```
static int total  ->  [ one box shared by all Counter objects ]
int instanceCount ->  [ one box PER Counter object ]
```

## Important lines

```java
static int total = 0;          // class-level memory
static void showTotal() { }    // call without an object
Counter.showTotal();           // called on the class
```

## Interview traps

1. Can a static method access an instance variable? **No** - it has no object (`this`).
2. Can static methods be overridden? **No** - same-signature static in a child is method *hiding*, chosen by reference type at compile time.
3. Can static methods be overloaded? **Yes** - overloading is about parameters, not `static`.

## Interview questions

1. What does static mean for a variable?
2. Can static methods access instance variables?
3. Can static methods be overridden?
4. When is a static block executed?

## Interview answer

A static member belongs to the class, not to any object - one copy, accessed by class name. Static methods have no `this`, so they cannot read instance variables directly. They cannot be overridden (only hidden), but they can be overloaded. Static blocks run once, the first time the class is loaded.

## Common mistake

Calling a static method through an object reference: it works, but confusing, and with a null reference it still runs (static calls need no object).

## Remember

- One static copy per class, not per object.
- Access via class name.
- No `this` in static methods.
- Static methods: hidden, never overridden.
