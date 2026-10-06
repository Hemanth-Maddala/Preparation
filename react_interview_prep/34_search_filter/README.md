# Search Filter

## What is it?
The most common coding-round task: an input filters a list in real time
using `Array.prototype.filter`.

## What this code demonstrates
Typing filters `users` case-insensitively; shows "No results" when empty.

## Important code
- `users.filter((name) => name.toLowerCase().includes(search.toLowerCase()))` —
  the core one-liner.
- `.toLowerCase()` on both sides so search is case-insensitive.
- `filtered.length === 0 ? <p>No results</p> : <ul>...</ul>` — empty state.

## Interview questions
1. How do you filter a list by user input?
2. Why `.toLowerCase()` on both sides?
3. How would you show an empty state?

## Common mistakes
- Forgetting `.toLowerCase()` — "ANU" won't match "anu".
- Filtering with `===` instead of `includes`.
- Not handling the empty-result case.

## Remember
- value → state → filter → render.
- `includes` for partial match, `===` for exact.
- Always render an empty state.
