// useContext — pass data deep down without prop drilling.
// Steps: createContext → Provider with a value → useContext to read it.

import { createContext, useState, useContext } from "react";

// 1. Create the context
const ThemeContext = createContext();

function App() {
  const [theme, setTheme] = useState("light");

  // 2. Wrap the tree with the Provider and pass a value
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Toolbar />
    </ThemeContext.Provider>
  );
}

function Toolbar() {
  // 3. Any nested component reads the value with useContext
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <div className={theme === "dark" ? "container dark" : "container"}>
      <h1>Theme: {theme}</h1>
      <button
        onClick={() => setTheme(theme === "light" ? "dark" : "light")}
      >
        Toggle theme
      </button>
      <p>No prop drilling needed — Toolbar reads theme straight from context.</p>
    </div>
  );
}

export default App;
