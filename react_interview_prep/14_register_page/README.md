# Register Page

## What is it?
A registration form with name, email, password, and confirm password —
validated with plain React state.

## What this code demonstrates
One state object, one onChange handler, and a validate() that checks
required fields, email format, password length, and password match.

## Important code
- One `form` object + `[e.target.name]` handler — stays small as fields grow.
- `form.password !== form.confirmPassword` — match check.
- `if (Object.keys(errs).length > 0) return;` — gate the submit.
- `if (success)` branch — replace the whole form after registering.

## Interview questions
1. How do you validate that two passwords match?
2. Why use one state object instead of four separate states?
3. What happens to other fields when you update one? (Spread `...form`.)

## Common mistakes
- Forgetting to spread `...form` — fields get wiped.
- Comparing passwords before either is filled.
- Letting the success screen replace the form but not resetting state.

## Remember
- Pattern: form object + computed key handler + validate + gate.
- confirmPassword error is a MATCH check, not a format check.
