# Forms

## What is it?
A form in React is usually a set of controlled inputs whose values live in
state, submitted with an `onSubmit` handler.

## What this code demonstrates
A name/email/password form driven by ONE state object and ONE `onChange`
handler shared by all inputs.

## Important code
- `const [form, setForm] = useState({ name: "", email: "", password: "" })`
  — one object for all fields.
- `setForm({ ...form, [e.target.name]: e.target.value })` — spread the old
  object, then update only the changed field (computed key).
- `onSubmit={handleSubmit}` + `e.preventDefault()` — handle the submit
  without reloading.

## Interview questions
1. Why store form values in state?
2. What does `[e.target.name]` do?
3. Why spread `...form` before updating one field?

## Common mistakes
- Forgetting `...form` — you wipe the other fields.
- Forgetting `e.preventDefault()` — page reloads.
- No `type="submit"` on the button — the form never submits.

## Remember
- Controlled inputs: `value` + `onChange`.
- One object + one handler keeps forms small.
- Always `preventDefault` on submit.
