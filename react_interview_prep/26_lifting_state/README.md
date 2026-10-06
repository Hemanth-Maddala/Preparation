# Lifting State Up

## What is it?
When two (or more) components need to share the same data, move that data
into their closest common parent, then pass it down via props.

## What this code demonstrates
`App` owns `name`. `NameInput` changes it, `NameDisplay` shows it — they
never talk to each other directly.

## Important code
- `const [name, setName] = useState("")` — state lives in `App`.
- `<NameInput name={name} onChange={setName} />` — value + updater as props.
- `<NameDisplay name={name} />` — read-only consumer.

## Interview questions
1. What does "lifting state up" mean?
2. Why can't siblings share state directly?
3. How do you decide WHERE to put shared state?

## Common mistakes
- Duplicating state in each child — they drift apart.
- Lifting state higher than needed — causes extra re-renders.
- Passing the whole state object when only a slice is needed.

## Remember
- Shared data → closest common parent.
- Pass value down, pass updater down.
- Rule: lift until the shared data lives in a common ancestor.
