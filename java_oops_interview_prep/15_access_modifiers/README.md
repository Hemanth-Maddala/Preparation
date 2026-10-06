# Access Modifiers

## What is it?

Four visibility levels for members (and classes): **private**, **default** (no keyword), **protected**, **public**. They control WHO can see/use a field or method.

## Example

Same-package demo: `private` id is invisible outside `Employee`, while default/protected/public members are reachable from `Main` in the same package. Private data is accessed through the class's own methods.

## Access table

| Modifier  | Same class | Same package | Subclass (any pkg) | Anywhere |
|-----------|:----------:|:------------:|:------------------:|:--------:|
| private   | yes        | no           | no                 | no       |
| default   | yes        | yes          | no                 | no       |
| protected | yes        | yes          | yes                | no       |
| public    | yes        | yes          | yes                | yes      |

## Important lines

```java
private String id;        // only this class
String dept;              // default = package only
protected double salary;  // package + subclasses
public String name;       // everyone
```

## Interview questions

1. What is the difference between default and protected?
2. Which modifier do you use for encapsulation?
3. Can a protected member be accessed from a different package?

## Interview answer

private = class only. default = package only. protected = package plus subclasses in other packages. public = everyone. protected is the only one that adds "subclass access" without opening up to everyone.

## Common mistake

Confusing default with public. No keyword means package-private, not public.

## Remember

- private > default > protected > public (widening).
- protected ≠ public: subclasses only outside the package.
- Encapsulation normally = private fields + public methods.
