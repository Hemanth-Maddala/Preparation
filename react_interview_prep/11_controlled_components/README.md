# Controlled Components

## What is it?
A controlled input's `value` comes from React state and its `onChange`
updates that state. React state and the input always match. This is the
standard React way.

## What this code demonstrates
A controlled input where state is the single source of truth, side by side
with an uncontrolled input.

## Important code
- `<input value={name} onChange={(e) => setName(e.target.value)} />` —
  value flows state → input, onChange flows input → state.
- Uncontrolled example: `<input defaultValue="" />` — React never tracks it.

## Interview questions
1. What is a controlled component?
2. Controlled vs uncontrolled — which is preferred and why?
3. What happens if you have `value` but no `onChange`?

## Common mistakes
- Forgetting `value` — React state and the UI drift apart.
- Forgetting `onChange` — the input becomes read-only (typed text never
  appears).
- Reading `.value` from the DOM directly instead of state.

## Remember
- value + onChange = controlled.
- State is the single source of truth.
- Always controlled in interviews.
