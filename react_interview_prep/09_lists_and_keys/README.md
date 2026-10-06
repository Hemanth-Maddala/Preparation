# Lists and Keys

## What is it?
Rendering an array as a list of elements with `map()`. Each rendered item
needs a `key` prop so React can track it across renders.

## What this code demonstrates
Mapping `users` into `<li>` elements with stable, unique `key`s.

## Important code
- `users.map((user) => <li key={user.id}>{user.name}</li>)` — the pattern.
- `key={user.id}` — stable unique id.

## Interview questions
1. Why is `key` required in lists?
2. Why shouldn't you always use the array index as key?
3. What happens when a list item's key changes?

## Common mistakes
- Using `index` as key when items can reorder, filter, or delete — React
  matches the wrong items and mixes up state/DOM.
- No key at all — React warns and falls back to position.
- Using `Math.random()` as key — destroys and recreates elements every
  render.

## Remember
- `map` returns a new array of JSX.
- Key must be unique among siblings.
- Key should be stable — prefer `id` over `index`.
