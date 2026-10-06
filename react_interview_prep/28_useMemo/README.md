# useMemo

## What is it?
`useMemo` caches the result of a computation and only recomputes it when
the listed dependencies change. It prevents expensive work from running on
every render.

## What this code demonstrates
A 1-million-iteration calculation cached with `[]` deps — clicking the
counter or theme button does not recompute it.

## Important code
- `const expensiveResult = useMemo(() => {...heavy loop...}, [])` — cached.
- `[count]` would recompute only when `count` changes.

## Interview questions
1. What does useMemo memoize? (A value, not a function.)
2. When is useMemo genuinely useful?
3. Why shouldn't you use useMemo for everything?

## Common mistakes
- Wrapping cheap operations in useMemo — overhead with no benefit.
- Memoizing to "fix" re-renders (that's usually React.memo's job).
- Forgetting deps — the memo returns a stale value forever.

## Remember
- useMemo → cache a VALUE.
- Only for expensive, repeated computations.
- Most computations are cheap — don't over-optimize.
