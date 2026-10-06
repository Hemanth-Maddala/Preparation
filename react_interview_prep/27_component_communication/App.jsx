// Component communication: the three directions of data flow.

import { useState } from "react";

// 1. Parent → Child: pass data as props
function Child({ message }) {
  return <p className="card">Received from parent: <strong>{message}</strong></p>;
}

// 2. Child → Parent: child calls a callback prop
function ChildWithButton({ onNotify }) {
  return (
    <button onClick={() => onNotify("Hi from the child!")}>
      Send message to parent
    </button>
  );
}

function App() {
  const [parentMessage, setParentMessage] = useState("Hello from parent");
  const [childMessage, setChildMessage] = useState("");
  const [counter, setCounter] = useState(0);

  return (
    <div className="container">
      <h1>Component Communication</h1>

      <h3>1. Parent → Child (props)</h3>
      <Child message={parentMessage} />
      <button onClick={() => setParentMessage("Updated message from parent")}>
        Change parent message
      </button>

      <h3>2. Child → Parent (callback prop)</h3>
      <ChildWithButton onNotify={setChildMessage} />
      {childMessage && <p>Parent received: {childMessage}</p>}

      <h3>3. Siblings → via shared parent state</h3>
      <button onClick={() => setCounter(counter + 1)}>
        Increment shared counter: {counter}
      </button>
      <Child message={`Shared counter value is ${counter}`} />
    </div>
  );
}

export default App;
