# useRef

## What is it?
`useRef` gives you a mutable object (`.current`) that survives renders but
does NOT trigger a re-render when changed. Two main uses: DOM references
and persistent values.

## What this code demonstrates
Focusing an input through a ref, and a ref-based counter that updates
without re-rendering.

## Important code
- `const inputRef = useRef(null)` then `ref={inputRef}` on the element.
- `inputRef.current.focus()` — access the DOM node.
- `countRef.current += 1` — mutate without a re-render.

## Interview questions
1. What is a ref?
2. useRef vs useState — when do you use which?
3. How do you focus an input on mount?
4. Why doesn't changing `ref.current` re-render?

## Common mistakes
- Using a ref for something the UI must display (it won't update).
- Forgetting `.current`.
- Using refs where state is the correct tool (form values, etc.).

## Remember
- `ref` attribute + `ref.current` = DOM node.
- Refs are for values that survive renders without rendering.
- Display things with useState; reach into the DOM with useRef.
