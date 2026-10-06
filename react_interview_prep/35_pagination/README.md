# Pagination

## What is it?
Showing a list one "page" at a time using a `page` state value and
`Array.prototype.slice`. Prev/Next buttons are disabled at the edges.

## What this code demonstrates
50 items, 5 per page, with Previous/Next and a page indicator.

## Important code
- `items.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE)` — the math.
- `Math.ceil(items.length / PAGE_SIZE)` — total pages.
- `disabled={page === 1}` / `disabled={page === totalPages}` — edges.

## Interview questions
1. How do you paginate a list?
2. What does `slice(start, end)` need to compute each page?
3. How do you prevent going before page 1 or past the last page?

## Common mistakes
- Off-by-one: using `page * SIZE` instead of `(page - 1) * SIZE`.
- Not disabling buttons — page goes out of range.
- Forgetting `Math.ceil` — total pages must round UP.

## Remember
- `slice((page-1) * size, page * size)`.
- `disabled` guards the edges.
- Combine with filter: filter first, then slice the filtered result.
