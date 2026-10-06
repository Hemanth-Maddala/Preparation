# useContext

## What is it?
Context shares data with many components without passing it through every
level as props (prop drilling). `useContext` reads the nearest Provider's
value.

## What this code demonstrates
A light/dark theme: `App` provides the theme, a deeply nested `Toolbar`
reads and changes it without any props.

## Important code
- `const ThemeContext = createContext();` — create it.
- `<ThemeContext.Provider value={{ theme, setTheme }}>` — provide.
- `const { theme, setTheme } = useContext(ThemeContext);` — consume.

## Interview questions
1. What problem does Context solve?
2. What is prop drilling?
3. When should Context be used — and when not?
4. What happens to all consumers when a context value changes?

## Common mistakes
- Putting everything in context "just in case" — every value change
  re-renders every consumer.
- Passing a new object literal as value each render — re-renders everyone.
- Creating the context inside a component (must be module-level).

## Remember
- createContext → Provider → useContext.
- Use for theme, auth, language — shared app-wide data.
- Keep context values small and specific.
