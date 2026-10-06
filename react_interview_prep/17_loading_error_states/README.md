# Loading / Error / Success

## What is it?
The standard way to handle async data: three pieces of state (data,
loading, error) and early returns so only one state renders at a time.

## What this code demonstrates
A fetch with full `try/catch/finally` and the three-branch render.

## Important code
- `if (loading) return <p>Loading...</p>` — first branch.
- `if (error) return <p>Error: {error}</p>` — second branch.
- `return data.map(...)` — success branch.
- `finally { setLoading(false); }` — always turns loading off, even on error.

## Interview questions
1. How do you handle loading/error states?
2. Why three separate state variables instead of one?
3. Why check loading before error? (Order matters — both can be true.)

## Common mistakes
- Forgetting `finally` → stuck on "Loading..." after an error.
- Not checking `res.ok` → you treat an HTTP 404/500 as success.
- Rendering `data` while it is still null → crash.

## Remember
- Three states: data, loading, error.
- Early returns: loading → error → data.
- `finally` guarantees cleanup.
