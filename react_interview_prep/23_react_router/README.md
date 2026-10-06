# React Router

## What is it?
React Router is the standard routing library. You declare which component
renders for each URL using `Routes` and `Route`, and navigate with `Link`.

## What this code demonstrates
Three pages (Home, About, Login) connected with routes and links.

## Important code
- `<BrowserRouter>` — wraps the app so routing works.
- `<Routes>` + `<Route path="/" element={<Home />} />` — URL → component.
- `<Link to="/about">` — clickable navigation (renders an `<a>`).

## Interview questions
1. What are the four main pieces of React Router?
2. `Link` vs a plain `<a>` tag?
3. What is `element` in `<Route>`?
4. How do routes match URLs?

## Common mistakes
- Using `<a href>` instead of `<Link>` — full page reload, state lost.
- Forgetting `BrowserRouter` — "useRoutes() may be used only in a
  `<Router>`" error.
- Not wrapping the app in the router in `main.jsx` in a real app.

## Remember
- BrowserRouter → Routes → Route → Link.
- `path` matches the URL, `element` is what renders.
- Use `Link` for navigation, never `<a href>`.
