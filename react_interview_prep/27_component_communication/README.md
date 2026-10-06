# Component Communication

## What is it?
The three ways components share data:
1. Parent → Child with props.
2. Child → Parent with callback props.
3. Sibling ↔ Sibling through the shared parent's state.

## What this code demonstrates
All three patterns in one small app.

## Important code
- `<Child message={parentMessage} />` — data flows down.
- `<ChildWithButton onNotify={setChildMessage} />` — the child calls
  `onNotify("...")` which is `setChildMessage` from the parent.
- `counter` lives in `App` so both siblings see it.

## Interview questions
1. How does a child send data to its parent?
2. How do two siblings communicate?
3. What is the flow of props vs events?

## Common mistakes
- Creating state in a child when a sibling needs it too (no shared access).
- Trying to call a parent's setter without passing it down.
- Over-complicating with Context when lifting state is enough.

## Remember
- Props down, callbacks up.
- Siblings meet through the parent.
- If it gets deep, Context or lifting fixes it — don't prop-drill 6 levels.
