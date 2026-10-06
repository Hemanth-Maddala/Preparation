# Encapsulation

## What is it?

Encapsulation is **data hiding**: fields are `private` and access goes through `public` methods. This gives controlled access, allows validation, and hides internal changes from the outside world.

## Example

`BankAccount.balance` is `private` - nobody can set it directly to a bad value. All changes go through `deposit` and `withdraw`, which validate amounts and check funds. Reading goes through `getBalance()`.

## Flow

```
Outside code
   |  deposit(50) / withdraw(30) / getBalance()
   v
BankAccount [ private double balance ]  <- validated methods only
```

## Important lines

```java
private double balance;      // hidden
void deposit(double amt) { if (amt <= 0) return; ... }  // validated
double getBalance() { return balance; }   // read-only
```

## Interview questions

1. What is encapsulation?
2. Why not make all fields public?
3. What is data hiding?
4. How does encapsulation enable validation?

## Interview answer

Encapsulation binds data and the methods that operate on it, and hides the data with private fields, exposing only public methods. Public fields let any code put the object in an invalid state and break callers when internals change; methods give control and validation.

## Common mistake

Thinking private means "secure". It is not security - it is encapsulation, a design tool to control how state changes.

## Remember

- `private` fields + `public` methods.
- Validates input before state changes.
- Read-only access instead of public fields.
- Change internals freely without breaking callers.
