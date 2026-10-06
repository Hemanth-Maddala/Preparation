# Observer Pattern

## What is it?

**Observer** establishes a one-to-many dependency: when the **subject** (publisher) changes, it notifies all registered **observers** (subscribers) automatically. Publisher/subscriber is the same idea.

## Example

`NewsPublisher` (subject) keeps a list of `Subscriber` (observer interface). `publish(...)` loops through the list and calls `notify(...)` on each. Adding a subscriber never changes the publisher's code.

## Flow

```
Subscriber (notify)  <----  NewsPublisher (subject)
   /      \                      | subscribe(...)
  Ravi   Priya                   | publish(...)
              notify() loop pushes news to all
```

## Important lines

```java
interface Subscriber { void notify(String news); }
private List<Subscriber> subscribers = new ArrayList<>();
for (Subscriber s : subscribers) { s.notify(news); }   // the notification
```

## Interview questions

1. What problem does Observer solve?
2. What are the subject and observer roles?
3. How is the publisher decoupled from subscribers?

## Interview answer

Observer lets a subject notify many interested parties without knowing their concrete classes. Subscribers implement an interface and register themselves; the subject just loops and calls notify(). Adding observers never modifies the subject, which keeps coupling low.

## Common mistake

Making the subject notify observers synchronously and blocking - for tiny interview examples it is fine, but real systems need care with ordering and failure.

## Remember

- Subject = publisher, observers = subscribers.
- One-to-many notification.
- Subject knows only the observer interface.
- Low coupling: add subscribers without editing the subject.
