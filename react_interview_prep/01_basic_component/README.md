# Basic Component

## What is it?
A React component is a function that returns JSX. The function name starts
with a capital letter, and JSX looks like HTML but lives inside JavaScript.

## What this code demonstrates
The absolute minimum: one function, one `return`, one `<h1>`.

## Important code
- `function App() {` — the component is a function.
- `return <h1>Hello React</h1>;` — the JSX the component renders.
- `export default App;` — so `main.jsx` can import and render it.

## Interview questions
1. What is a component?
2. Why must component names start with a capital letter?
3. What does a component return?
4. How is a component rendered on the page?

## Common mistakes
- Forgetting the capital letter → React treats it as an HTML tag.
- Forgetting `export default` → nothing renders.
- Returning nothing → blank page.

## Remember
- Component = function that returns JSX.
- `export default` so the app can use it.
- The component renders into `<div id="root">` via `main.jsx`.
