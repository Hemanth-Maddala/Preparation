// Custom hooks: reuse stateful logic across components.
// A custom hook is a function that uses other hooks and starts with "use".

import useCounter from "./useCounter.js";

function Counter({ label }) {
  const { count, increment, decrement, reset } = useCounter(0);

  return (
    <div className="card">
      <h3>{label}: {count}</h3>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}

function App() {
  // Two components use the same hook — each has its OWN state
  return (
    <div className="container">
      <h1>Custom Hook</h1>
      <Counter label="Counter A" />
      <Counter label="Counter B" />
    </div>
  );
}

export default App;
