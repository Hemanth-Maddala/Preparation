# Adapter Pattern

## What is it?

**Adapter** lets two incompatible interfaces work together. It wraps an existing class and presents it as the interface the client expects, translating calls in between.

## Example

The client only understands `Chargeable.charge()`. The existing `UsbCharger` only offers `plugUsb()`. `UsbChargerAdapter` implements `Chargeable`, holds a `UsbCharger`, and translates `charge()` into `plugUsb()`.

## Flow

```
Client (wants Chargeable)
      |
      v
 UsbChargerAdapter  implements Chargeable
      |  holds + translates
      v
 UsbCharger.plugUsb()   (existing, untouched)
```

## Important lines

```java
class UsbChargerAdapter implements Chargeable {
    private UsbCharger usbCharger;             // wraps existing class
    public void charge() { usbCharger.plugUsb(); }   // translation
}
```

## Interview questions

1. What problem does the Adapter pattern solve?
2. Adapter vs facade?
3. When is an adapter useful in real systems?

## Interview answer

Adapter bridges incompatible interfaces: it wraps an existing class and exposes the interface the client expects, translating calls. It lets you reuse legacy or third-party code without modifying it. A facade also wraps code but to simplify a large API, not to change an interface.

## Common mistake

Modifying the legacy class directly when you cannot (third-party or shared code). The adapter wraps instead of rewrites.

## Remember

- Wraps an existing class.
- Implements the expected interface.
- Translates calls.
- Reuses code without modifying it.
