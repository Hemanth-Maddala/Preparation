# Composition

## What is it?

**Composition** is a **HAS-A** relationship with *strong ownership* and a *lifecycle tie*: the whole creates its part, and the part exists only as long as the whole does. Deleting the car destroys its engine.

## Example

`Car` builds its own `Engine` inside its constructor. Nothing outside ever holds the engine reference - it belongs exclusively to the car.

## Flow

```
Car  <>----  Engine      (filled diamond = ownership)
  creates it             engine dies with the car
  owns it
```

## Important lines

```java
private Engine engine;       // part is a private field
Car() { engine = new Engine(); }   // whole CREATES the part
```

## Aggregation vs composition

|                     | Aggregation                  | Composition                      |
|---------------------|------------------------------|----------------------------------|
| Ownership           | weak                         | strong                           |
| Who creates the part| outside (injected)           | the whole itself                 |
| Part lifecycle      | outlives the whole           | dies with the whole              |
| Example             | Department HAS Employees     | Car HAS Engine                   |

## Interview questions

1. What is composition?
2. Composition vs aggregation?
3. Which one is "stronger" and why?

## Interview answer

Composition is strong ownership: the whole class creates its parts, so the parts have the same lifecycle as the whole. Aggregation only holds references to parts that were created elsewhere. Car-Engine is composition; Department-Employee is aggregation.

## Common mistake

Using aggregation when the part only makes sense inside the whole (e.g. exposing the engine to the world). The part should be private and created by the owner.

## Remember

- HAS-A with ownership.
- Whole creates the part.
- Part dies with the whole.
- Fill the UML diamond: that's composition.
