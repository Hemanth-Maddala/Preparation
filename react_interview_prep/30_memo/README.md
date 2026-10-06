# React.memo

## What is it?
`React.memo` is a higher-order component that memoizes a component. If its
props are unchanged (shallow comparison), React skips re-rendering it even
when the parent re-renders.

## What this code demonstrates
A memoized child that logs only when its actual prop (`count`) changes,
not when an unrelated parent state (`other`) changes.

## Important code
- `const ExpensiveChild = memo(function ExpensiveChild({ count }) {...})` —
  wrap the component in memo.
- `console.log` inside the child proves when it renders.

## Interview questions
1. What does React.memo do?
2. What is a shallow comparison?
3. When does memo NOT help? (Inline objects/arrays/functions change every
   render.)
4. memo vs useMemo?

## Common mistakes
- Using memo on components with unstable props (inline functions/objects)
  — it silently does nothing useful.
- Using memo everywhere — extra overhead on cheap components.
- Forgetting that memo still re-renders when props change.

## Remember
- memo stops re-renders when props are "the same".
- Shallow compare: new object/function props defeat it.
- useCallback pairs with memo to keep function props stable.
