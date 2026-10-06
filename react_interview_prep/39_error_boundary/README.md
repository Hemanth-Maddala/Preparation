# Error Boundary

## What is it?
An error boundary catches JavaScript errors thrown during rendering of its
children, and shows fallback UI instead of crashing the whole app.

## Why is it a class component?
Error boundaries still use class lifecycle methods
(`getDerivedStateFromError`, `componentDidCatch`) — there is no hook
equivalent yet. This is the one interview case where a class component is
still the right answer.

## What this code demonstrates
A boundary that catches a component that deliberately throws, and renders
"Something went wrong." instead.

## Important code
- `static getDerivedStateFromError()` — set `hasError: true`.
- `componentDidCatch(error, info)` — log the error.
- `render()` — fallback UI or `this.props.children`.

## Interview questions
1. What errors does an Error Boundary catch?
2. What does it NOT catch?
3. Why is it a class component?
4. How would you use it in a real app? (Wrap routes or sections.)

## Common mistakes
- Expecting it to catch errors in event handlers (it doesn't).
- Expecting it to catch async errors in `fetch` (it doesn't — handle those
  with try/catch + error state, as in folder 17).
- Expecting it to catch errors in itself (it can't — boundaries don't catch
  their own errors).

## Remember
- Catches: render/lifecycle errors in children.
- Doesn't catch: event handlers, async code, SSR, its own errors.
- Class component required — this is the exception, not the rule.
