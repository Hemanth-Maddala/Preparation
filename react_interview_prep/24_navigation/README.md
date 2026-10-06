# Navigation

## What is it?
Two ways to move between routes: declarative `Link` (an anchor the user
clicks) and imperative `useNavigate` (callable from code, e.g. right after
login).

## What this code demonstrates
A login button that calls `navigate("/dashboard")` after "logging in".

## Important code
- `const navigate = useNavigate();` — must be inside a Router context.
- `navigate("/dashboard")` — programmatic redirect.
- `<Link to="/">` — user-click navigation.

## Interview questions
1. `Link` vs `useNavigate` — when would you use each?
2. Can you use `useNavigate` outside a component? (No — it's a hook.)
3. How do you redirect after a login success?

## Common mistakes
- Calling `useNavigate()` outside a Router → error.
- Using `Link` when you need to navigate from an event handler.
- Forgetting the component using `useNavigate` is inside `<Routes>`/Router.

## Remember
- User clicks → `Link`.
- Code-driven (after login/logout/submit) → `useNavigate`.
- Both need the app inside a Router.
