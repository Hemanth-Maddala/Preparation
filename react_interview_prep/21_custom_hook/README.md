# Custom Hook

## What is it?
A custom hook is a function that uses other hooks and starts with `use`.
It lets you extract and reuse stateful logic across components.

## What this code demonstrates
`useCounter` wraps counter state + actions; two `Counter` components use
it, each with independent state.

## Important code
- `function useCounter(initial = 0)` — the hook.
- `useState` + helper functions inside, returning `{ count, increment,
  decrement, reset }`.
- `const { count, ... } = useCounter(0)` — consuming the hook.

## Interview questions
1. What is a custom hook?
2. Why do custom hooks start with "use"?
3. How do you share logic between two components with a custom hook?
4. When would you write `useFetch`?

## Common mistakes
- Naming it without the `use` prefix — React linting fails.
- Calling hooks conditionally or in loops inside your custom hook.
- Sharing state between hook users (each call gets its own state — which
  is usually what you want).

## Remember
- Custom hook = function starting with `use` that uses other hooks.
- Encapsulates logic AND state; each component call gets its own copy.
- Great candidates: useFetch, useLocalStorage, useCounter, useToggle.
