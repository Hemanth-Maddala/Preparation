# useState

## What is it?
`useState` adds state to a functional component. It returns `[value, setter]`.
Calling the setter updates the value and re-renders the component.

## What this code demonstrates
A counter. It shows both ways to update state and the difference between
them.

## Important code
- `const [count, setCount] = useState(0);` — state + setter.
- `setCount(count + 1)` — direct value.
- `setCount((prev) => prev + 1)` — updater function, uses latest state.
- Clicking **+3** proves the difference: three `count + 1` calls would give
  +1, but three `prev => prev + 1` calls give +3.

## Interview questions
1. What does `useState` return?
2. What happens when you call the setter?
3. What is the difference between `setCount(count + 1)` and
   `setCount(prev => prev + 1)`?
4. Why should you never mutate state directly?

## Common mistakes
- `state.count++` instead of using the setter — no re-render.
- Using `count + 1` when the new value depends on the previous state.
- Calling the setter inside the render body (infinite loop).

## Remember
- Setter triggers a re-render.
- Use the updater function form when new state depends on old state.
- Never mutate state directly — always create a new value.
