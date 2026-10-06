// useMemo: cache the RESULT of an expensive calculation.
// Recomputes only when the dependency array changes.

import { useMemo, useState } from "react";

function App() {
  const [count, setCount] = useState(0);
  const [dark, setDark] = useState(false);

  // Expensive calculation — cached. Runs once because deps are [].
  const expensiveResult = useMemo(() => {
    console.log("Computing expensive value...");
    let total = 0;
    for (let i = 0; i < 1000000; i++) total += i;
    return total;
  }, []);

  return (
    <div className={dark ? "container dark" : "container"}>
      <h1>useMemo</h1>
      <h2>Expensive result: {expensiveResult}</h2>

      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
      <button onClick={() => setDark(!dark)}>
        Toggle theme (does NOT recompute)
      </button>
      <p>Check the console — the calculation runs once, not on every render.</p>
    </div>
  );
}

export default App;
