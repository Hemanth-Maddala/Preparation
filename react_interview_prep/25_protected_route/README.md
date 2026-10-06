# Protected Route

## What is it?
A wrapper component that checks whether the user is authenticated. If not,
it redirects to the login page; if yes, it renders the protected page.

## What this code demonstrates
A `ProtectedRoute` wrapper, an in-memory `isAuth` state, and a Dashboard
that is unreachable when logged out.

## Important code
- `function ProtectedRoute({ isAuth, children })` — the pattern.
- `if (!isAuth) return <Navigate to="/login" replace />;` — redirect.
- `return children;` — render the protected content.
- `<Route path="/dashboard" element={<ProtectedRoute isAuth={isAuth}><Dashboard /></ProtectedRoute>} />`

## Interview questions
1. How do you protect a route?
2. Why `<Navigate ... replace />` instead of `useNavigate`?
3. Where should `isAuth` live — App state, Context, or localStorage?
4. What is the "children" pattern and why is it useful here?

## Common mistakes
- Protecting only the link, not the route — anyone can type the URL.
- Calling `navigate()` during render instead of returning `<Navigate>`.
- Storing only a boolean when you need the user object later.

## Remember
- Pattern: `isAuth ? children : <Navigate to="/login" replace />`.
- `replace` prevents "back" from returning to the protected page.
- In real apps `isAuth` comes from Context + localStorage (see 38).
