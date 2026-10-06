# hashCode()

## What is it?

`hashCode()` returns an int that describes an object for hash-based collections (HashMap/HashSet/HashTable). Its contract with equals() is the key interview point.

## The contract

1. If `a.equals(b)` is true, `a.hashCode()` MUST equal `b.hashCode()`.
2. Equal hashCodes do NOT require equal objects (collisions are allowed).
3. hashCode() must be consistent while the object is in a collection.

## Example

`Student` overrides both methods consistently. Two "Ravi, 7" students are equal AND share a hashCode, so a `HashSet` keeps only one.

## Flow

```
HashSet.add(new Student("Ravi",7))
  -> hashCode() 31*7 + "Ravi".hashCode()  -> bucket
  -> bucket already has an equal object?   -> equals() says yes -> skip
```

## What goes wrong if you break it

Override equals() but not hashCode(): equal objects land in DIFFERENT buckets, equals() is never called, and a HashSet stores duplicates. The collection quietly misbehaves.

## Important lines

```java
@Override public int hashCode() {
    return 31 * rollNo + name.hashCode();   // classic form
}
```

## Interview questions

1. What is the equals()/hashCode() contract?
2. Why override both together?
3. What happens if you only override equals()?

## Interview answer

Equal objects must have equal hashCodes because hash collections find an object by hashCode bucket first and confirm with equals() inside that bucket. Overriding only equals() means equal objects may land in different buckets, so the collection treats them as different and duplicates slip in.

## Common mistake

Using mutable fields in hashCode: if a field changes while the object sits in a HashSet, you can never find it again.

## Remember

- equal objects -> equal hashCodes (mandatory).
- Same hashCode does not mean equal objects.
- Override together, always.
- Use only immutable-ish fields in hashCode.
