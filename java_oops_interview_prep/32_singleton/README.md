# Singleton

## What is it?

**Singleton** ensures a class has exactly ONE instance and gives a global access point to it. Implementation: private constructor + private static instance + public static getter.

## Example

`Logger` uses eager initialization - the `INSTANCE` field is created when the class loads, which is inherently thread-safe (no locking). `l1 == l2` proves both getters return the same object.

## Flow

```
Logger.getInstance()
      |
      v
  INSTANCE (created once at class load)
      ^
      |  all callers get the same object
```

## Important lines

```java
private static final Logger INSTANCE = new Logger();  // one instance
private Logger() { }          // block outside creation
static Logger getInstance() { return INSTANCE; }
```

## Why Singleton can be problematic

- Global mutable state hides dependencies.
- Hard to test (you cannot easily inject a fake).
- Couples every caller to the singleton class.
- Thread-safety needs care (lazy versions need locking).

So: use it for genuinely single-instance services (logging, config, connection pools) - not as a default pattern.

## Interview questions

1. How do you write a thread-safe singleton?
2. Why can Singleton be an anti-pattern?
3. Eager vs lazy initialization?

## Interview answer

A modern simple approach is a `private static final` instance created at class load - eager init is thread-safe because class loading is synchronized. The downsides: hidden global state, poor testability, and tight coupling. Prefer dependency injection in most cases; use Singleton only where one instance is truly required.

## Common mistake

Writing a lazy singleton with a double-checked lock for a fresh interviewee answer - it is a performance/thread-safety minefield. Eager init is simpler and correct for almost all cases.

## Remember

- private constructor, static instance, static getter.
- Eager init = simplest thread-safe form.
- Global state = testability problem.
- Not a default pattern.
