# useCallback

## What is it?
`useCallback` returns the SAME function reference between renders (as long
as its dependencies don't change). This matters when you pass functions to
`React.memo` children — a new function reference would defeat the memo.

## What this code demonstrates
A memoized `Button` whose onClick stays stable, so re-rendering the parent
does not re-render the button.

## Important code
- `const handleClick = useCallback(() => {...}, [])` — stable reference.
- `const Button = memo(({ label, onClick }) => ...)` — re-renders only
  when props change (and stable onClick means props don't change).

## Interview questions
1. What does useCallback memoize? (A function reference.)
2. Why does a new inline function defeat React.memo?
3. useCallback vs useMemo?

## Common mistakes
- Wrapping every handler "just in case" — adds overhead.
- Forgetting deps → stale closure bugs.
- Using useCallback without a memoized child — no benefit.

## Remember
- useCallback → stable function reference.
- Its main partner is React.memo.
- If the parent re-renders, an inline arrow prop = new reference =
  child re-renders.
