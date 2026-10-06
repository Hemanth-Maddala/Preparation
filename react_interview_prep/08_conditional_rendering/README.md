# Conditional Rendering

## What is it?
Rendering different JSX based on a condition. The three standard patterns
are the ternary, the `&&` operator, and `if/else` before the return.

## What this code demonstrates
A login/logout toggle showing all three patterns at once.

## Important code
- `isLoggedIn ? <Dashboard /> : <Login />` — ternary.
- `isLoggedIn && <p>...</p>` — show only when true.
- `renderContent(isLoggedIn)` with `if/else` inside — clean for complex
  conditions.

## Interview questions
1. What are the ways to conditionally render in React?
2. When would you use a ternary vs `&&`?
3. Can you use `if` inside JSX? (No — ternary or `&&`.)

## Common mistakes
- `{0 && <X />}` renders "0". Use a boolean check like `length > 0`.
- Using `if` directly inside JSX `{ }` — syntax error.
- Returning different component trees and losing state (e.g. the input in
  Login resets when you switch). Fix: keep both mounted or use keys wisely.

## Remember
- Ternary: `cond ? A : B`.
- `&&`: `cond && <A />` (renders A or nothing).
- Early `return` in the function body is the cleanest for big branches.
