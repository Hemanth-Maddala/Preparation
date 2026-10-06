# Auth Flow

## What is it?
The complete demo authentication loop: login → store auth → navigate →
protected page → logout, with login persisted in localStorage.

## What this code demonstrates
Everything combined: fake API, localStorage persistence, protected route,
logout, and programmatic navigation.

## Important code
- `useState(() => JSON.parse(localStorage.getItem("auth")))` — restore on load.
- `localStorage.setItem("auth", JSON.stringify(data))` on login.
- `localStorage.removeItem("auth")` + `setUser(null)` on logout.
- `user ? <Dashboard /> : <Navigate to="/login" replace />` — protection.

## Interview questions
1. How do you persist login across a refresh?
2. Where does `user` state live and why?
3. Why is this NOT production authentication?

## Common mistakes
- Storing the token without JSON (must stringify/parse).
- Protecting only the link instead of the route.
- Believing localStorage is secure (it isn't — XSS can read it).

## Remember
- Flow: login → save → navigate → protect → logout → clear.
- localStorage for demo persistence only.
- Real apps: tokens, HttpOnly cookies, refresh, and CSRF protection.
