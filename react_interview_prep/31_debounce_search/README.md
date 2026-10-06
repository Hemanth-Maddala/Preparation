# Debounce Search

## What is it?
Debouncing delays an action (like a search/API call) until the user stops
typing. It prevents a network request on every keystroke.

## What this code demonstrates
Typing updates `query` immediately, but `debounced` — and therefore the
"search" — only updates 500ms after typing pauses.

## Important code
- `setTimeout(() => setDebounced(query), 500)` — the delay.
- `return () => clearTimeout(timer)` — cleanup cancels the previous timer,
  so only the last keystroke wins.
- Second `useEffect` on `[debounced]` — that is where you'd call the API.

## Interview questions
1. What is debouncing?
2. Why debounce a search input?
3. How does the cleanup make debounce work?
4. Debounce vs throttle — what's the difference?

## Common mistakes
- Forgetting the cleanup → every keystroke still fires (no debounce).
- Putting the API call in the same effect as the timer.
- Debouncing inside the render — must be in an effect/event.

## Remember
- Timer in effect + clearTimeout in cleanup = debounce.
- "Search" reacts to `debounced`, not to every keystroke.
- In a real app, replace the second effect's body with the fetch.
