# useReducer

## What is it?
`useReducer` manages state through a pure `reducer` function
`(state, action) => newState`. Components `dispatch` actions instead of
calling setters.

## What this code demonstrates
A counter where every state change is a named action.

## Important code
- `function reducer(state, action) { switch (action.type) {...} }` — all
  update logic in one place.
- `const [state, dispatch] = useReducer(reducer, { count: 0 })` — the hook.
- `dispatch({ type: "increment" })` — how components trigger updates.

## Interview questions
1. What is a reducer? Why must it be pure?
2. useReducer vs useState — when would you choose each?
3. What is an action?

## Common mistakes
- Mutating state inside the reducer — always return a new object.
- Async logic inside the reducer (reducers must be pure — do async work in
  the event handler/effect, then dispatch).
- Not handling the `default` case.

## Remember
- state + action → new state.
- Use it when state updates are complex or have many action types
  (todo list, form, cart).
- useState is enough for simple independent values.
