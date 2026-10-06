// React.memo: prevent unnecessary re-renders of a child.
// It does a shallow comparison of props and skips rendering when
// they haven't changed.

import { memo, useState } from "react";

// WITHOUT memo this child would re-render every time App re-renders.
const ExpensiveChild = memo(function ExpensiveChild({ count }) {
  console.log("Child rendered");
  return <p>Child count: {count}</p>;
});

function App() {
  const [count, setCount] = useState(0);
  const [other, setOther] = useState(0);

  return (
    <div className="container">
      <h1>React.memo</h1>
      <ExpensiveChild count={count} />

      <button onClick={() => setCount(count + 1)}>
        Change child prop (count: {count})
      </button>
      <button onClick={() => setOther(other + 1)}>
        Change unrelated parent state (other: {other})
      </button>
      <p>Check the console — the child only logs when its prop changes.</p>
    </div>
  );
}

export default App;
