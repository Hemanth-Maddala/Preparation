# Form Validation

## What is it?
Validating input with plain React state before submitting — required fields,
email format, password length. No Formik, no Yup.

## What this code demonstrates
A validate function returning an errors object, rendered inline under each
field, and a submit handler that stops when errors exist.

## Important code
- `validate()` — builds an `{ email, password }` errors object.
- `if (Object.keys(errs).length > 0) return;` — the "gate" in submit.
- `{errors.email && <p className="error">{errors.email}</p>}` — render.

## Interview questions
1. How do you validate a form without a library?
2. When do you validate — on change, on blur, or on submit?
3. How do you show an error next to the right field?

## Common mistakes
- Validating only in the render (runs on every keystroke and never tells
  the user anything useful).
- Not returning early on invalid — the form still "submits".
- Clearing errors at the wrong time (validate again on submit).

## Remember
- validate() → errors object → render + gate submit.
- Email check: `/^\S+@\S+\.\S+$/.test(value)`.
- Keep the errors object keyed by field name.
