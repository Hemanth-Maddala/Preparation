// Lifting state up: shared state lives in the closest common parent
// and is passed to children via props.

import { useState } from "react";

// Child 1: receives the value AND the updater as props
function NameInput({ name, onChange }) {
  return (
    <input
      value={name}
      onChange={(e) => onChange(e.target.value)}
      placeholder="Type your name"
    />
  );
}

// Child 2: displays the same state owned by the parent
function NameDisplay({ name }) {
  return <p>Hello, {name || "..."}!</p>;
}

function App() {
  // State lives HERE — not in either child.
  // Both children share it through props.
  const [name, setName] = useState("");

  return (
    <div className="container">
      <h1>Lifting State Up</h1>
      <NameInput name={name} onChange={setName} />
      <NameDisplay name={name} />
    </div>
  );
}

export default App;
