# Event Handling

## What is it?
React events (`onClick`, `onChange`, `onSubmit`) work like DOM events but
are written in camelCase and receive a synthetic event object `e`.

## What this code demonstrates
The three events you need for most interview tasks: button click, input
change, and form submit.

## Important code
- `onClick={handleClick}` — pass a function REFERENCE, never `handleClick()`.
- `onChange={(e) => setText(e.target.value)}` — read the input value.
- `onSubmit={handleSubmit}` with `e.preventDefault()` — stops the page
  reload (without it your state is lost).

## Interview questions
1. Why is it `onClick` and not `onclick`?
2. Why do you pass a function reference, not a call?
3. What is `e` and what does `e.target.value` give you?
4. Why call `e.preventDefault()` on form submit?

## Common mistakes
- Writing `onClick={handleClick()}` — fires during render.
- Forgetting `e.preventDefault()` — page reloads, state resets.
- Using a `<button>` without `type="submit"` inside a form.

## Remember
- Handlers are references: `onClick={fn}`.
- `e.preventDefault()` on forms is mandatory.
- `e.target.value` is how you read inputs.
