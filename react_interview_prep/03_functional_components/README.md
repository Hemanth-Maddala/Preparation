# Functional Components

## What is it?
A functional component is a plain JavaScript function that returns JSX.
Multiple components can be composed — one component renders others.

## What this code demonstrates
Composition: `App` renders `UserCard` twice. The same component is reused
without duplicating code.

## Important code
- `import UserCard from "./UserCard.jsx";` — bring the child in.
- `<UserCard />` inside `App`'s JSX — the component tree.
- `function UserCard() { return ... }` — the reusable piece.

## Interview questions
1. What is a functional component?
2. How do you compose components?
3. Can one component be used multiple times?

## Common mistakes
- Forgetting the import → ReferenceError.
- Naming the component with a lowercase letter.
- Putting logic-heavy code inside components instead of splitting them.

## Remember
- Components are functions that return JSX.
- Build bigger UI from smaller components.
- One file can contain several components, but keep it simple.
