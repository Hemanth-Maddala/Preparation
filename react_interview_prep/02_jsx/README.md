# JSX

## What is it?
JSX is a JavaScript syntax extension that looks like HTML. It is not HTML —
it gets compiled into `React.createElement` calls. Any JavaScript expression
can be embedded inside `{ }`.

## What this code demonstrates
Variables, expressions, ternaries, `className`, fragments, and calling
functions all inside JSX.

## Important code
- `Hello {name}` — output a variable.
- `{age + 1}` — run an expression.
- `{isDeveloper ? "..." : "..."}` — ternary.
- `className` — the JSX word for `class`.
- `<>...</>` — a fragment (no extra DOM node).
- `{items.map(...)}` — expressions can produce JSX.

## Interview questions
1. What is JSX? Is it HTML?
2. How do you embed a JavaScript value in JSX?
3. Why `className` and not `class`?
4. What is a fragment and when do you use it?
5. Why can't you use `if` directly inside JSX? (You use ternary or `&&`.)

## Common mistakes
- Using `class` instead of `className`.
- Trying to use `if` statements inside `{}`.
- Returning two sibling elements without a wrapper or fragment.

## Remember
- `{ }` = "evaluate this JavaScript".
- Ternary works inside JSX, `if` does not.
- Fragments let you return multiple elements without a wrapper div.
