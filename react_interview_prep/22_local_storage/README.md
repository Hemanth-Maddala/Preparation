# localStorage

## What is it?
`localStorage` is a browser API that stores key/value strings and survives
page refresh and browser restarts. Combined with `useState` + `useEffect`
it gives you persistence.

## What this code demonstrates
Saving a name on every change and reading it back on load.

## Important code
- `localStorage.getItem("key")` — read.
- `localStorage.setItem("key", name)` — write (strings only).
- `localStorage.removeItem("key")` — delete.
- `useState(() => localStorage.getItem(...) || "")` — lazy initializer,
  read once on mount.
- `useEffect(() => localStorage.setItem(...), [name])` — save on change.

## Interview questions
1. How do you persist state across a refresh?
2. Why the lazy initializer in useState?
3. When would you `JSON.stringify` / `JSON.parse`?

## Common mistakes
- Storing objects without `JSON.stringify` — you get "[object Object]".
- Reading localStorage during render without a lazy initializer.
- Forgetting the `||` default when the key is missing.

## Remember
- getItem / setItem / removeItem.
- Objects → JSON.stringify/parse.
- Lazy init for reading; effect for writing.
