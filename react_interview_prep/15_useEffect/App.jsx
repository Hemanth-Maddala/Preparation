// useEffect: run side effects after render — fetch, timers, logs.
// The dependency array controls WHEN the effect runs.

import { useState, useEffect } from "react";

function App() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState("");

  // 1. Runs once on mount (empty dependency array)
  useEffect(() => {
    console.log("Mounted");
  }, []);

  // 2. Runs on mount AND whenever `count` changes
  useEffect(() => {
    console.log("Count changed to:", count);
  }, [count]);

  // 3. Runs after EVERY render (no dependency array)
  useEffect(() => {
    console.log("Rendered");
  });

  // 4. With cleanup: the returned function runs before the effect
  //    re-runs and when the component unmounts
  useEffect(() => {
    console.log("Name effect started:", name);
    return () => console.log("Name effect cleaned up");
  }, [name]);

  return (
    <div className="container">
      <h1>useEffect</h1>
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Increment count</button>
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Type to trigger name effect"
      />
      <p>Open the browser console to see when each effect runs.</p>
    </div>
  );
}

export default App;
