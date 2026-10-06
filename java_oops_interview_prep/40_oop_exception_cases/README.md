# OOP + Exceptions

## What is it?

Exceptions are how Java signals errors, and they interact with OOP: inheritance (the hierarchy), overriding (rule about throws), and custom exceptions (a class you write).

## The hierarchy

```
Throwable
  ├── Error            (JVM problems - not handled)
  └── Exception
        ├── RuntimeException   (UNCHECKED: NPE, ArithmeticException...)
        └── (others)           (CHECKED: IOException, SQLException...)
```

- **Checked**: compiler forces you to handle them (try/catch or `throws`).
- **Unchecked**: `RuntimeException` and subclasses; no forced handling.

## Important lines

```java
throw new InsufficientFundsException("...");   // raise it
void withdraw(...) throws InsufficientFundsException { }  // declare it
try { ... } catch (InsufficientFundsException e) { }      // handle it
```

## The overriding rule (classic question)

When overriding a method, the override can throw **the same or narrower** checked exceptions (or none). It **cannot add new or broader** checked exceptions - otherwise callers catching the parent signature would be surprised by new failures. Unchecked exceptions have no such limit.

```java
class Parent { void p() throws Exception { } }
class Child  extends Parent { void p() { } }   // OK - narrower
// void p() throws IOException   also OK (IOException < Exception)
// void p() throws Throwable     NOT OK (broader)
```

## Interview questions

1. Checked vs unchecked exceptions?
2. What happens to checked exceptions when overriding?
3. When do you create a custom exception?

## Interview answer

Checked exceptions are declared in the method signature and must be handled; unchecked ones (RuntimeException) are not forced. An override may narrow or drop the checked exceptions of the parent but never broaden them, because callers depend on the parent contract. A custom exception class (extends Exception or RuntimeException) is worth writing when you want a meaningful, domain-specific error type.

## Common mistake

Catching exceptions and swallowing them (empty catch block). At least log or re-throw - silently ignoring errors hides bugs.

## Remember

- Checked = must handle; unchecked = optional.
- throw raises, throws declares, try/catch handles.
- Override: same or narrower checked exceptions only.
- Custom exceptions = small classes extending Exception/RuntimeException.
