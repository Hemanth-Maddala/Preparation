# Login Page

## What is it?
The single most important practical interview task: a login form with
controlled inputs, show/hide password, validation, loading, and
success/error states — all without a real backend.

## What this code demonstrates
A complete login page against a `fakeLogin` Promise.

## Important code
- State: `email`, `password`, `showPassword`, `errors`, `loading`,
  `error`, `user`.
- `type={showPassword ? "text" : "password"}` — show/hide toggle.
- `validate()` + `if (Object.keys(errs).length > 0) return;` — gate.
- `await fakeLogin(email, password)` in `try/catch/finally` — the async
  flow; `finally` guarantees loading turns off.
- `disabled={loading}` — prevents double submissions.
- `if (user) return <h2>Welcome...</h2>` — success branch.

## Interview questions
1. How do you show/hide the password?
2. How do you prevent multiple submissions?
3. What if the API fails?
4. How would you persist the login across a refresh?
5. How would you protect the dashboard after login?

## Common mistakes
- Forgetting `e.preventDefault()`.
- Not turning `loading` off when the call fails.
- Hiding the error message on the next submit attempt.
- Blocking success behind a real backend instead of a fake Promise.

## Remember
- Demo login: `test@test.com` / `password`.
- The order: state → inputs → onChange → validation → submit → loading →
  success/error. (Full walkthrough: REACT_LOGIN_PAGE_INTERVIEW.txt)
