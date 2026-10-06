// useCallback: keep a FUNCTION reference stable between renders,
// so memoized children don't re-render unnecessarily.

import { useCallback, useState, memo } from "react";

// React.memo: the child only re-renders when its props change
const Button = memo(({ label, onClick }) => {
  console.log(`Rendering: ${label}`);
  return <button onClick={onClick}>{label}</button>;
});

function App() {
  const [count, setCount] = useState(0);
  const [other, setOther] = useState(0);

  // useCallback keeps the SAME function object between renders,
  // so the memoized Button does not re-render on every parent render.
  const handleClick = useCallback(() => {
    setCount((c) => c + 1);
  }, []);

  return (
    <div className="container">
      <h1>useCallback</h1>
      <h2>Count: {count}</h2>

      <Button label="Increment count" onClick={handleClick} />
      <button onClick={() => setOther(other + 1)}>
        Re-render parent (other: {other})
      </button>
      <p>Check the console — the Button only logs when you click IT.</p>
    </div>
  );
}

export default App;
