# useEffect

## What is it?
A hook for side effects — work that happens outside rendering (fetching,
timers, subscriptions, logging). It runs after the component renders.

## What this code demonstrates
All four dependency-array cases plus cleanup, using console.log so you can
see exactly when each runs.

## Important code
- `useEffect(() => {...}, [])` — runs once on mount.
- `useEffect(() => {...}, [count])` — on mount + whenever `count` changes.
- `useEffect(() => {...})` — after every render.
- `return () => {...}` — cleanup: runs before the effect re-runs and on
  unmount. Used to clear timers/listeners.

## Interview questions
1. When does useEffect run?
2. What does the dependency array do?
3. What is cleanup and when is it called?
4. Why does a fetch belong inside useEffect and not in the render body?

## Common mistakes
- No dependency array with a fetch → infinite loop (runs every render).
- Missing deps → stale values. Wrong deps → wrong timing.
- Forgetting cleanup for intervals/subscriptions → memory leaks.

## Remember
- `[]` = once. `[x]` = when x changes. none = every render.
- Effects run AFTER render, never during it.
- Always clean up timers, listeners, and subscriptions.
