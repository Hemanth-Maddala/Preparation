# Props

## What is it?
Props are data passed from a parent component into a child component.
They flow one way: down. A child reads them but must never modify them.

## What this code demonstrates
Passing `name` and `age` into `User`, reading them, and reusing the same
component with different data.

## Important code
- `<User name="Hemanth" age={22} />` — strings in quotes, numbers in `{}`.
- `function User(props)` — the child receives one `props` object.
- `props.name`, `props.age` — read values.
- `function UserDestructured({ name, age })` — destructured version.

## Interview questions
1. What are props?
2. Which direction do props flow?
3. Are props read-only? Why?
4. How do you pass a number vs a string as a prop?

## Common mistakes
- Forgetting `{}` around numbers: `age={22}`, not `age="22"`.
- Trying to modify `props` inside the child (props are read-only).
- Missing `props.` when reading (`props.name`, not `name`).

## Remember
- Props = input to a component.
- Props flow down; callbacks flow up.
- Destructuring `({ name, age })` is the interview-friendly style.
