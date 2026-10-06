# API CRUD

## What is it?
Connecting React to a backend (here a public mock API) with the four HTTP
operations: GET, POST, PUT, DELETE.

## What this code demonstrates
Full CRUD against jsonplaceholder posts. No backend needed.

## Important code
- GET: `fetch(API).then((r) => r.json()).then(setPosts)` in `useEffect`.
- POST: `fetch(API, { method: "POST", headers, body: JSON.stringify(...) })`.
- PUT: `fetch(`${API}/${id}`, { method: "PUT", ... })` — full update.
- DELETE: `fetch(`${API}/${id}`, { method: "DELETE" })`.
- After each mutation, update local state to match the server.

## Interview questions
1. How do you make a POST request with fetch?
2. Why `Content-Type: application/json`?
3. Why update local state after the request? (Or optimistically before.)

## Common mistakes
- Forgetting `JSON.stringify` in the body.
- Not updating local state after a mutation — UI goes stale.
- Using the wrong method or missing the id in the URL.

## Remember
- GET to load, POST to create, PUT to update, DELETE to remove.
- After every write: refetch OR update local state.
- jsonplaceholder is perfect for interviews (no auth, no rate limits).
