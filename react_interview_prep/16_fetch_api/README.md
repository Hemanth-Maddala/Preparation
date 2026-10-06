# Fetch API

## What is it?
Making HTTP requests from React with the browser's `fetch()` inside
`useEffect`, saving the result into state.

## What this code demonstrates
A fetch on mount that converts the response to JSON and stores it in
state, with a basic loading flag.

## Important code
- `useEffect(() => {...}, [])` — fetch once on mount.
- `fetch(url).then((res) => res.json()).then((data) => setPosts(data))` —
  the classic chain: request → parse → store.
- `.catch(...)` — handles network errors.
- `posts.slice(0, 5)` — keep the render small.

## Interview questions
1. Why does the fetch live inside useEffect?
2. What does `res.json()` return? (A Promise of parsed JSON.)
3. Why the empty dependency array?
4. `.then` vs `async/await` — which do you prefer and why?

## Common mistakes
- Fetching inside the render body → runs every render.
- Forgetting the empty dependency array → infinite requests.
- Forgetting `.json()` → you store a Response object, not data.

## Remember
- Pattern: useEffect → fetch → .json() → setState.
- `[]` means "fetch once".
- Always handle the error path (see 17).
