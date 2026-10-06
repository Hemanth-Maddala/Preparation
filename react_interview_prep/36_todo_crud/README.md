# Todo CRUD

## What is it?
The classic practical task: a list where you can add, delete, toggle
complete, and edit items — all with plain `useState` (no Redux).

## What this code demonstrates
The four CRUD operations and their array patterns.

## Important code
- ADD: `setTodos([...todos, { id: Date.now(), text, completed: false }])`.
- DELETE: `setTodos(todos.filter((t) => t.id !== id))`.
- TOGGLE: `setTodos(todos.map((t) => t.id === id ? { ...t, completed: !t.completed } : t))`.
- EDIT: `editingId` + `editText` swap the label for an input.
- `id: Date.now()` — quick unique id (fine for demos).

## Interview questions
1. How do you add, delete, and update array items in state?
2. Why never `todos.push(...)` directly?
3. How does inline editing work? (editingId in state.)
4. How would you add persistence? (localStorage, see 22.)

## Common mistakes
- Mutating the array (`push`) instead of creating a new one.
- Using `index` as key — breaks edit/delete ordering.
- Not trimming or guarding empty input.

## Remember
- Immutable updates: spread to add, filter to delete, map to update.
- `Date.now()` gives a quick unique id.
- This pattern appears in almost every practical round.
