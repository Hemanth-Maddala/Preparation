// useState: the most important React hook.
// [value, setter] = useState(initialValue)

import { useState } from "react";
function App() {
  const [count, setCount] = useState(0);

  // Style 1: direct value — fine when you only update once per click
  const incrementDirect = () => setCount(count + 1);

  // Style 2: updater function — uses the latest state.
  // Without it, three setCount(count + 1) calls would only add 1
  // (all three would see the same old `count`).
  const incrementByThree = () => {
    setCount((prev) => prev + 1);
    setCount((prev) => prev + 1);
    setCount((prev) => prev + 1);
  };

  return (
    <div className="container">
      <h1>Count: {count}</h1>
      <button onClick={incrementDirect}>+1 (setCount(count + 1))</button>
      <button onClick={incrementByThree}>+3 (setCount(prev =&gt; prev + 1))</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}

export default App;
