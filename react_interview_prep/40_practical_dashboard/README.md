# Practical Dashboard

## What is it?
A tiny dashboard that reuses the patterns from earlier folders together:
components, props, useState, useEffect, fetch, loading/error, search, and
conditional rendering.

## What this code demonstrates
All the recurring interview patterns in one small page.

## Important code
- `StatCard({ label, value })` — presentational component via props.
- `useEffect` fetch with `try/catch/finally` — loading + error.
- `users.filter(...toLowerCase().includes(...))` — search.
- Early returns: `if (loading)` → `if (error)` → render data.

## Interview questions
1. Which patterns from earlier folders appear here?
2. Why derive `filtered` instead of storing it in state?
3. How would you add pagination on top?

## Common mistakes
- Mixing derived data into state instead of computing it in render.
- Not handling the empty-search-result case.
- Making the dashboard visually complicated — keep it functional.

## Remember
- This is your "combine everything" page.
- Derive, don't duplicate: filtered = base data + query.
- Build the same shape in a real interview: fetch → states → filter → UI.
